import pygame
import sys
from allConstants import *


class justZombie(pygame.sprite.Sprite):
    def __init__(self, row, hp):
        super().__init__()
        self.hp = hp
        self.speed = 0.5
        self.x = WIDTH2
        self.y = row * FIELD_CELL_HEIGHT + 25
        self.cur = 0
        self.row = row

    def update(self):
        self.image = self.data[self.cur]
        self.rect.x = self.x
        self.cur += 1
        self.cur %= len(self.data)
        self.x -= self.speed
        if self.hp <= 0:
            self.kill()
        elif 100 < self.x < 140:
            if lownmowers[self.row] == 0:
                lownmowers[self.row] = FIELD_LEFT
        elif self.x <= 100:
            return 'ZombieWin'


class konusZombie(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['konus']
        self.dataDamage1 = zombies['konusDamage1']
        self.dataDamage2 = zombies['konusDamage2']
        self.dataDamage3 = zombies['normal']
        self.dataDamage4 = zombies['normalDamage1']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        sms = super().update()
        only = zombies_hp['konus'] - zombies_hp['normal']
        if only // 3 * 2 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage1
        if only // 3 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage2
        if zombies_hp['normal'] // 2 < self.hp <= zombies_hp['normal']:
            self.data = self.dataDamage3
        if self.hp <= zombies_hp['normal'] // 2:
            self.data = self.dataDamage4
        return sms

class normalZombie(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['normal']
        self.dataDamage2 = zombies['normalDamage1']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        sms = super().update()
        if zombies_hp['normal'] // 2 < self.hp <= zombies_hp['normal']:
            self.data = self.data
        if self.hp <= zombies_hp['normal'] // 2:
            self.data = self.dataDamage2
        return sms


class normalZombieWithFlag(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['normalWithFlag']
        self.dataDamage2 = zombies['normalDamage1']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        sms = super().update()
        if zombies_hp['normalWithFlag'] // 2 < self.hp <= zombies_hp['normalWithFlag']:
            self.data = self.data
        if self.hp <= zombies_hp['normalWithFlag'] // 2:
            self.data = self.dataDamage2
        return sms


class bucketZombie(justZombie):
    def __init__(self, row, hp):
        super().__init__(row, hp)
        self.data = zombies['bucket']
        self.dataDamage1 = zombies['bucketDamage1']
        self.dataDamage2 = zombies['bucketDamage2']
        self.dataDamage3 = zombies['normal']
        self.dataDamage4 = zombies['normalDamage1']
        self.image = self.data[self.cur]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        sms = super().update()
        only = zombies_hp['bucket'] - zombies_hp['normal']
        if only // 3 * 2 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage1
        if only // 3 >= self.hp - zombies_hp['normal']:
            self.data = self.dataDamage2
        if zombies_hp['normal'] // 2 < self.hp <= zombies_hp['normal']:
            self.data = self.dataDamage3
        if self.hp <= zombies_hp['normal'] // 2:
            self.data = self.dataDamage4
        return sms
