from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path
import numpy as np
import csv

models = ['ground_truth', 'tts1', 'tts2', 'tts3']

gt_folder = Path("../../datasets/ground_truth")

root_result = "results/resemblyzer_"

for model in models:
  syn_folder = Path("../../datasets/" + model)

  # load audio files
  gt_files = sorted(gt_folder.glob("*.wav"))
  syn_files = sorted(syn_folder.glob("*.wav"))

  assert len(gt_files) == len(syn_files), "Mismatch in number of files!"

  encoder = VoiceEncoder()

  similarities = []
  for gt_path, syn_path in zip(gt_files, syn_files):
      gt_wav = preprocess_wav(gt_path)
      syn_wav = preprocess_wav(syn_path)

      gt_embed = encoder.embed_utterance(gt_wav)
      syn_embed = encoder.embed_utterance(syn_wav)

      similarity = np.inner(gt_embed, syn_embed)  # cosine distance
      similarities.append(similarity)

      results_pth = root_result + model + ".csv"
      with open(results_pth, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([gt_path.name, model,  f"{similarity:.4f}"])

      print(f"[{gt_path.name}] Ground Truth vs {model}: Similarity = {similarity:.4f}")

  #avg_similarity = np.mean(similarities)
  #print(f"\nAverage Speaker Similarity: {avg_similarity:.4f}")
