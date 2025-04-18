import os
import csv
from pathlib import Path
import whisper
from jiwer import wer, process_words
import warnings

def read_reference_file(file_path):
    reference_dict = {}
    with open(file_path, "r") as file:
        for line in file:
            audio_id, reference_text = line.strip().split("|", maxsplit=1)
            reference_dict[audio_id] = reference_text
    return reference_dict

def process_audio_files(audio_folder, reference_dict, model):
    """
    Processes .wav files and returns the results instead of writing them directly.
    
    Returns:
        list: List of [filename, score] rows including header.
    """
    results = [["filename", "score"]]

    for filename in os.listdir(audio_folder):
        if filename.endswith(".wav"):
            audio_file = os.path.join(audio_folder, filename)

            # Transcribe
            result = model.transcribe(audio_file)
            transcription = result["text"]
            
            audio_id = os.path.splitext(filename)[0]
            reference_text = reference_dict.get(audio_id, "")

            if not reference_text:
                print(f"Warning: No reference text found for {filename}. Skipping.")
                continue

            print(reference_text, "--", transcription)

            output = process_words(reference_text, transcription)
            error_rate = output.wer

            results.append([audio_id, f"{error_rate:.4f}"])

    return results

def save_results_to_csv(results, results_path):
    with open(results_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(results)

def main():
    warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

    model = whisper.load_model("small")
    root_audio_folder = Path("dataset")
    reference_file = Path("dataset/test_sentences.txt")

    reference_dict = read_reference_file(reference_file)

    for model_folder in ['ground_truth', 'tts1', 'tts2', 'tts3']:
        audio_folder = os.path.join(root_audio_folder, model_folder)
        results_path = f"results/Whisper_{model_folder}.csv"

        if os.path.exists(audio_folder):
            print(f"Processing files in {audio_folder}...")
            results = process_audio_files(audio_folder, reference_dict, model)
            save_results_to_csv(results, results_path)
        else:
            print(f"Warning: Folder {audio_folder} does not exist. Skipping.")

if __name__ == "__main__":
    main()
