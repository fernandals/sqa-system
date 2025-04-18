FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get install -y gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --break-system-packages --upgrade pip && pip install --break-system-packages -r requirements.txt

COPY . .

CMD ["bash", "-c", "python similarity.py && python wer.py"]
