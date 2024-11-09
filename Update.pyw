# Créé par Nicolas, le 23/01/2023 en Python 3.7

# Importation des modules
import os
import time
from zipfile import ZipFile
import sys
import shutil
import datetime
import pip
import random
import importlib
import sqlite3
import socket, sys
from threading import Thread
import base64
import pygame
from pygame.locals import *
import easygui

update_reset_stat = False
try :
    from Update_check import*
    from Version_Update import*
    if update_stat[0] == "update" and Update_Update != Version_Update:
        update = "update"
        update_reset_stat = True
        update_process = ["Update.delete(['Update.pyw', 'Version_Update.py'])", "Update.unzip(['Update.pyw','Version_Update.py','Update_label.png'])"]
    test = update_process
except :
    update_process = ["Update.delete(os.listdir())", "Update.unzip('all')"]

fenetre = pygame.display.set_mode((960,540))

pygame.init()

pygame.display.set_caption("BNL's Update Utility (Windows Python edition)")

continuer = True

font = pygame.font.Font(None, 30)

try:
    img_label = pygame.image.load("Update_label.png")
    label_loaded = True
except:
    label_loaded = False

def STOP(act=None):
    global continuer
    continuer = False
    pygame.quit()

    try :
        if update_stat[1] == "restart" and update_reset_stat:
            os.startfile("Update.bat")
        elif after_update == "Menu":
            os.startfile("Menu.bat")
    except :
        None

    exit()

class Upgrade_act:
    def __init__(self, target):
        self.target = target
        self.stat = "None"
        self.color = (255,255,255)
        self.text = ""

    def delete(self, liste):
        global avance
        global zipObject

        self.text = "Suppression en cours..."

        i = 0
        dec = 892 / len(liste)

        while i < len(liste):
            if liste[i] != "Update.pyw" and liste[i] != "Level mise à niveau.zip" and liste[i] != "Update_label.png":
                try:
                    shutil.rmtree(liste[i])
                except NotADirectoryError :
                    os.remove(liste[i])
            i += 1
            avance += dec

        avance = 892

        time.sleep(1)

        avance = 0

    def unzip(self, liste=[], directory=False):
        global zipObject
        global avance

        self.text = "Extraction en cours..."

        if liste == 'all':
            with ZipFile(self.target, 'r') as zipObject:
                listOfFileNames = zipObject.namelist()
                liste = listOfFileNames

                dec = 892 / len(liste)
                for fileName in liste:
                    zipObject.extract(fileName)
                    avance += dec

                avance = 892

        elif directory:
            with ZipFile(self.target, 'r') as zipObject:
                listOfFileNames = zipObject.namelist()

                dec = 892 / len(listOfFileNames)
                for fileName in listOfFileNames:
                    if fileName.startswith(liste):
                        zipObject.extract(fileName)
                    avance += dec

                avance = 892

        else:
            with ZipFile(self.target, 'r') as zipObject:

                dec = 892 / len(liste)
                for fileName in liste:
                    zipObject.extract(fileName)
                    avance += dec

                avance = 892

def select(liste):
    Update.text = "En attente de la fermeture de BNL's Box..."
    time.sleep(2)
    try:
        for e in liste:
            eval(e)
        if update_stat[1] == "restart" and update_reset_stat:
            Update.text = "Mise à jour de l'utilitaire terminée : redémarrage de BNL's Update Utility..."
        else:
            Update.text = "Mise à jour effectuée !"
        Update.color = (0,255,0)

    except Exception as e:
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        fichier=open("log.txt","a")
        fichier.write(str(dt_string) +"\n")
        fichier.write(str(e)+"\n")
        fichier.write("Localisation : BNL's Update Utility" +"\n")
        fichier.write("\n")
        fichier.close()

        Update.text = "Echec de la mise à niveau..."
        Update.color = (255,0,0)

    Update.stat = "finish"

ind1 = 0
ind2 = 0
ind3 = 0
ind4 = 0

avance = 0

Update = Upgrade_act("Level mise à niveau.zip")

Thread_n = Thread(target=select, args=(update_process,))
Thread_n.start()

def animation():
    global ind1
    global ind2
    global ind3
    global ind4

    if ind1 > 960*2:
        ind1 = 0
    elif ind2 > 540*2:
        ind2 = 0
    elif ind3 > 960*2:
        ind3 = 0
    elif ind4 > 540*2:
        ind4 = 0

    if ind1 > 960:
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(ind1-960,0,960, 5))
    else:
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(0,0,ind1, 5))
    if ind2 > 540:
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(955,ind2-540,5,540))
    else:
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(955,0,5,ind2))

    ind1 += 1
    ind2 += 1
    ind3 += 1
    ind4 += 1
    
def BNL_Box_Update_test(time_test):
    Update.text = "Test de BNL's Update Utility"
    time.sleep(time_test)
    
def startup_animation():
    for i in range(898):
        pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,960, 540))
    
        animation()

        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(960-ind3,535,960, 5))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(0,540-ind4,5,540))

        texte = font.render(Update.text, 1, (255,255,255))
        fenetre.blit(texte, (40, 406))
        
        if label_loaded:
            pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,50,900, 300),2,0)
            fenetre.blit(img_label, (34,54))

        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,400,2, i*(30/900)))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(928,400,2, i*(30/900)))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,450,2, i*(50/900)))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(928,450,2, i*(50/900)))

        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(32,400,i, 2))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(32,428,i, 2))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(32,450,i, 2))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(32,498,i, 2))

        pygame.display.flip()
    
startup_animation()
    
while continuer:

    pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,960, 540))

    animation()

    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(960-ind3,535,960, 5))
    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(0,540-ind4,5,540))

    texte = font.render(Update.text, 1, (255,255,255))
    fenetre.blit(texte, (40, 406))
    
    if label_loaded:
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,50,900, 300),2,0)
        fenetre.blit(img_label, (34,54))

    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,400,900, 30),2,0)
    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,450,900, 50),2,0)

    pygame.draw.rect(fenetre, Update.color, pygame.Rect(34,454,avance, 42))

    pygame.display.flip()


    if Update.stat == "finish":
        pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,960, 540))

        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(960-ind3,535,960, 5))
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(0,540-ind4,5,540))

        texte = font.render(Update.text, 1, (255,255,255))
        fenetre.blit(texte, (40, 406))
        if label_loaded:
            pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,50,900, 300),2,0)
            fenetre.blit(img_label, (34,54))

        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,400,900, 30),2,0)
        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(30,450,900, 50),2,0)

        pygame.draw.rect(fenetre, Update.color, pygame.Rect(34,454,avance, 42))
        pygame.display.flip()
        time.sleep(2)
        STOP()

    for event in pygame.event.get():
        if event.type == QUIT:
            STOP()

