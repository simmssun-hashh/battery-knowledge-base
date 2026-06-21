#!/usr/bin/env python3
"""
Ontology Sync Engine V1.1
将 ontology/domain/*.json 中的 ABox 实例同步到 ChromaDB openclaw_memory 集合
（与 local-memory 共用同一 ChromaDB，使用 BGE-small-zh-v1.5 向量编码）

设计原则:
  - Domain JSONs 是 source of truth
  - ChromaDB 是搜索缓存，使用 upsert 增量更新
  - 每条记录包含: text(搜索用), metadata(domain/class/properties), embeddings
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime, timezone

# 国内镜像加速（hf-mirror.com）
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

ONTOLOGY_DIR = Path("/home/node/.openclaw/workspace/ontology")
DOMAIN_DIR = ONTOLOGY_DIR / "domain"
CROSS_FILE = ONTOLOGY_DIR / "relations" / "cross_domain.json"

def load_domain_json(path):
    """加载 domain JSON 文件"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_abox_entities(domain_data):
    """
    从 domain JSON 的 abox 字段提取所有实体实例
    返回: [(entity_id, entity_data, domain_name, category), ...]
    """
    entities = []
    domain_name = domain_data.get('domain', 'unknown')
    domain_label = domain_data.get('name', domain_name)
    abox = domain_data.get('abox', {})

    for category, items in abox.items():
        if category in ('description',):
            continue
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    eid = item.get('id', f"{domain_name}_{category}_{len(entities)}")
                    entities.append((eid, item, domain_name, domain_label, category))
                elif isinstance(item, str):
                    entities.append((item, {'value': item}, domain_name, domain_label, category))

    # Also include TBox classes as searchable entities
    tbox = domain_data.get('tbox', {})
    classes = tbox.get('classes', [])
    for cls in classes:
        eid = cls.get('id', '')
        if eid:
            entities.append((eid, cls, domain_name, domain_label, 'tbox_class'))

    return entities

def entity_to_text(eid, entity_data, domain_name, category):
    """将实体转换为可搜索的文本表示"""
    parts = [eid]

    # Add class info
    cls = entity_data.get('class', '')
    if cls:
        parts.append(cls)

    # Add definition/description
    for key in ('definition', 'desc', 'description', 'label'):
        val = entity_data.get(key, '')
        if val:
            parts.append(val)
            break

    # Add numerical properties
    for prop_name in ('hasCapacity', 'hasMaxVoltage', 'hasDiffusionCoefficient',
                      'hasBandGap', 'hasConductivity', 'hasThermalStabilityRank',
                      'hasVolumeExpansion', 'capacity_mAh_g', 'nominal_voltage_V',
                      'thermal_stability_rank', 'volume_expansion_percent',
                      'energy_density_Wh_kg', 'cycle_life', 'cost_yuan_per_Wh',
                      'irr_percent', 'payback_years'):
        val = entity_data.get(prop_name, '')
        if val is not None and val != '':
            parts.append(f"{prop_name}:{val}")

    # Add key_properties
    kp = entity_data.get('key_properties', [])
    if kp and isinstance(kp, list):
        parts.extend(str(p) for p in kp)

    # Add instances/subclasses from TBox
    for key in ('instances', 'subclasses', 'triggers', 'key_attributes'):
        vals = entity_data.get(key, [])
        if vals and isinstance(vals, list):
            parts.extend(str(v) for v in vals)

    # Add rules
    rules = entity_data.get('rules', [])
    if rules and isinstance(rules, list):
        for r in rules:
            if isinstance(r, dict):
                parts.append(r.get('description', ''))

    # Add misc string fields
    for key in ('standard_id', 'full_name', 'implement_date', 'replaces',
                'key_thresholds', 'mechanism', 'consequence',
                'value', 'formula', 'application_scenario'):
        val = entity_data.get(key, '')
        if val:
            if isinstance(val, (list, dict)):
                parts.append(str(val))
            else:
                parts.append(str(val))

    return ' '.join(parts)

def main():
    print(json.dumps({"status": "start", "time": datetime.now(timezone.utc).isoformat()}))

    # Load all domain JSONs
    all_entities = []
    domain_files = sorted(DOMAIN_DIR.glob('*.json'))
    for dfile in domain_files:
        try:
            domain_data = load_domain_json(dfile)
            entities = extract_abox_entities(domain_data)
            all_entities.extend(entities)
            print(json.dumps({"domain": domain_data.get('domain'),
                              "entities_extracted": len(entities)}))
        except Exception as e:
            print(json.dumps({"error": str(e), "file": str(dfile)}))

    print(json.dumps({"total_entities": len(all_entities)}))

    # Write entity index file (structured cache for query lookup)
    index = {}
    for eid, entity_data, domain_name, domain_label, category in all_entities:
        index[f"onto_{domain_name}_{eid}"] = {
            "entity_data": entity_data,
            "domain": domain_name,
            "domain_label": domain_label,
            "category": category,
            "text": entity_to_text(eid, entity_data, domain_name, category)
        }

    index_path = ONTOLOGY_DIR / ".entity_index.json"
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump({
            "updated": datetime.now(timezone.utc).isoformat(),
            "total_entities": len(index),
            "entities": index
        }, f, ensure_ascii=False, indent=2)

    print(json.dumps({"index_written": str(index_path), "entities": len(index)}))

    # Now sync to ChromaDB
    try:
        import chromadb
        from sentence_transformers import SentenceTransformer

        print(json.dumps({"msg": "loading BGE model from hf-mirror.com"}))
        model = SentenceTransformer('BAAI/bge-small-zh-v1.5')
        
        # 使用 shared ChromaDB（与 local-memory 共用）
        workspace = DOMAIN_DIR.parent.parent  # ontology/domain/ -> ontology/ -> workspace/
        shared_db = str(workspace / "skills" / "local-memory" / "data")
        print(json.dumps({"msg": f"connecting to ChromaDB at {shared_db}"}))
        client = chromadb.PersistentClient(path=shared_db)

        # 使用 openclaw_memory 集合（与 local-memory 共用），Upsert 模式
        collection = client.get_or_create_collection(
            'openclaw_memory',
            metadata={"description": "OpenClaw memory (shared by ontology + local-memory)", "version": "V3.0"}
        )

        # 构建待同步列表 (domain前缀防重复)
        ids = []
        texts = []
        metadatas = []
        for eid, entity_data, domain_name, domain_label, category in all_entities:
            text = entity_to_text(eid, entity_data, domain_name, category)
            unique_id = f"onto_{domain_name}_{eid}"
            ids.append(unique_id)
            texts.append(text)
            metadatas.append({
                "domain": domain_name,
                "domain_label": domain_label,
                "category": category,
                "is_ontology": True
            })

        # Batch upsert with BGE embeddings
        batch_size = 100
        
        print(json.dumps({"msg": f"encoding {len(ids)} entities with BGE..."}))
        all_embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=True)

        for i in range(0, len(ids), batch_size):
            batch_ids = ids[i:i+batch_size]
            batch_texts = texts[i:i+batch_size]
            batch_metas = metadatas[i:i+batch_size]
            batch_embs = all_embeddings[i:i+batch_size].tolist()
            
            # Upsert: 写入或更新已有记录
            collection.upsert(
                ids=batch_ids,
                documents=batch_texts,
                embeddings=batch_embs,
                metadatas=batch_metas
            )

        print(json.dumps({
            "chromadb_synced": len(ids),
            "collection": "openclaw_memory",
            "total_in_collection": collection.count()
        }))

    except ImportError as e:
        print(json.dumps({"chromadb_skipped": str(e)}))

    print(json.dumps({"status": "complete"}))

if __name__ == '__main__':
    main()
