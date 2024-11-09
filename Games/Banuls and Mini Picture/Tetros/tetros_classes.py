import tetros_library 
import pygame
from math import *
from threading import *
import random as rn
from pygame.locals import *
from PIL import Image
import time as tm
import socket
#------------------------------------------------------------------------------------------------
class Pièce:
    def __init__(self,pack_de_text,id,posx,posy,vitesse,scalex,scaley):
        self.pox=posx
        self.posy=posy
        self.vitesse=vitesse
        self.sprite=pygame.transform.scale(pygame.image.load(f"Packs_de_textures\{pack_de_text}\id{id}.png").convert_alpha(),(scalex,scaley))
        