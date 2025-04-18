# sqa-system: Avaliação Objetiva de Qualidade de Fala

O **sqa-system** é uma ferramenta para análise quantitativa da qualidade da fala gerada por modelos de *Text-to-Speech (TTS)*. Utilizando métricas automáticas, o sistema processa os áudios da pasta `dataset` e gera relatórios detalhados para avaliação.

O sistema está containerizado com **Docker Compose**, eliminando problemas de compatibilidade entre bibliotecas e versões de Python.

---

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- `megatools` (para baixar o dataset):
  
  ```bash
  sudo apt install megatools
  ```
---

## Como Executar

### 1. Baixar o dataset (opcional)

Execute o script abaixo para baixar automaticamente o conjunto de dados necessário (cerca de 1.5 GB):

```bash
bash download_dataset.sh
```

🔗 Link direto: [MEGA](https://mega.nz/file/SP53xSTQ#CzW6ERyJYPGUYmcq-AvF_7SXsM2yFW2lXjayrBPU_rQ)

Esse script irá baixar e extrair o conteúdo para a pasta `dataset/`.

### 2. Gerar os *scores* com todas as métricas:

```bash
docker-compose up --build
```

Esse comando irá:

- Rodar o **UTMOS** (avaliação perceptiva)
- Rodar o **Whisper** (taxa de erro de transcrição)
- Rodar o **Resemblyzer** (similaridade de voz)
- Rodar o **ViSQOL** (qualidade perceptiva baseada em referência)
- Gerar os arquivos `.csv` na pasta `results/`

### 3. Comparar os modelos:

```bash
docker-compose run comparator
```

### 4. Visualizar os resultados:

Você pode abrir o notebook localmente:

```bash
jupyter notebook plots.ipynb
```

## Estrutura dos Diretórios

```perl
objective/
├── docker-compose.yml
├── UTMOS/
│   ├── Dockerfile
│    ...
│   ├── run_utmos.sh
│   └── requirements.txt
├── Resemblyzer+Whisper/
│   ├── Dockerfile
│   ├── similarity.py
│   ├── wer.py
│   └── requirements.txt
├── ViSQOL/
│   ├── Dockerfile
│   ├── mos_lqo.py
│   ├── WORKSPACE1
│   └── requirements.txt
├── dataset/
├── results/
├── comparing_models.py
├── Dockerfile.comparator
├── plots.ipynb
├── entrypoint.sh
├── README.md
├── requirements.txt
└── download_data.sh
```

## Sobre as Métricas

- **UTMOS**: Avalia a qualidade perceptiva dos áudios sintéticos utilizando um modelo treinado com dados humanos.

- **Whisper (WER)**: Realiza transcrição automática e calcula a *Word Error Rate (WER)*, uma métrica de inteligibilidade.

- **Resemblyzer**: Mede a semelhança entre o locutor real e o locutor sintetizado usando embeddings vocais.

- **ViSQOL**: Métrica objetiva de qualidade da fala baseada em comparação com referência, simulando a percepção auditiva humana.

## Contato

Contribuições são bem-vindas! Para dúvidas ou sugestões, abra uma issue ou envie um pull request.
