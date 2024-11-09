# Créé par Nicolas, le 02/11/2021 en Python 3.7
import psutil
import os
import pygame
from pygame.locals import *
import time
import sys
import datetime
import sqlite3

erreur=0

erreur_report = False

try:

    class Data_base:
        def __init__(self, name):
            self.name = name
        def connect(self):
            conn = None
            try:
                self.conn = sqlite3.connect(self.name)
            except Error as e:
                print(e)
            return self.conn
        def refresh(self):
            cur = self.connect().cursor()
            cur.execute("SELECT * FROM Variables")
            rows = cur.fetchall()
            for row in rows:
                try:
                    globals() [row[1]] = int(row[2])
                except:
                    globals() [row[1]] = row[2]
            cur.close()
        def get(self):
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Variables")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            cur.close()
        def update(self, name_var, val):
            cur = self.conn.cursor()
            cur.execute("UPDATE Variables SET stat = '"+val+"' WHERE name = '"+name_var+"';")
            self.conn.commit()
            self.refresh()
        def exit(self):
            self.conn.close()

    data_base = Data_base("data_base.db")
    data_base.refresh()

    def afficher_batons(n):
        x = 0
        for i in range(n):
            color = (255,255,0)
            pygame.draw.rect(fenetre, color, pygame.Rect(160,340-x,200, 15))
            x +=30
        pygame.display.flip()

    """
     Gestion de la fenêtre Pygame
    """

    # Initialisation de la bibliothèque Pygame
    pygame.init()
    # Création de la fenêtre
    fenetre = pygame.display.set_mode((400,430))
    # Gestion de l'icône de la fenêtre
    pygame.display.set_icon(pygame.image.load("Images/BNLalpha.png"))
    pygame.display.set_caption('Jauge (Python edition)')
    pygame.mixer.music.set_volume(volume_BNL/10)


    # Rafraichissement
    pygame.display.flip()
    continuer = True
    full=1
    x=0
    text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"

    if animations:
        pygame.mixer.music.load("Sounds/BNL-start.mp3")
        pygame.mixer.music.play()
        for i in range(119):
            text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
            fond1 = pygame.image.load(text).convert()
            fenetre.blit(fond1,(-440,-160))
            pygame.display.flip()
            x+=1
            time.sleep(0.02)

    battery = psutil.sensors_battery()
    if battery==None:
        while continuer:
            erreur=1
            erreur_1 = pygame.image.load("Erreur/erreur.png").convert()
            fenetre.blit(erreur_1,(0,0))
            pygame.display.flip()
            for event in pygame.event.get():

            # Pour quitter en fermant la fenêtre
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                        x=118
                        text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                        pygame.mixer.music.load("Sounds/BNL-shutdown.mp3")
                        pygame.mixer.music.play()
                        for i in range(119):
                            text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                            fond1 = pygame.image.load(text).convert()
                            fenetre.blit(fond1,(-440,-160))
                            pygame.display.flip()
                            x-=1
                            time.sleep(0.03)
                        pygame.quit()
                        continuer = False
                        os.startfile("Menu.bat")
                        sys.exit()

                if event.type == QUIT:
                    x=118
                    text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                    pygame.mixer.music.load("Sounds/BNL-shutdown.mp3")
                    pygame.mixer.music.play()
                    for i in range(119):
                        text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                        fond1 = pygame.image.load(text).convert()
                        fenetre.blit(fond1,(-440,-160))
                        pygame.display.flip()
                        x-=1
                        time.sleep(0.03)
                    sortie=0
                    pygame.quit()
                    continuer = False
                    sys.exit()


    fond = pygame.image.load("Images/fond.png").convert()
    sun = pygame.image.load("Images/solarcharge.jpg").convert()
    black = pygame.image.load("Images/Black.png").convert()
    # Gestion du titre en haut de la fenêtre
    pygame.display.set_caption("Solar Charge Level")
    # Positionnement
    fenetre.blit(fond,(0,0))
    fenetre.blit(sun,(30,90))
    fenetre.blit(black,(160,90))
    # Pour afficher un texte dans pygame, avec une police particulière
    font = pygame.font.Font(None, 40)
    texte = font.render("SOLAR CHARGE LEVEL", 1, (255,255,0))
    fenetre.blit(texte, (50, 50))
    saisie=0
    code_secret=0
    sortie=0
    while continuer and erreur==0:
        pygame.display.flip()
        battery = psutil.sensors_battery()
        level= battery.percent
        plugged = battery.power_plugged
        a_string = level/10
        float_str = float(a_string)
        test= int(float_str)
        if level==100 and plugged and full==1:
                    fenetre.blit(black,(160,90))
                    n=9
                    color = (255,255,0)
                    pygame.draw.rect(fenetre, color, pygame.Rect(160, 370, 200, 40))
                    afficher_batons(n)
                    font = pygame.font.Font(None, 40)
                    texte = font.render("SOLAR CHARGE LEVEL", 1, (255,255,0))
                    fenetre.blit(texte, (50, 50))
                    pygame.display.flip()
                    pygame.mixer.music.load("Sounds/Charge.mp3")
                    pygame.mixer.music.play()
                    full=0
        elif level>=10 and level<100:
                    fenetre.blit(black,(160,90))
                    n=test
                    color = (255,255,0)
                    pygame.draw.rect(fenetre, color, pygame.Rect(160, 370, 200, 40))
                    afficher_batons(n)
                    font = pygame.font.Font(None, 40)
                    texte = font.render("SOLAR CHARGE LEVEL", 1, (255,255,0))
                    fenetre.blit(texte, (50, 50))
                    pygame.display.flip()
                    full=1
                    time.sleep(0.5)
        elif plugged==0 and level==100:
            fenetre.blit(black,(160,90))
            n=9
            color = (255,255,0)
            pygame.draw.rect(fenetre, color, pygame.Rect(160, 370, 200, 40))
            afficher_batons(n)
            font = pygame.font.Font(None, 40)
            texte = font.render("SOLAR CHARGE LEVEL", 1, (255,255,0))
            fenetre.blit(texte, (50, 50))
            pygame.display.flip()
            full=1
            time.sleep(0.5)

        elif plugged and level<10:
                    fenetre.blit(black,(160,90))
                    n=0
                    color = (255,255,0)
                    pygame.draw.rect(fenetre, color, pygame.Rect(160, 370, 200, 40))
                    pygame.display.flip()
                    font = pygame.font.Font(None, 40)
                    pygame.display.flip()
        elif level<10 and not(plugged):
                    fenetre.blit(black,(160,90))
                    n=0
                    color = (255,0,0)
                    pygame.draw.rect(fenetre, color, pygame.Rect(160, 370, 200, 40))
                    pygame.display.flip()
                    font = pygame.font.Font(None, 40)
                    texte = font.render("WARNING", 1, (0,0,0))
                    fenetre.blit(texte, (190, 378))
                    pygame.display.flip()
                    pygame.mixer.music.load("Sounds/Son3.mp3")
                    pygame.mixer.music.play()
                    time.sleep(0.3)
                    fenetre.blit(black,(160,90))
                    font = pygame.font.Font(None, 40)
                    pygame.display.flip()
                    time.sleep(0.3)

         # Gestion des événements
        for event in pygame.event.get():

            # Pour quitter en fermant la fenêtre
            if event.type == QUIT:
                x=118
                text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                if animations:
                    pygame.mixer.music.load("Sounds/BNL-shutdown.mp3")
                    pygame.mixer.music.play()
                    for i in range(119):
                        text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                        fond1 = pygame.image.load(text).convert()
                        fenetre.blit(fond1,(-440,-160))
                        pygame.display.flip()
                        x-=1
                        time.sleep(0.03)
                sortie=0
                pygame.quit()
                continuer = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and saisie==0:
                    code_secret="B"
                    saisie=1
                if event.key == pygame.K_n and saisie==1:
                        code_secret+="N"
                        saisie=2
                if event.key == pygame.K_l and saisie==2:
                            code_secret+="L"
                            saisie=3
                if event.key != pygame.K_b and event.key != pygame.K_n and event.key != pygame.K_l and saisie==3:
                    code_secret=0
                    saisie=0

        if code_secret=="BNL":
            x=118
            text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
            if animations:
                pygame.mixer.music.load("Sounds/BNL-shutdown.mp3")
                pygame.mixer.music.play()
                for i in range(119):
                    text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                    fond1 = pygame.image.load(text).convert()
                    fenetre.blit(fond1,(-440,-160))
                    pygame.display.flip()
                    x-=1
                    time.sleep(0.03)
            pygame.quit()
            continuer = False
            sortie=1

    ex=0
    if sortie==1:
        os.startfile("Menu.bat")
        exit()

except Exception as e:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    fichier=open("log.txt","a")
    fichier.write(str(e)+"\n")
    fichier.write("Localisation : Level"+"\n")
    fichier.write(str(dt_string) +"\n")
    fichier.write("\n")
    continuer = False
    erreur_report = True
    erreur_détail = e

# Menu sécurisé d'erreur (accueil)
while erreur_report:
    check_up = True
    pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
    try :
        font = pygame.font.Font(font_BNL, 30)
    except :
        font = pygame.font.Font(None, 30)

    texte = font.render("Security mode", 5, (255,255,255))
    fenetre.blit(texte, (125, 10))
    texte = font.render("Level a rencontré une erreur...", 1, (255,255,255))
    fenetre.blit(texte, (10, 60))
    texte = font.render("Analyse via BNL's Box recommandée :", 1, (255,255,255))
    fenetre.blit(texte, (10, 100))
    texte = font.render("Accédez aux paramètres et tapez dans", 1, (255,255,255))
    fenetre.blit(texte, (10, 140))
    texte = font.render("la console : error/", 1, (255,255,255))
    fenetre.blit(texte, (10, 170))
    texte = font.render("En cas d'anomalies récurrentes,", 1, (255,255,255))
    fenetre.blit(texte, (10, 220))
    texte = font.render("contactez MINI Picture pour correctifs...", 1, (255,255,255))
    fenetre.blit(texte, (10, 250))
    texte = font.render("Appuyez sur ENTER", 1, (255,0,0))
    fenetre.blit(texte, (10, 300))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                pygame.quit()
                erreur_report = False
                os.startfile("Menu.bat")
                exit()

        if event.type == QUIT:
            pygame.quit()
            erreur_report = False
            exit()