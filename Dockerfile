# 使用官方Python运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 暴露端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 初始化数据库
RUN python init_db.py

# 生成模拟数据
RUN python generate_mock_data.py

# 运行应用
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
