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
        clock.tick(7)
    return shields['start_screen']()


def pause():

    screen.blit(gameMenu['pause'], (350, 50))
    volume = button(progressBarSound, 532, 175)
    screen.blit(volume.image, (532, 175))
    pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, game.soundVolume * 100 / 0.68, 10))
    screen.blit(soundPick, (540 + game.soundVolume * 100 / 0.68, 180))
    volFlag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(volume.rect, event.pos):
                    screen.blit(gameMenu['pause'], (350, 50))
                    screen.blit(volume.image, (532, 175))
                    screen.blit(soundPick, (event.pos[0] - 10, 179))
                    pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, event.pos[0] - 546, 10))
                    vol = (event.pos[0] - 540) * 0.68 / 100
                    if 1 > vol > 0.1:
                        game.soundVolume = vol
                        musicGame.set_volume(game.soundVolume)
                    elif vol > 1:
                        game.soundVolume = 1
                        musicGame.set_volume(1)
                    else:
                        game.soundVolume = 0
                        musicGame.set_volume(0)
                    volFlag = True
                if 376 <= event.pos[0] <= 732 and 465 <= event.pos[1] <= 529:
                    return
                if 448 <= event.pos[0] <= 658 and 388 <= event.pos[1] <= 432:
                    musicGame.stop()
                    return shields['start_screen']()
                if 448 <= event.pos[0] <= 658 and 334 <= event.pos[1] <= 475:
                    musicGame.stop()
                    return shields['game']()
            elif event.type == pygame.MOUSEBUTTONUP:
                if volFlag:
                    volFlag = False

        if volFlag and 450 <= event.pos[0] <= 800:
            screen.blit(gameMenu['pause'], (350, 50))
            screen.blit(volume.image, (532, 175))
            if event.pos[0] < 550:
                pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, 1, 10))
                screen.blit(soundPick, (540, 180))
            elif event.pos[0] > 700:
                pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, 140, 10))
                screen.blit(soundPick, (685, 180))
            else:
                pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, event.pos[0] - 546, 10))
                screen.blit(soundPick, (event.pos[0] - 10, 180))
            vol = (event.pos[0] - 540) * 0.68 / 100
            if 1 > vol > 0.1:
                game.soundVolume = vol
                musicGame.set_volume(game.soundVolume)
            elif vol > 1:
                game.soundVolume = 1
                musicGame.set_volume(1)
            else:
                game.soundVolume = 0
                musicGame.set_volume(0)

        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    intro_text = [""]

    musicMainMenu.play(-1)
    musicMainMenu.set_volume(game.soundVolume)

    indexAnimationMainMenu = 0
    screen.blit(mainMenu[indexAnimationMainMenu], (0, 0))

    bStart = button(menu['start'], 580, 80)
    bStartChange = button(menu['startChange'], 580, 80)
    bExit = button(menu['exit'], 930, 490)
    bExitChange = button(menu['exitChange'], 930, 490)
    screen.blit(bStart.image, (580, 80))
    screen.blit(bExit.image, (930, 505))
    flgStartB = False
    flgExitB = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                if 583 <= event.pos[0] <= 921 and 109 <= event.pos[1] <= 175:
                    flgStartB = True
                elif 788 <= event.pos[0] <= 902 and 175 <= event.pos[1] <= 218:
                    flgStartB = True
                elif 658 <= event.pos[0] <= 835 and 83 <= event.pos[1] <= 121:
                    flgStartB = True
                elif 620 <= event.pos[0] <= 788 and 175 <= event.pos[1] <= 200:
                    flgStartB = True
                else:
                    flgStartB = False
                if 930 <= event.pos[0] <= 1000 and 512 <= event.pos[1] <= 535:
                    flgExitB = True
                else:
                    flgExitB = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if 583 <= event.pos[0] <= 921 and 109 <= event.pos[1] <= 175:
                    screen.blit(bStartChange.image, (580, 80))
                    musicMainMenu.stop()
                    return shields['game']()
                elif 788 <= event.pos[0] <= 902 and 186 <= event.pos[1] <= 218:
                    screen.blit(bStartChange.image, (580, 80))
                    musicMainMenu.stop()
                    return shields['game']()
                elif 658 <= event.pos[0] <= 835 and 83 <= event.pos[1] <= 121:
                    screen.blit(bStartChange.image, (580, 80))
                    musicMainMenu.stop()
                    return shields['game']()
                elif 620 <= event.pos[0] <= 788 and 175 <= event.pos[1] <= 200:
                    screen.blit(bStartChange.image, (580, 80))
                    musicMainMenu.stop()
                    return shields['game']()
                elif 930 <= event.pos[0] <= 1000 and 512 <= event.pos[1] <= 535:
                    musicMainMenu.stop()
                    terminate()

        screen.blit(mainMenu[indexAnimationMainMenu // 2 - 1], (0, 0))
        if indexAnimationMainMenu >= len(mainMenu) * 2:
            indexAnimationMainMenu = 0
        else:
            indexAnimationMainMenu += 1

        if not flgStartB:
            screen.blit(bStart.image, (580, 80))
        else:
            screen.blit(bStartChange.image, (580, 80))

        if not flgExitB:
            screen.blit(bExit.image, (930, 505))
        else:
            screen.blit(bExitChange.image, (930, 505))

        pygame.display.flip()
        clock.tick(FPS)


def game():
    zs = pygame.sprite.Group()

    musicGame.play(-1)
    musicGame.set_volume(game.soundVolume)

    game.suns = 5000
    screen.blit(gamesSprites['yardDay'], (0, 0))
    field = Field(FIELD_WIDTH, FIELD_HEIGHT, FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT, FIELD_LEFT, FIELD_TOP, screen, game)
    panel = Panel(PANEL_WIDTH, PANEL_CELL_WIDTH, PANEL_CELL_HEIGHT, PANEL_LEFT, PANEL_TOP, PANEL_STEP, screen, game)
    bMenu = button(gamesSprites['buttonMenu'],  WIDTH2 - 170, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(event.pos)
                if pygame.Rect.collidepoint(bMenu.rect, event.pos):
                    shields['pause']()
                temp = field.get_click(event.pos, panel.checkPlant)
                if temp[0] == True:
                    panel.checkPlant = ''
                    panel.returnSostoynie()
                    game.suns = temp[1]
                panel.get_click(event.pos)

        if random.choice([0] * 44 + [1]):
            x = random.randint(0, 2)
            if x == 0:
                zs.add(classZombie.konusZombie(random.randint(0, 4), 100))
            elif x == 1:
                zs.add(classZombie.normalZombie(random.randint(0, 4), 100))
            else:
                zs.add(classZombie.bucketZombie(random.randint(0, 4), 100))

        screen.blit(gamesSprites['yardDay'], (0, 0))
        screen.blit(gamesSprites['buttonMenu'], (WIDTH2 - 170, 0))
        screen.blit(gamesSprites['panelSun'], (170, 0))
        textSun = fontSun.render(str(game.suns), True, colors['black'])
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
musicMainMenu.play(-1)
musicMainMenu.set_volume(game.soundVolume)

while True:
    temp = shields['start_screen']()
