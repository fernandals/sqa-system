import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import csv
import os
import pygame

import csv
from typing import List, Dict

def load_dataset(metadata_path: str = "datasets/metadata.csv") -> List[Dict[str, str]]:
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

    print(data)

    return data


# Função para salvar resultados no CSV
def save_to_csv(data, filename="resultados.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ParticipantID", "AudioID", "MOS", "Similarity", "Transcription"])
        writer.writerow(data)

# Função para tocar áudio
def play_audio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

# Classe principal da aplicação
class TTSQualityTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TTS Quality Test")
        self.audio_files = load_dataset()
        self.current_audio_index = 0
        self.participant_id = simpledialog.askstring("ID", "Digite seu ID ou nome:")
        
        # Variáveis para capturar as respostas
        self.mos_score = tk.IntVar()
        self.similarity_score = tk.IntVar()
        self.transcription = tk.StringVar()
        
        # Tela inicial
        self.init_screen()
    
    def init_screen(self):
        tk.Label(self.root, text="Bem-vindo ao teste de TTS!").pack(pady=10)
        tk.Label(self.root, text="Pressione Iniciar para começar.").pack(pady=10)
        tk.Button(self.root, text="Iniciar", command=self.start_test).pack(pady=20)
    
    def start_test(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.test_screen()
    
    def test_screen(self):
        if self.current_audio_index >= len(self.audio_files):
            self.end_screen()
            return
        
        audio_id = self.audio_files[self.current_audio_index]
        tk.Label(self.root, text=f"Avaliando: {audio_id}").pack(pady=10)
        
        # Botão para tocar o áudio
        tk.Button(self.root, text="Reproduzir Áudio", command=lambda: play_audio(audio_id)).pack(pady=10)
        
        # Escalas de avaliação
        tk.Label(self.root, text="Qualidade (MOS):").pack(pady=5)
        tk.Scale(self.root, from_=1, to=5, orient="horizontal", variable=self.mos_score).pack(pady=5)
        
        tk.Label(self.root, text="Similaridade de Locutor:").pack(pady=5)
        tk.Scale(self.root, from_=1, to=5, orient="horizontal", variable=self.similarity_score).pack(pady=5)
        
        # Campo de transcrição
        tk.Label(self.root, text="Digite o texto ouvido:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.transcription).pack(pady=5)
        
        # Botão para avançar
        tk.Button(self.root, text="Próximo", command=self.save_response).pack(pady=20)
    
    def save_response(self):
        # Salvar os dados no CSV
        audio_id = self.audio_files[self.current_audio_index]
        data = [
            self.participant_id,
            audio_id,
            self.mos_score.get(),
            self.similarity_score.get(),
            self.transcription.get()
        ]
        save_to_csv(data)
        
        # Avançar para o próximo áudio
        self.current_audio_index += 1
        for widget in self.root.winfo_children():
            widget.destroy()
        self.test_screen()
    
    def end_screen(self):
        tk.Label(self.root, text="Obrigado por participar!").pack(pady=20)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(pady=20)

# Executar o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = TTSQualityTestApp(root)
    root.mainloop()
