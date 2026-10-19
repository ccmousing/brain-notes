# 用官方 Python 3.12 精简镜像做底子
FROM python:3.12-slim

# onnxruntime（chromadb 用）需要 libgomp1，slim 镜像默认没有
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# 容器里的工作目录
WORKDIR /app

# 先只复制依赖文件，利用 Docker 缓存：代码变了不用重装依赖
COPY pyproject.toml uv.lock ./

# 安装 uv，再用 uv 装项目依赖
RUN pip install uv && uv sync --no-dev

# 再复制项目代码
COPY . .

# Streamlit 默认端口
EXPOSE 8501

# 容器启动时执行
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.address=0.0.0.0"]

ENV PYTHONPATH=/app
