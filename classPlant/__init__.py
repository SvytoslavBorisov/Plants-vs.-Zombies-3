import pygame
import random
import os


size = width, height = 1366, 768


def load_image(name, size, colorkey=None):
    fullname = os.path.join('Graphics', name)
    if size != (0, 0):
        return pygame.transform.scale(pygame.image.load(fullname).convert_alpha(), size)
    else:
        return pygame.image.load(fullname).convert()


class Plant(pygame.sprite.Sprite):

    def __init__(self, fileOfSprite, size):
        super().__init__()
        self.image = load_image(f'{fileOfSprite}.png', size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)