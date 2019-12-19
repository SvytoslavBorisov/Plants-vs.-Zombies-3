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
    if size != (0, 0):
        return pygame.transform.scale(pygame.image.load(fullname).convert_alpha(), size)
    else:
        return pygame.image.load(fullname).convert()


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

PANEL_WIDTH = 6
PANEL_CELL_WIDTH = 125
PANEL_CELL_HEIGHT = 75
PANEL_LEFT = 30
PANEL_TOP = 75
PANEL_STEP = 10

plants = {'wallNut': [load_image(f'Graphics/animationGatlingPea/{i}.png', SIZE_OF_PLANT) for i in range(23)],
          'gatlingPea': [load_image(f'Graphics/animationGatlingPea/{i}.png', SIZE_OF_PLANT) for i in range(23)],
          'gatlingPeaShoot': [load_image(f'Graphics/animationGatlingPeaShoot/{i}.png', SIZE_OF_PLANT) for i in range(15)],
          'sunrise': [load_image(f'Graphics/animationSunrise/{i}.png', SIZE_OF_PLANT) for i in range(16)],
          'sunriseGiveSun': [load_image(f'Graphics/animationSunriseGiveSun/{i}.png', SIZE_OF_PLANT) for i in range(14)]}

cards = {'gatlingPea': load_image('Graphics/cards/gatlingPea.png', SIZE_OF_CARDS),
         'sunrise': load_image('Graphics/cards/sunrise.png', SIZE_OF_CARDS)}
