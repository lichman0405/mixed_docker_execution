# 基础镜像
FROM python:3.10-slim

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 创建挂载目录
WORKDIR /usr/src/app
RUN mkdir -p host_code

# 复制应用代码
COPY app/ ./app/

# 暴露端口
EXPOSE 1234

# 启动 FastAPI 应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1234"]
