# syntax=docker/dockerfile:1

FROM registry.group-ds.com/cloudladder/runtime:python3.8-slim
WORKDIR /app
COPY . .

# 构建容器时的指令
RUN apt-get update
RUN apt-get install libgomp1
RUN pip install -U pip  # -U upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip config set install.trusted-host 'pypi.tuna.tsinghua.edu.cn mirrors.aliyun.com pypi.douban.com pypi.mirrors.ustc.edu.cn'
RUN pip config set global.extra-index-url ' http://mirrors.aliyun.com/pypi/simple/ http://pypi.douban.com/simple/ http://pypi.mirrors.ustc.edu.cn/simple/'
RUN pip config set global.timeout 120
RUN pip install .

# 容器运行时的指令
CMD [" uvicorn dophin_scheduler_app:app  --host 0.0.0.0 --port 80"]


