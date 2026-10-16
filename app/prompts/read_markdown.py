from app.config import DEEPSEEK_API_KEY
from openai import OpenAI
from pathlib import Path

# read note
note_path = Path(r"D:\doubaoziliao\xuexijihua\学习计划\学习计划.md")

# create a agent_chat
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1")

# create a content
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {
            "role": "system",
            "content": f"你是一个笔记整理助手，阅读用户提供的笔记内容，并总结出要点。\n笔记内容如下：\n{note_path.read_text(encoding='utf-8')}",
        },
        {
            "role": "user",
            "content": f"请阅读以下内容并总结要点：\n{note_path.read_text(encoding='utf-8')}",
        },
    ],
    stream=False,
)

print(response.choices[0].message.content)
