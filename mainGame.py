import pygame
from classPlant import *
from classPanel import Panel
from classField import Field
from zombies import classZombie
from allConstants import *
from classGame import *
import sys


class button(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


def terminate():
    pygame.quit()
    sys.exit()


def load_screen():

    screen.blit(load_screen_sprites[0], (0, 0))
    k = 0
    while k < 13:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        k += 1
        screen.blit(load_screen_sprites[k], (0, 0))

        pygame.display.flip()
        clock.tick(5)
    return shields['start_screen']()


def pause():

    screen.blit(gameMenu['pause'], (350, 50))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if 376 <= event.pos[0] <= 732 and 465 <= event.pos[1] <= 529:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    intro_text = [""]

    fon = pygame.transform.scale(pygame.image.load('Graphics/other/mainMenu.png'), (WIDTH2, HEIGHT2))
    screen.blit(fon, (0, 0))
    bStart = button(menu['start'], 580, 80)
    screen.blit(bStart.image, (580, 80))
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
                if pygame.Rect.collidepoint(bStart.rect, event.pos):
                    return shields['game']()
        pygame.display.flip()
        clock.tick(FPS)


def game():
    zs = pygame.sprite.Group()
    game.suns = 5000
    screen.blit(sBackGround, (0, 0))
    field = Field(FIELD_WIDTH, FIELD_HEIGHT, FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT, FIELD_LEFT, FIELD_TOP, screen, game)
    panel = Panel(PANEL_WIDTH, PANEL_CELL_WIDTH, PANEL_CELL_HEIGHT, PANEL_LEFT, PANEL_TOP, PANEL_STEP, screen, game)
    bMenu = button(sMenu,  WIDTH2 - 170, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(bMenu.rect, event.pos):
                    shields['pause']()
                temp = field.get_click(event.pos, panel.checkPlant)
                if temp[0] == True:
                    panel.checkPlant = ''
                    panel.returnSostoynie()
                    game.suns = temp[1]
                panel.get_click(event.pos)

        if random.choice([0] * 44 + [1]):
            x = random.randint(0, 1)
            if x:
                zs.add(classZombie.konusZombie(random.randint(0, 4), 100))
            else:
                zs.add(classZombie.normalZombie(random.randint(0, 4), 100))

        screen.blit(sBackGround, (0, 0))
        screen.blit(sMenu, (WIDTH2 - 170, 0))
        screen.blit(panelSun, (170, 0))
        textSun = fontSun.render(str(game.suns), True, BLACK)
        screen.blit(textSun, (250, 15))
        field.render()
        panel.render()
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

shields = {'load_screen': load_screen,
           'start_screen': start_screen,
           'game': game,
           'pause': pause}

game = Game(5000)

while True:
    temp = shields['start_screen']()
