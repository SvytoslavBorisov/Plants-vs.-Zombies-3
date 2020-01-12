import pygame
import random
import os
from allConstants import *


class Squash(pygame.sprite.Sprite):
    def __init__(self, row, col):
        super().__init__()
        spritesNormal, spritesJump = plants['squash'],  plants['squashJump']
        self.images_listNormal, self.images_listJump, self.objects, self.coordsAnimation = [], [], [], []
        self.cur_frame, self.glb_cur_frame, self.cur_frameJump, self.numAnim = 0, 0, 0, 0
        self.row, self.col, self.jump = row, col, True
        self.x, self.y, self.cost = 1, 1, 75
        for i in range(8):
            self.coordsAnimation.append([4, -8])
        for i in range(8):
            self.coordsAnimation.append([3, +7])
        for i in range(4):
            self.coordsAnimation.append([2, 1])
        for i in range(len(spritesNormal)):
            self.images_listNormal.append(spritesNormal[i])
        for i in range(len(spritesJump)):
            self.images_listJump.append(spritesJump[i])
        self.glb_len, self.glb_lenJump = len(self.images_listNormal), len(self.images_listJump)

    def update(self, *args):
        x = FIELD_CELL_WIDTH * self.row + FIELD_LEFT
        if self.jump:
            self.cur_frame = (self.cur_frame + 1) % self.glb_len
            self.image = self.images_listNormal[self.cur_frame]
            for z in zs:
                if x >= z.x >= x - 100 and self.col == z.row:
                    self.jump = False
        else:
            self.cur_frameJump = (self.cur_frameJump + 1) % self.glb_lenJump
            self.image = self.images_listJump[self.cur_frameJump]
            self.x += self.coordsAnimation[self.numAnim][0]
            self.y += self.coordsAnimation[self.numAnim][1]
            self.numAnim += 1
            if self.cur_frameJump + 1 == self.glb_lenJump:
                for z in zs:
                    if x >= z.x >= x - 100 and self.col == z.row:
                        z.hp = 0
                return 'DEL'
        return [self.x, self.y]