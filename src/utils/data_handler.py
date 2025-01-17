import csv
import random
import uuid

from typing import List, Dict

class DataHandler:
    def __init__(self):
        self.audio_files = self.load_dataset()
        self.current_audio_index = 0
        self.participant_id = str(uuid.uuid4())  # Generate a unique UUID for the participant

        # Selecionando amostras igualmente
        models = [name for name in self.audio_files[0].keys() if name not in {'audio_id', 'ground_truth'}]

        samples_per_model = len(self.audio_files) // len(models)
        remainder = len(self.audio_files) % len(models)

        self.balanced_model_list = models * samples_per_model
        self.balanced_model_list += random.sample(models, remainder)  # adiciona o resto aleatoriamente
        random.shuffle(self.balanced_model_list)

    def load_dataset(self, metadata_path: str = "datasets/metadata.csv") -> List[Dict[str, str]]:
        """Load dataset metadata from a CSV file, extracting TTS folders dynamically.

        Args:
            metadata_path (str): Path to the metadata CSV file.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing metadata, 
                                with TTS folders as individual keys.
        """
        data = []

        try:
            with open(metadata_path, mode="r") as metadata_file:
                reader = csv.DictReader(metadata_file)
                
                for row in reader:
                    tts_folders = {
                        # change this start with for another keyword !
                        key: value for key, value in row.items() if key.startswith("tts")
                    }
                    
                    record = {
                        "audio_id": row["audio_id"],
                        "ground_truth": row["ground_truth"],
                    }
                    record.update(tts_folders)
                    
                    data.append(record)

        except FileNotFoundError:
            print(f"Error: Metadata file not found at {metadata_path}")
        except KeyError as e:
            print(f"Error: Missing expected column in metadata file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data