import pygame


class Game:
    def __init__(self, suns):
        self.suns = suns
        self.soundVolume = 0
        self.time = 0
        self.name = 'NoName'