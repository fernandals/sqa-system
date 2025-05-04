from pathlib import Path
import csv
import utmosv2  # Installed via pip from GitHub

def compute_mos_scores(model, audio_paths):
    results = [["filename", "mos"]]
    for path in audio_paths:
        mos = model.predict(input_path=str(path))
        results.append([path.name, f"{mos:.4f}"])
        print(f"[{path.name}] MOS = {mos:.4f}")
    return results

def save_results_to_csv(results, output_csv):
    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(results)

def main():
    models = ['ground_truth', 'tts1', 'tts2', 'tts3']
    root_data = Path("dataset")
    root_result = Path("results")

    model = utmosv2.create_model(pretrained=True)
    
    for model_name in models:
        folder = root_data / model_name
        audio_paths = sorted(folder.glob("*.wav"))
        results = compute_mos_scores(model, audio_paths)
        
        output_csv = root_result / f"UTMOS_{model_name}.csv"
        save_results_to_csv(results, output_csv)

if __name__ == "__main__":
    main()
