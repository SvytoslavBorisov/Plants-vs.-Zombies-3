import pygame
import os


def load_image(name, size):
    fullname = os.path.join(name)
    return pygame.transform.scale(pygame.image.load(fullname).convert_alpha(), size)


SIZE1 = WIDTH1, HEIGHT1 = 700, 600
SIZE2 = WIDTH2, HEIGHT2 = 1026, 600
SIZE_OF_PLANT = (80, 80)
SIZE_OF_CARDS = (125, 75)
SIZE_OF_CARDS_ZOMBIE = (160, 160)

pygame.init()
screen = pygame.display.set_mode(SIZE2)
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

PANEL_WIDTH = 4
PANEL_CELL_WIDTH = 125
PANEL_CELL_HEIGHT = 75
PANEL_LEFT = 30
PANEL_TOP = 75
PANEL_STEP = 10

ALMANAH_WIDTH = 6
ALMANAH_HEIGHT = 4
ALMANAH_CELL_WIDTH = 125
ALMANAH_CELL_HEIGHT = 75
ALMANAH_LEFT = 40
ALMANAH_TOP = 95
ALMANAH_STEP_TOP = 5
ALMANAH_STEP_LEFT = 8

ALMANAH_ZOMBIE_WIDTH = 3
ALMANAH_ZOMBIE_HEIGHT = 3
ALMANAH_ZOMBIE_CELL_WIDTH = 160
ALMANAH_ZOMBIE_CELL_HEIGHT = 160
ALMANAH_ZOMBIE_LEFT = 40
ALMANAH_ZOMBIE_TOP = 95
ALMANAH_ZOMBIE_STEP_TOP = 5
ALMANAH_ZOMBIE_STEP_LEFT = 8

fontSun = pygame.font.Font('freesansbold.ttf', 30)

gamesSprites = {'yardDay':    pygame.image.load('Graphics/other/Frontyard.jpg').convert(),
                'buttonMenu': load_image(f'Graphics/other/menu.png', (160, 50)),
                'panelSun':   load_image(f'Graphics/other/panelSun.png', (160, 60)),
                'punkteer':   load_image('Graphics/cards/punkteer.png', SIZE_OF_CARDS),
                'shovel':     load_image(f'Graphics/other/shovel.png', (59, 62)),
                'shovelB':    load_image(f'Graphics/other/bShovel.png', (54, 54))}

mainMenu = [load_image(f'Graphics/other/animationStartMenu/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', (WIDTH2, HEIGHT2)) for i in range(11)]

zombieWon = load_image('Graphics/other/ZombiesWon.jpg', (564, 468))

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
          'squashJump': [load_image(f'Graphics/plants/animationSquashJump/{"0" *(4 - len(str(i + 1))) + str(i + 1)}.png', SIZE_OF_PLANT) for i in range(20)],
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
         'cabbage': load_image('Graphics/cards/cabbage.png', SIZE_OF_CARDS),
         'normal': load_image('Graphics/cards/zombie.png', SIZE_OF_CARDS_ZOMBIE),
         'bucket': load_image('Graphics/cards/zombieBucket.png', SIZE_OF_CARDS_ZOMBIE),
         'normalWithFlag': load_image('Graphics/cards/zombieWithFlag.png', SIZE_OF_CARDS_ZOMBIE),
         'konus': load_image('Graphics/cards/zombieKonus.png', SIZE_OF_CARDS_ZOMBIE)}

description = {'gatlingPea': load_image('Graphics/description/gatlingPea.png', (88, 16)),
         'sunrise': load_image('Graphics/description/sunrise.png', (88, 16)),
         'wallNut': load_image('Graphics/description/wallNut.png', (88, 16)),
         'potatoBomb': load_image('Graphics/description/potatoBomb.png', (88, 16)),
         'squash': load_image('Graphics/description/squash.png', (88, 16)),
         'cabbage': load_image('Graphics/description/gatlingPea.png', (88, 16))}

descriptionNoSun = {'gatlingPea': load_image('Graphics/description/gatlingPeaNoSun.png', (88, 32)),
         'sunrise': load_image('Graphics/description/sunriseNoSun.png', (88, 32)),
         'wallNut': load_image('Graphics/description/wallNutNoSun.png', (88, 32)),
         'potatoBomb': load_image('Graphics/description/potatoBombNoSun.png', (88, 32)),
         'squash': load_image('Graphics/description/squashNoSun.png', (88, 32)),
         'cabbage': load_image('Graphics/description/gatlingPeaNoSun.png', (88, 32))}

descriptionNoTime = {'gatlingPea': load_image('Graphics/description/gatlingPeaNoTime.png', (88, 32)),
         'sunrise': load_image('Graphics/description/sunriseNoTime.png', (88, 32)),
         'wallNut': load_image('Graphics/description/wallNutNoTime.png', (88, 32)),
         'potatoBomb': load_image('Graphics/description/potatoBombNoTime.png', (88, 32)),
         'squash': load_image('Graphics/description/squashNoTime.png', (88, 32)),
         'cabbage': load_image('Graphics/description/sunriseNoTime.png', (88, 32))}

zombies = {'konus': [load_image(f'Graphics/zombies/animationKonus/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'konusDamage1': [load_image(f'Graphics/zombies/animationKonusLittleDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'konusDamage2': [load_image(f'Graphics/zombies/animationKonusBigDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'bucket': [load_image(f'Graphics/zombies/animationbucket/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'bucketDamage1': [load_image(f'Graphics/zombies/animationBucketLittleDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'bucketDamage2': [load_image(f'Graphics/zombies/animationBucketBigDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'normal': [load_image(f'Graphics/zombies/animationNormal/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'normalDamage1': [load_image(f'Graphics/zombies/animationNormalLittleDamage/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)],
           'normalWithFlag': [load_image(f'Graphics/zombies/animationNormalWithFlag/{str(i + 1).rjust(4, "0")}.png', (165, 145)) for i in range(21)]}

almanac_structure = {'normal1': load_image('Graphics/other/almanah1.png', (118, 110)),
           'almanahMenu': load_image('Graphics/other/almanahMenu.png', SIZE2),
           'change': load_image('Graphics/other/almanah.png', (118, 110)),
           'viewPlant': load_image('Graphics/other/viewPlantButton.png', (199, 38)),
           'viewZombies': load_image('Graphics/other/viewZombiesButton.png', (261, 39)),
           'close': load_image('Graphics/other/closeAlmanahButton.png', (109, 22)),
           'almanahMainMenu': load_image('Graphics/other/almanahMainMenu.png', SIZE2),
           'almanahMainMenuZombie': load_image('Graphics/other/almanahMainMenuZombie.png', SIZE2),
           'closeMainMenu': load_image('Graphics/other/almanahMainMenuClose.png', (170, 51)),
           'backMainMenu': load_image('Graphics/other/almanahMainMenuBack.png', (171, 51))}

almanac_text = {'gatlingPea': [],
                'sunrise': [],
                'wallNut': [],
                'potatoBomb': [],
                'squash': [],
                'normal': [],
                'normalWithFlag': [],
                'konus': [],
                'bucket': []}

fontText = pygame.font.Font('freesansbold.ttf', 15)

for y in almanac_text.keys():
    with open(f'Graphics/description/{y}.txt', 'r') as f:
        data = f.readlines()
        data = ''.join(data)
        for x in data.split('\n'):
            almanac_text[y].append(fontText.render(x, 1, (0, 0, 0)))

musicMainMenu = pygame.mixer.Sound('Sounds/Soundtrack Main Menu.wav')
musicGame = pygame.mixer.Sound('Sounds/Soundtrack Day Stage.wav')
newVol = pygame.mixer.Sound('Sounds/The Zombies are .wav')
#music.play(-1)

plants_hp = {'gatlingPea': 100,
            'sunrise': 100,
            'wallNut': 500,
            'potatoBomb': 75,
            'squash': 75}

zombies_hp = {'normal': 80,
              'normalWithFlag': 80,
              'konus': 230,
              'bucket': 350}

lownmowers = [0, 0, 0, 0, 0]
