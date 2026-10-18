from pathlib import Path
import chromadb
from openai import OpenAI
from app.config import DEEPSEEK_API_KEY
import re

note_dir = Path(r"D:\doubaoziliao\xuexijihua")
md_files = list(note_dir.glob("**/*.md"))


chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="chunked_note")


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

collection.add(ids=all_ids, documents=all_docs, metadatas=all_metas)
print(f"\n共索引 {collection.count()} 个块")
question = "我的学习计划 v2.0 是关于什么的"
results = collection.query(
    query_texts=[question],
    n_results=6,  # Chroma will embed this for you
)

print("\n--- 检索到的来源 ---")
for meta, dist in zip(results["metadatas"][0], results["distances"][0]):
    print(f"{meta['source']}  距离 {dist:.3f}")

context = "\n\n---\n\n".join(results["documents"][0])


# create a chat
llm = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1")
response = llm.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": f"根据以下笔记内容回答问题，不要编造：\n\n{context}",
        },
        {"role": "user", "content": question},
    ],
)

# print answer

print("\n=== 问题 ===")
print(question)
print("\n=== AI 回答 ===")
print(response.choices[0].message.content)
