import pygame
from classPlant import *
from classPanel import Panel
from classField import Field
from zombies import classZombie
from allConstants import *
import sys


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = [""]

    fon = pygame.transform.scale(pygame.image.load('Graphics/other/fon.png'), (WIDTH2, HEIGHT2))
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
                return shields['game']()
        pygame.display.flip()
        clock.tick(FPS)


def game():
    suns = 0
    zs = pygame.sprite.Group()
    screen.blit(sBackGround, (0, 0))
    field = Field(FIELD_WIDTH, FIELD_HEIGHT, FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT, FIELD_LEFT, FIELD_TOP, screen)
    panel = Panel(PANEL_WIDTH, PANEL_CELL_WIDTH, PANEL_CELL_HEIGHT, PANEL_LEFT, PANEL_TOP, PANEL_STEP, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if field.get_click(event.pos, panel.checkPlant):
                    panel.checkPlant = ''
                panel.get_click(event.pos)

        if random.choice([0] * 44 + [1]):
            zs.add(classZombie.konusZombie(random.randint(0, 4), 100))

        screen.blit(sBackGround, (0, 0))
        panel.render()
        field.render()
        zs.update()
        zs.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


pygame.init()
pygame.display.set_caption('Plants VS Zombies 4')
pygame.display.set_icon(pygame.image.load('Graphics/other/icon.png'))
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode(SIZE2)
clock = pygame.time.Clock()

shields = {'start_screen': start_screen,
           'game': game}
while True:
    temp = shields['start_screen']()


