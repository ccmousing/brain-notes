from app.config import DEEPSEEK_API_KEY

from openai import OpenAI

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个助手"},
        {"role": "user", "content": "你好，介绍一下你自己"},
    ],
    stream=False,
)


print(response.choices[0].message.content)
