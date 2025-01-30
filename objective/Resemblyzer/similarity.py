from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
import numpy as np
import csv

def load_audio_files(gt_folder, syn_folder):
    """
    Loads and sorts the audio files from ground truth and synthetic folders.
    
    Args:
        gt_folder (Path): Path to the ground truth audio folder.
        syn_folder (Path): Path to the synthetic audio folder.
    
    Returns:
        list, list: Sorted lists of ground truth and synthetic audio file paths.
    """
    gt_files = sorted(gt_folder.glob("*.wav"))
    syn_files = sorted(syn_folder.glob("*.wav"))
    
    assert len(gt_files) == len(syn_files), "Mismatch in number of files!"
    
    return gt_files, syn_files

def compute_similarity(gt_files, syn_files, encoder, results_pth):
    """
    Computes speaker similarity between ground truth and synthetic audio files.
    
    Args:
        gt_files (list): List of ground truth audio file paths.
        syn_files (list): List of synthetic audio file paths.
        encoder (VoiceEncoder): Pretrained speaker encoder.
        results_pth (str): Path to save the CSV results.
    """
    with open(results_pth, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "score"])
    
    for gt_path, syn_path in zip(gt_files, syn_files):
        gt_wav = preprocess_wav(gt_path)
        syn_wav = preprocess_wav(syn_path)

        gt_embed = encoder.embed_utterance(gt_wav)
        syn_embed = encoder.embed_utterance(syn_wav)

        similarity = np.inner(gt_embed, syn_embed)  # cosine distance
        
        with open(results_pth, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([gt_path.name, f"{similarity:.4f}"])
        
        print(f"[{gt_path.name}] Ground Truth vs {syn_path.parent.name}: Similarity = {similarity:.4f}")

def main():
    models = ['ground_truth', 'tts1', 'tts2', 'tts3']
    gt_folder = Path("../../datasets/ground_truth")
    root_result = "results/resemblyzer_"
    encoder = VoiceEncoder()
    
    for model in models:
        syn_folder = Path("../../datasets/" + model)
        results_pth = root_result + model + ".csv"
        
        gt_files, syn_files = load_audio_files(gt_folder, syn_folder)
        compute_similarity(gt_files, syn_files, encoder, results_pth)

if __name__ == "__main__":
    main()
