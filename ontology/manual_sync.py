#!/usr/bin/env python3
"""
手动 BGE 编码 + ChromaDB 写入脚本
将 battery_system.json 中的 ABox 实体编码写入 openclaw_memory 集合
绕过 sync.py 的 ChromaDB ONNX 下载问题，直接用 sentence-transformers + BGE
"""

import os, sys, json, uuid
from datetime import datetime, timezone

# 网络环境
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(SCRIPT_DIR)
SKILL_DIR = os.path.join(WORKSPACE, 'skills', 'local-memory')

sys.path.insert(0, os.path.join(SKILL_DIR, 'scripts'))

DB_PATH = os.path.join(SKILL_DIR, 'data')
COLLECTION = "openclaw_memory"
MODEL_NAME = "BAAI/bge-small-zh-v1.5"
ONTOLOGY_DOMAIN = "battery_system"

def load_battery_system():
    path = os.path.join(WORKSPACE, 'ontology', 'domain', 'battery_system.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def entity_to_text(entity, domain_data):
    """将 ABox entity 转换为可嵌入的文本"""
    parts = [f"{entity['id']}"]
    
    if 'name' in entity:
        parts.append(entity['name'])
    if 'definition' in entity:
        parts.append(entity['definition'])
    
    # 添加属性
    if 'attributes' in entity and isinstance(entity['attributes'], dict):
        for k, v in entity['attributes'].items():
            parts.append(f"{k}: {v}")
    
    # 添加关系
    if 'relations' in entity and isinstance(entity['relations'], list):
        parts.append(f"关系: {', '.join(entity['relations'])}")
    
    # 添加工程规则
    if 'rules' in entity and isinstance(entity['rules'], list):
        for rule in entity['rules']:
            if isinstance(rule, dict):
                parts.append(rule.get('description', ''))
            elif isinstance(rule, str):
                parts.append(rule)
    
    # 添加关键机制
    if 'key_mechanisms' in entity:
        for mech in entity['key_mechanisms']:
            parts.append(mech)
    
    # 添加核心洞见
    if 'core_insight' in entity:
        parts.append(entity['core_insight'])
    
    text = ' '.join([str(p) for p in parts if p])
    return text

def extract_new_entities(domain_data):
    """从 domain JSON 中提取需要同步的实体"""
    entities_to_sync = []
    
    # ABox entities (nested list structure)
    abox = domain_data.get('abox', {})
    abox_entities = abox.get('entities', [])
    
    for group in abox_entities:
        if isinstance(group, list):
            for entity in group:
                if isinstance(entity, dict) and 'id' in entity:
                    text = entity_to_text(entity, domain_data)
                    entity_id = entity['id']
                    entities_to_sync.append({
                        'id': f"onto_{ONTOLOGY_DOMAIN}_{entity_id}",
                        'text': text,
                        'entity_id': entity_id,
                        'domain': ONTOLOGY_DOMAIN,
                        'label': entity.get('name', entity_id),
                    })
        elif isinstance(group, dict) and 'id' in group:
            text = entity_to_text(group, domain_data)
            entity_id = group['id']
            entities_to_sync.append({
                'id': f"onto_{ONTOLOGY_DOMAIN}_{entity_id}",
                'text': text,
                'entity_id': entity_id,
                'domain': ONTOLOGY_DOMAIN,
                'label': group.get('name', entity_id),
            })
    
    # Incremental learning sessions (as entity bundles)
    inc = abox.get('incremental_learning', {})
    for session_key, session in inc.items():
        if session_key == 'last_session':
            continue
        texts = []
        if 'document' in session:
            texts.append(f"学习文档: {session['document']}")
        if 'core_insight' in session:
            texts.append(f"核心洞见: {session['core_insight']}")
        if 'key_mechanisms' in session:
            for m in session['key_mechanisms']:
                texts.append(f"关键机理: {m}")
        if 'entities_added' in session:
            texts.append(f"新增实体: {', '.join(session['entities_added'])}")
        if 'period' in session:
            texts.append(f"学习周期: {session['period']}")
        if 'documents' in session:
            for doc in session['documents']:
                texts.append(f"学习材料: {doc}")
        if 'cross_book_synthesis' in session:
            for synth in session['cross_book_synthesis']:
                texts.append(f"跨书综合: {synth}")
        if 'knowledge_sources' in session:
            for src in session['knowledge_sources']:
                texts.append(f"知识来源: {src}")
        
        text = ' '.join(texts)
        entities_to_sync.append({
            'id': f"onto_learn_{session_key}",
            'text': text,
            'entity_id': session_key,
            'domain': ONTOLOGY_DOMAIN,
            'label': session.get('document', session_key),
        })
    
    return entities_to_sync

def main():
    print("1. 加载 battery_system.json ...")
    domain_data = load_battery_system()
    
    print("2. 提取实体 ...")
    entities = extract_new_entities(domain_data)
    print(f"   共 {len(entities)} 个实体待同步")
    
    print("3. 加载 BGE 模型 ...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(MODEL_NAME)
    print("   模型加载完毕")
    
    print("4. 连接 ChromaDB ...")
    import chromadb
    client = chromadb.PersistentClient(path=DB_PATH)
    col = client.get_or_create_collection(COLLECTION)
    
    # 检查已有实体
    existing = col.get(where={'is_ontology': True})
    existing_ids = set(existing['ids'])
    print(f"   已有 {len(existing_ids)} 个本体实体")
    
    # 过滤出新实体
    new_entities = [e for e in entities if e['id'] not in existing_ids]
    print(f"   新实体 {len(new_entities)} 个待写入")
    
    if not new_entities:
        print("5. 没有新实体，跳过写入")
        return
    
    print("5. BGE 编码 ...")
    texts = [e['text'] for e in new_entities]
    embeddings = model.encode(texts, normalize_embeddings=True)
    print(f"   编码完成: {embeddings.shape}")
    
    print("6. 写入 ChromaDB ...")
    now = datetime.now(timezone.utc).isoformat()
    batch_size = 20
    
    for i in range(0, len(new_entities), batch_size):
        batch = new_entities[i:i+batch_size]
        batch_emb = embeddings[i:i+batch_size].tolist()
        
        col.add(
            ids=[e['id'] for e in batch],
            documents=[e['text'] for e in batch],
            embeddings=batch_emb,
            metadatas=[{
                'is_ontology': True,
                'domain': e['domain'],
                'domain_label': ONTOLOGY_DOMAIN,
                'entity_id': e['entity_id'],
                'label': e['label'],
                'category': 'entity',
                'importance': 0.9,
                'created_at': now,
            } for e in batch],
        )
        print(f"   批次 {i//batch_size + 1}: {len(batch)} 条写入完成")
    
    print(f"\n✅ 完成！共写入 {len(new_entities)} 个本体实体")
    print(f"   openclaw_memory 总记录: {col.count()}")

if __name__ == '__main__':
    main()
