FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dashboard3.py .

EXPOSE 8503

RUN apt-get update && apt-get install -y iputils-ping curl

HEALTHCHECK CMD curl --fail http://localhost:8503/_stcore/health

ENTRYPOINT ["streamlit", "run", "dashboard3.py", "--server.port=8503", "--server.address=0.0.0.0"]

RUN apt-get update && apt-get install -y tzdata
ENV TZ=Asia/Seoul

# 기본 실행 명령어 제거 (docker run에서 지정) 