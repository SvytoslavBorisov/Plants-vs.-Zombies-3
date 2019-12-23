import pygame
import random
import os
from allConstants import *


class Sunrise(pygame.sprite.Sprite):

    def __init__(self, row, col):
        super().__init__()

        spritesNormal = plants['sunrise']
        spritesGive = plants['sunriseGiveSun']


        self.images_listNormal = []
        self.rectsNormal = []

        self.images_listGive = []
        self.spritesGive = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        self.object = []
        self.row = row
        self.col = col

        for j in range(5):
            for i in range(len(spritesNormal)):
                self.images_listNormal.append(spritesNormal[i])
                self.images_listNormal.append(spritesNormal[i])
                self.rectsNormal.append(self.images_listNormal[i].get_rect())
                self.rectsNormal.append(self.images_listNormal[i].get_rect())

        for i in range(len(spritesGive)):
            self.images_listGive.append(spritesGive[i])
            self.spritesGive.append(self.images_listGive[i].get_rect())

        self.glb_len = len(self.images_listNormal)

    def update(self):

        if self.glb_cur_frame == 0:
            self.cur_frame = (self.cur_frame + 1) % self.glb_len
            if self.cur_frame == 0:
                self.glb_len = len(self.images_listGive)
                self.image = self.images_listGive[self.cur_frame]
                self.glb_cur_frame = 1
            else:
                self.glb_len = len(self.images_listNormal)
                self.image = self.images_listNormal[self.cur_frame]
                self.glb_cur_frame = 0
        else:
            self.cur_frame = (self.cur_frame + 1) % self.glb_len
            if self.cur_frame == 0:
                self.glb_len = len(self.images_listNormal)
                self.image = self.images_listNormal[self.cur_frame]
                self.glb_cur_frame = 0
            else:
                self.glb_len = len(self.images_listGive)
                self.image = self.images_listGive[self.cur_frame]
                self.glb_cur_frame = 1
                if self.cur_frame == 10:
                    self.object.append(
                        Sun(self.row, self.col, plants['sun'], self.rectsNormal[0].x, self.rectsNormal[0].y))


class Sun(pygame.sprite.Sprite):
    def __init__(self, row, col, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = FIELD_CELL_WIDTH * row + FIELD_LEFT + 15
        self.rect.y = FIELD_CELL_HEIGHT * col + FIELD_TOP + 0
        self.coordsAnimation = [[0, 0], [0, -5], [4, -5], [6, -5], [5, 5], [0, 4], [0, 4], [0, 5], [0, 5], [0, 5]]
        self.numAnim = 0
        self.active = True

    def update(self):
        if self.active:
            if self.numAnim < len(self.coordsAnimation):
                self.rect = self.rect.move(self.coordsAnimation[int(self.numAnim)])
                self.numAnim += 0.5
            return self.rect
        else:
            del self