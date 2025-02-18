import csv
import random
import uuid
import os

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

    def load_dataset(self, metadata_path: str = "../datasets/metadata.txt") -> List[Dict[str, str]]:
        """Load dataset metadata from a TXT file, parsing fields separated by '|'.

        Args:
            metadata_path (str): Path to the metadata TXT file.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing metadata, 
                                  with TTS folders as individual keys.
        """
        data = []

        try:
            with open(metadata_path, mode="r") as metadata_file:
                for line in metadata_file:
                    fields = line.strip().split("|")
                    
                    if len(fields) < 3:
                        print(f"Skipping malformed line: {line.strip()}")
                        continue
                    
                    record = {
                        "audio_id": fields[0],
                        "ground_truth": fields[1],
                        "tts1": fields[2],
                        "tts2": fields[3] if len(fields) > 3 else None,
                        "tts3": fields[4] if len(fields) > 4 else None
                    }
                    
                    data.append(record)

        except FileNotFoundError:
            print(f"Error: Metadata file not found at {metadata_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data
        
    def save_response(self, responses, filename="results.csv"):
        """
        Save the collected responses to a CSV file.

        Args:
        - responses (list): List of dictionaries containing participant_id, audio_id, test_type, and response
        - filename (str): The CSV filename to save the data
        """
        file_exists = os.path.isfile(filename)
        
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["ParticipantID", "ModelID", "AudioID", "TestType", "Response"])

            for response in responses:
                test_type = response['test_type']
                response_value = response['response']
                
                row = [response['participant_id'], response['model_id'], response['audio_id'], test_type, response_value]
                writer.writerow(row)

    def save_participant_info(self, participant_id, age, occupation, filename="participants_info.csv"):
        """
        Save participant's personal information (ID, Age, Occupation) to a CSV file.

        Args:
        - participant_id (str): Unique identifier for the participant
        - age (str): Age of the participant
        - occupation (str): Participant's occupation
        - filename (str): The CSV filename to save the data
        """
        file_exists = os.path.isfile(filename)

        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["ParticipantID", "Age", "Occupation"])

            writer.writerow([participant_id, age, occupation])