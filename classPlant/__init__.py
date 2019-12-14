import pygame
import random
import os


size = width, height = 700, 600


def load_image(name, size, colorkey=None):
    fullname = os.path.join(name)
    if size != (0, 0):
        return pygame.transform.scale(pygame.image.load(fullname).convert_alpha(), size)
    else:
        return pygame.image.load(fullname).convert()


class Plant(pygame.sprite.Sprite):

    def __init__(self, sprites):
        super().__init__()
        self.images_list = []
        self.rects = []
        self.cur_frame = 0
        for i in range(len(sprites)):
            self.images_list.append(sprites[i])
            self.rects.append(self.images_list[i].get_rect())

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.images_list)
        self.image = self.images_list[self.cur_frame]


class GatlingPea(Plant):

    def __init__(self, spritesNormal, spritesShoot):
        self.images_listNormal = []
        self.rectsNormal = []

        self.images_listShoot = []
        self.rectsShoot = []

        self.cur_frame = 0
        self.glb_cur_frame = 0

        for i in range(len(spritesNormal)):
            self.images_listNormal.append(spritesNormal[i])
            self.rectsNormal.append(self.images_listNormal[i].get_rect())

        for i in range(len(spritesShoot)):
            self.images_listShoot.append(spritesShoot[i])
            self.rectsShoot.append(self.images_listShoot[i].get_rect())

        self.glb_len = len(self.images_listNormal)

    def update(self):

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