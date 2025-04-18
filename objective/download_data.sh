#!/bin/bash

URL="https://mega.nz/file/SP53xSTQ#CzW6ERyJYPGUYmcq-AvF_7SXsM2yFW2lXjayrBPU_rQ"
OUTPUT="dataset.tar.gz"
EXTRACT_DIR="dataset"

# Check if megadl or mega-get is installed
if ! command -v megadl &> /dev/null && ! command -v mega-get &> /dev/null; then
    echo "❌ megadl or mega-get is not installed."
    echo "👉 Install megatools or MEGAcmd before running this script."
    exit 1
fi

echo "📥 Baixando dataset..."
if command -v megadl &> /dev/null; then
    megadl "$URL" --path "$OUTPUT"
else
    mega-get "$URL" .
fi

echo "📦 Extraindo arquivos..."
mkdir -p "$EXTRACT_DIR"
tar -xvf "$OUTPUT" -C "$EXTRACT_DIR" --strip-components=1

echo "🧹 Limpando arquivos temporários..."
rm "$OUTPUT"

echo "✅ Dataset pronto na pasta: $EXTRACT_DIR"
