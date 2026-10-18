# Brain · 笔记 AI 助手

给自己的 Obsidian 笔记库做一个 RAG 问答助手——问自己的笔记，AI 从笔记里找答案回答。

## 功能

- 📚 遍历 Obsidian 笔记库所有 Markdown 文件
- 🔍 向量检索最相关的段落（Chroma）
- 💬 基于检索内容回答问题（DeepSeek LLM）

## 技术栈

- **Python** + **uv** 包管理
- **Chroma** 向量数据库（本地 embedding，无需额外 API）
- **DeepSeek API**（OpenAI 兼容接口）
- **python-dotenv** 管理环境变量

## 快速开始

### 1. 安装依赖
```bash
uv sync
```

### 2. 配置环境变量
复制 `.env.example` 为 `.env`，填入你的 DeepSeek API Key：
```
DEEPSEEK_API_KEY=sk-xxxxxxxx
```

### 3. 运行
```bash
# 最小测试：读单个文件问 AI
uv run python practice/01_hello_llm.py

# RAG 闭环：检索笔记库 + AI 回答
uv run python practice/05_index_notes.py
```

## 项目状态

> ⚠️ 开发中，尚未达到生产可用

- [x] M1：最小闭环（读单个 md 文件，AI 基于内容回答）
- [x] M2：RAG 闭环（遍历笔记库 + Chroma 检索 + LLM 回答）
- [ ] M2 优化：文本切块 + Chroma 持久化
- [ ] M3：Web 界面（Streamlit）
- [ ] M4：Docker 化 + 开源

## 项目结构

```
main_agent/
├── app/
│   ├── config.py          # 读环境变量
│   └── prompts/           # prompt 模板
├── practice/              # 练习脚本（踩坑用）
│   ├── 01_hello_llm.py    # 最小 LLM 调用
│   ├── 02_test_path.py    # pathlib 读文件
│   ├── 03_scan_notes.py   # 遍历笔记库
│   ├── 04_rag_demo.py     # Chroma Quickstart
│   └── 05_index_notes.py  # RAG 完整闭环
├── .env                   # 环境变量（不进 git）
└── pyproject.toml
```
