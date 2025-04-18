FROM python:3.8-slim

# Evita prompts de timezone etc.
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências básicas
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN apt install -y software-properties-common

WORKDIR /app

COPY requirements.txt .
RUN pip install --break-system-packages --upgrade pip==24.0 setuptools==69.1.1
RUN pip install --break-system-packages -r requirements.txt

COPY . .

CMD ["bash", "run_utmos.sh"]
