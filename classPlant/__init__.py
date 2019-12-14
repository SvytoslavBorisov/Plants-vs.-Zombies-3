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

    def __init__(self, fileOfSprite, count, size):
        super().__init__()
        self.images_list = []
        self.rects = []
        self.cur_frame = 0
        if count != 0:
            for i in range(count):
                self.images_list.append(load_image(f'{fileOfSprite}/{i}.png', size))
                self.rects.append(self.images_list[i].get_rect())
        else:
            self.images_list.append(load_image(f'{fileOfSprite}.png', size))
            self.rects.append(self.images_list[0].get_rect())

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.images_list)
        self.image = self.images_list[self.cur_frame]