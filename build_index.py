from pathlib import Path
import chromadb
from openai import OpenAI
from app.config import DEEPSEEK_API_KEY
import re
import os

note_dir = Path(os.getenv("NOTES_DIR", "./notes"))
md_files = list(note_dir.glob("**/*.md"))

# persistent client数据持久化 change use get_or_create_collection
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="chunked_note")


# 先收集所有块，最后一次性加入
all_ids = []
all_docs = []
all_metas = []

for file_path in md_files:
    text = file_path.read_text(encoding="utf-8")
    chunks = [c.strip() for c in re.split(r"\n(?=#{1,6}\s)", text) if c.strip()]
    # 每一块单独加：id = 文件名_序号，metadata 记文件名
    for i, chunk in enumerate(chunks):
        all_ids.append(f"{file_path.name}_{i}")
        all_docs.append(chunk)
        all_metas.append({"source": file_path.name})
    print(f"{file_path.name}: {len(chunks)} 块")

# 增加一个判断，如果已经索引过，则跳过
if collection.count() == 0:
    for file_path in md_files:
        collection.add(ids=all_ids, documents=all_docs, metadatas=all_metas)
    print(f"首次建库，共索引 {collection.count()} 个块")
else:
    print(f"已从磁盘加载 {collection.count()} 个块，跳过索引")


print(f"\n共索引 {collection.count()} 个块")
