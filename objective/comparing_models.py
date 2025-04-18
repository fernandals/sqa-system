import pandas as pd
import glob
import os

def load_metric_results(metric_prefix):
    """
    Loads CSV result files that start with a given metric prefix from the results folder.

    Args:
        metric_prefix (str): Prefix used in the result filenames (e.g., 'UTMOS').

    Returns:
        pd.DataFrame: A DataFrame with models as columns and filenames as index.
    """
    csv_files = glob.glob(f"results/{metric_prefix}_*.csv")
    metric_data = {}

    for file in csv_files:
        base_name = os.path.basename(file)
        model_name = base_name.replace(f"{metric_prefix}_", "").replace(".csv", "")

        df = pd.read_csv(file)
        if "filename" in df.columns and "score" in df.columns:
            metric_data[model_name] = df.set_index("filename")["score"]
        else:
            print(f"Warning: Skipping {file} as it does not contain expected columns.")

    if metric_data:
        return pd.DataFrame(metric_data).sort_index(axis=1)
    else:
        return pd.DataFrame()  # return empty dataframe if nothing valid

def main():
    # metrics = ['UTMOS', 'resemblyzer', 'whisper', 'visqol']
    metrics = ['Resemblyzer', 'Whisper']

    for metric in metrics:
        df = load_metric_results(metric)
        if not df.empty:
            df.to_csv(f"results/{metric}_comparison.csv")
            print(f"✅ Saved results/{metric}_comparison.csv")
        else:
            print(f"⚠️  No valid data found for {metric}. Skipping.")

if __name__ == "__main__":
    main()
