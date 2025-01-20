# sqa-system: Speech Quality Assessment System

O sqa-system é uma ferramenta para avaliação de modelos de Text-to-Speech (TTS), projetada para ajudar na análise da qualidade da fala gerada por diferentes modelos.

## Requisitos

- Python: 3.10.16

## Instalação e Execução 

Siga os passos abaixo para configurar o ambiente e executar o sistema:

#### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/fernandals/sqa-system.git
cd sqa-system
```

#### 2. Criar e Ativar o Ambiente Virtual

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

#### 3. Instalar as Dependências

Instale todas as dependências necessárias:

```bash
pip install -r requirements.txt
```

#### Execute o Sistema

Execute o sistema usando o Streamlit:

```
streamlit run src/app.py
```

O aplicativo será iniciado e você poderá acessá-lo diretamente no seu navegador.
