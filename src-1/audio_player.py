import threading
import time
from tkinter import ttk
import pygame

class AudioPlayer:
    def __init__(self, root, audio_path):
        self.root = root
        self.audio_path = audio_path
        self.is_playing = False
        self.current_time = 0

        # Inicializar pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_path)
        self.audio_length = pygame.mixer.Sound(self.audio_path).get_length()

        # Criar os widgets do reprodutor
        self.create_widgets()

    def create_widgets(self):
        # Botão Play/Pause
        self.play_button = ttk.Button(self.root, text="Play", command=self.toggle_play_pause)
        self.play_button.pack(pady=10)

        # Barra de progresso
        self.progress = ttk.Scale(self.root, from_=0, to=self.audio_length, orient="horizontal", length=300)
        self.progress.pack(pady=10)
        self.progress.bind("<ButtonRelease-1>", self.seek_audio)

        # Thread para atualizar progresso
        self.update_thread = threading.Thread(target=self.update_progress, daemon=True)
        self.update_thread.start()

    def toggle_play_pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.play_button.config(text="Play")
        else:
            pygame.mixer.music.unpause() if pygame.mixer.music.get_busy() else pygame.mixer.music.play()
            self.play_button.config(text="Pause")
        self.is_playing = not self.is_playing

    def seek_audio(self, event):
        new_time = self.progress.get()
        pygame.mixer.music.play(start=new_time)
        self.is_playing = True
        self.play_button.config(text="Pause")

    def update_progress(self):
        while True:
            if self.is_playing:
                self.current_time = pygame.mixer.music.get_pos() / 1000
                self.progress.set(self.current_time)
            time.sleep(0.1)
