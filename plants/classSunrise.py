import pygame
import allConstants


class Sunrise(pygame.sprite.Sprite):

    def __init__(self, row, col, game):
        super().__init__()

        spritesNormal = allConstants.plants['sunrise']
        spritesGive = allConstants.plants['sunriseGiveSun']

        self.images_listNormal = []
        self.rectsNormal = []

        self.images_listGive = []
        self.spritesGive = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        self.game = game

        self.objects = []
        self.row = row
        self.col = col
        self.cost = 50

        for j in range(1):
            for i in range(len(spritesNormal)):
                self.images_listNormal.append(spritesNormal[i])
                if i & 1:
                    self.images_listNormal.append(spritesNormal[i])
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
                    self.objects.append(
                        Sun(self.row, self.col, allConstants.plants['sun'], self.rectsNormal[0].x, self.rectsNormal[0].y))
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

    def update(self, *args):
        if self.active:
            if self.numAnim < len(self.coordsAnimation):
                self.rect = self.rect.move(self.coordsAnimation[int(self.numAnim)])
                self.numAnim += 0.5
            return self.rect
        elif self.active == False:
            if self.rect.x > 270 or self.rect.y > 15:
                self.rect = self.rect.move([-abs(self.const.x - 270) / 10, -abs(self.const.y - 15) / 10])
                return self.rect
            else:
                self.kill = True
                del self