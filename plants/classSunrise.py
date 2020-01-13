import pygame
import allConstants
import math
import random


class Sunrise(pygame.sprite.Sprite):

    def __init__(self, row, col, game):
        super().__init__()
        spritesNormal = allConstants.plants['sunrise']
        spritesGive = allConstants.plants['sunriseGiveSun']
        self.images_listNormal, self.rectsNormal = [], []
        self.images_listGive, self.spritesGive, self.objects = [], [], []
        self.cur_frame, self.glb_cur_frame = 0, 0
        self.game = game
        self.row, self.col = row, col
        self.cost = 50
        for j in range(14):
            for i in range(len(spritesNormal)):
                self.images_listNormal.append(spritesNormal[i])
                if i & 1:
                    self.images_listNormal.append(spritesNormal[i])
        for i in range(len(spritesGive)):
            self.images_listGive.append(spritesGive[i])
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
                    self.objects.append(
                        Sun(self.row, self.col, allConstants.plants['sun'], -1, -1))
        i = 0
        while i < len(self.objects):
            if self.objects[i].kill:
                del self.objects[i]
                self.game.suns += 25
            else:
                i += 1


class Sun(pygame.sprite.Sprite):
    def __init__(self, row, col, image, x, y):
        super().__init__()
        self.image = image
        self.type = 'sun'
        self.kill = False
        self.row = row
        self.col = col
        if x == -1 and y == -1:
            self.const = self.image.get_rect()
            self.const.x = allConstants.FIELD_CELL_WIDTH * row + allConstants.FIELD_LEFT + 10
            self.const.y = allConstants.FIELD_CELL_HEIGHT * col + allConstants.FIELD_TOP - 25

            self.rect = self.image.get_rect()
            self.rect.x = allConstants.FIELD_CELL_WIDTH * row + allConstants.FIELD_LEFT + 10
            self.rect.y = allConstants.FIELD_CELL_HEIGHT * col + allConstants.FIELD_TOP - 25

            self.coordsAnimation = []
            for i in range(4):
                self.coordsAnimation.append([2, -4.5])
            for i in range(4):
                self.coordsAnimation.append([1, 4.5])
            for i in range(7):
                self.coordsAnimation.append([0.5, 4.5])
            self.numAnim = 0
            self.active = True
        else:
            self.const = self.image.get_rect()
            self.const.x = x
            self.const.y = y

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.coordsAnimation = []
            for i in range(random.randint(24, 50)):
                self.coordsAnimation.append([0, 5])
            self.numAnim = 0
            self.active = True

    def update(self, *args):
        if self.active:
            if self.numAnim < len(self.coordsAnimation):
                self.rect = self.rect.move(self.coordsAnimation[int(self.numAnim)])
                self.numAnim += 0.5
            return self.rect
        elif self.active == False:

            pos = pygame.math.Vector2((self.rect.x, self.rect.y))
            dir = pygame.math.Vector2((170, 0)) - pos
            distance = dir.length()
            if distance > 0:
                dir = dir / distance
                pos += dir * min(distance, 20)
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                return self.rect
            self.kill = True
            del self