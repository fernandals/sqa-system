import pandas as pd
import glob

def load_metric_results(metric_folder):
    """
    Loads speaker similarity or WER scores from CSV files in a given metric folder.

    Args:
        metric_folder (str): Name of the folder containing result CSV files.

    Returns:
        pd.DataFrame: A DataFrame where columns represent different models,
                      indexed by filenames, with scores as values.
    """
    csv_files = glob.glob(metric_folder + "/results/*.csv")
    metric_data = {}

    for file in csv_files:
        model_name = file.split("/")[-1].replace(".csv", "")  # extract model name from filename
        df = pd.read_csv(file)

        if "filename" in df.columns and "score" in df.columns:
            metric_data[model_name] = df.set_index("filename")["score"]
        else:
            print(f"Warning: Skipping {file} as it does not contain expected columns.")

    # sorting columns alphabetically
    return pd.DataFrame(metric_data).sort_index(axis=1)


def main():
    """
    Loads and compares speaker similarity or WER scores from different models,
    then saves the results in a comparative CSV file for each metric.
    """

    metrics_folders = ['UTMOS', 'Resemblyzer', 'Whisper']

    for metric in metrics_folders:
        comparative_df = load_metric_results(metric)
        
        if not comparative_df.empty:
            comparative_df.to_csv(f"{metric}_comparison.csv")
            print(f"Saved {metric}_comparison.csv")
        else:
            print(f"Warning: No valid data found for {metric}. Skipping.")

if __name__ == "__main__":
    main()
