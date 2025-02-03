# sqa-system: Speech Quality Assessment System

O **sqa-system** é uma ferramenta para avaliação da qualidade de fala gerada por modelos de Text-to-Speech (TTS). Ele inclui métodos de avaliação **subjetiva** e **objetiva**, permitindo uma análise completa da performance dos modelos.

## Estrutura do Repositório

O repositório está organizado em duas seções principais:

- **subjective/**: Contém o sistema para avaliação subjetiva da qualidade da fala.
- **objective/**: Contém o sistema para avaliação objetiva da qualidade da fala.

Cada uma dessas seções possui um README dedicado com instruções detalhadas para execução, incluindo requisitos, instalação e execução.

## Organização dos Dados

Os dados utilizados pelo sistema devem estar organizados conforme a estrutura a seguir:

- **datasets/**: Diretório principal onde os dados devem ser armazenados.
  - **ground_truth/**: Pasta contendo os áudios reais.
  
  - Pastas com nome começando com **"tts"**: Cada pasta contém áudios sintéticos. Dentro de cada uma dessas pastas, devem haver apenas arquivos de áudio `.wav`, e os arquivos devem ter o mesmo nome que os arquivos na pasta **ground_truth** para que o sistema consiga realizar a comparação corretamente.

  - **metadata.txt**: Arquivo que contém as informações de cada áudio no formato:

    ```
    audio_id|path_to_audio_tts1|path_to_audio_tts2|path_to_audio_tts3
    ```

    Onde `audio_id` é o identificador do áudio, e `path_to_audio_tts1`, `path_to_audio_tts2` e `path_to_audio_tts3` são os caminhos para os respectivos áudios sintéticos. Os caminhos devem ser relativos à pasta **datasets**.

  - **test_sentences.txt**: Arquivo com a transcrição dos áudios, organizado da seguinte forma:

    ```
    audio_id|normalized_reference_text
    ```

    Onde `audio_id` é o identificador do áudio e `normalized_reference_text` é a transcrição do áudio normalizada.

## Como Executar

Para rodar um dos sistemas, acesse a pasta correspondente (**subjective/** ou **objective/**) e siga as instruções do respectivo README.

```bash
cd subjective  # ou cd objective
cat README.md  # Leia as instruções para execução
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

Para mais detalhes sobre cada tipo de avaliação, consulte os READMEs dentro das respectivas pastas.
