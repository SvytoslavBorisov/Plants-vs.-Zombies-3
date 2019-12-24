import pygame
from allConstants import *


class justZombie(pygame.sprite.Sprite):
    def __init__(self, row, hp):
        super().__init__()
        self.hp = hp
        self.x = WIDTH2
        self.y = row * FIELD_CELL_HEIGHT 
        self.cur = 0

    
class konusZombie(justZombie):        
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['konus']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x -= 1
        self.image = self.data[self.cur]
        self.rect.x = self.x
        self.cur += 1
        self.cur %= len(self.data)
        if self.x < 140:
            self.kill()
