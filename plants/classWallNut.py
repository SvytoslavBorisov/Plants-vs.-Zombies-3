import pygame
import random
import os
from allConstants import *


class WallNut(pygame.sprite.Sprite):

    def __init__(self, row, col):
        super().__init__()

        spritesNormal = plants['wallNut']

        self.images_list = []
        self.objects = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        self.row = row
        self.col = col

        for i in range(len(spritesNormal)):
            self.images_list.append(spritesNormal[i])

        self.glb_len = len(self.images_list)

    def update(self, *args):
        self.cur_frame = (self.cur_frame + 1) % self.glb_len
        self.image = self.images_list[self.cur_frame]

