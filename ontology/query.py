#!/usr/bin/env python3
"""
Ontology Query Interface V1.0
统一的 Ontology 索引层查询入口

用法:
  python3 ontology/query.py --query "LFP扩散系数"
  python3 ontology/query.py --query "钠电" --limit 5

返回: JSON，包含查询结果 + 结构化实体数据 + 跨域关联
"""

import json
import sys
import argparse
from pathlib import Path

ONTOLOGY_DIR = Path("/home/node/.openclaw/workspace/ontology")
INDEX_PATH = ONTOLOGY_DIR / ".entity_index.json"
DOMAIN_DIR = ONTOLOGY_DIR / "domain"
CROSS_FILE = ONTOLOGY_DIR / "relations" / "cross_domain.json"

def load_index():
    """加载实体索引缓存"""
    if INDEX_PATH.exists():
        with open(INDEX_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def load_cross_domain():
    """加载跨域关系"""
    if CROSS_FILE.exists():
        with open(CROSS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def search_chromadb(query, limit=5):
    """在 ChromaDB 中语义搜索（使用手动 BGE 编码避免 ChromaDB ONNX 下载）"""
    try:
        import os, certifi
        os.environ.setdefault('HF_ENDPOINT', 'https://hf-mirror.com')
        os.environ.setdefault('REQUESTS_CA_BUNDLE', certifi.where())
        os.environ.setdefault('SSL_CERT_FILE', certifi.where())

        import chromadb
        from sentence_transformers import SentenceTransformer

        # Use existing local-memory ChromaDB (not a new collection)
        DB_PATH = str(ONTOLOGY_DIR.parent / "skills" / "local-memory" / "data")
        client = chromadb.PersistentClient(path=DB_PATH)
        collection = client.get_collection('openclaw_memory')

        # Manually encode to avoid ChromaDB ONNX model download
        model = SentenceTransformer('BAAI/bge-small-zh-v1.5')
        embeddings = model.encode([query]).tolist()
        results = collection.query(
            query_embeddings=embeddings,
            n_results=min(limit, collection.count()),
            where={'is_ontology': True}
        )

        output = []
        if results.get('ids') and results['ids'][0]:
            for i, eid in enumerate(results['ids'][0]):
                item = {
                    "id": eid,
                    "distance": round(results['distances'][0][i], 4) if results.get('distances') else None,
                    "metadata": results['metadatas'][0][i] if results.get('metadatas') else {},
                }
                # Look up full entity from index
                index = load_index()
                if index and eid in index.get('entities', {}):
                    item['entity_data'] = index['entities'][eid]['entity_data']
                    item['domain_label'] = index['entities'][eid].get('domain_label', '')
                output.append(item)

        return output
    except Exception as e:
        return [{"error": str(e)}]

def search_fallback(query, limit=5):
    """ChromaDB 不可用时的关键词回退搜索"""
    index = load_index()
    if not index:
        return []

    query_lower = query.lower()
    results = []

    for eid, entity in index.get('entities', {}).items():
        text = entity.get('text', '')
        text_lower = text.lower()
        # Simple keyword scoring
        score = sum(1 for word in query_lower.split() if word in text_lower)
        if score > 0:
            results.append((score, eid, entity))

    results.sort(key=lambda x: -x[0])
    return [{
        "id": r[1],
        "entity_data": r[2].get('entity_data', {}),
        "domain_label": r[2].get('domain_label', ''),
        "domain": r[2].get('domain', ''),
        "keyword_score": r[0]
    } for r in results[:limit]]

def get_cross_relations(entity_id):
    """获取跨域关联"""
    cross = load_cross_domain()
    if not cross:
        return []

    relations = []
    for rel in cross.get('abox_relations', []):
        if rel.get('from') == entity_id or rel.get('to') == entity_id:
            relations.append(rel)

    for rel in cross.get('tbox_relations', []):
        if entity_id in rel.get('from_class', '') or entity_id in rel.get('to_class', ''):
            relations.append(rel)

    return relations

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', required=True, help='搜索查询')
    parser.add_argument('--limit', type=int, default=5, help='返回条数')
    parser.add_argument('--with-relations', action='store_true', help='包含跨域关联')
    args = parser.parse_args()

    output = {
        "query": args.query,
        "timestamp": "",
        "results": [],
        "source": ""
    }

    from datetime import datetime, timezone
    output['timestamp'] = datetime.now(timezone.utc).isoformat()

    # Try ChromaDB first
    results = search_chromadb(args.query, args.limit)

    if results and not results[0].get('error'):
        output['source'] = 'chromadb'
        output['results'] = results
    else:
        # Fallback to keyword search
        output['source'] = 'keyword_fallback'
        output['results'] = search_fallback(args.query, args.limit)

    # Add cross-domain relations if requested
    if args.with_relations and output['results']:
        for r in output['results']:
            r['cross_relations'] = get_cross_relations(r.get('id', ''))

    # Summary
    index = load_index()
    output['index_stats'] = {
        "total_entities": index.get('total_entities', 0) if index else 0,
        "index_updated": index.get('updated', '') if index else '',
        "domains": len(list(DOMAIN_DIR.glob('*.json')))
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
