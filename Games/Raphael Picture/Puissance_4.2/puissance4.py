
import time
import sys
import pygame
import json
from pygame.locals import *
from random import randint

pygame.display.set_caption("Puissance 4 by Raphaël")
pygame.display.set_icon(pygame.image.load("images/wall-e.png"))

def principal():
	window.blit(pygame.image.load("images/start.png").convert(), (0,0))
	pygame.display.flip()
	while True:
		pygame.time.Clock().tick(frame)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 489 > event.pos[1]:
						puissance4()
					if 488 < event.pos[1]:
						aide()
			if event.type == KEYDOWN:
				puissance4()

def aide():
	window.blit(pygame.image.load("images/help.png").convert(), (0,0))
	pygame.display.flip()
	while True:
		pygame.time.Clock().tick(frame)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == KEYDOWN:
				principal()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					principal()


def menu():
	time.sleep(1.5)
	menu = pygame.image.load("images/menu.png").convert()
	window.blit(menu, (230, 200))
	pygame.display.flip()
	while True:
		pygame.time.Clock().tick(frame)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 200 < event.pos[1] < 239:
						if 230 < event.pos[0] < 364:
							principal()
						if 364 < event.pos[0] < 498:
							puissance4()
			if event.type == KEYDOWN:
				if event.key == K_KP0:
					principal()
				if event.key == K_KP1:
					puissance4()

def puissance4():
    n = 0
    window.blit(pygame.image.load("images/grille.png").convert(), (0, 0))
    pygame.display.flip()
    background = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
    w = 0
    plein = 0
    player = randint(1,2)
    tyellow = pygame.image.load("images/tyellow.png").convert()
    tred = pygame.image.load("images/tred.png").convert()
    while True:
    	while True:
    		if n > 41:
    			window.blit(pygame.image.load("images/equality.png").convert(), (245, 100))
    			pygame.display.flip()
    			menu()
    		if player == 1:
    			window.blit(tyellow, (500, 550))
    			pygame.display.flip()
    		else:
    			window.blit(tred, (500, 550))
    			pygame.display.flip()
    		col = selectcol()
    		for k in range(6):
    			if background[col][k] == 0:
    				background[col][k] = player
    				grille(k, col, player)
    				break
    			if k == 5:
    				plein = 1
    		if plein == 0:
    			break
    		plein = 0
    	n += 1
    	if player == 1:
    		player = 2
    	else:
    		player = 1
    	if n > 6:
    		w = gagnant(background)
    		if w == 1 or w == 2:
    			menu()

def selectcol():
	while True:
		pygame.time.Clock().tick(frame)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 10 < event.pos[1] < 525:
						if 31 < event.pos[0] < 103:
							return 0
						if 118 < event.pos[0] < 187:
							return 1
						if 202 < event.pos[0] < 272:
							return 2
						if 287 < event.pos[0] < 357:
							return 3
						if 373 < event.pos[0] < 443:
							return 4
						if 457 < event.pos[0] < 527:
							return 5
						if 542 < event.pos[0] < 612:
							return 6
			if event.type == KEYDOWN:
				if event.key == K_KP1:
					return 0
				if event.key == K_KP2:
					return 1
				if event.key == K_KP3:
					return 2
				if event.key == K_KP4:
					return 3
				if event.key == K_KP5:
					return 4
				if event.key == K_KP6:
					return 5
				if event.key == K_KP7:
					return 6

def gagnant(b):
	if ligne(b)[0] == 1:
		résultat(ligne(b)[1], ligne(b)[2], ligne(b)[3], ligne(b)[4], ligne(b)[5], ligne(b)[6], ligne(b)[7], ligne(b)[8], ligne(b)[9])
		return 1
	if colone(b)[0] == 1:
		résultat(colone(b)[1], colone(b)[2], colone(b)[3], colone(b)[4], colone(b)[5], colone(b)[6], colone(b)[7], colone(b)[8], colone(b)[9])
		return 1
	if diaglltr(b)[0] == 1:
		résultat(diaglltr(b)[1], diaglltr(b)[2], diaglltr(b)[3], diaglltr(b)[4], diaglltr(b)[5], diaglltr(b)[6], diaglltr(b)[7], diaglltr(b)[8], diaglltr(b)[9])
		return 1
	if diagtllr(b)[0] == 1:
		résultat(diagtllr(b)[1], diagtllr(b)[2], diagtllr(b)[3], diagtllr(b)[4], diagtllr(b)[5], diagtllr(b)[6], diagtllr(b)[7], diagtllr(b)[8], diagtllr(b)[9])
		return 1
	if ligne(b)[0] == 2:
		résultat(ligne(b)[1], ligne(b)[2], ligne(b)[3], ligne(b)[4], ligne(b)[5], ligne(b)[6], ligne(b)[7], ligne(b)[8], ligne(b)[9])
		return 2
	if colone(b)[0] == 2:
		résultat(colone(b)[1], colone(b)[2], colone(b)[3], colone(b)[4], colone(b)[5], colone(b)[6], colone(b)[7], colone(b)[8], colone(b)[9])
		return 2
	if diaglltr(b)[0] == 2:
		résultat(diaglltr(b)[1], diaglltr(b)[2], diaglltr(b)[3], diaglltr(b)[4], diaglltr(b)[5], diaglltr(b)[6], diaglltr(b)[7], diaglltr(b)[8], diaglltr(b)[9])
		return 2
	if diagtllr(b)[0] == 2:
		résultat(diagtllr(b)[1], diagtllr(b)[2], diagtllr(b)[3], diagtllr(b)[4], diagtllr(b)[5], diagtllr(b)[6], diagtllr(b)[7], diagtllr(b)[8], diagtllr(b)[9])
		return 2
	return 0

def ligne(b):
	for l in range(6):
		for k in range(4):
			if b[k][l] == b[k+1][l] == b[k+2][l] == b[k+3][l] == 1:
				return [1,b,k,l,k+1,l,k+2,l,k+3,l]
			if b[k][l] == b[k+1][l] == b[k+2][l] == b[k+3][l] == 2:
				return [2,b,k,l,k+1,l,k+2,l,k+3,l]
	return [0]

def colone(b):
	for k in range(7):
		for l in range(3):
			if b[k][l] == b[k][l+1] == b[k][l+2] == b[k][l+3] == 1:
				return [1,b,k,l,k,l+1,k,l+2,k,l+3]
			if b[k][l] == b[k][l+1] == b[k][l+2] == b[k][l+3] == 2:
				return [2,b,k,l,k,l+1,k,l+2,k,l+3]
	return [0]

def diaglltr(b):
	for k in range(4):
		for l in range(3):
			if b[k][l] == b[k+1][l+1] == b[k+2][l+2] == b[k+3][l+3] == 1:
				return [1,b,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
			if b[k][l] == b[k+1][l+1] == b[k+2][l+2] == b[k+3][l+3] == 2:
				return [2,b,k,l,k+1,l+1,k+2,l+2,k+3,l+3]
	return [0]

def diagtllr(b):
	for k in range(4):
		for l in range(3):
			if b[k][5-l] == b[k+1][4-l] == b[k+2][3-l] == b[k+3][2-l] == 1:
				return [1,b,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
			if b[k][5-l] == b[k+1][4-l] == b[k+2][3-l] == b[k+3][2-l] == 2:
				return [2,b,k,5-l,k+1,4-l,k+2,3-l,k+3,2-l]
	return [0]

def grille(coord1, coord2, color):
	pioncollin = [coord1, coord2]
	c = [440 + pioncollin[0]*-85, 28 + pioncollin[1]*85]
	if color == 1:
		pionj = pygame.image.load("images/pionj.png").convert()
		window.blit(pionj, (c[1], c[0]))
	else:
		pionr = pygame.image.load("images/pionr.png").convert()
		window.blit(pionr, (c[1], c[0]))
	pygame.display.flip()

def résultat(b, k1, c1, k2, c2, k3, c3, k4, c4):
	window.blit(pygame.image.load("images/grille.png").convert(), (0, 0))
	c = b[k1][c1]
	grille(c1, k1, c)
	grille(c2, k2, c)
	grille(c3, k3, c)
	grille(c4, k4, c)
	if b[k1][c1] == 1:
		window.blit(pygame.image.load("images/rouge.png").convert(), (80, 525))
	else:
		window.blit(pygame.image.load("images/jaune.png").convert(), (80, 525))
	pygame.display.flip()


if __name__ == '__main__':
	for setup in json.load(open("setup.json")):
		frame = setup.pop("frame")
	pygame.init()
	window = pygame.display.set_mode((648,604), RESIZABLE)
	principal()

