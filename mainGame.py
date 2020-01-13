import pygame
import sys
import os
from classGame import *


def inputName():
    pygame.font.init()
    font = pygame.font.Font('Graphics/other/Blood.otf', 32)
    input_box = pygame.Rect(8, 192, 504, 36)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    image = pygame.image.load('Graphics/other/inputName.png')
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 180 <= event.pos[0] <= 335 and 234 <= event.pos[1] <= 270:
                    return text
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.blit(image, (0, 0))
        txt_surface = font.render(text, True, color)
        width = max(504, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 1)
        pygame.display.flip()
        clock.tick(30)


pygame.init()
pygame.display.set_caption('Lawn Of Undead')
pygame.display.set_icon(pygame.image.load('Graphics/other/icon.png'))
screen = pygame.display.set_mode((510, 280))
clock = pygame.time.Clock()
gamePeremen = Game(500)
gamePeremen.name = inputName()
if gamePeremen.name == '':
    gamePeremen.name = 'NoName'
gamePeremen.soundVolume = 0


from classPlant import *
from classPanel import Panel
from classField import Field
from classAlmanahPlant import AlmanahPlant
from classAlmanahZombie import AlmanahZombie
from zombies import classZombie
from plants import *
from allConstants import *



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
    pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, gamePeremen.soundVolume * 100 / 0.68, 10))
    screen.blit(soundPick, (540 + gamePeremen.soundVolume * 100 / 0.68, 180))
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
                        gamePeremen.soundVolume = vol
                        musicGame.set_volume(gamePeremen.soundVolume)
                    elif vol > 1:
                        gamePeremen.soundVolume = 1
                        musicGame.set_volume(1)
                    else:
                        gamePeremen.soundVolume = 0
                        musicGame.set_volume(0)
                    volFlag = True
                if 376 <= event.pos[0] <= 732 and 465 <= event.pos[1] <= 529:
                    return
                if 448 <= event.pos[0] <= 658 and 388 <= event.pos[1] <= 432:
                    musicGame.stop()
                    with open('record.pack', 'a') as f:
                        f.write(gamePeremen.name + ': ' + str(gamePeremen.time // 20 // 60) + ':' +
                                str(gamePeremen.time // 20 % 60) + '\n')
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
                gamePeremen.soundVolume = vol
                musicGame.set_volume(gamePeremen.soundVolume)
            elif vol > 1:
                gamePeremen.soundVolume = 1
                musicGame.set_volume(1)
            else:
                gamePeremen.soundVolume = 0
                musicGame.set_volume(0)

        pygame.display.flip()
        clock.tick(FPS)


def start_screen():

    musicMainMenu.play(-1)

    indexAnimationMainMenu = 0
    screen.blit(mainMenu[indexAnimationMainMenu], (0, 0))

    bStart = button(menu['start'], 580, 80)
    bStartChange = button(menu['startChange'], 580, 80)

    font = pygame.font.Font('Graphics/other/Blood.otf', 20)
    txt_surface = font.render(gamePeremen.name, True, pygame.Color(0, 0, 0))
    screen.blit(txt_surface, (130, 85))

    bExit = button(menu['exit'], 929, 497)
    bExitChange = button(menu['exitChange'], 929, 497)

    bOption = button(menu['options'], 767, 487)
    bOptionChange = button(menu['optionsChange'], 767, 487)

    bHelp = button(menu['help'], 856, 588)
    bHelpChange = button(menu['helpChange'], 856, 515)

    bRecord = button(menu['record'], 20, 120)

    screen.blit(bStart.image, (580, 80))
    screen.blit(bExit.image, (929, 497))
    screen.blit(bRecord.image, (20, 120))
    screen.blit(bHelp.image, (856, 515))
    screen.blit(bOption.image, (767, 487))

    flgStartB = False
    flgExitB = False
    flgAlmanahB = False
    flgHelpB = False
    flgOptions = False

    while True:
        musicMainMenu.set_volume(gamePeremen.soundVolume)
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
                if 929 <= event.pos[0] <= 995 and 497 <= event.pos[1] <= 535:
                    flgExitB = True
                else:
                    flgExitB = False
                if 600 <= event.pos[0] <= 718 and 380 <= event.pos[1] <= 490:
                    flgAlmanahB = True
                else:
                    flgAlmanahB = False
                if 856 <= event.pos[0] <= 904 and 515 <= event.pos[1] <= 545:
                    flgHelpB = True
                else:
                    flgHelpB = False
                if 767 <= event.pos[0] <= 837 and 487 <= event.pos[1] <= 517:
                    flgOptions = True
                else:
                    flgOptions = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #print(event.pos)
                if 583 <= event.pos[0] <= 921 and 109 <= event.pos[1] <= 175:
                    screen.blit(bStartChange.image, (580, 80))
                    musicMainMenu.stop()
                    return shields['game']()
                if 20 <= event.pos[0] <= 310 and 120 <= event.pos[1] <= 180:
                    musicMainMenu.stop()
                    shields['record']()
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
                elif 929 <= event.pos[0] <= 995 and 497 <= event.pos[1] <= 535:
                    musicMainMenu.stop()
                    terminate()
                elif 600 <= event.pos[0] <= 718 and 380 <= event.pos[1] <= 490:
                    shields['almanahChange']()
                elif 856 <= event.pos[0] <= 904 and 515 <= event.pos[1] <= 545:
                    shields['help']()
                elif 767 <= event.pos[0] <= 837 and 487 <= event.pos[1] <= 517:
                    shields['musicPause']()

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
            screen.blit(bExit.image, (929, 497))
        else:
            screen.blit(bExitChange.image, (929, 497))

        if not flgHelpB:
            screen.blit(bHelp.image, (856, 515))
        else:
            screen.blit(bHelpChange.image, (856, 515))

        if not flgOptions:
            screen.blit(bOption.image, (767, 487))
        else:
            screen.blit(bOptionChange.image, (767, 487))

        screen.blit(bRecord.image, (20, 120))
        screen.blit(txt_surface, (130, 85))

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
    musicGame.set_volume(gamePeremen.soundVolume)

    gamePeremen.suns = 50
    zs.empty()
    lownmowers[0] = 0
    lownmowers[1] = 0
    lownmowers[2] = 0
    lownmowers[3] = 0
    lownmowers[4] = 0
    field = Field(FIELD_WIDTH, FIELD_HEIGHT, FIELD_CELL_WIDTH, FIELD_CELL_HEIGHT, FIELD_LEFT, FIELD_TOP, screen, gamePeremen)
    panel = Panel(PANEL_WIDTH, PANEL_CELL_WIDTH, PANEL_CELL_HEIGHT, PANEL_LEFT, PANEL_TOP, PANEL_STEP, screen, gamePeremen)
    bMenu = button(gamesSprites['buttonMenu'],  WIDTH2 - 170, 0)
    objects = []
    flgPlant = False
    flgShovel = False
    while True:
        gamePeremen.time += 1
        if (gamePeremen.time + 1) % 300 == 0:
            objects.append(classSunrise.Sun(0, 0, plants['sun'], random.randint(200, 900), -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('record.pack', 'a') as f:
                    f.write(gamePeremen.name + ': ' + str(gamePeremen.time // 20 // 60) + ':' +
                            str(gamePeremen.time // 20 % 60) + '\n')
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
                    gamePeremen.suns = temp[1]
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
        if random.choice([0] * k1 + [1] * 4):
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
        screen.blit(gamesSprites['panelScore'], (390, 3))
        screen.blit(gamesSprites['shovelB'], (330, 3))

        field.render()
        panel.render()

        event = pygame.mouse.get_pos()
        if flgPlant:
            field.mouse_move(event)
            screen.blit(plants[panel.checkPlant[0]][0], (event[0] - 25, event[1] - 25))
        panel.mouse_move(event)

        textSun = fontSun.render(str(gamePeremen.suns), True, colors['black'])
        screen.blit(textSun, (240, 15))

        textSun = fontSun.render(str(gamePeremen.time // 20 // 60) + ':' + str(gamePeremen.time // 20 % 60),
                                 True, colors['black'])
        screen.blit(textSun, (430, 15))

        for x in sorted(zs.sprites(), key=lambda x: x.row):
            if x.update() == 'ZombieWin':
                screen.blit(zombieWon, (300, 100))
                with open('record.pack', 'a') as f:
                    f.write(gamePeremen.name + ': ' + str(gamePeremen.time // 20 // 60) + ':' +
                            str(gamePeremen.time // 20 % 60) + '\n')
                shields['start_screen']()
            screen.blit(x.image, (x.rect.x, x.rect.y))

        i = 0
        while i < len(objects):
            objects[i].update()
            if objects[i].kill:
                del objects[i]
                gamePeremen.suns += 25
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


def record():
    screen.blit(recordMenu, (0, 0))

    data = []

    files = os.listdir()
    for x in files:
        if x[-4:] == 'pack':
            with open(x, 'r') as f:
                data += f.readlines()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 133 <= event.pos[0] <= 886 and 18 <= event.pos[1] <= 76:
                    return

        screen.blit(recordMenu, (0, 0))
        i = 0
        for x in sorted(data, key=lambda x: [int(x[:-1].split(':')[1]), int(x[:-1].split(':')[2])], reverse=True):
            font = pygame.font.Font('Graphics/other/Blood.otf', 32)
            if x[-1] == '\n':
                txt_surface = font.render(str(i + 1) + '. ' + x[:-1], True, pygame.Color(0, 0, 0))
            else:
                txt_surface = font.render(str(i + 1) + '. ' + x, True, pygame.Color(0, 0, 0))
            screen.blit(txt_surface, (50, 100 + i * 50))
            i += 1

        pygame.display.flip()
        clock.tick(FPS)


def help1():
    screen.blit(menu['helpScreen'], (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 416 <= event.pos[0] <= 614 and 521 <= event.pos[1] <= 560:
                    return

        screen.blit(menu['helpScreen'], (0, 0))

        pygame.display.flip()
        clock.tick(FPS)


def musicPause():

    screen.blit(gameMenu['pauseMusic'], (350, 50))
    volume = button(progressBarSound, 532, 175)
    screen.blit(volume.image, (532, 175))
    pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, gamePeremen.soundVolume * 100 / 0.68, 10))
    screen.blit(soundPick, (540 + gamePeremen.soundVolume * 100 / 0.68, 180))
    volFlag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect.collidepoint(volume.rect, event.pos):
                    screen.blit(gameMenu['pauseMusic'], (350, 50))
                    screen.blit(volume.image, (532, 175))
                    pygame.draw.rect(screen, colors['blue'], pygame.Rect(546, 185, event.pos[0] - 546, 10))
                    screen.blit(soundPick, (event.pos[0] - 10, 179))
                    vol = (event.pos[0] - 540) * 0.68 / 100
                    if 1 > vol > 0.1:
                        gamePeremen.soundVolume = vol
                        musicGame.set_volume(gamePeremen.soundVolume)
                    elif vol > 1:
                        gamePeremen.soundVolume = 1
                        musicGame.set_volume(1)
                    else:
                        gamePeremen.soundVolume = 0
                        musicGame.set_volume(0)
                    volFlag = True
                if 376 <= event.pos[0] <= 732 and 465 <= event.pos[1] <= 529:
                    return
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if volFlag:
                    volFlag = False

        if volFlag and 450 <= event.pos[0] <= 800:
            screen.blit(gameMenu['pauseMusic'], (350, 50))
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
                gamePeremen.soundVolume = vol
                musicGame.set_volume(gamePeremen.soundVolume)
            elif vol > 1:
                gamePeremen.soundVolume = 1
                musicGame.set_volume(1)
            else:
                gamePeremen.soundVolume = 0
                musicGame.set_volume(0)

        pygame.display.flip()
        clock.tick(FPS)


SIZE2 = WIDTH2, HEIGHT2 = 1026, 600
screen = pygame.display.set_mode(SIZE2)

shields = {'load_screen': load_screen,
           'start_screen': start_screen,
           'game': game,
           'pause': pause,
           'almanahChange': almanahChange,
           'almanahMainMenuPlant': almanahMainMenuPlant,
           'almanahMainMenuZombie': almanahMainMenuZombie,
           'record': record,
           'help': help1,
           'musicPause': musicPause}

musicMainMenu.set_volume(gamePeremen.soundVolume)

while True:
    temp = shields['start_screen']()
