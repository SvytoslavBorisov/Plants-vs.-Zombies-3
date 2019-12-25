import pygame
import os


SIZE1 = WIDTH1, HEIGHT1 = 700, 600
SIZE2 = WIDTH2, HEIGHT2 = 1026, 600
SIZE_OF_PLANT = (80, 80)
SIZE_OF_CARDS = (125, 75)


pygame.init()
screen = pygame.display.set_mode(SIZE1)


def load_image(name, size):
    fullname = os.path.join(name)
    return pygame.transform.scale(pygame.image.load(fullname).convert_alpha(), size)


FPS = 20

RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLUE = pygame.Color("blue")
YELLOW = pygame.Color("yellow")
BLACK = pygame.Color("black")

FIELD_WIDTH = 9
FIELD_HEIGHT = 5
FIELD_CELL_WIDTH = 82
FIELD_CELL_HEIGHT = 99
FIELD_LEFT = 245
FIELD_TOP = 80

PANEL_WIDTH = 4
PANEL_CELL_WIDTH = 125
PANEL_CELL_HEIGHT = 75
PANEL_LEFT = 30
PANEL_TOP = 75
PANEL_STEP = 10

sBackGround = pygame.image.load('Graphics/other/Frontyard.jpg').convert()
sMenu = load_image(f'Graphics/other/menu.png', (160, 50))
panelSun = load_image(f'Graphics/other/panelSun.png', (160, 60))

fontSun = pygame.font.Font('freesansbold.ttf', 30)
pygame.font.get_fonts()
plants = {'wallNut': [load_image(f'Graphics/plants/animationWallNut/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', (70, 80)) for i in range(44)],
          'gatlingPea': [load_image(f'Graphics/plants/animationGatlingPea/{i}.png', SIZE_OF_PLANT) for i in range(23)],
          'gatlingPeaShoot': [load_image(f'Graphics/plants/animationGatlingPeaShoot/{i}.png', SIZE_OF_PLANT) for i in range(14)],
          'pea': load_image(f'Graphics/plants/animationGatlingPeaShoot/pea.png', (27, 27)),
          'sunrise': [load_image(f'Graphics/plants/animationSunrise/{i}.png', SIZE_OF_PLANT) for i in range(15)],
          'sunriseGiveSun': [load_image(f'Graphics/plants/animationSunriseGiveSun/{i}.png', SIZE_OF_PLANT) for i in range(14)],
          'sun': load_image(f'Graphics/plants/animationSunriseGiveSun/sun.png', (70, 70)),
          'potatoBomb': [load_image(f'Graphics/plants/animationPotatoBomb/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', SIZE_OF_PLANT) for i in range(4)],
          'lownMower': load_image(f'Graphics/other/lownMower.png', (75, 75))}

cards = {'gatlingPea': load_image('Graphics/cards/gatlingPea.png', SIZE_OF_CARDS),
         'sunrise': load_image('Graphics/cards/sunrise.png', SIZE_OF_CARDS),
         'wallNut': load_image('Graphics/cards/wallNut.png', SIZE_OF_CARDS),
         'potatoBomb': load_image('Graphics/cards/potatoBomb.png', SIZE_OF_CARDS)}

zombies = {'konus': [load_image(f'Graphics/zombies/animationKonus/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)]}