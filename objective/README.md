# sqa-system: Avaliação Objetiva de Qualidade de Fala

O **sqa-system** (avaliação objetiva) é uma ferramenta para a análise quantitativa da qualidade da fala gerada por modelos de Text-to-Speech (TTS). Utilizando métricas automáticas, o sistema processa os áudios da pasta `dataset` e gera relatórios detalhados para avaliação.

## Metodologia de Avaliação

Para realizar a comparação final, é necessário gerar os _scores_ de cada métrica. O repositório inclui três abordagens principais:

- **UTMOS**: Avalia a qualidade perceptiva dos áudios sintéticos.
- **Whisper**: Calcula a taxa de erro no conteúdo falado.
- **Resemblyzer**: Mede a semelhança entre a voz do áudio real e a voz sintética.

## Configuração e Execução

### UTMOS

#### Configuração do Ambiente

1. Criar um ambiente virtual com **Python 3.8.18**.
2. Atualizar dependências:
   ```bash
   pip install --upgrade pip==24.0 setuptools==69.1.1
   ```
3. Instalar os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

#### Execução

```bash
cd UTMOS
bash run_utmos.sh
```

Os _scores_ serão armazenados na pasta `results` em formato `.csv`.

---

### Resemblyzer e Whisper

#### Configuração do Ambiente

1. Criar um ambiente virtual com **Python 3.10.16**.
2. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```

#### Execução

Para calcular a similaridade da voz:
```bash
cd Resemblyzer
python similarity.py
```

Para calcular a taxa de erro na transcrição:
```bash
cd Whisper
python wer.py
```

---

## Comparando Modelos

Após a geração dos _scores_ em todas as métricas, execute:

```bash
python comparing_models.py
```

Serão gerados relatórios comparativos para cada métrica avaliada.

---

## Visualização de Resultados

Para gerar gráficos comparativos e analisar visualmente os resultados, utilize o _notebook_:

```bash
jupyter notebook plots.ipynb
```

Execute as células disponíveis para visualizar os _plots_ de análise.

