```
# Main-Agent


## 技术栈
- Python 3.12 + uv
- FastAPI（接口）
- LangGraph（Agent 编排，后加）
- SQLAlchemy + SQLite/MySQL（持久化）

## 铁律
- 不要推倒重写，增量迭代
- 密钥必须从 .env 读，禁止硬编码
- Tool 入参必须用 Pydantic 校验
- 业务代码里禁止出现 api.deepseek.com 这种硬编码 URL，统一走 llm_client.py
```