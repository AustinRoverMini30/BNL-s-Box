import pygame
from math import *
from threading import *
import random as rn
from pygame.locals import *
from PIL import Image
import time as tm
import socket
#------------------------------------------------------------------------------------------------
Pack_selectionné="Base"
image_fond=pygame.transform.scale(pygame.image.load(f"Packs_de_textures\{Pack_selectionné}\Fond_jeu_normal.png"),(1920,1080))
image_plateau=pygame.transform.scale(pygame.image.load(f"Packs_de_textures\{Pack_selectionné}\grille_base.png"),(720,1080))