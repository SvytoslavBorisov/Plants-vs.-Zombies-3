import pygame


pygame.init()
pygame.display.set_caption('Lawn Of Undead')
pygame.display.set_icon(pygame.image.load('Graphics/other/icon.png'))
SIZE2 = WIDTH2, HEIGHT2 = 1026, 600
screen = pygame.display.set_mode(SIZE2)


from classPlant import *
from classPanel import Panel
from classField import Field
from classAlmanahPlant import AlmanahPlant
from classAlmanahZombie import AlmanahZombie
from zombies import classZombie
from plants import *
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect.collidepoint(volume.rect, event.pos):
                    screen.blit(gameMenu['pause'], (350, 50))
                    screen.blit(volume.image, (532, 175))
                    pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, event.pos[0] - 546, 10))
                    screen.blit(soundPick, (event.pos[0] - 10, 179))
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
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
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
    flgAlmanahB = False
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
                if 600 <= event.pos[0] <= 718 and 380 <= event.pos[1] <= 490:
                    flgAlmanahB = True
                else:
                    flgAlmanahB = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #print(event.pos)
                if 583 <= event.pos[0] <= 921 and 109 <= event.pos[1] <= 175:
                    screen.blit(bStartChange.image, (580, 80))
                    musicMainMenu.stop()
                    return shields['game']()
                elif 788 <= event.pos[0] <= 902 and 175 <= event.pos[1] <= 218:
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
                elif 600 <= event.pos[0] <= 718 and 380 <= event.pos[1] <= 490:
                    return shields['almanahChange']()

        screen.blit(mainMenu[indexAnimationMainMenu // 2 - 1], (0, 0))
        if flgAlmanahB:
            screen.blit(almanac_structure['change'], (600, 380))
        else:
            screen.blit(almanac_structure['normal1'], (600, 380))
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


def almanahMainMenuZombie():

    screen.blit(almanac_structure['almanahMainMenuZombie'], (0, 0))
    screen.blit(almanac_structure['closeMainMenu'], (848, 543))
    screen.blit(almanac_structure['backMainMenu'], (568, 543))

    panel = AlmanahZombie(ALMANAH_ZOMBIE_WIDTH, ALMANAH_ZOMBIE_HEIGHT, ALMANAH_ZOMBIE_CELL_WIDTH, ALMANAH_ZOMBIE_CELL_HEIGHT,
                          ALMANAH_ZOMBIE_LEFT, ALMANAH_ZOMBIE_TOP, ALMANAH_ZOMBIE_STEP_TOP, ALMANAH_ZOMBIE_STEP_LEFT, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                panel.get_click(event.pos)
                if 848 <= event.pos[0] <= 1019 and 543 <= event.pos[1] <= 594:
                    return shields['start_screen']()
                elif 568 <= event.pos[0] <= 738 and 543 <= event.pos[1] <= 594:
                    return shields['almanahChange']()

        screen.blit(almanac_structure['almanahMainMenuZombie'], (0, 0))
        screen.blit(almanac_structure['closeMainMenu'], (848, 543))
        screen.blit(almanac_structure['backMainMenu'], (568, 543))

        panel.render()
        pygame.display.flip()
        clock.tick(FPS)


def almanahMainMenuPlant():

    screen.blit(almanac_structure['almanahMainMenu'], (0, 0))
    screen.blit(almanac_structure['closeMainMenu'], (848, 543))
    screen.blit(almanac_structure['backMainMenu'], (568, 543))

    panel = AlmanahPlant(ALMANAH_WIDTH, ALMANAH_HEIGHT, ALMANAH_CELL_WIDTH, ALMANAH_CELL_HEIGHT, ALMANAH_LEFT, ALMANAH_TOP, ALMANAH_STEP_TOP, ALMANAH_STEP_LEFT, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                panel.get_click(event.pos)
                if 848 <= event.pos[0] <= 1019 and 543 <= event.pos[1] <= 594:
                    return shields['start_screen']()
                elif 568 <= event.pos[0] <= 738 and 543 <= event.pos[1] <= 594:
                    return shields['almanahChange']()

        screen.blit(almanac_structure['almanahMainMenu'], (0, 0))
        screen.blit(almanac_structure['closeMainMenu'], (848, 543))
        screen.blit(almanac_structure['backMainMenu'], (568, 543))

        panel.render()
        pygame.display.flip()
        clock.tick(FPS)


def almanahChange():

    screen.blit(almanac_structure['almanahMenu'], (0, 0))
    screen.blit(almanac_structure['viewPlant'], (166, 346))
    screen.blit(almanac_structure['viewZombies'], (625, 346))
    screen.blit(almanac_structure['close'], (868, 568))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 868 <= event.pos[0] <= 977 and 568 <= event.pos[1] <= 590:
                    return shields['start_screen']()
                elif 166 <= event.pos[0] <= 365 and 346 <= event.pos[1] <= 384:
                    return shields['almanahMainMenuPlant']()
                elif 625 <= event.pos[0] <= 824 and 346 <= event.pos[1] <= 384:
                    return shields['almanahMainMenuZombie']()

        pygame.display.flip()
        clock.tick(FPS)


def game():
    k1 = kk = 900
    timer = 100
    start = 0
    fl1, fl2, fl3 = 0, 0, 0
    musicGame.play(-1)
    musicGame.set_volume(game.soundVolume)

    game.suns = 50
    zs.empty()
    lownmowers = [0, 0, 0, 0, 0]
    field = Field(FIELD_WIDTH, FIELD_HEIGHT, FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT, FIELD_LEFT, FIELD_TOP, screen, game)
    panel = Panel(PANEL_WIDTH, PANEL_CELL_WIDTH, PANEL_CELL_HEIGHT, PANEL_LEFT, PANEL_TOP, PANEL_STEP, screen, game)
    bMenu = button(gamesSprites['buttonMenu'],  WIDTH2 - 170, 0)
    objects = []
    flgPlant = False
    flgShovel = False
    while True:
        game.time += 1
        if (game.time + 1) % 300 == 0:
            objects.append(classSunrise.Sun(0, 0, plants['sun'], random.randint(200, 900), -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 330 <= event.pos[0] <= 384 and 3 <= event.pos[1] <= 57:
                    flgShovel = not flgShovel
                if pygame.Rect.collidepoint(bMenu.rect, event.pos):
                    shields['pause']()
                temp = field.get_click(event.pos, panel.checkPlant, objects, flgShovel)
                objects = temp[2]
                if temp[0] == True:
                    panel.checkPlant = ''
                    panel.returnSostoynie(True)
                    game.suns = temp[1]
                    flgPlant = False
                flgShovel = temp[3]
                panel.get_click(event.pos)
                if panel.checkPlant:
                    screen.blit(plants[panel.checkPlant[0]][0], event.pos)
                    flgPlant = True
                    flgShovel = False
                else:
                    flgPlant = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                panel.checkPlant = ''
                panel.returnSostoynie(True)
                flgPlant = False
                flgShovel = False

        start += 1
        if start >= timer:
            start = 0
            if k1 > 100:
                k1 -= 20
        if random.choice([0] * k1 + [1] * 2):
            if kk // 3 * 2 < k1 <= kk:
                if fl1 == 0:
                    x = 3
                    fl1 = 1
                else:
                    x = 0
            elif kk // 3 < k1 <= kk // 3 * 2:
                if fl2 == 0:
                    x = 3
                    fl2 = 1
                else:
                    x = random.randint(0, 1)
            elif k1 <= kk // 3:
                if fl3 == 0:
                    x = 3
                    fl3 = 1
                else:
                    x = random.randint(0, 2)
            if x == 0:
                zs.add(classZombie.normalZombie(random.randint(0, 4), zombies_hp['normal']))
            elif x == 1:
                zs.add(classZombie.konusZombie(random.randint(0, 4), zombies_hp['konus']))
            elif x == 3:
                zs.add(classZombie.normalZombieWithFlag(random.randint(0, 4), zombies_hp['normal']))
                newVol.play()
            else:
                zs.add(classZombie.bucketZombie(random.randint(0, 4), zombies_hp['bucket']))

        for z in zs:
            k = int((z.x - FIELD_LEFT - 60) // FIELD_CELL_WIDTH + 2)
            if 0 <= k < FIELD_WIDTH and field.board[k][z.row] != '':
                z.x += z.speed
                field.hp[k][z.row] -= 1
                if field.hp[k][z.row] < 0:
                    field.hp[k][z.row] = -1
                    field.board[k][z.row] = ''

        screen.blit(gamesSprites['yardDay'], (0, 0))
        screen.blit(gamesSprites['buttonMenu'], (WIDTH2 - 170, 0))
        screen.blit(gamesSprites['panelSun'], (170, 0))
        screen.blit(gamesSprites['shovelB'], (330, 3))

        field.render()
        panel.render()

        event = pygame.mouse.get_pos()
        if flgPlant:
            field.mouse_move(event)
            screen.blit(plants[panel.checkPlant[0]][0], (event[0] - 25, event[1] - 25))
        panel.mouse_move(event)

        textSun = fontSun.render(str(game.suns), True, colors['black'])
        screen.blit(textSun, (240, 15))

        for x in sorted(zs.sprites(), key=lambda x: x.row):
            if x.update() == 'ZombieWon':
                return shields['pause']
            screen.blit(x.image, (x.rect.x, x.rect.y))

        i = 0
        while i < len(objects):
            objects[i].update()
            if objects[i].kill:
                del objects[i]
                game.suns += 25
            else:
                screen.blit(objects[i].image, (objects[i].rect.x, objects[i].rect.y))
                i += 1

        if flgShovel:
            pygame.mouse.set_visible(False)
            field.mouse_move(event)
            screen.blit(gamesSprites['shovel'], [event[0] - 25, event[1] - 25])
        else:
            pygame.mouse.set_visible(True)

        pygame.display.flip()
        clock.tick(FPS)


clock = pygame.time.Clock()

shields = {'load_screen': load_screen,
           'start_screen': start_screen,
           'game': game,
           'pause': pause,
           'almanahChange': almanahChange,
           'almanahMainMenuPlant': almanahMainMenuPlant,
           'almanahMainMenuZombie': almanahMainMenuZombie}

game = Game(500)
musicMainMenu.set_volume(game.soundVolume)

while True:
    temp = shields['game']()
