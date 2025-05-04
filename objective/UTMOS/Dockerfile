FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y ffmpeg git gcc build-essential libsndfile1 wget && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone https://github.com/sarulab-speech/UTMOSv2.git /app
RUN sed -i 's/.to("cuda")/.to("cpu")/g' /app/utmosv2/_core/model/_common.py
RUN sed -i 's/tensor.to(device)/tensor.to("cpu")/g' /app/utmosv2/**/*.py

COPY requirements.txt .

RUN pip install --break-system-packages --upgrade pip && \
    pip install --break-system-packages -r requirements.txt && \
    pip install --break-system-packages \
        torch==2.2.0+cpu \
        torchaudio==2.2.0+cpu \
        -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install --break-system-packages git+https://github.com/sarulab-speech/UTMOSv2.git


COPY . .

CMD ["python", "mos.py"]
