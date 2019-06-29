import pygame as py
# to manage the sounds
class soundtrack():
    path = "./assets/song.mp3"

    def __init__(sef):
        py.mixer.init()
        return

    def load(self):
        py.mixer.music.load(self.path)
        return

    def play(self):
        py.mixer.music.play()
        return
