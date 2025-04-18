from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
import numpy as np
import csv

def load_audio_files(gt_folder, syn_folder):
    gt_files = sorted(gt_folder.glob("*.wav"))
    syn_files = sorted(syn_folder.glob("*.wav"))
    assert len(gt_files) == len(syn_files), "Mismatch in number of files!"
    return gt_files, syn_files

def compute_similarity(gt_files, syn_files, encoder):
    results = [["filename", "score"]]  # header

    for gt_path, syn_path in zip(gt_files, syn_files):
        gt_wav = preprocess_wav(gt_path)
        syn_wav = preprocess_wav(syn_path)

        gt_embed = encoder.embed_utterance(gt_wav)
        syn_embed = encoder.embed_utterance(syn_wav)

        similarity = np.inner(gt_embed, syn_embed)
        results.append([gt_path.name, f"{similarity:.4f}"])
        
        print(f"[{gt_path.name}] Ground Truth vs {syn_path.parent.name}: Similarity = {similarity:.4f}")

    return results

def save_results_to_csv(results, results_pth):
    with open(results_pth, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(results)

def main():
    models = ['ground_truth', 'tts1', 'tts2', 'tts3']
    gt_folder = Path("dataset/ground_truth")
    root_result = "results/Resemblyzer_"
    encoder = VoiceEncoder()
    
    for model in models:
        syn_folder = Path("dataset/" + model)
        results_pth = root_result + model + ".csv"

        gt_files, syn_files = load_audio_files(gt_folder, syn_folder)
        results = compute_similarity(gt_files, syn_files, encoder)
        save_results_to_csv(results, results_pth)

if __name__ == "__main__":
    main()
