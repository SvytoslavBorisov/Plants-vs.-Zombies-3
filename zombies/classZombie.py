import pygame
from allConstants import *


class justZombie(pygame.sprite.Sprite):
    def __init__(self, row, hp):
        super().__init__()
        self.hp = hp
        self.x = WIDTH2
        self.y = row * FIELD_CELL_HEIGHT + 25
        self.cur = 0
        self.row = row

    def update(self):
        self.x -= 0.5
        self.image = self.data[self.cur]
        self.rect.x = self.x
        self.cur += 1
        self.cur %= len(self.data)
        print(self.hp)
        if self.x < 140 or self.hp <= 0:
            self.kill()


class konusZombie(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['konus']
        self.dataDamage1 = zombies['konusDamage1']
        self.dataDamage2 = zombies['konusDamage2']
        self.dataDamage3 = zombies['normal']
        # self.data += self.dataDamage1 + self.dataDamage2 + self.dataDamage3  # TEST
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        super().update()
        only = zombies_hp['konus'] - zombies_hp['normal']
        if only // 3 * 2 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage1
        if only // 3 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage2
        if self.hp <= zombies_hp['normal']:
            self.data = self.dataDamage3


class normalZombie(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['normal']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class normalZombieWithFlag(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['normalWithFlag']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class bucketZombie(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['bucket']
        self.dataDamage1 = zombies['bucketDamage1']
        self.dataDamage2 = zombies['bucketDamage2']
        self.dataDamage3 = zombies['normal']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        super().update()
        only = zombies_hp['bucket'] - zombies_hp['normal']
        if only // 3 * 2 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage1
        if only // 3 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage2
        if self.hp <= zombies_hp['normal']:
            self.data = self.dataDamage3
