import pygame
import random
import os
from allConstants import *


class Squash(pygame.sprite.Sprite):

    def __init__(self, row, col):
        super().__init__()

        spritesNormal = plants['squash']

        self.cost = 75

        self.images_listNormal = []
        self.rectsNormal = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        self.objects = []
        self.row = row
        self.col = col

        for i in range(len(spritesNormal)):
            self.images_listNormal.append(spritesNormal[i])
            self.rectsNormal.append(self.images_listNormal[i].get_rect())

        self.glb_len = len(self.images_listNormal)

    def update(self, *args):

        self.cur_frame = (self.cur_frame + 1) % self.glb_len
        self.image = self.images_listNormal[self.cur_frame]