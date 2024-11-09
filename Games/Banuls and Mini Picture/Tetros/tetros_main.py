#Project TETROS
import tetros_library
import tetros_classes 
import pygame
from math import *
from threading import *
import random as rn
from pygame.locals import *
from PIL import Image
import time as tm
import socket
#-------------------------------------------------------------------------------
pygame.init()
fenêtre=pygame.display.set_mode((1920,1080),FULLSCREEN)
a=tetros_classes.Pièce(tetros_library.Pack_selectionné,1,900,600,1,120,120)
continuer=True
while continuer:
    fenêtre.blit(tetros_library.image_fond,(0,0))
    fenêtre.blit(tetros_library.image_plateau,(600,0))
    fenêtre.blit(a.sprite,(a.pox,a.posy))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            continuer=False
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                continuer=False