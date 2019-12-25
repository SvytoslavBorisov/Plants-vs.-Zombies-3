import pygame
import random
import os
from allConstants import *
from plants import classSunrise, classGatlingPea, classWallNut, classPotato


def choicePlant(indPlant, coords, game):
    if indPlant == 'gatlingPea':
        return classGatlingPea.GatlingPea(*coords)
    elif indPlant == 'sunrise':
        return classSunrise.Sunrise(*coords, game)
    elif indPlant == 'wallNut':
        return classWallNut.WallNut(*coords)
    elif indPlant == 'potatoBomb':
        return classPotato.PotatoBomb(*coords)
    else:
        return classSunrise.Sunrise(*coords, game)
