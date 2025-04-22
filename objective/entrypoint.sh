#!/bin/bash

echo "🔍 Verificando se os arquivos de resultados estão prontos..."

FILES=(
  "results/Resemblyzer_ground_truth.csv"
  "results/Resemblyzer_tts1.csv"
  "results/Resemblyzer_tts2.csv"
  "results/Resemblyzer_tts3.csv"
  "results/Whisper_ground_truth.csv"
  "results/Whisper_tts1.csv"
  "results/Whisper_tts2.csv"
  "results/Whisper_tts3.csv"
  #"results/ViSQOL_tts1.csv"
  #"results/ViSQOL_tts2.csv"
  #"results/ViSQOL_tts3.csv"
  #"results/UTMOS_tts1.csv"
  #"results/UTMOS_tts2.csv"
  #"results/UTMOS_tts3.csv"
  #"results/UTMOS_ground_truth.csv"
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
