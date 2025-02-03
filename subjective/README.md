# sqa-system: Avaliação Subjetiva de Qualidade de Fala

O **sqa-system** (avaliação subjetiva) é um sistema para analisar a qualidade da fala gerada por modelos de Text-to-Speech (TTS) com base em percepção humana. O sistema gera um formulário de avaliação dos áudios dentro da pasta `dataset` e armazena essas informações para futura análise.

## Requisitos

- Python: 3.10.16

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e executar o sistema.

### 1. Clonar o Repositório

```bash
git clone https://github.com/fernandals/sqa-system.git
cd sqa-system/subjective
```

### 2. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para instalar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:

  ```bash
  .\venv\Scripts\activate
  ```

- No macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

## Como Executar

Para rodar o sistema de avaliação subjetiva, execute:

```bash
streamlit run src/app.py
```

O aplicativo será iniciado e estará acessível diretamente no navegador.
