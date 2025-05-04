# Use a slim python image
FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV BAZEL_BUILD_OPTS="--jobs=2 --local_ram_resources=2048 --local_cpu_resources=2"

# 1. Install minimal dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    python3-dev \
    build-essential \
    gnupg \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Bazel
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/bazel.gpg
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
RUN apt-get update && apt-get install -y bazel-5.3.2
RUN ln -s /usr/bin/bazel-5.3.2 /usr/bin/bazel
RUN bazel --version

WORKDIR /app

# 3. Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 4. Clone ViSQOL
RUN git clone https://github.com/google/visqol.git /visqol

# 5. Replace WORKSPACE with your fixed version
COPY WORKSPACE1 /visqol/WORKSPACE

# 6. Build ViSQOL
WORKDIR /visqol
#RUN bazel clean --expunge && \
#    bazel build :visqol -c opt

RUN bazel clean --expunge && \
    bazel build :visqol -c opt --define=PROTOBUF_PYTHON=1 \
    --jobs=2 \
    --local_ram_resources=2048 \
    --local_cpu_resources=2 \
    --copt=-march=native \
    --copt=-Wno-unused-command-line-argument

# 7. Install Python package
RUN pip install .

# 8. Final setup
WORKDIR /app
COPY . .
ENV VISQOL_BIN=/visqol/bazel-bin/visqol
ENV VISQOL_CONFIG=/visqol/config/visqol_config.json

CMD ["python", "mos_lqo.py"]