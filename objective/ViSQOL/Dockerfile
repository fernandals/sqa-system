# --- STAGE 1: Builder (compila VisQol + instala pacotes Python) ---
FROM python:3.10-slim AS builder

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive  
# Opções para Bazel (menos threads/cache menor)
ENV BAZEL_BUILD_OPTS="--jobs=2 --local_ram_resources=2048 --local_cpu_resources=2"

# Instala dependências de build e ffmpeg para testes se necessário
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gnupg \
    apt-transport-https \
    build-essential \
    python3-dev \
    ffmpeg \
  && rm -rf /var/lib/apt/lists/*

# Instala Bazel
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg \
      | gpg --dearmor > /etc/apt/trusted.gpg.d/bazel.gpg
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" \
      | tee /etc/apt/sources.list.d/bazel.list
RUN apt-get update && apt-get install -y bazel-5.3.2 \
  && ln -s /usr/bin/bazel-5.3.2 /usr/bin/bazel

# Mostra versão para debug
RUN bazel --version

# Instala pip + dependências Python (inclui numpy antes do build)
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Clona o repositório oficial e aplica WORKSPACE personalizado
WORKDIR /visqol
RUN git clone https://github.com/google/visqol.git .
COPY WORKSPACE1 ./WORKSPACE

# Constrói o binário VisQol
RUN bazel clean --expunge && \
    bazel build :visqol -c opt --define=PROTOBUF_PYTHON=1 $BAZEL_BUILD_OPTS \
                --copt=-march=native \
                --copt=-Wno-unused-command-line-argument

# Instala o pacote Python dentro de /install para copiar depois
RUN pip install . --prefix=/install


# --- STAGE 2: Runtime (imagem enxuta para execução) ---
FROM python:3.10-slim AS runtime
ENV DEBIAN_FRONTEND=noninteractive

# Instala apenas ffmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
  && rm -rf /var/lib/apt/lists/*

# Copia o binário VisQol do builder
COPY --from=builder /visqol/bazel-bin/visqol /usr/local/bin/visqol

# Copia pacotes VisQol instalados em /install para o path do Python
COPY --from=builder /install /usr/local

# Copia o app e o requirements.txt
WORKDIR /app
COPY . .

# Instala novamente os requisitos Python do projeto (inclui librosa)
RUN pip install --no-cache-dir -r requirements.txt

# Configura variáveis de ambiente do VisQOL
ENV VISQOL_BIN=/usr/local/bin/visqol
ENV VISQOL_CONFIG=/usr/local/lib/python3.10/site-packages/visqol/config/visqol_config.json

# Executa seu script por padrão
CMD ["python", "mos_lqo.py"]
