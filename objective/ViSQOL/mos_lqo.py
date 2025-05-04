import os
import csv
from pathlib import Path
import librosa
import numpy as np
from visqol import visqol_lib_py
from visqol.pb2 import visqol_config_pb2


def load_audio_files(gt_folder: Path, syn_folder: Path):
    gt_files = sorted(gt_folder.glob("*.wav"))
    syn_files = sorted(syn_folder.glob("*.wav"))
    
    assert len(gt_files) == len(syn_files), f"Mismatch: {len(gt_files)} ground-truth vs {len(syn_files)} synthetic files"
    return gt_files, syn_files


def get_visqol_config(mode: str = "audio") -> visqol_config_pb2.VisqolConfig:
    config = visqol_config_pb2.VisqolConfig()

    if mode == "audio":
        config.audio.sample_rate = 48000
        config.options.use_speech_scoring = False
        svr_model = "libsvm_nu_svr_model.txt"
    elif mode == "speech":
        config.audio.sample_rate = 16000
        config.options.use_speech_scoring = True
        svr_model = "lattice_tcditugenmeetpackhref_ls2_nl60_lr12_bs2048_learn.005_ep2400_train1_7_raw.tflite"
    else:
        raise ValueError(f"Unknown mode '{mode}'. Use 'audio' or 'speech'.")

    config.options.svr_model_path = os.path.join(
        os.path.dirname(visqol_lib_py.__file__), "model", svr_model
    )
    return config


def compute_visqol_scores(gt_files, syn_files, config, output_csv_path: str):
    api = visqol_lib_py.VisqolApi()
    api.Create(config)

    with open(output_csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "MOS-LQO"])

        for gt_path, syn_path in zip(gt_files, syn_files):
            try:
                #ref_audio, _ = librosa.load(gt_path, sr=config.audio.sample_rate, mono=True)
                #deg_audio, _ = librosa.load(syn_path, sr=config.audio.sample_rate, mono=True)

                #ref_audio = ref_audio.astype(np.float64)
                #deg_audio = deg_audio.astype(np.float64)

                ref_audio, _ = librosa.load(gt_path, sr=config.audio.sample_rate, mono=True, dtype=np.float64)
                deg_audio, _ = librosa.load(syn_path, sr=config.audio.sample_rate, mono=True, dtype=np.float64)

                # Ensure equal length
                min_len = min(len(ref_audio), len(deg_audio))
                ref_audio = ref_audio[:min_len]
                deg_audio = deg_audio[:min_len]

                result = api.Measure(ref_audio.tolist(), deg_audio.tolist())
                moslqo = result.moslqo

                writer.writerow([gt_path.name, f"{moslqo:.4f}"])
                print(f"[{gt_path.name}] MOS-LQO = {moslqo:.4f}")

            except Exception as e:
                print(f"⚠️ Error with {gt_path.name}: {e}")


def run_all_models(gt_folder: Path, models: list[str], mode: str = "audio"):
    config = get_visqol_config(mode)
    result_dir = Path("results")
    result_dir.mkdir(exist_ok=True)

    for model in models:
        syn_folder = Path(f"dataset/{model}")
        output_csv = result_dir / f"ViSQOL_{model}.csv"

        print(f"\n🔍 Running ViSQOL for model: {model}")
        gt_files, syn_files = load_audio_files(gt_folder, syn_folder)
        compute_visqol_scores(gt_files, syn_files, config, str(output_csv))


def main():
    models = ["tts1", "tts2", "tts3"]
    gt_folder = Path("dataset/ground_truth")
    run_all_models(gt_folder, models, mode="audio")  # Change to "speech" if needed


if __name__ == "__main__":
    main()
