import pygame
import random
import os
from allConstants import *


class Squash(pygame.sprite.Sprite):

    def __init__(self, row, col):
        super().__init__()

        spritesNormal = plants['squash']
        spritesJump = plants['squashJump']

        self.cost = 75

        self.images_listNormal = []
        self.images_listJump = []
        self.rectsNormal = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        self.cur_frameJump = 0

        self.objects = []
        self.row = row
        self.col = col
        self.jump = True
        self.x = 1
        self.y = 1

        self.coordsAnimation = []
        for i in range(8):
            self.coordsAnimation.append([4, -8])
        for i in range(8):
            self.coordsAnimation.append([3, +7])
        for i in range(4):
            self.coordsAnimation.append([2, 1])
        self.numAnim = 0

        for i in range(len(spritesNormal)):
            self.images_listNormal.append(spritesNormal[i])
            self.rectsNormal.append(self.images_listNormal[i].get_rect())

        for i in range(len(spritesJump)):
            self.images_listJump.append(spritesJump[i])
            self.rectsNormal.append(self.images_listJump[i].get_rect())

        self.glb_len = len(self.images_listNormal)
        self.glb_lenJump = len(self.images_listJump)

    def update(self, *args):

        if self.jump:
            self.cur_frame = (self.cur_frame + 1) % self.glb_len
            self.image = self.images_listNormal[self.cur_frame]
            x = FIELD_CELL_WIDTH * self.row + FIELD_LEFT
            for z in zs:
                if x >= z.x >= x - 100 and self.col == z.row:
                    self.jump = False
            return [self.x, self.y]
        else:
            self.cur_frameJump = (self.cur_frameJump + 1) % self.glb_lenJump
            self.image = self.images_listJump[self.cur_frameJump]
            self.x += self.coordsAnimation[self.numAnim][0]
            self.y += self.coordsAnimation[self.numAnim][1]
            self.numAnim += 1
            if self.cur_frameJump + 1 == self.glb_lenJump:
                x = FIELD_CELL_WIDTH * self.row + FIELD_LEFT
                for z in zs:
                    if x >= z.x >= x - 100 and self.col == z.row:
                        z.hp = 0
                return 'DEL'
            return [self.x, self.y]