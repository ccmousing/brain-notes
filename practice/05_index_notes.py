import chromadb
from pathlib import Path
from app.config import DEEPSEEK_API_KEY
from openai import OpenAI

# create chrmabd collection
chromadb_client = chromadb.Client()
collection = chromadb_client.create_collection(name="note")

note_dir = Path(r"D:\doubaoziliao\xuexijihua")

md_files = list(note_dir.glob("**/*.md"))


# index  md files to chromadb collection
def extract_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


for file_path in md_files:
    text = extract_text(file_path)
    collection.add(ids=[str(file_path)], documents=[text])

print(f"索引了 {len(md_files)} 个文件")
# read
question = "我的学习计划 v2.0 是关于什么的"
results = collection.query(
    query_texts=[question],
    n_results=3,  # Chroma will embed this for you
)


context = "\n\n---\n\n".join(results["documents"][0])

# create a chat
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1")
response = client.chat.completions.create(
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
