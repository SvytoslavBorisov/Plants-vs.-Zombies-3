import pygame
import random
import os
from allConstants import *
from plants import classSunrise, classGatlingPea, classWallNut


def choicePlant(indPlant, coords):
    if indPlant == 'gatlingPea':
        return classGatlingPea.GatlingPea(*coords)
    elif indPlant == 'sunrise':
        return classSunrise.Sunrise(*coords)
    elif indPlant == 'wallNut':
        return classWallNut.WallNut(*coords)
    else:
        return classSunrise.Sunrise(*coords)
