import os
import csv
import whisper
from jiwer import wer, process_words

def read_reference_file(file_path):
    """
    Reads a file organized as `audio_id|reference_text` and returns a dictionary.

    Args:
        file_path (str): Path to the file containing audio IDs and reference texts.

    Returns:
        dict: A dictionary where the key is the audio ID and the value is the reference text.
    """
    reference_dict = {}

    with open(file_path, "r") as file:
        for line in file:
            audio_id, reference_text = line.strip().split("|", maxsplit=1)
            reference_dict[audio_id] = reference_text

    return reference_dict

def process_audio_files(audio_folder, reference_dict, model, csv_writer):
    """
    Process all .wav files in the folder, transcribe them, and calculate WER.

    Args:
        audio_folder (str): Path to the folder containing .wav files.
        reference_dict (dict): Dictionary mapping audio IDs to reference texts.
        model: The Whisper model for transcription.
        csv_writer: CSV writer object to write results to a file.
    """
    for filename in os.listdir(audio_folder):
        if filename.endswith(".wav"):
            audio_file = os.path.join(audio_folder, filename)

            # getting transcriptions            
            result = model.transcribe(audio_file)
            transcription = result["text"]
            
            audio_id = os.path.splitext(filename)[0]  # remove the .wav extension
            reference_text = reference_dict.get(audio_id, "")
            
            if not reference_text:
                print(f"Warning: No reference text found for {filename}. Skipping.")
                continue
            
            print(reference_text, "--", transcription)

            output = process_words(reference_text, transcription)
            error_rate = output.wer

            #error_rate = wer(reference_text, transcription)
            
            csv_writer.writerow([audio_id, f"{error_rate:.4f}"])

def main():
    model = whisper.load_model("small") 

    root_audio_folder = "../../datasets/"
    reference_file = "../../datasets/test_sentences.txt"

    reference_dict = read_reference_file(reference_file)

    # for each model calculate wer
    for model_folder in ['ground_truth', 'tts1', 'tts2', 'tts3']:
        with open("results/whisper_" + model_folder + ".csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  

            csv_writer.writerow(["filename", "score"])

            audio_folder = os.path.join(root_audio_folder, model_folder)
            if os.path.exists(audio_folder):
                print(f"Processing files in {audio_folder}...")
                process_audio_files(audio_folder, reference_dict, model, csv_writer)
            else:
                print(f"Warning: Folder {audio_folder} does not exist. Skipping.")

if __name__ == "__main__":
    main()
