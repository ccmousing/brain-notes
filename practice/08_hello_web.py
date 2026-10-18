import streamlit as st
import chromadb
from openai import OpenAI
from app.config import DEEPSEEK_API_KEY


# 缓存向量库，只加载一次
@st.cache_resource
def load_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_or_create_collection(name="chunked_note")


collection = load_collection()
llm = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1")

st.title("Brain 笔记助手")
question = st.text_input("输入你想问的问题")

if question:
    # 检索
    results = collection.query(query_texts=[question], n_results=6)
    context = "\n\n---\n\n".join(results["documents"][0])

    # 调 LLM
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
    st.write("### 回答")
    st.write(response.choices[0].message.content)
