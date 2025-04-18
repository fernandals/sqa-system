#!/bin/bash

echo "🔍 Verificando se os arquivos de resultados estão prontos..."

FILES=(
  "results/resemblyzer_ground_truth.csv"
  "results/resemblyzer_tts1.csv"
  "results/resemblyzer_tts2.csv"
  "results/resemblyzer_tts3.csv"
  "results/whisper_ground_truth.csv"
  "results/whisper_tts1.csv"
  "results/whisper_tts2.csv"
  "results/whisper_tts3.csv"
  #"results/visqol_tts1.csv"
  #"results/visqol_tts2.csv"
  #"results/visqol_tts3.csv"
  #"results/utmost_tts1.csv"
  #"results/utmost_tts2.csv"
  #"results/utmost_tts3.csv"
  #"results/utmost_ground_truth.csv"
)

for file in "${FILES[@]}"; do
  while [ ! -f "$file" ]; do
    echo "⏳ Aguardando $file..."
    sleep 2
  done
  echo "✅ Encontrado: $file"
done

echo "🚀 Todos os arquivos encontrados. Iniciando comparação..."
python comparing_models.py
