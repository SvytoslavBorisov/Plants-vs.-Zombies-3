import pygame
from classPlant import Plant, load_image, GatlingPea, Sunrise
from classPanel import Panel
from classField import Field
from allConstants import *
import sys


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = [""]

    fon = pygame.transform.scale(pygame.image.load('Graphics/other/fon.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


pygame.init()
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode(SIZE1)
clock = pygame.time.Clock()

start_screen()

plants = {'wallNut': [load_image(f'Graphics/animationGatlingPea/{i}.png', SIZE_OF_PLANT) for i in range(23)],
          'gatlingPea': [load_image(f'Graphics/animationGatlingPea/{i}.png', SIZE_OF_PLANT) for i in range(23)],
          'gatlingPeaShoot': [load_image(f'Graphics/animationGatlingPeaShoot/{i}.png', SIZE_OF_PLANT) for i in range(15)],
          'sunrise': [load_image(f'Graphics/animationSunrise/{i}.png', SIZE_OF_PLANT) for i in range(15)]}

sBackGround = pygame.image.load('Graphics/other/Frontyard.jpg').convert()

screen = pygame.display.set_mode(SIZE2)

screen.blit(sBackGround, (0, 0))
field = Field(FIELD_WIDTH, FIELD_HEIGHT, FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT, FIELD_LEFT, FIELD_TOP, screen)
panel = Panel(PANEL_WIDTH, PANEL_CELL_WIDTH, PANEL_CELL_HEIGHT, PANEL_LEFT, PANEL_TOP, PANEL_STEP, screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field.get_click(event.pos, GatlingPea(plants['gatlingPea'], plants['gatlingPeaShoot']))
            else:
                field.get_click(event.pos, Sunrise(plants['sunrise']))

    screen.blit(sBackGround, (0, 0))
    panel.render()
    field.render()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
