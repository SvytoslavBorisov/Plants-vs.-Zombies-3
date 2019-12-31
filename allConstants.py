import pygame
import os


def load_image(name, size):
    fullname = os.path.join(name)
    return pygame.transform.scale(pygame.image.load(fullname).convert_alpha(), size)


SIZE1 = WIDTH1, HEIGHT1 = 700, 600
SIZE2 = WIDTH2, HEIGHT2 = 1026, 600
SIZE_OF_PLANT = (80, 80)
SIZE_OF_CARDS = (125, 75)

pygame.init()
screen = pygame.display.set_mode(SIZE1)
FPS = 20
zs = pygame.sprite.Group()

colors = {'red': pygame.Color("red"),
          'green': pygame.Color("green"),
          'blue': pygame.Color("blue"),
          'yellow': pygame.Color("yellow"),
          'black': pygame.Color("black")}

FIELD_WIDTH = 9
FIELD_HEIGHT = 5
FIELD_CELL_WIDTH = 82
FIELD_CELL_HEIGHT = 99
FIELD_LEFT = 245
FIELD_TOP = 80

PANEL_WIDTH = 5
PANEL_CELL_WIDTH = 125
PANEL_CELL_HEIGHT = 75
PANEL_LEFT = 30
PANEL_TOP = 75
PANEL_STEP = 10
fontSun = pygame.font.Font('freesansbold.ttf', 30)

gamesSprites = {'yardDay':    pygame.image.load('Graphics/other/Frontyard.jpg').convert(),
                'buttonMenu': load_image(f'Graphics/other/menu.png', (160, 50)),
                'panelSun':   load_image(f'Graphics/other/panelSun.png', (160, 60)),
                'punkteer':   load_image('Graphics/cards/punkteer.png', SIZE_OF_CARDS)}

mainMenu = [load_image(f'Graphics/other/animationStartMenu/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', (WIDTH2, HEIGHT2)) for i in range(11)]

plants = {'wallNut': [load_image(f'Graphics/plants/animationWallNut/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', (70, 80)) for i in range(44)],
          'gatlingPea': [load_image(f'Graphics/plants/animationGatlingPea/{i}.png', SIZE_OF_PLANT) for i in range(23)],
          'gatlingPeaShoot': [load_image(f'Graphics/plants/animationGatlingPeaShoot/{i}.png', SIZE_OF_PLANT) for i in range(14)],
          'pea': load_image(f'Graphics/plants/animationGatlingPeaShoot/pea.png', (27, 27)),
          'pea1': load_image(f'Graphics/plants/animationGatlingPeaShoot/pea.png', (9, 27)),
          'sunrise': [load_image(f'Graphics/plants/animationSunrise/{i}.png', SIZE_OF_PLANT) for i in range(15)],
          'sunriseGiveSun': [load_image(f'Graphics/plants/animationSunriseGiveSun/{i}.png', SIZE_OF_PLANT) for i in range(14)],
          'sun': load_image(f'Graphics/plants/animationSunriseGiveSun/sun.png', (70, 70)),
          'potatoBomb': [load_image(f'Graphics/plants/animationPotatoBomb/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', SIZE_OF_PLANT) for i in range(4)],
          'squash': [load_image(f'Graphics/plants/animationSquash/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', SIZE_OF_PLANT) for i in range(17)],
          'cabbage': [load_image(f'Graphics/plants/animationCabbage/{"0" *(4 - len(str(i))) + str(i) if i != 0 else "0000"}.png', (200, 120)) for i in range(23)],
          'lownMower': load_image(f'Graphics/other/lownMower.png', (75, 75))}

menu = {'start': load_image(f'Graphics/other/SelectorScreen_StartAdventure_Button1.png', (350, 141)),
        'startChange': load_image(f'Graphics/other/SelectorScreen_StartAdventure_Highlight.png', (350, 141)),
        'exit': load_image(f'Graphics/other/buttonExit.png', (70, 30)),
        'exitChange': load_image(f'Graphics/other/buttonExitChange.png', (70, 30)),
        }

gameMenu = {'pause': load_image(f'Graphics/other/pauseMenu.png', (410, 490))}

load_screen_sprites = [load_image(f'Graphics/other/animationLoadScreen/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', (WIDTH2, HEIGHT2)) for i in range(14)]

soundPick = load_image(f'Graphics/other/soundPick.png', (20, 20))
progressBarSound = load_image(f'Graphics/other/soundProgressBar.png', (182, 32))

cards = {'gatlingPea': load_image('Graphics/cards/gatlingPea.png', SIZE_OF_CARDS),
         'sunrise': load_image('Graphics/cards/sunrise.png', SIZE_OF_CARDS),
         'wallNut': load_image('Graphics/cards/wallNut.png', SIZE_OF_CARDS),
         'potatoBomb': load_image('Graphics/cards/potatoBomb.png', SIZE_OF_CARDS),
         'squash': load_image('Graphics/cards/squash.png', SIZE_OF_CARDS),
         'cabbage': load_image('Graphics/cards/cabbage.png', SIZE_OF_CARDS)}

zombies = {'konus': [load_image(f'Graphics/zombies/animationKonus/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'konusDamage1': [load_image(f'Graphics/zombies/animationKonusLittleDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'konusDamage2': [load_image(f'Graphics/zombies/animationKonusBigDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'bucket': [load_image(f'Graphics/zombies/animationbucket/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'normal': [load_image(f'Graphics/zombies/animationNormal/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)]}

musicMainMenu = pygame.mixer.Sound('Sounds/Soundtrack Main Menu.wav')
musicGame = pygame.mixer.Sound('Sounds/Soundtrack Day Stage.wav')
#music.play(-1)

zombies_hp = {'normal': 80,
              'konus': 230,
              'bucket': 350}