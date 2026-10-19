# Brain · 笔记 AI 助手

给自己的 Obsidian 笔记库做一个 RAG 问答助手——问自己的笔记，AI 从笔记里找答案回答。

## 功能

- 📚 遍历 Obsidian 笔记库所有 Markdown 文件
- ✂️ 按 Markdown 标题智能切块
- 🔍 向量检索最相关的段落（Chroma，本地 embedding）
- 💬 基于检索内容回答问题（DeepSeek LLM）
- 🌐 Streamlit 网页界面，流式输出打字机效果
- 🐳 Docker 一键启动

## 技术栈

- **Python** + **uv** 包管理
- **Chroma** 向量数据库（本地 all-MiniLM 模型，无需额外 embedding API）
- **DeepSeek API**（OpenAI 兼容接口）
- **Streamlit** 网页界面
- **Docker / docker-compose** 容器化

## 快速开始（推荐 Docker）

### 前置条件
- 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### 1. 克隆代码
```bash
git clone https://github.com/你的用户名/brain-notes.git
cd brain-notes
```

### 2. 配置环境变量
复制 `.env.example` 为 `.env`，填入你的配置：
```
# DeepSeek API Key（必填）
DEEPSEEK_API_KEY=sk-xxxxxxxx

# 你的 Obsidian 笔记库路径（必填，建库时读取笔记文件）
NOTES_DIR=你的笔记库文件夹路径
```

### 3. 首次使用：建向量库
```bash
docker compose run --rm app python build_index.py
```
遍历笔记库，切块，存入 Chroma，只需跑一次。

### 4. 启动
```bash
docker compose up --build
```
第一次会 build 镜像（几分钟），之后秒启动。

### 4. 打开浏览器
访问 http://localhost:8501 ，输入问题即可。

---

## 本地开发（不用 Docker）

```bash
# 安装依赖
uv sync

# 配置 .env（同上）

# 启动网页
uv run streamlit run app.py
```



## 项目结构

```
brain-notes/
├── app/
│   └── config.py              # 读环境变量
├── app.py                     # Streamlit 网页入口
├── build_index.py             # 建向量库脚本
├── Dockerfile
├── docker-compose.yml
├── .env.example               # 环境变量模板
└── pyproject.toml
```
