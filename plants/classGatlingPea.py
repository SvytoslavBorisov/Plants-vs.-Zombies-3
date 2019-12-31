import pygame
import random
import os
from allConstants import *


class GatlingPea(pygame.sprite.Sprite):

    def __init__(self, row, col):
        super().__init__()

        spritesNormal = plants['gatlingPea']
        spritesShoot = plants['gatlingPeaShoot']

        self.images_listNormal = []
        self.rectsNormal = []

        self.objects = []
        self.cost = 75

        self.images_listShoot = []
        self.rectsShoot = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        self.row = row
        self.col = col

        for i in range(len(spritesNormal)):
            self.images_listNormal.append(spritesNormal[i])
            self.rectsNormal.append(self.images_listNormal[i].get_rect())

        for i in range(len(spritesShoot)):
            self.images_listShoot.append(spritesShoot[i])
            self.rectsShoot.append(self.images_listShoot[i].get_rect())

        self.glb_len = len(self.images_listNormal)

    def update(self, *args):
        if self.glb_cur_frame == 0:
            self.cur_frame = (self.cur_frame + 1) % self.glb_len
            if self.cur_frame == 0:
                self.glb_len = len(self.images_listShoot)
                self.image = self.images_listShoot[self.cur_frame]
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
                self.glb_len = len(self.images_listShoot)
                self.image = self.images_listShoot[self.cur_frame]
                self.glb_cur_frame = 1
                if self.cur_frame == 10:
                    self.objects.append(
                        Pea(self.row, self.col, plants['pea'], self.rectsNormal[0].x, self.rectsNormal[0].y))
        i = 0
        while i < len(self.objects):
            if self.objects[i].kill:
                del self.objects[i]
            else:
                i += 1


class Pea(pygame.sprite.Sprite):

    def __init__(self, row, col, image, x, y):
        super().__init__()
        self.image = image
        self.type = 'pea'
        self.rect = self.image.get_rect()
        self.rect.x = FIELD_CELL_WIDTH * row + FIELD_LEFT + 55
        self.rect.y = FIELD_CELL_HEIGHT * col + FIELD_TOP + 15
        self.row = col
        self.col = row
        self.kill = False

    def update(self, *args):
        self.rect = self.rect.move(10, 0)
        if self.rect.x > WIDTH2:
            self.kill = True
            return None
        for z in zs:
            if self.rect.x - 80 >= z.x >= self.rect.x - 90 and self.row == z.row:
                z.hp -= 10
                self.kill = True
                return None
        return self.rect
