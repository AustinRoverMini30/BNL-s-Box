
# Créé par Nicolas, le 18/11/2021 en Python 3.7

"""Importation des modules : en cas d'absence de certains, le programme lancera automatiquement leur installation avant de redémarrer"""

étape_programme = "Importation des modules"

# Importation des modules (pré-installés normalement)

import pip
import os
import time

continuer = True
erreur_report = False
test_error = True

# Suppression des fichiers du dossier __pycache__ (.pyc).

try:
    del_cache = os.listdir("__pycache__")
    for elem in del_cache:
        try:
            os.remove(f"__pycache__\{elem}")
        except:
            None
except:
    None

# Importation des modules (installés, ou nécessitant une installation en cas d'erreur d'importation)

try:
    import music_tag
    import psutil
    import pygame
    import PIL
    import yt_dlp
    from yt_dlp.postprocessor import FFmpegPostProcessor    
    from zipfile import ZipFile
    import random
    import datetime
    import importlib
    import sqlite3
    import socket, sys
    from threading import Thread
    import base64
    from math import *
    import requests
    import io
    import shutil
    import hashlib

    from PIL import Image , ImageDraw, ImageFilter
    from pygame.locals import *
    import pyperclip
    import gdown
    import easygui

    taille = (1280,720)
    test_error = False

    import djitellopy
    from djitellopy import Tello
    import cv2
    import numpy

except ModuleNotFoundError:
    os.startfile("Update all.bat")
    exit()

# Fermeture de l'intégralité du programme
def STOP(os_start=None):
    global continuer
    global paramètres
    global menu_continuer
    global soundtrack
    global video
    global video_old
    global animations_continuer
    global fond_écran
    global upgrade_continuer
    global version_continuer
    global veille
    global jeux
    global jeux_menu
    global Puissance4
    global Puissance4_by_Maxime
    global Menu_skin1
    global Jump
    global Jump_active
    global Jump_menu
    global TANK_M
    global Minesweeper
    global Minesweeper_menu
    global Minesweeper_game
    global Vilallongue_chroni_game
    global data_base
    global mail_box
    global mail_box_init
    global tools
    global Youtube_downloader
    global Youtube_downloader_menu
    global Youtube_downloader_playlist_listing
    global Youtube_downloader_settings
    global tools_selection
    global Tello_control
    global Tello_control_check_up
    global Tello_control_before_flight
    global Tello_control_flight_mode
    global Tello_control_menu
    global Tello_log
    global Youtube_loading_signal

    pygame.font.quit()
    
    try:
        Tello_log.close()
    except:
        None

    continuer = False
    paramètres=False
    menu_continuer=False
    soundtrack=False
    video=False
    video_old = False
    animations_continuer=False
    fond_écran=False
    upgrade_continuer=False
    version_continuer=False
    veille = False
    jeux = False
    jeux_menu = False
    Puissance4 = False
    Puissance4_by_Maxime = False
    Menu_skin1 = False
    Jump = False
    Jump_menu = False
    Jump_active = False
    TANK_M = False
    Minesweeper = False
    Minesweeper_menu = False
    Minesweeper_game = False
    Vilallongue_chroni_game = False
    mail_box = False
    mail_box_init = False
    tools = False
    Youtube_downloader = False
    Youtube_downloader_menu = False
    Youtube_downloader_playlist_listing = False
    Youtube_downloader_settings = False
    tools_selection = False

    Tello_control = False
    Tello_control_check_up = False
    Tello_control_before_flight = False
    Tello_control_flight_mode = False
    Tello_control_menu = False

    try:
        Youtube_loading_signal.stop_signal()
    except:
        None
    
    pygame.mixer.music.pause()
    try:
        fermeture(173)
    except:
        None
    pygame.quit()
    try:
        if widget_soundtrack :
            fichier=open("Widgets_soundtrack_pos.py","w")
            fichier.write("widget_soundtrack_coor = ["+str(widget_soundtrack_coor[0])+","+str(widget_soundtrack_coor[1])+"]"+"\n")
            fichier.write("widget_soundtrack = True")
            fichier.close()
        if not(widget_soundtrack) :
            fichier=open("Widgets_soundtrack_pos.py","w")
            fichier.write("widget_soundtrack_coor = [0,0]"+"\n")
            fichier.write("widget_soundtrack = False")
            fichier.close()

        if widget_level :
            fichier=open("Widgets_level_pos.py","w")
            fichier.write("widget_level_coor = ["+str(widget_level_coor[0])+","+str(widget_level_coor[1])+"]"+"\n")
            fichier.write("widget_level = True")
            fichier.close()
        if not(widget_level) :
            fichier=open("Widgets_level_pos.py","w")
            fichier.write("widget_level_coor = [0,0]"+"\n")
            fichier.write("widget_level = False")
            fichier.close()
    except:
        None

    if os_start != None:
        os.startfile(os_start)

    try:
        data_base.exit()
    except:
        None
    try:
        music_data.exit()
    except:
        None

    exit()

# Début de la boucle "try" : en cas d'erreur, Python sautera directement au menu d'erreur

try:
    """Déclaration de l'objet "Data_base", qui exploite la base de données SQL"""
    class Data_base:
        def __init__(self, name):
            self.name = name
        def connect(self):
            conn = None
            try:
                fichier=open(self.name,"r")
                fichier.close()
                self.conn = sqlite3.connect(self.name, check_same_thread=False)
            except Exception as e:
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
                    if row[2][0] == "(" or row[2][0] == "[":
                        globals() [row[1]] = eval(row[2])
                    else:
                        globals() [row[1]] = row[2]
            cur.close()

        def get(self, command):
            cur = self.conn.cursor()
            cur.execute(command)
            rows = cur.fetchall()
            liste_s = []
            for row in rows:
                row = list(row)
                row[-1] = row[-1].replace("\\\\", "\\")
                liste_s.append(row)
            cur.close()
            return liste_s

        def update(self, name_var, val):
            cur = self.conn.cursor()
            cur.execute("UPDATE Variables SET stat = '"+val+"' WHERE name = '"+name_var+"';")
            self.conn.commit()
            self.refresh()
        def exit(self):
            self.conn.close()
        def add(self, rule, elem):
            cur = self.conn.cursor()
            cur.execute(rule+str(elem)+";")
            self.conn.commit()
        def delete(self, rule, elem):
            cur = self.conn.cursor()
            cur.execute(rule+str(elem)+";")
            self.conn.commit()

    data_base = Data_base("data_base.db")
    data_base.refresh()

    music_data = Data_base("audio_data.db")
    music_data.connect()

    """ Importation du fichier de langue """
    sys.path.insert(0, './Lang/')

    import Lang

    importlib.import_module(f".{Lang_selected}", "Lang")

    langue = eval(f"Lang.{Lang_selected}")

    """ Initialisation de la fenêtre """
    étape_programme = "Configuration/ouverture de la fenêtre"
    try:
        pygame.display.set_icon(pygame.image.load("Images/BNL_box_icon.png"))
    except:
        None
    try :
        if full_screen :
            flags = FULLSCREEN
            fenetre = pygame.display.set_mode(taille, flags)
        else :
            fenetre = pygame.display.set_mode((1280,720))

    except:
        fenetre = pygame.display.set_mode((1280,720))

    pygame.init()

    pygame.display.set_caption("BNL's Box (Windows Python edition)")

    """ Importation des fichiers externes (.py), comportant diverses informations relatives aux widgets, à la personnalisation, etc."""
    étape_programme = "Importation des fichiers externes"
    import Update_check
    import Changelog_txt_up
    from Version_Menu import*
    from Version_Level import*
    from Version_Update import*
    from Variables import*
    from Widgets_soundtrack_pos import*
    from Widgets_level_pos import*
    from Changelog_txt import*
    from Update_check import*

    """Initialisation de variables diverses"""

    étape_programme = "Variables"

    décalage_widget = [0,0]
    full=1
    x=0
    p=0
    lecture=True
    titre=""
    temps=0
    avance=0
    position_selecteur = 0
    liste = []
    score_card = 0
    yt_dlp_thread_list = 0
    video_old = False

    if Skin_selected == "Legacy":
        Menu_skin1 = True
        menu_continuer = False
        Menu_skin2 = False

    elif Skin_selected == "Titanium":
        menu_continuer = True
        Menu_skin1 = False
        Menu_skin2 = False

    elif Skin_selected == "Carroussel":
        menu_continuer = False
        Menu_skin2 = True
        Menu_skin1 = False

    now = datetime.datetime.now()

    """ Assignation d'un thème en fonction de la date, si thèmes automatiques activés """
    if Auto_theme:
        if now.month == 12 and now.day < 29 and now.day > 10:
            theme_selected = "MINI_Picture_original_christmas_theme"
        """
        elif now.month == 7 and now.day == 14:
            theme_selected = "MINI_Picture_original_Bastille_day"
        elif now.month == 1 and now.day == 1:
            theme_selected = "MINI_Picture_original_New_Year"
        """

    """ Déclaration de l'objet "Carroussel", support du menu principal Carroussel, des menu vidéos et jeux """
    class Carroussel :
        def __init__(self, liste, path, name):
            self.name = name
            self.liste = liste
            self.selection = 0
            self.selection_temp1 = len(liste)-1
            self.selection_temp2 = len(liste)-2
            self.selection_temp3 = 1
            self.selection_temp4 = 2
            self.path = path
        def open(self):
            global vignette_1
            global vignette_2
            global vignette_3
            global vignette_4
            global vignette_5

            vignette_1 = pygame.image.load(self.path+self.liste[self.selection_temp2]+".png").convert_alpha()
            vignette_5 = pygame.image.load(self.path+self.liste[self.selection_temp4]+".png").convert_alpha()

            vignette_3 = pygame.image.load(self.path+self.liste[self.selection]+".png").convert_alpha()

            vignette_2 = pygame.image.load(self.path+self.liste[self.selection_temp1]+".png").convert_alpha()
            vignette_4 = pygame.image.load(self.path+self.liste[self.selection_temp3]+".png").convert_alpha()

            vignette_1 = pygame.transform.scale(vignette_1, (300,169))
            vignette_5 = pygame.transform.scale(vignette_5, (300,169))

            vignette_2 = pygame.transform.scale(vignette_2, (400,225))
            vignette_4 = pygame.transform.scale(vignette_4, (400,225))

            if transition_check:

                for i in range(125) :
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))

                    fenetre.blit(vignette_1,(100,-225+i*4))
                    fenetre.blit(vignette_5,(880,775-i*4))
                    fenetre.blit(vignette_2,(200,747-i*4))
                    fenetre.blit(vignette_4,(680,-253+i*4))
                    fenetre.blit(vignette_3,(-701+i*8,168))
                    fenetre.blit(Gauche_video2,(-65+i,500))
                    fenetre.blit(Droite_video2,(1314-i,500))

                    if jeux:
                        fenetre.blit(Selection_menu,(455,0))
                        fenetre.blit(texte_jeux, (500, 20))
                        fenetre.blit(Autopilot_menu,(755,0))
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(100,5))
                    else:
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        None
        def close(self):
            global vignette_1
            global vignette_2
            global vignette_3
            global vignette_4
            global vignette_5

            vignette_2 = pygame.image.load(self.path+self.liste[self.selection_temp1]+".png").convert_alpha()
            vignette_5 = pygame.image.load(self.path+self.liste[self.selection_temp4]+".png").convert_alpha()

            vignette_3 = pygame.image.load(self.path+self.liste[self.selection]+".png").convert_alpha()

            vignette_1 = pygame.image.load(self.path+self.liste[self.selection_temp2]+".png").convert_alpha()
            vignette_4 = pygame.image.load(self.path+self.liste[self.selection_temp3]+".png").convert_alpha()

            vignette_1 = pygame.transform.scale(vignette_1, (300,169))
            vignette_5 = pygame.transform.scale(vignette_5, (300,169))

            vignette_2 = pygame.transform.scale(vignette_2, (400,225))
            vignette_4 = pygame.transform.scale(vignette_4, (400,225))

            if transition_check:

                for i in range(125) :
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))

                    fenetre.blit(vignette_1,(100,275-i*4))
                    fenetre.blit(vignette_5,(880,275+i*4))
                    fenetre.blit(vignette_2,(200,247+i*4))
                    fenetre.blit(vignette_4,(680,247-i*4))
                    fenetre.blit(vignette_3,(299-i*8,168))
                    fenetre.blit(Gauche_video2,(60-i,500))
                    fenetre.blit(Droite_video2,(1189+i,500))

                    if jeux:
                        fenetre.blit(Selection_menu,(455,0))
                        fenetre.blit(texte_jeux, (500, 20))
                        fenetre.blit(Autopilot_menu,(755,0))
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(100,5))
                    else:
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        None
            """
            self.selection = 0
            self.selection_temp1 = len(self.liste)-2
            self.selection_temp2 = len(self.liste)-1
            self.selection_temp3 = 1
            self.selection_temp4 = 2
            """
        def left(self):

            if transition_check:

                vignette_trans = pygame.image.load(self.path+self.liste[self.selection_trans]+".png").convert_alpha()
                vignette_trans = pygame.transform.scale(vignette_trans, (300,169))

                vignette_1_ref = pygame.image.load(self.path+self.liste[self.selection_temp2]+".png").convert_alpha()
                vignette_5_ref = pygame.image.load(self.path+self.liste[self.selection_temp4]+".png").convert_alpha()

                vignette_3_ref = pygame.image.load(self.path+self.liste[self.selection_old]+".png").convert_alpha()

                vignette_2_ref = pygame.image.load(self.path+self.liste[self.selection_temp1]+".png").convert_alpha()
                vignette_4_ref = pygame.image.load(self.path+self.liste[self.selection_temp3]+".png").convert_alpha()

                vignette_1_use = pygame.transform.scale(vignette_1_ref, (300,169))
                vignette_5_use = pygame.transform.scale(vignette_5_ref, (300,169))

                vignette_2_use = pygame.transform.scale(vignette_2_ref, (400,225))
                vignette_4_use = pygame.transform.scale(vignette_4_ref, (400,225))

                vignette_3_use = pygame.transform.scale(vignette_3_ref, (682,384))

                for i in range(70):

                    vignette_1_use = pygame.transform.scale(vignette_1_ref, (300+(4*i*0.3546),(300+(4*i*0.3546))/1.777))

                    vignette_4_use = pygame.transform.scale(vignette_4_ref, (400-(4*i*0.3546),(400-(4*i*0.3546))/1.777))
                    vignette_2_use = pygame.transform.scale(vignette_2_ref, (400+4*i,(400+4*i)/1.777))

                    vignette_3_use = pygame.transform.scale(vignette_3_ref, (682-4*i,(682-4*i)/1.777))

                    fenetre.blit(wallpapers_use.wallpaper,(0,0))

                    fenetre.blit(vignette_trans,(-464+4*i*2,275))
                    fenetre.blit(vignette_1_use,(100+(4*i*0.3546),275-(4*i*0.09929)))

                    fenetre.blit(vignette_5_use,(880+4*i*4,275))

                    fenetre.blit(vignette_4_use,(680+(4*i*0.7092),247+(4*i*0.09929)))

                    if i*4 < 141 :
                        fenetre.blit(vignette_2_use,(200+(4*i*0.3546),247-(4*i*0.28014)))
                        fenetre.blit(vignette_3_use,(299+(4*i*1.3510),168+(4*i*0.28014)))
                    else:
                        fenetre.blit(vignette_3_use,(299+(4*i*1.3510),168+(4*i*0.28014)))
                        fenetre.blit(vignette_2_use,(200+(4*i*0.3546),247-(4*i*0.28014)))

                    if self.name != "menu_carroussel":
                        fenetre.blit(Menu,(1150,20))
                    if self.name == "menu_games":
                        fenetre.blit(Selection_menu,(455,0))
                        fenetre.blit(texte_jeux, (500, 20))
                        fenetre.blit(Autopilot_menu,(755,0))
                    fenetre.blit(Gauche_video1,(60,505))
                    fenetre.blit(Droite_video2,(1189,500))

                    if carr_title_bar_stat == "enable":
                        fenetre.blit(carr_title_bar,(0,606))
                        texte = font.render(carr_lang_translate[menu_carroussel.liste[menu_carroussel.selection]], 1, color_menu)
                        fenetre.blit(texte, (20, 650))
                        fenetre.blit(carr_level_sun,(1070, 630))

                        try :
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                                afficher_batons_carr(n,1150,630)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                                afficher_batons_carr(n,1150,630)
                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (1130, 650))

                        except:
                            texte = font.render("ERROR", 1, (255,0,0))
                            fenetre.blit(texte, (1130,650))

                        fenetre.blit(widget_soundtrack_reculer,(600,650))
                        fenetre.blit(widget_soundtrack_avancer,(780,650))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_pause,(690,650))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(690,650))

                        texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                        fenetre.blit(texte, (600,620))

                        fenetre.blit(audio_reader_proc.min,(490,613))

                    if jeux:
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(100,5))
                    else:
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        None

        def right(self):
            if transition_check:

                vignette_trans = pygame.image.load(self.path+self.liste[self.selection_trans]+".png").convert_alpha()
                vignette_trans = pygame.transform.scale(vignette_trans, (300,169))

                vignette_1_ref = pygame.image.load(self.path+self.liste[self.selection_temp2]+".png").convert_alpha()
                vignette_5_ref = pygame.image.load(self.path+self.liste[self.selection_temp4]+".png").convert_alpha()

                vignette_3_ref = pygame.image.load(self.path+self.liste[self.selection_old]+".png").convert_alpha()

                vignette_2_ref = pygame.image.load(self.path+self.liste[self.selection_temp1]+".png").convert_alpha()
                vignette_4_ref = pygame.image.load(self.path+self.liste[self.selection_temp3]+".png").convert_alpha()

                vignette_1_use = pygame.transform.scale(vignette_1_ref, (300,169))
                vignette_5_use = pygame.transform.scale(vignette_5_ref, (300,169))

                vignette_2_use = pygame.transform.scale(vignette_2_ref, (400,225))
                vignette_4_use = pygame.transform.scale(vignette_4_ref, (400,225))

                vignette_3_use = pygame.transform.scale(vignette_3_ref, (682,384))

                for i in range(70):

                    vignette_5_use = pygame.transform.scale(vignette_5_ref, (300+(4*i*0.3546),(300+(4*i*0.3546))/1.777))

                    vignette_2_use = pygame.transform.scale(vignette_2_ref, (400-(4*i*0.3546),(400-(4*i*0.3546))/1.777))
                    vignette_4_use = pygame.transform.scale(vignette_4_ref, (400+4*i,(400+4*i)/1.777))

                    vignette_3_use = pygame.transform.scale(vignette_3_ref, (682-4*i,(682-4*i)/1.777))

                    fenetre.blit(wallpapers_use.wallpaper,(0,0))

                    fenetre.blit(vignette_1_use,(100-4*i*2,275))
                    fenetre.blit(vignette_trans,(1444-4*i*2,275))
                    fenetre.blit(vignette_5_use,(880-(4*i*0.7092),275-(4*i*0.09929)))

                    fenetre.blit(vignette_2_use,(200-(4*i*0.3546),247+(4*i*0.09929)))

                    if i*4 < 141 :
                        fenetre.blit(vignette_4_use,(680-(4*i*1.3510),247-(4*i*0.28014)))
                        fenetre.blit(vignette_3_use,(299-(4*i*0.35106),168+(4*i*0.28014)))
                    else:
                        fenetre.blit(vignette_3_use,(299-(4*i*0.35106),168+(4*i*0.28014)))
                        fenetre.blit(vignette_4_use,(680-(4*i*1.3510),247-(4*i*0.28014)))

                    if self.name != "menu_carroussel":
                        fenetre.blit(Menu,(1150,20))
                    if self.name == "menu_games":
                        fenetre.blit(Selection_menu,(455,0))
                        fenetre.blit(texte_jeux, (500, 20))
                        fenetre.blit(Autopilot_menu,(755,0))
                    fenetre.blit(Gauche_video2,(60,500))
                    fenetre.blit(Droite_video1,(1189,505))

                    if carr_title_bar_stat == "enable":
                        fenetre.blit(carr_title_bar,(0,606))
                        texte = font.render(carr_lang_translate[menu_carroussel.liste[menu_carroussel.selection]], 1, color_menu)
                        fenetre.blit(texte, (20, 650))
                        fenetre.blit(carr_level_sun,(1070, 630))

                        try :
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                                afficher_batons_carr(n,1150,630)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                                afficher_batons_carr(n,1150,630)
                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (1130, 650))

                        except:
                            texte = font.render("ERROR", 1, (255,0,0))
                            fenetre.blit(texte, (1130,650))

                        fenetre.blit(widget_soundtrack_reculer,(600,650))
                        fenetre.blit(widget_soundtrack_avancer,(780,650))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_pause,(690,650))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(690,650))

                        texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                        fenetre.blit(texte, (600,620))

                        fenetre.blit(audio_reader_proc.min,(490,613))

                    if jeux:
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(100,5))
                    else:
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        None

    class Tello_system:
        def __init__(self):
            self.connexion = False
            self.connected = False
            self.fly = False

            self.txt_menu = langue.tello_disconnected
            self.txt2_menu = ""
            self.thread = None

            self.battery = 0
            self.flight_time = 0
            self.roll = 0
            self.pitch = 0
            self.temperature = 0
            self.barometer = 0
            self.altitude = 0
            self.stat_check = ""
            self.wifi_signal = 0

            self.move_n = 20
            self.rotate_n = 2

            self.stat = langue.tello_ready
            self.stat_sec = 0

            self.color_check = (0,0,0)

            self.takeoff_security_lock = True

            self.img_rec = None
            self.img = None

            self.record_stat = False

            self.act = False

        def connect(self, stat):
            global tello
            global Tello_log

            try :
                self.txt2_menu = langue.tello_contact
                self.connexion = True
                tello.connect()

                self.connexion = False
                self.connected = True

                self.txt_menu = langue.tello_is_connected
                self.txt2_menu = langue.tello_connection_approved
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                Tello_log.write(f"{dt_string}   Connexion établie..."+"\n")
                Tello_log.write("\n")

            except:
                self.connexion = False
                self.txt_menu = langue.tello_not_connected
                self.txt2_menu = langue.tello_no_connection
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                Tello_log.write(f"{dt_string}   Echec de la connexion..."+"\n")
                Tello_log.write("\n")

                time.sleep(1)
                self.txt2_menu = ""

        def connect_process(self):
            global Tello_log
            
            now = datetime.datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            Tello_log.write(f"{dt_string}   Initialisation de la connexion..."+"\n")
            Tello_log.write("\n")
            
            self.thread = Thread(target=self.connect, args=(None,))
            self.thread.start()

        def safety_quit_check(self):
            global Tello_log
            if not(self.fly):
                return True
            else:
                return False

        def check_up(self):
            try:
                self.battery = tello.get_battery()
                self.altitude = tello.get_distance_tof()
                self.flight_time = tello.get_flight_time()
                self.roll = tello.get_roll()
                self.pitch = tello.get_pitch()
                self.temperature = tello.get_temperature()
                self.barometer = tello.get_barometer()

                if (self.altitude <= 10) and (self.battery >= 25) and (abs(self.pitch) <= 10) and (abs(self.roll) <= 10):
                    self.stat_check = langue.tello_ready_and_authorized_to_fly
                    self.color_check = (0,255,0)
                else:
                    self.stat_check = langue.tello_fly_not_recommended
                    self.color_check = (255,0,0)
            except:
                None

        def minimal_check_up(self, test):
            while Tello_control_flight_mode:
                try:
                    self.battery = tello.get_battery()
                    self.altitude = tello.get_distance_tof()
                    self.flight_time = tello.get_flight_time()
                    self.roll = tello.get_roll()
                    self.pitch = tello.get_pitch()

                    if (self.altitude <= 10) and (self.battery >= 25) and (abs(self.pitch) <= 10) and (abs(self.roll) <= 10):
                        self.stat = langue.tello_ready
                        self.stat_sec = 0
                    elif not(self.fly):
                        self.stat = langue.tello_danger
                        self.stat_sec = 1
                except:
                    None

        def takeoff_security(self, test):
            global Tello_log
            global tello

            now = datetime.datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            Tello_log.write(f"{dt_string}   Requête de décollage..."+"\n")
            Tello_log.write("\n")

            if not(self.takeoff_security_lock) and self.safety_quit_check() and self.stat_sec != 1 and not(self.fly) and not(self.act):
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                Tello_log.write(f"{dt_string}   Requête accordée..."+"\n")
                Tello_log.write("\n")
                
                self.act = True
                self.fly = True
                self.stat_txt = langue.tello_take_off
                try:
                    tello.takeoff()
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Décollage réussi..."+"\n")
                    Tello_log.write("\n")
                except:
                    self.fly = False
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Echec du décollage..."+"\n")
                    Tello_log.write("\n")

                self.act = False

                self.stat_txt = langue.tello_in_fly
                
            else:
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                Tello_log.write(f"{dt_string}   Requête refusée..."+"\n")
                Tello_log.write("\n")

        def land_protocol(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                Tello_log.write(f"{dt_string}   Tentative d'atterrissage..."+"\n")
                Tello_log.write("\n")
                
                self.act = True
                self.stat_txt = langue.tello_landing

                tello.land()
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Appareil au sol..."+"\n")
                Tello_log.write("\n")

                self.act = False
                self.fly = False
                self.takeoff_security_lock = True
                self.stat = langue.tello_ready
                self.stat_sec = 0

        def left(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.move_left(self.move_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Gauche : {self.move_n} cm"+"\n")
                Tello_log.write("\n")

        def right(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.move_right(self.move_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Droite : {self.move_n} cm"+"\n")
                Tello_log.write("\n")

        def forward(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.move_forward(self.move_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Avant : {self.move_n} cm"+"\n")
                Tello_log.write("\n")

        def back(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.move_back(self.move_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Arrière : {self.move_n} cm"+"\n")
                Tello_log.write("\n")

        def up(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.move_up(self.move_n)
                self.act = False
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Montée : {self.move_n} cm"+"\n")
                Tello_log.write("\n")

        def down(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.move_down(self.move_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Descente : {self.move_n} cm"+"\n")
                Tello_log.write("\n")

        def yaw_clock(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.rotate_clockwise(self.rotate_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Rotation horaire : {self.rotate_n}°"+"\n")
                Tello_log.write("\n")

        def yaw_counter_clock(self, test):
            global Tello_log
            global tello

            if self.fly and not(self.act):
                self.act = True
                tello.rotate_counter_clockwise(self.rotate_n)
                self.act = False

                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Rotation anti-horaire : {self.rotate_n}°"+"\n")
                Tello_log.write("\n")

        def get_img(self, test):
            global Tello_log
            global tello

            while Tello_control_flight_mode:

                temp = tello.get_frame_read()

                self.img_rec = temp.frame
                frame = cv2.cvtColor(self.img_rec, cv2.COLOR_BGR2RGB)
                frame = numpy.rot90(frame)
                frame = numpy.flipud(frame)

                frame = pygame.surfarray.make_surface(frame)

                self.img = frame

        def get_wifi(self,test):
            global Tello_log

            while Tello_control_flight_mode:

                temp = tello.query_wifi_signal_noise_ratio()
                try:
                    self.wifi_signal = int(temp)
                except:
                    None

                time.sleep(test)

        def take_picture(self, test):
            global Tello_log

            try:
                if not(os.path.isdir("Tello_picture")):
                    os.makedirs("Tello_picture")
                    cv2.imwrite("Tello_picture/Tello_pic0.png", self.img_rec)
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Photo enregistrée : Tello_picture/Tello_pic0.png"+"\n")
                    Tello_log.write("\n")
                elif os.listdir("Tello_picture/") == []:
                    cv2.imwrite("Tello_picture/Tello_pic0.png", self.img_rec)
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Photo enregistrée : Tello_picture/Tello_pic0.png"+"\n")
                    Tello_log.write("\n")
                else:
                    liste = os.listdir("Tello_picture/")

                    for elem in liste:
                        if "Tello_pic" not in elem:
                            liste.remove(elem)

                    last = liste[-1]
                    last = last.split("Tello_pic")
                    last = last[-1].split(".png")
                    last = int(last[0])+1

                    cv2.imwrite(f"Tello_picture/Tello_pic{last}.png", self.img_rec)
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Photo enregistrée : Tello_picture/Tello_pic{last}.png"+"\n")
                    Tello_log.write("\n")

            except Exception as e:
                print(e)
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                Tello_log.write(f"{dt_string}   Erreur lors de l'enregistrement de la photo..."+"\n")
                Tello_log.write("\n")

        def take_video(self, test):
            global Tello_log

            try:
                if not(os.path.isdir("Tello_video")):
                    os.makedirs("Tello_video")
                    height, width, _ = self.img_rec.shape
                    video = cv2.VideoWriter("Tello_video/Tello_vid0.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Enregistrement vidéo : Tello_video/Tello_vid0.mp4"+"\n")
                    Tello_log.write("\n")

                elif os.listdir("Tello_video/") == []:
                    height, width, _ = self.img_rec.shape
                    video = cv2.VideoWriter("Tello_video/Tello_vid0.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Enregistrement vidéo : Tello_video/Tello_vid0.mp4"+"\n")
                    Tello_log.write("\n")
                else:
                    liste = os.listdir("Tello_video/")

                    for elem in liste:
                        if "Tello_vid" not in elem:
                            liste.remove(elem)

                    last = liste[-1]
                    last = last.split("Tello_vid")
                    last = last[-1].split(".mp4")
                    last = int(last[0])+1

                    height, width, _ = self.img_rec.shape
                    video = cv2.VideoWriter(f"Tello_video/Tello_vid{last}.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

                    now = datetime.datetime.now()
                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                    Tello_log.write(f"{dt_string}   Enregistrement vidéo : Tello_video/Tello_vid{last}.mp4"+"\n")
                    Tello_log.write("\n")

                while self.record_stat:
                    video.write(self.img_rec)
                    time.sleep(1 / 30)

                video.release()

            except Exception as e:
                print(e)
                self.record_stat = False
                
                now = datetime.datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))                
                Tello_log.write(f"{dt_string}   Erreur lors de l'enregistrement de la vidéo..."+"\n")
                Tello_log.write("\n")

    # Définition du menu vidéos
    video_bonus_list = os.listdir("Videos")
    for i in range (len(video_bonus_list)):
        video_bonus_list[i] = video_bonus_list[i].replace(".mp4","")

    videos_carroussel = Carroussel(video_bonus_list, "Miniature/","videos_carroussel")

    # Définition du menu Carroussel
    menu_carroussel = Carroussel(["Accueil", "Videos", "Jauge", "Audio_player", "Jeux", "Parametres", "Credits", "Messages", "Outils", "Quitter"], "Images/Theme/"+theme_selected+"/Menu/Carroussel/","menu_carroussel")

    # Définition du menu jeux
    menu_games = Carroussel(["P4_R", "Memory_Cards", "P4_M", "Tetros", "WALL-E's_Jump", "T.A.N.K.S", "Minesweeper", "Vilallongue_chroni"],"Images/","menu_games")

    # Définition du dictionnaire "carr_lang_translate", utilisé par le menu principal Carroussel, et servant à afficher le nom des onglets dans la barre inférieure, en fonction de la langue sélectionnée.
    carr_lang_translate = {"Accueil" : langue.title_home, "Videos" : langue.title_videos, "Jauge" : langue.title_level, "Audio_player" : langue.title_audio_player, "Jeux" : langue.title_games, "Parametres" : langue.title_parameters, "Credits" : langue.title_credits, "Messages" : langue.title_intercomm, "Outils" : langue.title_tools, "Quitter" : langue.title_quit}

    """ Déclaration de l'objet "Music_player", permettant à la fois le contrôle de la bande son via l'onglet dédié, le widget (menu principal Titanium-Widgets) ou la barre inférieure (menu principal Carroussel) """
    class Music_player:
        def __init__(self, id, stat, playlist, defilement=False):
            self.id = id
            self.defilement = defilement
            if playlist != []:
                file = music_tag.load_file(playlist[self.id][0])
                self.music = pygame.mixer.music.load(playlist[self.id][0])
                self.time = int(float(str(file [ '#length' ])))
                if str(file['album']) != "":
                    self.album = str(file['album'])
                else:
                    self.album = "Album inconnu"

                if str(file["title"]) != "":
                    self.title = str(file["title"])
                    self.title_reader = self.title
                    self.title_widget = self.title
                    if len(self.title) > 35:
                        self.title = " "*35 + self.title + " "*35
                        self.title_widget = self.title[:35]
                        if not(self.defilement):
                            self.defilement = True
                            title_widget_defilement = Thread(target=self.defilement_txt,args=())
                            title_widget_defilement.start()
                    else:
                        self.defilement = False
                else:
                    album_title = playlist[self.id][0]
                    album_title = album_title.split("\\")
                    album_title = album_title[-1].split(".")
                    self.title = album_title[-2]
                    self.title_reader = self.title
                    self.title_widget = self.title
                    if len(self.title) > 35:
                        self.title = " "*35 + self.title + " "*35
                        self.title_widget = self.title[:35]
                        if not(self.defilement):
                            self.defilement = True
                            title_widget_defilement = Thread(target=self.defilement_txt,args=())
                            title_widget_defilement.start()
                    else:
                        self.defilement = False

            else:
                self.title = ""
                self.time = 1
                self.album = ""
                self.title = ""
                self.title_widget = ""
                self.title_reader = ""

            try:
                album_temp = music_tag.load_file(playlist[id][0])
                album_temp = io.BytesIO(album_temp['artwork'].first.data)
                self.min = pygame.transform.scale(pygame.image.load(album_temp).convert_alpha(), (100,100))
            except:
                self.min = audio_player_unknown_min
            self.stat = stat
            self.playlist = playlist

        def lecture(self):
            if self.stat:
                pygame.mixer.music.play()
            else:
                if self.playlist != []:
                    pygame.mixer.music.unpause()
        def pause(self):
            self.stat = False
            pygame.mixer.music.pause()
        def is_finish(self):
            if pygame.mixer.music.get_pos()//1000 == self.time:
                self.stat = False
                return True
        def avancer(self):
            if self.id < (len(self.playlist)-1):
                self.defilement = False
                self.__init__(self.id+1,True, self.playlist, self.defilement)
                audio_reader_proc.lecture()
            elif self.is_finish():
                self.defilement = False
                pygame.mixer.music.stop()
                self.__init__(0,True, self.playlist, self.defilement)

        def reculer(self):
            if self.id > 0 and (pygame.mixer.music.get_pos()//1000) <= 2:
                self.defilement = False
                self.__init__(self.id-1,True, self.playlist, self.defilement)
                audio_reader_proc.lecture()
            elif self.id == 0 or (pygame.mixer.music.get_pos()//1000) > 2 :
                self.defilement = False
                pygame.mixer.music.stop()
                pygame.mixer.music.play()

        def defilement_txt(self):
            i = 0
            e = 0
            while not(self.is_finish()) and self.defilement and continuer:
                self.title_widget = self.title[i:(35+i)]
                self.title_reader = self.title[e:(40+e)]
                time.sleep(0.3)
                if (35+i) == len(self.title):
                    i = 0
                else:
                    i+= 1

                if (40+e) == len(self.title):
                    e = 0
                else:
                    e+= 1
        
        def go_to_time(self, time_gived):
            pygame.mixer.music.set_pos(time_gived)   
            
    def albums_listing():
        global list_albums
        global liste_variables_albums
        global album_init_search
        
        list_albums = music_data.get(music_album_command)
        liste_variables_albums = []
    
        for i in range(len(list_albums)):
            try:
                album_temp = music_tag.load_file(list_albums[i][0])
                album_temp = io.BytesIO(album_temp['artwork'].first.data)
                album_temp = pygame.image.load(album_temp).convert_alpha()
            except:
                album_temp = audio_player_unknown
            globals() ["album"+ str(i)] = pygame.transform.scale(album_temp, (100,100))
    
        for i in range(len(list_albums)):
            liste_variables_albums.append(globals() ["album"+str(i)])
    
        album_init_search = False

    étape_programme = "Chargement des images/positions"

    """ Déclaration de l'objet "Wallpapers", chargeant les différentes images de fonds d'écran, en fonction du choix de l'utilisateur """
    class Wallpapers:
        def __init__(self, path, scale, blur_radius):
            self.path = path
            self.scale = scale

            self.wallpaper = pygame.image.load("Images/Wallpapers/"+str(path)+"/fondmenu.png").convert_alpha()
            self.wallpaper = pygame.transform.scale(self.wallpaper, scale)

            self.left = pygame.image.load("Images/Wallpapers/"+str(path)+"/Gauche.png").convert_alpha()
            self.left = pygame.transform.scale(self.left, (scale[0]/2,scale[1]))

            self.left_txt = pygame.image.load("Images/Wallpapers/"+str(path)+"/Gauche_txt.png").convert_alpha()
            self.left_txt = pygame.transform.scale(self.left_txt, (379,scale[1]))

            self.right = pygame.image.load("Images/Wallpapers/"+str(path)+"/Droite.png").convert_alpha()
            self.right = pygame.transform.scale(self.right, (scale[0]/2,scale[1]))

            self.blur_radius = blur_radius

            self.create_blur(blur_radius)

        def create_blur(self, blur_radius):

            self.blur_radius = blur_radius

            blur_temp = Image.open("Images/Wallpapers/"+str(self.path)+"/fondmenu.png").filter(ImageFilter.GaussianBlur(radius=self.blur_radius))
            blur_temp.putalpha(255)

            self.blur = pygame.image.fromstring(blur_temp.tobytes(), blur_temp.size, blur_temp.mode)
            
            #pygame.image.save(self.blur, "Test.png")

    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

    # Chargement des images du lecteur multimédia
    Son = pygame.image.load("Miniature/Soundtrack.png").convert_alpha()
    Lecture = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Lecture.png").convert_alpha()
    Pause = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Pause.png").convert_alpha()
    Avancer = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Avancer.png").convert_alpha()
    Reculer = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Reculer.png").convert_alpha()
    Lecture1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Lecture1.png").convert_alpha()
    Pause1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Pause1.png").convert_alpha()
    Avancer1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Avancer1.png").convert_alpha()
    Reculer1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Reculer1.png").convert_alpha()

    Menu1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Menu.png").convert_alpha()
    Menu11 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Menu1.png").convert_alpha()

    # Chargement des miniatures de langues (langues intégrées par défaut)
    french_lang = pygame.image.load("Images/french.png").convert_alpha()
    english_lang = pygame.image.load("Images/english.png").convert_alpha()
    spanish_lang = pygame.image.load("Images/spanish.png").convert_alpha()

    # Chargement des images du contrôle de volume (soundtrack et paramètres)
    sound_up = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/volume_up.png").convert_alpha()
    sound_down = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/volume_down.png").convert_alpha()
    sound_up1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/volume_up1.png").convert_alpha()
    sound_down1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/volume_down1.png").convert_alpha()

    sound_viewer = pygame.image.load("Images/volume_viewer.png").convert_alpha()
    sound_viewer_general = pygame.image.load("Images/volume_viewer_general.png").convert_alpha()

    pos_sound_up_audio_player = sound_up.get_rect(topleft=(360,610))
    pos_sound_down_audio_player = sound_down.get_rect(topleft=(60,610))

    # Chargement des images du menu changelog
    changelog_logo = pygame.image.load("Images/BNL_changelog_logo.png")

    # Video

    MP4_icon = pygame.image.load("Images/mp4_original.png")
    MP4_icon2 = pygame.image.load("Images/mp4_2original.png")
    pos_MP4 = MP4_icon.get_rect(topleft=(120,500))

    MOV_icon = pygame.image.load("Images/mov_original.png")
    MOV_icon2 = pygame.image.load("Images/mov_2original.png")
    pos_MOV = MP4_icon.get_rect(topleft=(220,500))

    MKV_icon = pygame.image.load("Images/mkv_original.png")
    MKV_icon2 = pygame.image.load("Images/mkv_2original.png")
    pos_MKV = MP4_icon.get_rect(topleft=(320,500))

    WEBM_icon = pygame.image.load("Images/webm_original.png")
    WEBM_icon2 = pygame.image.load("Images/webm_2original.png")
    pos_WEBM = MP4_icon.get_rect(topleft=(520,500))

    FLV_icon = pygame.image.load("Images/flv_original.png")
    FLV_icon2 = pygame.image.load("Images/flv_2original.png")
    pos_FLV = MP4_icon.get_rect(topleft=(420,500))

    AVI_icon = pygame.image.load("Images/avi_original.png")
    AVI_icon2 = pygame.image.load("Images/avi_2original.png")
    pos_AVI = MP4_icon.get_rect(topleft=(620,500))

    # Audio

    MP3_icon = pygame.image.load("Images/mp3_original.png")
    MP3_icon2 = pygame.image.load("Images/mp3_2original.png")
    pos_MP3 = MP4_icon.get_rect(topleft=(120,550))

    M4A_icon = pygame.image.load("Images/m4a_original.png")
    M4A_icon2 = pygame.image.load("Images/m4a_2original.png")
    pos_M4A = MP4_icon.get_rect(topleft=(220,550))

    WAV_icon = pygame.image.load("Images/wav_original.png")
    WAV_icon2 = pygame.image.load("Images/wav_2original.png")
    pos_WAV = MP4_icon.get_rect(topleft=(320,550))

    OPUS_icon = pygame.image.load("Images/opus_original.png")
    OPUS_icon2 = pygame.image.load("Images/opus_2original.png")
    pos_OPUS = MP3_icon.get_rect(topleft=(520,550))

    FLAC_icon = pygame.image.load("Images/flac_original.png")
    FLAC_icon2 = pygame.image.load("Images/flac_2original.png")
    pos_FLAC = MP4_icon.get_rect(topleft=(420,550))

    OGG_icon = pygame.image.load("Images/ogg_original.png")
    OGG_icon2 = pygame.image.load("Images/ogg_2original.png")
    pos_OGG = MP4_icon.get_rect(topleft=(620,550))

    # Bitrate

    i64kbps_icon = pygame.image.load("Images/64kbps_original.png")
    i64kbps_icon2 = pygame.image.load("Images/64kbps_2original.png")
    pos_64kbps = MP4_icon.get_rect(topleft=(820,500))

    i128kbps_icon = pygame.image.load("Images/128kbps_original.png")
    i128kbps_icon2 = pygame.image.load("Images/128kbps_2original.png")
    pos_128kbps = MP3_icon.get_rect(topleft=(920,500))

    i192kbps_icon = pygame.image.load("Images/192kbps_original.png")
    i192kbps_icon2 = pygame.image.load("Images/192kbps_2original.png")
    pos_192kbps = MP4_icon.get_rect(topleft=(820,550))

    i320kbps_icon = pygame.image.load("Images/320kbps_original.png")
    i320kbps_icon2 = pygame.image.load("Images/320kbps_2original.png")
    pos_320kbps = MP4_icon.get_rect(topleft=(920,550))

    transfer_min = pygame.image.load("Images/transfer.png")
    transfer_min1 = pygame.image.load("Images/transfer1.png")
    pos_transfer_min = transfer_min.get_rect(topleft=(1240,650))

    # Chargement des images de l'onglet BNL's Drone Control (dont miniature du sélecteur)

    tello_icon_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Tello.png").convert_alpha()
    tello_icon = pygame.image.load("Images/Tello_icon.png")
    pos_tello_icon = tello_icon.get_rect(topleft=(80,275))

    tello_connexion = pygame.image.load("Images/Tello_connexion.png")
    pos_tello_connexion = tello_connexion.get_rect(topleft=(455,500))

    tello_check = pygame.image.load("Images/Tello_check.png")
    pos_tello_check = tello_check.get_rect(topleft=(500,500))

    tello_battery_min = pygame.image.load("Images/Tello_battery.png")
    tello_wifi_min = pygame.image.load("Images/Tello_wifi.png")
    tello_move_min = pygame.image.load("Images/Tello_move.png")
    tello_rotate_min = pygame.image.load("Images/Tello_rotate.png")

    tello_lock = pygame.image.load("Images/Tello_lock.png")
    tello_unlock = pygame.image.load("Images/Tello_unlock.png")
    pos_tello_lock = tello_lock.get_rect(topleft=(1100,610))

    tello_picture = pygame.image.load("Images/Tello_picture.png")
    pos_tello_picture = tello_picture.get_rect(topleft=(950,610))

    tello_rec = pygame.image.load("Images/Tello_rec.png")
    tello_rec_run = pygame.image.load("Images/Tello_rec_run.png")
    pos_tello_rec = tello_rec.get_rect(topleft=(800,610))

    # Chargement des miniatures de fonds d'écran intégrés (Paramètres -> Personnalisation)
    fondmenu0_a = pygame.image.load("Miniature/fondmenu.png").convert_alpha()
    fondmenu1_a = pygame.image.load("Miniature/fondmenu1.png").convert_alpha()
    fondmenu2_a = pygame.image.load("Miniature/fondmenu2.png").convert_alpha()
    fondmenu3_a = pygame.image.load("Miniature/fondmenu3.png").convert_alpha()
    fondmenu4_a = pygame.image.load("Miniature/fondmenu4.png").convert_alpha()
    fondmenu5_a = pygame.image.load("Miniature/fondmenu5.png").convert_alpha()
    fondmenu6_a = pygame.image.load("Miniature/fondmenu6.png").convert_alpha()
    fondmenu7_a = pygame.image.load("Miniature/fondmenu7.png").convert_alpha()
    fondmenu8_a = pygame.image.load("Miniature/fondmenu8.png").convert_alpha()

    # Chargement des témoins de découpage (découpage automatique des fonds d'écran)
    create_pic_left_txt = pygame.image.load("Images/create_pic_left_txt.png")
    create_pic_left = pygame.image.load("Images/create_pic_left.png")
    create_pic_right = pygame.image.load("Images/create_pic_right.png")
    create_pic_mini = pygame.image.load("Images/create_pic_mini.png")

    # Chargement des miniatures des skins (Paramètres -> Personnalisation)
    titanium_widgets_BNL = pygame.image.load("Miniature/titanium_widgets_BNL.png").convert_alpha()
    old_style = pygame.image.load("Miniature/old_style.png").convert_alpha()
    carroussel_skin = pygame.image.load("Miniature/Carroussel.png").convert_alpha()

    # Chargement des miniatures des themes intégrés (Paramètres -> Personnalisation)
    MINI_Picture_original = pygame.image.load("Images/Theme/MINI_Picture_original/Theme_view.png")
    MINI_Picture_original_black_theme = pygame.image.load("Images/Theme/MINI_Picture_original_black_theme/Theme_view.png")
    MINI_Picture_original_alpha_theme = pygame.image.load("Images/Theme/MINI_Picture_original_alpha_theme/Theme_view.png")

    # Chargement des miniatures des polices intégrés (Paramètres -> Personnalisation)
    Overpass = pygame.image.load("Fonts/font0/font_view.png")
    DynaPuff = pygame.image.load("Fonts/font1/font_view.png")
    SourceSansPro = pygame.image.load("Fonts/font2/font_view.png")
    Great_Vibes = pygame.image.load("Fonts/font3/font_view.png")

    # Chargement des témoins couleurs intégrés (Paramètres -> Personnalisation)
    Rouge = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Rouge.png").convert_alpha()
    Bleu = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Bleu.png").convert_alpha()
    Violet = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Violet.png").convert_alpha()
    Vert = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Vert.png").convert_alpha()
    Jaune = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Jaune.png").convert_alpha()
    Cyan = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Cyan.png").convert_alpha()
    
    Color_wheel = pygame.image.load("Images/Color_wheel.png").convert_alpha()
    color_check_box = pygame.image.load("Images/yt_dlp_check_box.png")
    color_check_box1 = pygame.image.load("Images/yt_dlp_check_box1.png")
    
    color_white = pygame.image.load("Images/white_color.png")
    color_black = pygame.image.load("Images/black_color.png")
            
    pos_color_text = color_check_box.get_rect(topleft=(350,185))
    pos_color_aux = color_check_box.get_rect(topleft=(350,285))
    pos_color_menu = color_check_box.get_rect(topleft=(350,385))

    pos_color_white = color_black.get_rect(topleft=(1200,500))
    pos_color_black = color_black.get_rect(topleft=(1200,600))

    # Chargement des images relatives aux sous-menus du menu paramètres (plus de couleurs, plus de thèmes, plus de polices, etc.)

    more_colors = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
    more_themes = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
    more_fonts = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
    more_wallpapers = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
    new_wallpapers = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()

    pos_new_wallpapers = new_wallpapers.get_rect(topleft=(1150,150))

    # Chargement des images de BNL's Intercomm

    server_pic = pygame.image.load("Images/server.png").convert_alpha()
    client_pic = pygame.image.load("Images/client.png").convert_alpha()
    
    intercomm_last_ip = pygame.image.load("Images/Intercomm_last_ip.png").convert_alpha()
    pos_intercomm_last_ip = intercomm_last_ip.get_rect(topleft=(530,450))

    # Chargement du curseur de défilement de la page
    scroll_bar = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/scroll_bar.png").convert_alpha()

    class Scroll:
        def __init__(self, coor, val, stat):
            self.id = id
            self.coor = coor
            self.pos = scroll_bar.get_rect(topleft=self.coor)
            self.val = val

    class Submenu:
        def __init__(self, img, coor, txt, stat):
            self.img = pygame.image.load(img).convert_alpha()
            self.coor = coor
            self.txt = font_widget.render(txt, 1, (color_txt))
            self.stat = stat
            self.coor_txt = [coor[0]+5, coor[1]+5]
            self.pos = self.img.get_rect(topleft=self.coor)
            self.selection = ""

        def set_pos(self, coor):
            self.coor = coor
            self.coor_txt = [coor[0]+10, coor[1]+10]
            self.pos = self.img.get_rect(topleft=self.coor)

    # Chargement des sélecteurs du menu principal et du lecteur multimédia
    Selection_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Selection_menu.png").convert_alpha()
    Selection_soundtrack = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Selection_soundtrack.png").convert_alpha()

    # Chargement des boutons d'actions (BNL's Web Service, BNL's Intercomm, pop-up, etc.)
    bouton_Python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_bouton.png").convert_alpha()
    bouton_C = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/C#_bouton.png").convert_alpha()
    bouton_Abord = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Annuler_bouton.png").convert_alpha()
    bouton_OK = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Bouton_OK.png").convert_alpha()

    bouton_connexion = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/bouton_connexion.png").convert_alpha()
    pos_bouton_connexion = bouton_connexion.get_rect(topleft=(590,650))

    # Chargements des images du témoin de téléchargement (mise à jour, recherche de mises à jour, etc.)
    download_stat_tem = pygame.image.load("Images/Download_stat_tem.png").convert_alpha()
    download_stat_downloading = pygame.image.load("Images/Download_stat_downloading1.png").convert_alpha()
    download_stat_animation1 = pygame.image.load("Images/Download_stat_downloading1.png").convert_alpha()
    download_stat_animation2 = pygame.image.load("Images/Download_stat_downloading2.png").convert_alpha()
    download_stat_animation3 = pygame.image.load("Images/Download_stat_downloading3.png").convert_alpha()
    download_stat_animation4 = pygame.image.load("Images/Download_stat_downloading4.png").convert_alpha()
    download_stat_animation5 = pygame.image.load("Images/Download_stat_downloading5.png").convert_alpha()
    download_stat_animation6 = pygame.image.load("Images/Download_stat_downloading6.png").convert_alpha()

    liste_donwload_animation = [download_stat_animation1,download_stat_animation2,download_stat_animation3,download_stat_animation4,download_stat_animation5,download_stat_animation6,download_stat_animation1]

    # Chargement des images des boutons du menu paramètres (rechercher les mises à jour, update, update all, delete all, etc.)
    bouton_search_update = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Search_update.png").convert_alpha()

    bouton_update_python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_update.png").convert_alpha()
    bouton_update_all_python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_update_all.png").convert_alpha()
    bouton_delete_all_python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_delete_all.png").convert_alpha()

    pos_bouton_search_update = bouton_search_update.get_rect(topleft=(250,502))

    # Chargement du témoin de sélection (Paramètres -> Personnalisation)
    Selection = pygame.image.load("Images/BNL1.png").convert_alpha()

    # Chargement des icônes du menu principal Titanium-Widgets
    BNLmenu= pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Parametres.png").convert_alpha()
    DVD = pygame.image.load("Images/DVD.png").convert_alpha()
    Soundtrack = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Soundtrack.png").convert_alpha()
    Soundtrack_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Soundtrack_menu.png").convert_alpha()
    Autopilot_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Autopilot.png").convert_alpha()
    MO_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/M-O.png").convert_alpha()
    Lounge_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Lounge.png").convert_alpha()
    Intercomm_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Message.png").convert_alpha()
    Solar = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Solar.png").convert_alpha()
    Bonus = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Bonus.png").convert_alpha()
    Autre = pygame.image.load("Images/Autre.png").convert_alpha()
    tools_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Outils.png").convert_alpha()
    Color_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Color_wheel.png").convert_alpha()

    # Chargement de l'icône de retour au menu principal
    Menu = pygame.image.load("Images/BNLalpha.png").convert_alpha()

    # Chargement du fond du menu Bonus (legacy : accessible en paramètrant l'ancien menu)
    fondbonus = pygame.image.load("Bonus/Bonus88.png").convert_alpha()

    # Obsolète : relique du cycle 2.0 (antérieur au menu paramètres à tuiles)
    Version = pygame.image.load("Miniature/Version.png").convert_alpha()

    # Chargement du curseur du lecteur multimédia
    Curseur = pygame.image.load("Images/Statut.png").convert_alpha()

    # Chargement des tuiles du menu Paramètres
    Infos= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Infos.png").convert_alpha()
    Infos1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Infos1.png").convert_alpha()
    Modules= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Modules.png").convert_alpha()
    Modules1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Modules1.png").convert_alpha()
    Animations= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Animations.png").convert_alpha()
    Animations1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Animations1.png").convert_alpha()
    touche_vide= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/touche_vide.png").convert_alpha()
    Fond_paramètres= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Fond_parametres.png").convert_alpha()
    Fond_paramètres1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Fond_parametres1.png").convert_alpha()

    # Chargement des images du menu "A propos"
    Credits_history_picture = pygame.image.load("Images/Credits_history_picture.png").convert_alpha()
    Credits_changelog_picture = pygame.image.load("Images/Credits_changelog_picture.png").convert_alpha()
    Credits_help_picture = pygame.image.load("Images/Credits_help_picture.png").convert_alpha()
    Credits_about_picture = pygame.image.load("Images/Credits_about_picture.png").convert_alpha()

    Credits_history_picture_min = pygame.image.load("Images/Credits_history_picture_min.png").convert_alpha()
    Credits_changelog_picture_min = pygame.image.load("Images/Credits_changelog_picture_min.png").convert_alpha()
    Credits_help_picture_min = pygame.image.load("Images/Credits_help_picture_min.png").convert_alpha()
    Credits_about_picture_min = pygame.image.load("Images/Credits_about_picture_min.png").convert_alpha()

    Credits_logo = pygame.image.load("Images/Credits_logo.png").convert_alpha()

    Credits_history_Level_1x = pygame.image.load("Images/credits_history_level_1x.png").convert_alpha()

    Credits_history_Level_2x = pygame.image.load("Images/credits_history_level_2x.png").convert_alpha()
    Credits_history_Level_2x1 = pygame.image.load("Images/credits_history_level_2x1.png").convert_alpha()
    Credits_history_Level_2x2 = pygame.image.load("Images/credits_history_level_2x2.png").convert_alpha()

    Credits_history_BNLBox_3x = pygame.image.load("Images/credits_history_level_3x.png").convert_alpha()
    Credits_history_BNLBox_3x1 = pygame.image.load("Images/credits_history_level_3x1.png").convert_alpha()
    Credits_history_BNLBox_3x2 = pygame.image.load("Images/credits_history_level_3x2.png").convert_alpha()

    Credits_history_BNLBox_4x = pygame.image.load("Images/credits_history_level_4x.png").convert_alpha()
    Credits_history_BNLBox_4x1 = pygame.image.load("Images/credits_history_level_4x1.png").convert_alpha()
    Credits_history_BNLBox_4x2 = pygame.image.load("Images/credits_history_level_4x2.png").convert_alpha()

    pos_Credits_history_picture = Credits_history_picture.get_rect(topleft=(100,200))
    pos_Credits_changelog_picture = Credits_changelog_picture.get_rect(topleft=(400,200))
    pos_Credits_help_picture = Credits_help_picture.get_rect(topleft=(700,200))
    pos_Credits_about_picture = Credits_about_picture.get_rect(topleft=(1000,200))

    # Chargement du fond de visibilité (selon thèmes)
    fond_visibilité = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/fond_visibilite.png").convert_alpha()

    # Chargement du fond noir (universel)
    fondmulti= pygame.image.load("Images/fondmulti.png").convert_alpha()

    # Chargement des boutons ON/OFF du menu Paramètres
    ON_OFF_maker= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/ON_OFF_maker.png").convert_alpha()
    ON = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/ON.png").convert_alpha()
    OFF = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/OFF.png").convert_alpha()

    pos_ON_OFF_update = ON_OFF_maker.get_rect(topleft=(850,600))
    pos_ON_OFF_update_web = ON_OFF_maker.get_rect(topleft=(850,650))

    pos_ON_OFF_intercomm = ON_OFF_maker.get_rect(topleft=(460,150))
    pos_ON_OFF_compatibility_enforced = ON_OFF_maker.get_rect(topleft=(460,500))

    UP_button = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/up.png").convert_alpha()
    UP_button1 = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/up1.png").convert_alpha()
    DOWN_button = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/down.png").convert_alpha()
    DOWN_button1 = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/down1.png").convert_alpha()
    
    # Chargement des images de l'onglet yt_dlp (dont miniature du sélecteur)
    yt_dlp_icon_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/yt_dlp.png").convert_alpha()
    yt_dlp_icon = pygame.image.load("Images/yt_dlp_icon.png")
    pos_yt_dlp_icon = yt_dlp_icon.get_rect(topleft=(880,275))

    yt_dlp_download = pygame.image.load("Images/yt_dlp_download_icon.png")
    yt_dlp_download2 = pygame.image.load("Images/yt_dlp_download_icon2.png")
    pos_yt_dlp_download = yt_dlp_download.get_rect(topleft=(20,500))

    yt_dlp_playlist_button = pygame.image.load("Images/yt_dlp_playlist_list.png")
    pos_playlist_selection = yt_dlp_playlist_button.get_rect(topleft=(20,300))

    yt_dlp_check_box = pygame.image.load("Images/yt_dlp_check_box.png")
    yt_dlp_check_box1 = pygame.image.load("Images/yt_dlp_check_box1.png")
    
    yt_dlp_settings = pygame.image.load("Images/yt_dlp_settings.png")
    pos_yt_dlp_settings = yt_dlp_settings.get_rect(topleft=(1175,120))
    
    pos_ON_OFF_yt_dlp_set_album = ON_OFF_maker.get_rect(topleft=(850,167))
    pos_ON_OFF_yt_dlp_set_title = ON_OFF_maker.get_rect(topleft=(850,217))
    pos_ON_OFF_yt_dlp_set_artist = ON_OFF_maker.get_rect(topleft=(850,267))

    # Chargement des images du menu jeux

    score_reset = pygame.image.load("Images/Theme/"+theme_selected+"/Autre/score_reset.png").convert_alpha()
    score_reset1 = pygame.image.load("Images/Theme/"+theme_selected+"/Autre/score_reset1.png").convert_alpha()
    card_reset = pygame.image.load("Images/Theme/"+theme_selected+"/Autre/card_reset.png").convert_alpha()
    card_reset1 = pygame.image.load("Images/Theme/"+theme_selected+"/Autre/card_reset1.png").convert_alpha()
    pos_score_card_reset = score_reset.get_rect(topleft=(1100,500))
    pos_card_reset = card_reset.get_rect(topleft=(1100,600))

    Gauche_fp = pygame.image.load("Games/Mini Picture Original/Cartes/Gauche1.png")
    Gauche_f = pygame.image.load("Games/Mini Picture Original/Cartes/Gauche2.png")
    Droite_fp = pygame.image.load("Games/Mini Picture Original/Cartes/Droite1.png")
    Droite_f = pygame.image.load("Games/Mini Picture Original/Cartes/Droite2.png")

    Gauche_video1 = pygame.image.load("Images/Gauche1_video.png")
    Gauche_video2 = pygame.image.load("Images/Gauche2_video.png")
    Droite_video1 = pygame.image.load("Images/Droite1_video.png")
    Droite_video2 = pygame.image.load("Images/Droite2_video.png")

    pos_Gauche_video = Gauche_video2.get_rect(topleft=(60,500))
    pos_Droite_video = Droite_video2.get_rect(topleft=(1189,500))

    Puissance4_logo = pygame.image.load("Images/Puissance4logo.png").convert_alpha()
    Puissance4_logo_Maxime = pygame.image.load("Images/Fond_puissance.png").convert_alpha()
    MPOriginal = pygame.image.load("Images/Mini Picture Original.png").convert_alpha()
    Tetris_logo = pygame.image.load("Images/Tetris_logo.png").convert_alpha()
    Jump_logo = pygame.image.load("Images/Jump_logo.png").convert_alpha()

    """Chargement des widgets"""
    # Soundtrack
    widget_soundtrack_skin = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Soundtrack Widget.png")
    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

    widget_soundtrack_miniature = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Soundtrack Widget Miniature.png")
    pos_widget_soundtrack_miniature = widget_soundtrack_miniature.get_rect(topleft=(1190,50))

    widget_soundtrack_lecture = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Lecture_widget.png")
    widget_soundtrack_pause = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Pause_widget.png")
    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
    widget_soundtrack_reculer = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Reculer_widget.png")
    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
    widget_soundtrack_avancer = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Avancer_widget.png")
    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))

    #Jauge
    widget_level_miniature = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Level Widget Miniature.png")
    pos_widget_level_miniature = widget_level_miniature.get_rect(topleft=(1190,130))

    widget_level_skin = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Level Widget.png")
    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

    #Barre de stockage

    widget_barre = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Widgets_barre.png")

    widget_signet_open = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Signet_open.png")
    pos_widget_signet_open = widget_signet_open.get_rect(topleft=(1152,500))

    widget_signet_close = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Signet_close.png")
    pos_widget_signet_close = widget_signet_close.get_rect(topleft=(1251,500))

    # Chargement des images de la barre inférieure du menu principal Carroussel

    carr_title_bar = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Carroussel/title_bar.png")
    carr_level_sun = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Carroussel/solarcharge.png")

    pos_carr_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(690,650))
    pos_carr_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(600,650))
    pos_carr_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(780,650))

    # Chargement des images de l'onglet Lecteur Audio (dont miniature du sélecteur)
    audio_player_icon_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Audio_player.png").convert_alpha()
    audio_player_icon = pygame.image.load("Images/Audio_player_icon.png")

    audio_player_update_button_menu = pygame.image.load("Images/Audio_player_update_menu.png")
    pos_audio_player_update_menu_button = audio_player_update_button_menu.get_rect(topleft=(1000,600))

    audio_player_dir_button = pygame.image.load("Images/Audio_player_dir.png")
    audio_player_dir_button1 = pygame.image.load("Images/Audio_player_dir1.png")
    pos_audio_player_update_button = audio_player_dir_button.get_rect(topleft=(1100,650))

    audio_player_dir_add_button = pygame.image.load("Images/Audio_player_dir_add.png")
    pos_audio_player_add_button = audio_player_dir_add_button.get_rect(topleft=(1200,650))

    audio_player_album = pygame.image.load("Images/Album.png")
    audio_player_album_min = pygame.image.load("Images/Album_min.png")
    pos_audio_player_album = audio_player_album.get_rect(topleft=(50,200))

    audio_player_artist = pygame.image.load("Images/Artist.png")
    audio_player_artist_min = pygame.image.load("Images/Artist_min.png")
    pos_audio_player_artist = audio_player_artist.get_rect(topleft=(300,200))

    audio_player_genre = pygame.image.load("Images/Genre.png")
    audio_player_genre_min = pygame.image.load("Images/Genre_min.png")
    pos_audio_player_genre = audio_player_genre.get_rect(topleft=(550,200))

    audio_player_soundtrack = pygame.image.load("Images/Soundtrack.png")
    pos_audio_player_soundtrack = audio_player_soundtrack.get_rect(topleft=(1000,200))

    audio_player_unknown = pygame.image.load("Images/Album_unknown.png")
    audio_player_unknown_min = pygame.transform.scale(audio_player_unknown, (100,100))

    pos_audio_reculer = widget_soundtrack_reculer.get_rect(topleft=(700,550))
    pos_audio_play = widget_soundtrack_pause.get_rect(topleft=(800,550))
    pos_audio_avancer = widget_soundtrack_avancer.get_rect(topleft=(900,550))

    audio_player_reader_icon = pygame.image.load("Images/Audio_reader.png")
    pos_audio_player_reader_icon = audio_player_reader_icon.get_rect(topleft=(1000,20))

    audio_player_menu_icon = pygame.image.load("Images/Audio_player_menu.png")
    pos_audio_player_menu_icon = audio_player_menu_icon.get_rect(topleft=(900,20))

    audio_reader_proc = Music_player(0,False,[])

    # Chargement des images du jeu "WALL-E's Memory" Mini Picture Original + variables + positions

    cartes_logo = pygame.image.load("Games/Mini Picture Original/Cartes/carte logo.png").convert_alpha()

    carte_dos = pygame.image.load("Games/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()

    sélection_carte1 = 0
    sélection_carte2 = 0

    liste_cartes = ["Games/Mini Picture Original/Cartes/AUTO carte.png","Games/Mini Picture Original/Cartes/Axiom carte.png", "Games/Mini Picture Original/Cartes/Eve carte.png","Games/Mini Picture Original/Cartes/Journal carte.png",
    "Games/Mini Picture Original/Cartes/MO carte.png","Games/Mini Picture Original/Cartes/Poster carte.png","Games/Mini Picture Original/Cartes/Space carte.png","Games/Mini Picture Original/Cartes/WALL E2 carte.png",
    "Games/Mini Picture Original/Cartes/Shelby Forthright carte.png"]

    liste_cartes2 = random.sample(liste_cartes,9)

    liste_pos = [(100,50),(260,50),(420,50),(580,50),(740,50),(900,50),(100,260),(260,260),(420,260),(580,260),(740,260),(900,260),(100,470),(260,470),(420,470),(580,470),(740,470),(900,470)]

    liste_pos2 = random.sample(liste_pos,18)

    """ Déclaration de l'objet "Card_WMG", alloué au jeu WALL-E's Memory """
    class Cards_WMG:
        def __init__(self, img, coor, stat, id):
            self.coor = coor
            self.stat = stat
            self.img = pygame.image.load(img).convert_alpha()
            self.pos = self.img.get_rect(topleft=(self.coor))
            self.id = id
            self.img_def = img

        def check_stat(self):
            if self.stat == 1 or self.stat == 2:
                self.img = pygame.image.load(self.img_def).convert_alpha()
            else:
                self.img = pygame.image.load("Games/Mini Picture Original/Cartes/Carte dos.png").convert_alpha()

    carte1 = Cards_WMG(liste_cartes2[0],liste_pos2[0],0,1)
    carte2 = Cards_WMG(liste_cartes2[1],liste_pos2[1],0,2)
    carte3 = Cards_WMG(liste_cartes2[2],liste_pos2[2],0,3)
    carte4 = Cards_WMG(liste_cartes2[3],liste_pos2[3],0,4)
    carte5 = Cards_WMG(liste_cartes2[4],liste_pos2[4],0,5)
    carte6 = Cards_WMG(liste_cartes2[5],liste_pos2[5],0,6)
    carte7 = Cards_WMG(liste_cartes2[6],liste_pos2[6],0,7)
    carte8 = Cards_WMG(liste_cartes2[7],liste_pos2[7],0,8)
    carte9 = Cards_WMG(liste_cartes2[8],liste_pos2[8],0,9)
    carte1_bis = Cards_WMG(liste_cartes2[0],liste_pos2[9],0,1)
    carte2_bis = Cards_WMG(liste_cartes2[1],liste_pos2[10],0,2)
    carte3_bis = Cards_WMG(liste_cartes2[2],liste_pos2[11],0,3)
    carte4_bis = Cards_WMG(liste_cartes2[3],liste_pos2[12],0,4)
    carte5_bis = Cards_WMG(liste_cartes2[4],liste_pos2[13],0,5)
    carte6_bis = Cards_WMG(liste_cartes2[5],liste_pos2[14],0,6)
    carte7_bis = Cards_WMG(liste_cartes2[6],liste_pos2[15],0,7)
    carte8_bis = Cards_WMG(liste_cartes2[7],liste_pos2[16],0,8)
    carte9_bis = Cards_WMG(liste_cartes2[8],liste_pos2[17],0,9)

    class Minesweeper_class:
        def __init__(self, id, size, mine_prop, img_base, img_mine, img_reveal, img_flag, img_size, coor):
            self.id = id
            self.grille = []
            self.size = size
            self.nb_mine = int((1/mine_prop)*(size[0]*size[1]))
            self.img_base = pygame.image.load(img_base).convert_alpha()
            self.img_base = pygame.transform.scale(self.img_base, img_size)

            self.img_mine = pygame.image.load(img_mine).convert_alpha()
            self.img_mine = pygame.transform.scale(self.img_mine, img_size)

            self.img_reveal = pygame.image.load(img_reveal).convert_alpha()
            self.img_reveal = pygame.transform.scale(self.img_reveal, img_size)

            self.img_flag = pygame.image.load(img_flag).convert_alpha()
            self.img_flag = pygame.transform.scale(self.img_flag, img_size)

            self.coor = coor
            self.liste_pos = []
            self.pas = img_size[0]

            self.grille_voisins = []
            self.stat = "game"
            self.count = 0 

        def create_grille(self):
            for i in range(self.size[1]):
                self.grille.append([0]*self.size[0])
                self.grille_voisins.append([0]*self.size[0])

            for i in range(self.nb_mine):
                coor_temp = ((random.randint(0,self.size[1]-1),(random.randint(0,self.size[0]-1))))
                while self.grille[coor_temp[0]][coor_temp[1]] == 1:
                    coor_temp = ((random.randint(0,self.size[1]-1),(random.randint(0,self.size[0]-1))))
                self.grille[coor_temp[0]][coor_temp[1]] = 1

            self.check_voisins()

        def draw_grille(self):
            global Minesweeper_init
            for i in range(self.size[1]):
                for j in range(self.size[0]):
                    if self.grille[i][j] == 0 or self.grille[i][j] == 1:
                        fenetre.blit(self.img_base, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                    elif self.grille[i][j] == 2:
                        fenetre.blit(self.img_reveal, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                        texte = font_widget.render(str(self.grille_voisins[i][j]), 5, (255,255,255))
                        fenetre.blit(texte, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                    elif self.grille[i][j] == 3:
                        fenetre.blit(self.img_mine, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                    elif self.grille[i][j] == 4 or self.grille[i][j] == 5:
                        fenetre.blit(self.img_flag, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))

            if self.count == (self.size[0]*self.size[1]-self.nb_mine):
                pop_up()
                texte = font_big.render(langue.game_c_win, 5, (color_txt))
                fenetre.blit(texte, (550, 250))
                pygame.display.flip()
                time.sleep(3)
                Minesweeper_init = True

            for elem in self.grille:
                if 3 in elem:
                    self.stat = "lose"
                    for i in range(self.size[1]):
                        for j in range(self.size[0]):
                            if self.grille[i][j] == 0:
                                fenetre.blit(self.img_base, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                            elif self.grille[i][j] == 2:
                                fenetre.blit(self.img_reveal, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                                texte = font_widget.render(str(self.grille_voisins[i][j]), 5, (255,255,255))
                                fenetre.blit(texte, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                            elif self.grille[i][j] == 1 or self.grille[i][j] == 5:
                                fenetre.blit(self.img_mine, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                            elif self.grille[i][j] == 4:
                                fenetre.blit(self.img_flag, (j*self.pas+self.coor[0], i*self.pas+self.coor[1]))
                    break

        def check_voisins(self):
            for i in range(len(self.grille)):
                for j in range(len(self.grille[0])):
                    if self.grille[i][j] != 1 and self.grille[i][j] != 3:
                        if i == 0:
                            if j > 0:
                                if self.grille[i][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i+1][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                            if j < self.size[0]-1:
                                if self.grille[i][j+1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i+1][j+1] == 1:
                                    self.grille_voisins[i][j] += 1

                            if self.grille[i+1][j] == 1:
                                self.grille_voisins[i][j] += 1

                        elif i == self.size[1]-1:
                            if j > 0:
                                if self.grille[i][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i-1][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                            if j < self.size[0]-1:
                                if self.grille[i][j+1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i-1][j+1] == 1:
                                    self.grille_voisins[i][j] += 1

                            if self.grille[i-1][j] == 1:
                                self.grille_voisins[i][j] += 1

                        else:
                            if j > 0:
                                if self.grille[i][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i-1][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i+1][j-1] == 1:
                                    self.grille_voisins[i][j] += 1
                            if j < self.size[0]-1:
                                if self.grille[i][j+1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i-1][j+1] == 1:
                                    self.grille_voisins[i][j] += 1
                                if self.grille[i+1][j+1] == 1:
                                    self.grille_voisins[i][j] += 1

                            if self.grille[i+1][j] == 1:
                                self.grille_voisins[i][j] += 1
                            if self.grille[i-1][j] == 1:
                                self.grille_voisins[i][j] += 1

        def create_pos(self):
            name = 0
            for i in range(self.size[1]):
                for j in range(self.size[0]):
                    self.liste_pos.append(Minesweeper_pos("pos_"+str(name), (j*self.pas+self.coor[0], i*self.pas+self.coor[1]), self.img_base))
                    name += 1

        def mine_is_click(self, coor, flag=False):
            liste_temp = [0,1,4,5]
            liste_temp2 = [4,5]
            for elem in self.liste_pos:
                if elem.pos.collidepoint(coor):
                    if self.grille[(elem.coor[1]-self.coor[1])//self.pas][(elem.coor[0]-self.coor[0])//self.pas] in liste_temp:
                        if flag:
                            if self.grille[(elem.coor[1]-self.coor[1])//self.pas][(elem.coor[0]-self.coor[0])//self.pas] in liste_temp2:
                                self.grille[(elem.coor[1]-self.coor[1])//self.pas][(elem.coor[0]-self.coor[0])//self.pas] -= 4
                            else:
                                self.grille[(elem.coor[1]-self.coor[1])//self.pas][(elem.coor[0]-self.coor[0])//self.pas] += 4
                        elif self.grille[(elem.coor[1]-self.coor[1])//self.pas][(elem.coor[0]-self.coor[0])//self.pas] not in liste_temp2:
                            self.grille[(elem.coor[1]-self.coor[1])//self.pas][(elem.coor[0]-self.coor[0])//self.pas] += 2
                            self.count += 1

    class Minesweeper_pos:
        def __init__(self, name, coor, img):
            self.name = name
            self.coor = coor
            self.pos = img.get_rect(topleft=coor)
            
    Minesweeper_fond = pygame.image.load("Games/Mini Picture Original/Wall-E Minesweeper/fond.png").convert_alpha()
    Minesweeper_alpha = pygame.image.load("Games/Mini Picture Original/Wall-E Minesweeper/fond_alpha.png").convert_alpha()
    Minesweeper_selector = pygame.image.load("Games/Mini Picture Original/Wall-E Minesweeper/Selection_menu.png").convert_alpha()
    
    pos_DOWN_Minesweeper_mine = DOWN_button.get_rect(topleft=(950,250))
    pos_UP_Minesweeper_mine = UP_button.get_rect(topleft=(1050,250))
    
    pos_DOWN_Minesweeper_width = DOWN_button.get_rect(topleft=(950,300))
    pos_UP_Minesweeper_width = UP_button.get_rect(topleft=(1050,300))
    
    pos_DOWN_Minesweeper_height = DOWN_button.get_rect(topleft=(950,350))
    pos_UP_Minesweeper_height = UP_button.get_rect(topleft=(1050,350))

    # Chargement des images du jeu "WALL-E's Jump" Mini Picture Original + variables + positions

    Jump_menu_play_button = pygame.image.load("Games/Mini Picture Original/Jump/play_button.png").convert_alpha()
    pos_Jump_menu_play_button = Jump_menu_play_button.get_rect(topleft=(50,250))

    Jump_menu_settings_button = pygame.image.load("Games/Mini Picture Original/Jump/settings_button.png").convert_alpha()
    Jump_menu_help_button = pygame.image.load("Games/Mini Picture Original/Jump/help_button.png").convert_alpha()
    Jump_menu_quit_button = pygame.image.load("Games/Mini Picture Original/Jump/quit_button.png").convert_alpha()
    pos_Jump_menu_quit_button = Jump_menu_quit_button.get_rect(topleft=(50,400))

    Jump_menu_alpha = pygame.image.load("Games/Mini Picture Original/Jump/menu_alpha_part.png").convert_alpha()

    Jump_player = pygame.image.load("Games/Mini Picture Original/Jump/player.png").convert_alpha()
    Jump_player1 = pygame.image.load("Games/Mini Picture Original/Jump/player1.png").convert_alpha()
    Jump_player_cube = pygame.image.load("Games/Mini Picture Original/Jump/player_cube.png").convert_alpha()
    Jump_obstacle1 = pygame.image.load("Games/Mini Picture Original/Jump/obstacle1.png").convert_alpha()
    Jump_obstacle2 = pygame.image.load("Games/Mini Picture Original/Jump/obstacle2.png").convert_alpha()
    Jump_obstacle3 = pygame.image.load("Games/Mini Picture Original/Jump/obstacle3.png").convert_alpha()
    Jump_dirt1 = pygame.image.load("Games/Mini Picture Original/Jump/dirt.png").convert_alpha()
    Jump_dirt2 = pygame.image.load("Games/Mini Picture Original/Jump/dirt.png").convert_alpha()
    Jump_cloud1 = pygame.image.load("Games/Mini Picture Original/Jump/cloud1.png").convert_alpha()
    Jump_cloud2 = pygame.image.load("Games/Mini Picture Original/Jump/cloud2.png").convert_alpha()
    Jump_cloud3 = pygame.image.load("Games/Mini Picture Original/Jump/cloud3.png").convert_alpha()
    Jump_cloud4 = pygame.image.load("Games/Mini Picture Original/Jump/cloud4.png").convert_alpha()
    Jump_landscape = pygame.image.load("Games/Mini Picture Original/Jump/earth_landscape.png").convert_alpha()

    # Chargement des images de Tetros, une production de Maxime Picture et de MINI Picture

    Tetros_fond = pygame.image.load("Games/Banuls and Mini Picture/Tetros/Images/fond.png").convert_alpha()
    Tetros_alpha = pygame.image.load("Games/Banuls and Mini Picture/Tetros/Images/fond_alpha.png").convert_alpha()
    Tetros_selector = pygame.image.load("Games/Banuls and Mini Picture/Tetros/Images/Selection_menu.png").convert_alpha()
    
    # Chargement des miniatures de Vilallongue_chroni, une production de Vilallongue Picture
    
    Vilallongue_min0 = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond_min0.jpg").convert_alpha()
    pos_Vilallongue_min0 = Vilallongue_min0.get_rect(topleft=(40,40))
    Vilallongue_min1 = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond_min1.jpg").convert_alpha()
    pos_Vilallongue_min1 = Vilallongue_min0.get_rect(topleft=(250,40))
    Vilallongue_min2 = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond_min2.jpg").convert_alpha()
    pos_Vilallongue_min2 = Vilallongue_min0.get_rect(topleft=(460,40))
    Vilallongue_min3 = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond_min3.jpg").convert_alpha()
    pos_Vilallongue_min3 = Vilallongue_min0.get_rect(topleft=(670,40))
    Vilallongue_min4 = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond_min4.jpg").convert_alpha()
    pos_Vilallongue_min4 = Vilallongue_min0.get_rect(topleft=(880,40))

    """Définition des positions de diverses images"""

    pos_Menu = Menu.get_rect(topleft=(1150,20))

    # Initialisation de la postion initialle du sélecteur du menu principal
    pos_Selecteur = Selection_menu.get_rect(topleft=(0,position_selecteur))

    # Initialisation de la positon des boutons du lecteur multimédia
    pos_Pause = Pause.get_rect(topleft=(1136,144))
    pos_Lecture = Lecture.get_rect(topleft=(1136,576))
    pos_Avancer = Avancer.get_rect(topleft=(1136,432))
    pos_Reculer = Reculer.get_rect(topleft=(1136,288))
    pos_Menu1 = Reculer.get_rect(topleft=(1136,0))

    # Initialisation des positions du contrôle de volume (soundtrack ou paramètres)
    pos_sound_up = sound_up.get_rect(topleft=(1036,150))
    pos_sound_down = sound_down.get_rect(topleft=(1036,450))

    # Inititialisation de la position des tuiles du menu Paramètres
    pos_Version = Version.get_rect(topleft=(20,20))
    pos_Infos = Infos.get_rect(topleft=(0,0))
    pos_Infos1 = Infos1.get_rect(topleft=(0,0))
    pos_Modules = Modules.get_rect(topleft=(0,180))
    pos_Modules1 = Modules1.get_rect(topleft=(0,180))
    pos_Animations = Modules.get_rect(topleft=(0,360))
    pos_Animations1 = Modules1.get_rect(topleft=(0,360))
    pos_Fond_paramètres = Fond_paramètres.get_rect(topleft=(0,540))
    pos_Fond_paramètres1 = Fond_paramètres1.get_rect(topleft=(0,540))

    # Inititialisation de la position des miniatures des fonds d'écran (Paramètres -> Personnalisation)
    pos_fondmenu0_a = fondmenu0_a.get_rect(topleft=(250,150))
    pos_fondmenu1_a = fondmenu1_a.get_rect(topleft=(460,150))
    pos_fondmenu2_a = fondmenu1_a.get_rect(topleft=(460,273))
    pos_fondmenu3_a = fondmenu3_a.get_rect(topleft=(670,150))
    pos_fondmenu4_a = fondmenu4_a.get_rect(topleft=(880,150))
    pos_fondmenu5_a = fondmenu5_a.get_rect(topleft=(250,273))

    # Initialisation des positions des miniatures des skins
    pos_titanium_widgets_BNL = fondmenu4_a.get_rect(topleft=(250,600))
    pos_old_style = fondmenu5_a.get_rect(topleft=(550,600))

    # Inititialisation de la position des boutons du menu relatif aux pop-up
    pos_bouton_Python = bouton_Python.get_rect(topleft=(500,650))
    pos_bouton_Abord = bouton_Abord.get_rect(topleft=(700,650))
    pos_bouton_C = bouton_C.get_rect(topleft=(710,490))
    pos_bouton_OK = bouton_OK.get_rect(topleft=(100,650))

    # Initialisation des positions des flèches du menu jeux
    pos_Gauche_f = Gauche_f.get_rect(topleft=(30,260))
    pos_Droite_f = Droite_f.get_rect(topleft=(1205,260))

    # Initialisation du carroussel (menu principal Carroussel)

    vignette_1 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp1]+".png").convert_alpha()
    vignette_5 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp4]+".png").convert_alpha()

    vignette_3 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection]+".png").convert_alpha()

    vignette_2 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp2]+".png").convert_alpha()
    vignette_4 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp3]+".png").convert_alpha()

    vignette_1 = pygame.transform.scale(vignette_1, (300,169))
    vignette_5 = pygame.transform.scale(vignette_5, (300,169))

    vignette_2 = pygame.transform.scale(vignette_2, (400,225))
    vignette_4 = pygame.transform.scale(vignette_4, (400,225))

    """Initialisation des textes et de leur position, du menu principal Titanium-Widgets, ainsi que de la police d'écriture"""
    def font_init():
        global font
        global font_widget
        global font_soundtrack
        global font_popup
        global font_credits
        global font_big
        global font_audio_reader
        global font_games_menu
        global font_score
        global font_color
        global font_underline
        global texte_accueil
        global texte_vidéos
        global texte_jauge
        global texte_audio_player
        global texte_jeux
        global texte_paramètres
        global texte_credits
        global texte_quitter
        global texte_intercomm
        global texte_tools
        global texte_color

        font = pygame.font.Font(font_selected, 25)
        font_underline = pygame.font.Font(font_selected, 25)
        font_underline.underline = True
        font_widget = pygame.font.Font(font_selected, 19)
        font_soundtrack = pygame.font.Font(font_selected, 15)
        font_popup = pygame.font.Font(font_selected, 20)
        font_credits = pygame.font.Font(font_selected, 15)
        font_big = pygame.font.Font(font_selected, 60)
        font_audio_reader = pygame.font.Font(font_selected, 30)
        font_games_menu = pygame.font.Font(font_selected, 20)
        font_score = pygame.font.Font(None, 40)
        font_color = pygame.font.Font(None, 30)
        texte_accueil = font.render(langue.title_home, 1, color_menu)
        texte_vidéos = font.render(langue.title_videos, 1, color_menu)
        texte_jauge = font.render(langue.title_level, 1, color_menu)
        texte_audio_player = font.render(langue.title_audio_player, 1, color_menu)
        texte_jeux = font.render(langue.title_games, 1, color_menu)
        texte_paramètres = font.render(langue.title_parameters, 1, color_menu)
        texte_credits = font.render(langue.title_credits, 1, color_menu)
        texte_quitter = font.render(langue.title_quit, 1, color_menu)
        texte_intercomm = font.render(langue.title_intercomm, 1, color_menu)
        texte_tools = font.render(langue.title_tools, 1, color_menu)
        texte_color = font.render("Couleurs", 1, color_menu)

    font_init()

    pygame.display.flip()

    """ Déclaration de l'objet "intercomm_crypt", chargé d'encoder et de décoder les messages de BNL's Intercomm """
    class intercomm_crypt:
        def __init__(self):

            my_key_aee = 0
            
            while my_key_aee <= 0:

                min = 130
                max = min + 10
                primer_number = []
                
                for number in range (min, max + 1):  
                    if number > 1:  
                        for i in range (2, number):  
                            if (number % i) == 0:  
                                break  
                        else:  
                            primer_number.append(number)
                            
                my_key_number = random.sample(primer_number, 2)
                
                my_key_n = my_key_number[0] * my_key_number[1]
                
                my_key_phi = (my_key_number[0]-1) * (my_key_number[1]-1)
                
                my_key_e = random.randint(10,100)
                
                while gcd(my_key_e, my_key_phi) != 1:
                    my_key_e += 1
                    
                my_key_aee = extended_gcd(my_key_e,my_key_phi)[1]
                
                self.my_public_key = (my_key_n, my_key_e)
                self.my_private_key = (my_key_n, my_key_aee)

            self.encode_protocole = "(a**self.other_public_key[1])%self.other_public_key[0]"            
            self.decode_protocole = "(a**self.my_private_key[1])%self.my_private_key[0]"

        def other_decode_protocole_assign(self, key):
            global compatibility_mode
            if key == "compatibility_mode":
                compatibility_mode = 1
            else:
                compatibility_mode = 0
                self.other_public_key = eval(key)

        def encode(self, string):
            string = str(string)
            liste = []
            for e in string:
                a = ord(e)
                liste.append(eval(self.encode_protocole))
            return str(liste)

        def decode(self, liste):
            liste = eval(liste)
            string = ""
            for e in liste:
                a = e
                string += chr(int(eval(self.decode_protocole)))
            return string

        def encode_general(self, string):
            string = str(string)
            liste = []
            for e in string:
                a = ord(e)
                liste.append(a)
            return str(liste)
        def decode_general(self, liste):
            liste = eval(liste)
            string = ""
            for e in liste:
                a = e
                string += chr(int(a))
            return string

        def version_check(self, string):
            global compatibility_mode
            string = self.decode_general(string)
            string = string.split(".")
            my_version = Version_Intercomm.split(".")
            if string[0] != "compatibility_mode":
                if string[0] != my_version[0]:
                    if string[1] != my_version[1]:
                        compatibility_mode = 1
                    else:
                        compatibility_mode = 0
                else:
                    compatibility_mode = 2
            else:
                if string[1] != my_version[0]:
                    compatibility_mode = 2
                else:
                    compatibility_mode = 1 
                
            if compatibility_mode != 1:
                compatibility_mode = intercomm_compatibility_enforced    
                
    class Loading_signal:
        def __init__(self, name, img_list, sleep, coor, stat):
            self.name = name
            self.img_list = img_list
            self.sleep = sleep                        
            self.stat = stat
            self.indice = 0
            self.img_in_use = None
            self.Thread = None
            
            if type(self.img_list) == str:
                path = img_list
                self.img_list = os.listdir(path)
                for i in range(len(self.img_list)):
                    self.img_list[i] = pygame.image.load(f"{path}/{self.img_list[i]}").convert_alpha()
                    
            if coor == "centred":
                temp = (taille[0]//2)-((self.img_list[0].get_width())//2)
                temp2 = (taille[1]//2)-((self.img_list[0].get_height())//2)
                self.coor = (temp, temp2)
                
            elif coor[0] == "half_centred":
                temp = (taille[0]//2)-((self.img_list[0].get_width())//2)
                self.coor = (temp, coor[1])

            elif coor[1] == "half_centred":
                temp = (taille[1]//2)-((self.img_list[0].get_height())//2)
                self.coor = (coor[0], temp)
                
            elif len(coor) == 3:
                if coor[0] == "centred":
                    temp = ((taille[0]-coor[1])//2)-((self.img_list[0].get_width())//2)+(coor[1])
                    temp2 = ((taille[1]-coor[2])//2)-((self.img_list[0].get_height())//2)+(coor[2])
                    self.coor = (temp, temp2)               
                
            else:
                self.coor = coor
            
        def signal_with_img(self):
            while self.stat:
                self.img_in_use = self.img_list[self.indice]
                time.sleep(self.sleep)
                if self.indice == len(self.img_list)-1:
                    self.indice = 0
                else:
                    self.indice += 1
                    
        def start_signal(self):
            self.stat = True
            self.Thread = Thread(target=self.signal_with_img, args=(), daemon=True)
            self.Thread.start()
                
        def stop_signal(self):
            self.stat = False
            self.indice = 0
            self.img_in_use = None
            
    Youtube_loading_signal = Loading_signal("yt-dlp", "Images/Signal", 0.05, (800,650), False)
    Audio_player_loading_signal = Loading_signal("Audio_player", "Images/Signal", 0.05, "centred", False)
    Wallpapers_loading_signal = Loading_signal("Wallpapers", "Images/Signal", 0.05, ("centred",180,0), False)

    # Réglage du volume (général), selon le réglage de l'utilisateur
    pygame.mixer.music.set_volume(volume_BNL/10)

    # Action du système "AdaptoRAM" (si activé), activant/désactivant les animations et transitions en fonction de la RAM disponible (présent dans chaque boucle)
    if AdaptoRAM_check:
        if psutil.virtual_memory()[1] < RAM_free:
            animations = False
            transition_check = False

    """Initialisation des animations et des fonctions"""
    if continuer:
        étape_programme = "Animations d'ouverture"
        # Animation du logo MINI Picture au lancement
        if animations:
            pygame.mixer.music.load("Sounds/Jingle.mp3")
            pygame.mixer.music.play()
            sortie = True
            for i in range(248):
                if sortie:
                    text="Logo/Logo"+str(i)+".png"
                    fond1 = pygame.image.load(text).convert_alpha()
                    fenetre.blit(fond1,(0,0))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                sortie = False
                    time.sleep(0.02)
            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,1280,720))

        étape_programme ="Initialisation des fonctions"

        # Affichage de la jauge de batterie (widget jauge), issu à l'origine d'un jeu du professeur
        def afficher_batons(n,décalage1,décalage2):
            x = 0
            for i in range(n):
                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+décalage1+125,widget_level_coor[1]+décalage2+255-x,150, 15))
                x +=25

        # Affichage de la jauge de batterie (menu principal Carroussel --> barre inférieure --> jauge), issu à l'origine d'un jeu du professeur
        def afficher_batons_carr(n,coor1,coor2):
            x = 0
            for i in range(n):
                pygame.draw.rect(fenetre, color_level, pygame.Rect(coor1+x,coor2,5, 60))
                x +=10

        # Transition entre les onglets (legacy : toujours en activité)
        def transition_ouverture(n):
            translation=0
            if transition_check:
                for i in range(n):

                    fenetre.blit(wallpapers_use.left,(-640+translation,0))
                    fenetre.blit(wallpapers_use.right,(1281-translation,0))

                    pygame.display.update([(-640+translation,0),(1281-translation,0)])
                    pygame.display.flip()
                    translation+=2

        # Animation BNL à la fermeture
        def fermeture(n):
            if animations:
                run = True
                fenetre.blit(fondmulti,(0,0))
                x=n
                text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                pygame.mixer.music.load("Sounds/BNL-shutdown.mp3")
                pygame.mixer.music.play()
                for i in range(n+1):
                    if run:
                        text="Images/BNL animation/Buy N' Large logo-"+str(x)+".png"
                        fond1 = pygame.image.load(text).convert_alpha()
                        fenetre.blit(fond1,(0,0))
                        pygame.display.flip()
                        x-=1
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                    run = False
                        time.sleep(0.02)

        # Animations BNL à l'ouverture
        def ouverture(n):
            pygame.mixer.music.load("Sounds/BNL-start.mp3")
            pygame.mixer.music.play()
            run = True
            for i in range(n):
                if run:
                    text="Images/BNL animation/Buy N' Large logo-"+str(i)+".png"
                    fond1 = pygame.image.load(text).convert_alpha()
                    fenetre.blit(fond1,(0,0))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                run = False
                    time.sleep(0.02)

            pygame.mixer.music.unload()

        if animations:
            ouverture(173)

        # Animation du menu principal (Titanium-Widgets) au démarrage/transitions
        def ouverture_titre(n,check,ost):
            
            global avance
            
            if transition_check:
                x=n
                global position_selecteur

                for i in range(n):
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                    if widget_soundtrack :
                        a_string=pygame.mixer.music.get_pos()/1000
                        float_str = float(a_string)
                        test= int(float_str)
                        temps = 200/audio_reader_proc.time
                        avance=temps*test
                        fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0]+x*10,widget_soundtrack_coor[1]))
                        texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                        fenetre.blit(texte, (widget_soundtrack_coor[0]+x*10+15, widget_soundtrack_coor[1]+33))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+x*10+95,widget_soundtrack_coor[1]+152))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+x*10+95,widget_soundtrack_coor[1]+152))

                        fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+x*10+15,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+x*10+175,widget_soundtrack_coor[1]+152))
                        fenetre.blit(Curseur, (widget_soundtrack_coor[0]+x*10+9+avance, widget_soundtrack_coor[1]+103))

                        fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+x*10+240,widget_soundtrack_coor[1]+70))

                    if widget_level:
                        fenetre.blit(widget_level_skin,(widget_level_coor[0]+x*10,widget_level_coor[1]))

                        try :
                            battery = psutil.sensors_battery()
                            level= battery.percent
                            plugged = battery.power_plugged
                            a_string = level/10
                            float_str = float(a_string)
                            test= int(float_str)
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,x*10,0)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,x*10,0)

                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+x*10+125, widget_level_coor[1]+280, 150, 30))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (widget_level_coor[0]+x*10+150, widget_level_coor[1]+285))

                        except :
                            texte = font.render("ERROR", 1, (255,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+x*10+155,widget_level_coor[1]+155))

                    if i <= 30 :
                        fenetre.blit(widget_signet_close,(1310-2*i,500))
                    else :
                        fenetre.blit(widget_signet_close,(1252,500))

                    fenetre.blit(texte_accueil, (20-x, 20))

                    fenetre.blit(texte_vidéos, (20-x, 90))

                    fenetre.blit(texte_jauge, (20-x, 160))

                    fenetre.blit(texte_audio_player, (20-x, 230))

                    fenetre.blit(texte_jeux, (20-x, 300))

                    fenetre.blit(texte_paramètres, (20-x, 370))

                    fenetre.blit(texte_credits, (20-x, 440))

                    fenetre.blit(texte_intercomm, (20-x, 510))

                    fenetre.blit(texte_tools, (20-x, 580))

                    fenetre.blit(texte_quitter, (20-x, 650))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))

                    if position_selecteur == 70:
                        fenetre.blit(Bonus,(300-x*2,70))
                    if position_selecteur == 140:
                        fenetre.blit(Solar,(291-x*2,140))
                    if position_selecteur == 210:
                        fenetre.blit(audio_player_icon_min,(291-x*2,210))
                    if position_selecteur == 280:
                        fenetre.blit(Autopilot_menu,(300-x*2,280))
                    if position_selecteur == 350:
                        fenetre.blit(BNLmenu,(291-x*2,350))
                    if position_selecteur == 420:
                        fenetre.blit(Lounge_menu,(300-x*2,420))
                    if position_selecteur == 490:
                        fenetre.blit(Intercomm_menu,(300-x*2,490))
                    if position_selecteur == 560:
                        fenetre.blit(tools_min,(300-x*2,560))
                    if position_selecteur == 630:
                        fenetre.blit(MO_menu,(300-x*2,630))

                    if check == 1:
                        fenetre.blit(Selection_menu,(0,x))
                    elif check ==2:
                        fenetre.blit(Selection_menu,(-x*2,position_selecteur))
                    pygame.display.flip()
                    x-=1
            if widget_signet :
                widget_barre_transition(1)

        # Animation du menu principal (Titanium-Widgets) lors des transitions (fermeture)
        def fermeture_titre(n,check,ost):
            
            global avance
            
            if transition_check:
                x=0
                global position_selecteur
                if widget_signet :
                    widget_barre_transition(2)
                for i in range(n):
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    if widget_soundtrack:
                        a_string=pygame.mixer.music.get_pos()/1000
                        float_str = float(a_string)
                        test= int(float_str)
                        temps = 200/audio_reader_proc.time
                        avance=temps*test
                        fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0]+i*10,widget_soundtrack_coor[1]))
                        texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                        fenetre.blit(texte, (widget_soundtrack_coor[0]+i*10+15, widget_soundtrack_coor[1]+33))

                        if pygame.mixer.music.get_busy():
                            fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+i*10+95,widget_soundtrack_coor[1]+152))
                        elif not(pygame.mixer.music.get_busy()):
                            fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+i*10+95,widget_soundtrack_coor[1]+152))

                        fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+i*10+15,widget_soundtrack_coor[1]+152))
                        fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+i*10+175,widget_soundtrack_coor[1]+152))
                        fenetre.blit(Curseur, (widget_soundtrack_coor[0]+i*10+9+avance, widget_soundtrack_coor[1]+103))

                        fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+i*10+240,widget_soundtrack_coor[1]+70))

                    if widget_level:
                        fenetre.blit(widget_level_skin,(widget_level_coor[0]+i*10,widget_level_coor[1]))

                        try :
                            battery = psutil.sensors_battery()
                            level= battery.percent
                            plugged = battery.power_plugged
                            a_string = level/10
                            float_str = float(a_string)
                            test= int(float_str)
                            if level>=10 and level<100:
                                n=test
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,i*10,0)
                            elif level==100:
                                n=9
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                                afficher_batons(n,i*10,0)

                            elif plugged and level<10:
                                n=0
                                pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                            elif level<10 and not(plugged):
                                pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+i*10+125, widget_level_coor[1]+280, 150, 30))
                                texte = font.render("WARNING", 1, (0,0,0))
                                fenetre.blit(texte, (widget_level_coor[0]+i*10+150, widget_level_coor[1]+285))

                        except:
                            texte = font.render("ERROR", 1, (255,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+i*10+155,widget_level_coor[1]+155))

                    fenetre.blit(widget_signet_close,(1252+2*i,500))

                    fenetre.blit(texte_accueil, (20-x, 20))

                    fenetre.blit(texte_vidéos, (20-x, 90))

                    fenetre.blit(texte_jauge, (20-x, 160))

                    fenetre.blit(texte_audio_player, (20-x, 230))

                    fenetre.blit(texte_jeux, (20-x, 300))

                    fenetre.blit(texte_paramètres, (20-x, 370))

                    fenetre.blit(texte_credits, (20-x, 440))

                    fenetre.blit(texte_intercomm, (20-x, 510))

                    fenetre.blit(texte_tools, (20-x, 580))

                    fenetre.blit(texte_quitter, (20-x, 650))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))

                    if position_selecteur == 70:
                        fenetre.blit(Bonus,(300-x*2,70))
                    if position_selecteur == 140:
                        fenetre.blit(Solar,(291-x*2,140))
                    if position_selecteur == 210:
                        fenetre.blit(audio_player_icon_min,(291-x*2,210))
                    if position_selecteur == 280:
                        fenetre.blit(Autopilot_menu,(300-x*2,280))
                    if position_selecteur == 350:
                        fenetre.blit(BNLmenu,(291-x*2,350))
                    if position_selecteur == 420:
                        fenetre.blit(Lounge_menu,(300-x*2,420))
                    if position_selecteur == 490:
                        fenetre.blit(Intercomm_menu,(300-x*2,490))
                    if position_selecteur == 560:
                        fenetre.blit(tools_min,(300-x*2,560))
                    if position_selecteur == 630:
                        fenetre.blit(MO_menu,(300-x*2,630))

                    if check == 1:
                        fenetre.blit(Selection_menu,(0,x))
                    elif check ==2:
                        fenetre.blit(Selection_menu,(-x*2,position_selecteur))
                    elif check == 3:
                        fenetre.blit(Selection_menu,(0,position_selecteur))

                    pygame.display.flip()
                    x+=1

        # Animation des tuiles du menu Paramètres à l'ouverture
        def Tuiles_ouverture():
            fenetre.blit(wallpapers_use.left,(0,0))
            fenetre.blit(wallpapers_use.right,(640,0))
            if transition_check:
                y = 1

                for i in range(180):
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Animations,(-180+y,360))
                    fenetre.blit(Infos,(-180+y,0))
                    fenetre.blit(Modules,(-180+y,180))
                    fenetre.blit(Fond_paramètres,(-180+y,540))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()
                    y+=1

                y = 1

                if not(Blur_background):
                    for i in range(64):

                        fenetre.blit(wallpapers_use.wallpaper,(0,0))
                        fenetre.blit(fond_visibilité, (-1280+i*20,0))

                        fenetre.blit(Menu,(1150,20))
                        fenetre.blit(Animations,(0,360))
                        fenetre.blit(Infos,(0,0))
                        fenetre.blit(Modules,(0,180))
                        fenetre.blit(Fond_paramètres,(0,540))
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(400,5))
                        pygame.display.flip()

            else:
                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))
                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))
                pygame.display.flip()

        # Animation des tuiles du menu Paramètres à la fermeture
        def Tuiles_fermeture():
            fenetre.blit(wallpapers_use.left,(0,0))
            fenetre.blit(wallpapers_use.right,(640,0))
            if transition_check:
                y = 1
                if not(Blur_background):
                    for i in range(64):
                        fenetre.blit(wallpapers_use.wallpaper,(0,0))
                        fenetre.blit(fond_visibilité, (0-i*20,0))
                        fenetre.blit(Menu,(1150,20))
                        fenetre.blit(Animations,(0,360))
                        fenetre.blit(Infos,(0,0))
                        fenetre.blit(Modules,(0,180))
                        fenetre.blit(Fond_paramètres,(0,540))
                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(400,5))
                        pygame.display.flip()
                        y+=16

                y = 1

                for i in range(180):
                    fenetre.blit(wallpapers_use.left,(0,0))
                    fenetre.blit(wallpapers_use.right,(640,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Animations,(0-y,360))
                    fenetre.blit(Infos,(0-y,0))
                    fenetre.blit(Modules,(0-y,180))
                    fenetre.blit(Fond_paramètres,(0-y,540))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()
                    y+=1

        # Animation des tuiles du lecteur multimédia à l'ouverture (retiré du service et remplacé par le lecteur multimédia)
        def Tuiles_soundtrack_ouverture():
            fenetre.blit(wallpapers_use.left,(0,0))
            fenetre.blit(wallpapers_use.right,(640,0))
            fenetre.blit(Soundtrack,(500,35))
            if transition_check:
                y = 1
                for i in range(193):

                    a_string=pygame.mixer.music.get_pos()/1000
                    float_str = float(a_string)
                    test= int(float_str)
                    temps = 580/audio_reader_proc.time
                    avance=temps*test

                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                    fenetre.blit(Soundtrack,(1280-i*5,35))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()

                for i in range(144):

                    a_string=pygame.mixer.music.get_pos()/1000
                    float_str = float(a_string)
                    test= int(float_str)
                    temps = 580/audio_reader_proc.time
                    avance=temps*test

                    fenetre.blit(wallpapers_use.left,(0,0))
                    fenetre.blit(wallpapers_use.right,(640,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,794-y,580, 2))
                    fenetre.blit(Curseur, (325+avance, 780-y))

                    fenetre.blit(Pause,(1280-y,144))
                    fenetre.blit(Lecture,(1280-y,576))
                    fenetre.blit(Avancer,(1280-y,432))
                    fenetre.blit(Reculer,(1280-y,288))
                    fenetre.blit(Menu1,(1280-y,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()
                    y+=1

                y = 1

                for i in range(71):

                    a_string=pygame.mixer.music.get_pos()/1000
                    float_str = float(a_string)
                    test= int(float_str)
                    temps = 580/audio_reader_proc.time
                    avance=temps*test

                    fenetre.blit(wallpapers_use.left,(0,0))
                    fenetre.blit(wallpapers_use.right,(640,0))
                    fenetre.blit(fond_visibilité, (-1136+y,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,650,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636))

                    fenetre.blit(Pause,(1136,144))
                    fenetre.blit(Lecture,(1136,576))
                    fenetre.blit(Avancer,(1136,432))
                    fenetre.blit(Reculer,(1136,288))
                    fenetre.blit(Menu1,(1136,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()
                    y+=16

            else:
                fenetre.blit(Soundtrack,(315,35))
                fenetre.blit(Lecture,(1136,576))
                fenetre.blit(Avancer,(1136,432))
                fenetre.blit(Reculer,(1136,288))
                fenetre.blit(Menu1,(1136,0))
                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))
                pygame.display.flip()

        # Animation des tuiles du lecteur multimédia à la fermeture (retiré du service et remplacé par le lecteur multimédia)
        def Tuiles_soundtrack_fermeture():
            fenetre.blit(wallpapers_use.wallpaper,(0,0))
            fenetre.blit(Soundtrack,(315,35))
            if transition_check:
                if volume_control == "enable":
                    volume_control_transition("out",1)
                y = 1
                x=315

                for i in range(71):

                    a_string=pygame.mixer.music.get_pos()/1000
                    float_str = float(a_string)
                    test= int(float_str)
                    temps = 580/audio_reader_proc.time
                    avance=temps*test

                    fenetre.blit(wallpapers_use.left,(0,0))
                    fenetre.blit(wallpapers_use.right,(640,0))
                    fenetre.blit(fond_visibilité, (0-y,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,650,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636))

                    fenetre.blit(Pause,(1136,144))
                    fenetre.blit(Lecture,(1136,576))
                    fenetre.blit(Avancer,(1136,432))
                    fenetre.blit(Reculer,(1136,288))
                    fenetre.blit(Menu11,(1136,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()
                    y+=16

                y = 1

                for i in range(144):

                    a_string=pygame.mixer.music.get_pos()/1000
                    float_str = float(a_string)
                    test= int(float_str)
                    temps = 580/audio_reader_proc.time
                    avance=temps*test

                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,650+y,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636+y))

                    fenetre.blit(Pause,(1136+y,144))
                    fenetre.blit(Lecture,(1136+y,576))
                    fenetre.blit(Avancer,(1136+y,432))
                    fenetre.blit(Reculer,(1136+y,288))
                    fenetre.blit(Menu11,(1136+y,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()
                    y+=1

                for i in range(193):

                    a_string=pygame.mixer.music.get_pos()/1000
                    float_str = float(a_string)
                    test= int(float_str)
                    temps = 580/audio_reader_proc.time
                    avance=temps*test

                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                    fenetre.blit(Soundtrack,(315+i*5,35))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()

            else:

                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))
                pygame.display.flip()

        # Animation du menu changelog/mise à jour lors de son apparition/disparition
        def changelog(stat,txt):
            if transition_check:
                texte_changelog_version = font.render(txt, 1, color_menu)
                if stat == "entry":
                    for i in range(128):
                        if Blur_background:
                            fenetre.blit(wallpapers_use.blur, (0,0))
                        else:
                            fenetre.blit(wallpapers_use.wallpaper, (0,0))
                            fenetre.blit(fond_visibilité,(-1280+i*10,0))
                        fenetre.blit(Selection_menu,(-825+i*10,0))
                        fenetre.blit(texte_changelog_version, (-760+i*10, 20))
                        fenetre.blit(changelog_logo,(-525+i*10,4))

                        pygame.display.flip()

                        for event in pygame.event.get():
                            None

                if stat == "out":
                    for i in range(128):
                        if Blur_background:
                            fenetre.blit(wallpapers_use.blur, (0,0))
                        else:
                            fenetre.blit(wallpapers_use.wallpaper, (0,0))
                            fenetre.blit(fond_visibilité,(0-i*10,0))
                        fenetre.blit(Selection_menu,(455-i*10,0))
                        fenetre.blit(texte_changelog_version, (530-i*10, 20))
                        fenetre.blit(changelog_logo,(755-i*10,4))

                        pygame.display.flip()

                        for event in pygame.event.get():
                            None

        transition_ouverture(322)

        if Skin_selected == "Legacy":
            Menu_skin1 = True
            menu_continuer = False
        elif Skin_selected == "Titanium":
            menu_continuer = True
            if First_start == 0 and not(Update_at_start):
                ouverture_titre(200,1,0)
            elif First_start == 1:
                changelog("entry","BNL's Box "+str(Version_Menu))
            Menu_skin1 = False
        elif Skin_selected == "Carroussel":
            Menu_skin2 = True
            if First_start == 0 and not(Update_at_start):
                menu_carroussel.open()
            elif First_start == 1:
                changelog("entry","BNL's Box "+str(Version_Menu))
            Menu_skin1 = False

        # Animation du contrôleur de volume (lecteur multimédia)
        def volume_control_transition(statut,sortie):
            if statut == "out":
                for j in range(25):
                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                    g = 15
                    fenetre.blit(Selection_soundtrack, (0,31+18*(p-1)))
                    for i in range(38):
                        texte = font_soundtrack.render(liste[i], 1, (255,255,255))
                        fenetre.blit(texte, (10, g))
                        g += 18

                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,650,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636))
                    fenetre.blit(sound_up,(1036+j*4,150))
                    fenetre.blit(sound_down,(1036+j*4,450))
                    fenetre.blit(sound_viewer,(1036+j*4,431-sound_viewer_pos))
                    if not(pygame.mixer.music.get_busy()):
                        fenetre.blit(Pause1,(1136,144))
                    else:
                        fenetre.blit(Pause,(1136,144))
                    fenetre.blit(Lecture,(1136,576))
                    fenetre.blit(Avancer,(1136,432))
                    fenetre.blit(Reculer,(1136,288))
                    if sortie == 1 :
                        fenetre.blit(Menu11,(1136,0))
                    else :
                        fenetre.blit(Menu1,(1136,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()

            if statut == "entry":
                for j in range(25):
                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                    g = 15
                    fenetre.blit(Selection_soundtrack, (0,31+18*(p-1)))
                    for i in range(38):
                        texte = font_soundtrack.render(liste[i], 1, (255,255,255))
                        fenetre.blit(texte, (10, g))
                        g += 18

                    fenetre.blit(Soundtrack,(315,35))
                    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,650,580, 2))
                    fenetre.blit(Curseur, (325+avance, 636))
                    fenetre.blit(sound_up,(1136-j*4,150))
                    fenetre.blit(sound_down,(1136-j*4,450))
                    fenetre.blit(sound_viewer,(1136-j*4,431-sound_viewer_pos))
                    if not(pygame.mixer.music.get_busy()):
                        fenetre.blit(Pause1,(1136,144))
                    else:
                        fenetre.blit(Pause,(1136,144))
                    fenetre.blit(Lecture,(1136,576))
                    fenetre.blit(Avancer,(1136,432))
                    fenetre.blit(Reculer,(1136,288))
                    fenetre.blit(Menu1,(1136,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))
                    pygame.display.flip()

        # Animations d'ouverture/fermeture de la barre inférieure (menu principal Carroussel)
        def carr_title_bar_transition(statut, sortie):
            if statut == "entry" and transition_check:
                for i in range(57):
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))

                    fenetre.blit(vignette_1,(100,275))
                    fenetre.blit(vignette_5,(880,275))

                    fenetre.blit(vignette_2,(200,247))
                    fenetre.blit(vignette_4,(680,247))

                    fenetre.blit(vignette_3,(299,168))

                    fenetre.blit(Gauche_video2,(60,500))
                    fenetre.blit(Droite_video2,(1189,500))

                    fenetre.blit(carr_title_bar,(0,720-i*2))

                    texte = font.render(carr_lang_translate[menu_carroussel.liste[menu_carroussel.selection]], 1, color_menu)
                    fenetre.blit(texte, (20, 650+114-i*2))
                    fenetre.blit(carr_level_sun,(1070, 630+114-i*2))

                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)

                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+114-i*2,10, 60))
                            afficher_batons_carr(n,1150,630+114-i*2)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+114-i*2,10, 60))
                            afficher_batons_carr(n,1150,630+114-i*2)
                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+114-i*2,10, 60))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+114-i*2,10, 60))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (1130, 650+114-i*2))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (1130,650+114-i*2))

                    fenetre.blit(widget_soundtrack_reculer,(600,650+114-i*2))
                    fenetre.blit(widget_soundtrack_avancer,(780,650+114-i*2))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(690,650+114-i*2))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(690,650+114-i*2))

                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (600,620+114-i*2))

                    fenetre.blit(audio_reader_proc.min,(490,613+114-i*2))

                    pygame.display.flip()

            if statut == "out" and transition_check:
                for i in range(57):
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))

                    fenetre.blit(vignette_1,(100,275))
                    fenetre.blit(vignette_5,(880,275))

                    fenetre.blit(vignette_2,(200,247))
                    fenetre.blit(vignette_4,(680,247))

                    fenetre.blit(vignette_3,(299,168))

                    fenetre.blit(Gauche_video2,(60,500))
                    fenetre.blit(Droite_video2,(1189,500))

                    fenetre.blit(carr_title_bar,(0,606+i*2))
                    texte = font.render(carr_lang_translate[menu_carroussel.liste[menu_carroussel.selection]], 1, color_menu)
                    fenetre.blit(texte, (20, 650+i*2))
                    fenetre.blit(carr_level_sun,(1070, 630+i*2))

                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+i*2,10, 60))
                            afficher_batons_carr(n,1150,630+i*2)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+i*2,10, 60))
                            afficher_batons_carr(n,1150,630+i*2)
                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+i*2,10, 60))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630+i*2,10, 60))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (1130, 650+i*2))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (1130,650+i*2))

                    fenetre.blit(widget_soundtrack_reculer,(600,650+i*2))
                    fenetre.blit(widget_soundtrack_avancer,(780,650+i*2))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(690,650+i*2))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(690,650+i*2))

                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (600,620+i*2))

                    fenetre.blit(audio_reader_proc.min,(490,613+i*2))

                    pygame.display.flip()

        # Animation du sélecteur du menu principal (Titanium and widgets)
        def sélecteur(commande):
            global position_selecteur

            if commande == "UP" and position_selecteur != 0:
                for i in range(35):
                    position_selecteur -= 2
                    fenetre.blit(wallpapers_use.left_txt, (0,0))

                    fenetre.blit(texte_accueil, (20, 20))

                    fenetre.blit(texte_vidéos, (20, 90))

                    fenetre.blit(texte_jauge, (20, 160))

                    fenetre.blit(texte_audio_player, (20, 230))

                    fenetre.blit(texte_jeux, (20, 300))

                    fenetre.blit(texte_paramètres, (20, 370))

                    fenetre.blit(texte_credits, (20, 440))

                    fenetre.blit(texte_intercomm, (20, 510))

                    fenetre.blit(texte_tools, (20, 580))

                    fenetre.blit(texte_quitter, (20, 650))

                    fenetre.blit(Selection_menu,(0,position_selecteur))
                    pygame.display.flip()
                    time.sleep(0.001)

            if commande == "DOWN" and position_selecteur <= 560  :
                for i in range(35):
                    position_selecteur += 2
                    fenetre.blit(wallpapers_use.left_txt, (0,0))

                    fenetre.blit(texte_accueil, (20, 20))

                    fenetre.blit(texte_vidéos, (20, 90))

                    fenetre.blit(texte_jauge, (20, 160))

                    fenetre.blit(texte_audio_player, (20, 230))

                    fenetre.blit(texte_jeux, (20, 300))

                    fenetre.blit(texte_paramètres, (20, 370))

                    fenetre.blit(texte_credits, (20, 440))

                    fenetre.blit(texte_intercomm, (20, 510))

                    fenetre.blit(texte_tools, (20, 580))

                    fenetre.blit(texte_quitter, (20, 650))

                    fenetre.blit(Selection_menu,(0,position_selecteur))
                    pygame.display.flip()
                    time.sleep(0.001)

    # Réinitialisation des cartes du jeu "WALL-E's Memory"
    def reset_cartes():
        global carte1
        global carte2
        global carte3
        global carte4
        global carte5
        global carte6
        global carte7
        global carte8
        global carte9

        global carte1_bis
        global carte2_bis
        global carte3_bis
        global carte4_bis
        global carte5_bis
        global carte6_bis
        global carte7_bis
        global carte8_bis
        global carte9_bis

        global sélection_carte1
        global sélection_carte2

        global liste_cartes
        global liste_cartes2

        global liste_pos

        global score_card

        sélection_carte1 = 0
        sélection_carte2 = 0

        liste_cartes = ["Games/Mini Picture Original/Cartes/AUTO carte.png","Games/Mini Picture Original/Cartes/Axiom carte.png", "Games/Mini Picture Original/Cartes/Eve carte.png","Games/Mini Picture Original/Cartes/Journal carte.png",
        "Games/Mini Picture Original/Cartes/MO carte.png","Games/Mini Picture Original/Cartes/Poster carte.png","Games/Mini Picture Original/Cartes/Space carte.png","Games/Mini Picture Original/Cartes/WALL E2 carte.png",
        "Games/Mini Picture Original/Cartes/Shelby Forthright carte.png"]
        liste_cartes2 = random.sample(liste_cartes,9)

        liste_pos = [(100,50),(260,50),(420,50),(580,50),(740,50),(900,50),(100,260),(260,260),(420,260),(580,260),(740,260),(900,260),(100,470),(260,470),(420,470),(580,470),(740,470),(900,470)]
        liste_pos2 = random.sample(liste_pos,18)

        score_card = 0

        carte1 = Cards_WMG(liste_cartes2[0],liste_pos2[0],0,1)
        carte2 = Cards_WMG(liste_cartes2[1],liste_pos2[1],0,2)
        carte3 = Cards_WMG(liste_cartes2[2],liste_pos2[2],0,3)
        carte4 = Cards_WMG(liste_cartes2[3],liste_pos2[3],0,4)
        carte5 = Cards_WMG(liste_cartes2[4],liste_pos2[4],0,5)
        carte6 = Cards_WMG(liste_cartes2[5],liste_pos2[5],0,6)
        carte7 = Cards_WMG(liste_cartes2[6],liste_pos2[6],0,7)
        carte8 = Cards_WMG(liste_cartes2[7],liste_pos2[7],0,8)
        carte9 = Cards_WMG(liste_cartes2[8],liste_pos2[8],0,9)
        carte1_bis = Cards_WMG(liste_cartes2[0],liste_pos2[9],0,1)
        carte2_bis = Cards_WMG(liste_cartes2[1],liste_pos2[10],0,2)
        carte3_bis = Cards_WMG(liste_cartes2[2],liste_pos2[11],0,3)
        carte4_bis = Cards_WMG(liste_cartes2[3],liste_pos2[12],0,4)
        carte5_bis = Cards_WMG(liste_cartes2[4],liste_pos2[13],0,5)
        carte6_bis = Cards_WMG(liste_cartes2[5],liste_pos2[14],0,6)
        carte7_bis = Cards_WMG(liste_cartes2[6],liste_pos2[15],0,7)
        carte8_bis = Cards_WMG(liste_cartes2[7],liste_pos2[16],0,8)
        carte9_bis = Cards_WMG(liste_cartes2[8],liste_pos2[17],0,9)

    # Animation d'apparition de la fenêtre pop-up
    def pop_up():
        m = 1
        for i in range(100):
            pygame.draw.rect(fenetre, color_aux, pygame.Rect(640-m,360-m,1+m*2, 1+m*2))
            pygame.display.flip()
            m += 2
            time.sleep(0.001)
            pygame.draw.rect(fenetre, color_aux, pygame.Rect(638-m,358-m,4+m*2, 4+m*2))
            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-m,360-m,1+m*2, 1+m*2))

    # Animation de la barre contenant les widgets (Titanium and widgets skin)
    def widget_barre_transition(statut):
        if statut == 1 :
            for i in range(50):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                if widget_soundtrack :
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                    try :
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1280-2*i,0))
                fenetre.blit(widget_signet_open,(1252-2*i,500))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1290-2*i,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1290-2*i,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

        if statut == 2 :
            for i in range(50):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                if widget_soundtrack :
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                    try :
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180+2*i,0))
                fenetre.blit(widget_signet_close,(1152+2*i,500))

                if not(widget_soundtrack) :
                    fenetre.blit(widget_soundtrack_miniature,(1190+2*i,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190+2*i,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

    # Animation des widgets (Titanium and widgets skin) lors de leur apparition ou disparition
    def widget_animation(widget,statut):
        global widget_soundtrack_coor
        global pos_widget_soundtrack_skin
        global widget_level_coor
        global pos_widget_level_skin
        global décalage_widget
        global avance
        if widget == "soundtrack" and statut == 1:
            for i in range(45):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                fenetre.blit(widget_soundtrack_miniature,(1190+2*i,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

            for i in range(70):
                
                a_string=pygame.mixer.music.get_pos()/1000
                float_str = float(a_string)
                test= int(float_str)
                temps = 200/audio_reader_proc.time
                avance=temps*test
                
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                fenetre.blit(widget_soundtrack_skin,(1280-2*i,32))
                texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                fenetre.blit(texte, (1280-2*i+15, 32+33))

                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_pause,(1280-2*i+95,widget_soundtrack_coor[1]+152))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(1280-2*i+95,widget_soundtrack_coor[1]+152))

                fenetre.blit(widget_soundtrack_reculer,(1280-2*i+15,32+152))
                fenetre.blit(widget_soundtrack_avancer,(1280-2*i+175,32+152))
                fenetre.blit(Curseur, (1280-2*i+9+avance, 32+103))

                fenetre.blit(audio_reader_proc.min,(1280-2*i+240,32+70))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))
                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

            widget_soundtrack_coor = [1140,32]
            pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
            décalage_widget = [0,0]

        if widget == "soundtrack" and statut == 2:
            i = 0
            while widget_soundtrack_coor[0]+2*i < 1280:
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0]+2*i,widget_soundtrack_coor[1]))

                texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                fenetre.blit(texte, (widget_soundtrack_coor[0]+2*i+15, widget_soundtrack_coor[1]+33))

                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+2*i+95,widget_soundtrack_coor[1]+152))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+2*i+95,widget_soundtrack_coor[1]+152))

                fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+2*i+15,widget_soundtrack_coor[1]+152))
                fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+2*i+175,widget_soundtrack_coor[1]+152))
                fenetre.blit(Curseur, (widget_soundtrack_coor[0]+2*i+9+avance, widget_soundtrack_coor[1]+103))

                fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+2*i+240,widget_soundtrack_coor[1]+70))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))
                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()
                
                i += 1

            for i in range(50):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                if widget_level:
                    fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))
                    try :
                        battery = psutil.sensors_battery()
                        level= battery.percent
                        plugged = battery.power_plugged
                        a_string = level/10
                        float_str = float(a_string)
                        test= int(float_str)
                        if level>=10 and level<100:
                            n=test
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)
                        elif level==100:
                            n=9
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            afficher_batons(n,0,0)

                        elif plugged and level<10:
                            n=0
                            pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        elif level<10 and not(plugged):
                            pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                            texte = font.render("WARNING", 1, (0,0,0))
                            fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                    except:
                        texte = font.render("ERROR", 1, (255,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))
                fenetre.blit(widget_soundtrack_miniature,(1290-2*i,50))

                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

            widget_soundtrack_coor = [0,0]
            pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
            décalage_widget = [0,0]

        if widget == "level" and statut == 1:
            for i in range(45):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                if widget_soundtrack:
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                fenetre.blit(widget_level_miniature,(1190+2*i,130))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

            for i in range(70):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                fenetre.blit(widget_level_skin,(1280-2*i,32))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                        afficher_batons(n,(widget_level_coor[0])*(-1)+1280-2*i,(widget_level_coor[1])*(-1)+32)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                        afficher_batons(n,(widget_level_coor[0])*(-1)+1280-2*i,(widget_level_coor[1])*(-1)+32)

                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(1280-2*i+125, 32+280, 150, 30))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (1280-2*i+150, 32+285))

                except Exception as e:
                    texte = font.render("ERROR", 1, (255,0,0))
                    fenetre.blit(texte, (1280-2*i+155,widget_level_coor[1]+155))

                if widget_soundtrack:
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

            widget_level_coor = [1140,32]
            pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))
            décalage_widget = [0,0]

        if widget == "level" and statut == 2:
            i = 0
            while widget_level_coor[0]+2*i < 1280 :
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                fenetre.blit(widget_level_skin,(widget_level_coor[0]+2*i,widget_level_coor[1]))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,2*i,0)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,2*i,0)

                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+2*i+125, widget_level_coor[1]+280, 150, 30))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+2*i+150, widget_level_coor[1]+285))

                except Exception as e:
                    texte = font.render("ERROR", 1, (255,0,0))
                    fenetre.blit(texte, (widget_level_coor[0]+2*i+155,widget_level_coor[1]+155))

                if widget_soundtrack:
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))
                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()
                
                i += 1

            for i in range(50):
                fenetre.blit(wallpapers_use.wallpaper, (0,0))

                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))
                fenetre.blit(widget_level_miniature,(1290-2*i,130))

                if not(widget_soundtrack):
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))
                else :
                    fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                    texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                    fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))

                    if pygame.mixer.music.get_busy():
                        fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                    elif not(pygame.mixer.music.get_busy()):
                        fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                    fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                    fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                    fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

                fenetre.blit(Selection_menu,(0,position_selecteur))

                fenetre.blit(texte_accueil, (20, 20))

                fenetre.blit(texte_vidéos, (20, 90))

                fenetre.blit(texte_jauge, (20, 160))

                fenetre.blit(texte_audio_player, (20, 230))

                fenetre.blit(texte_jeux, (20, 300))

                fenetre.blit(texte_paramètres, (20, 370))

                fenetre.blit(texte_credits, (20, 440))

                fenetre.blit(texte_intercomm, (20, 510))

                fenetre.blit(texte_tools, (20, 580))

                fenetre.blit(texte_quitter, (20, 650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                if position_selecteur == 70:
                    fenetre.blit(Bonus,(300,70))
                if position_selecteur == 140:
                    fenetre.blit(Solar,(291,140))
                if position_selecteur == 210:
                    fenetre.blit(audio_player_icon_min,(291,210))
                if position_selecteur == 280:
                    fenetre.blit(Autopilot_menu,(300,280))
                if position_selecteur == 350:
                    fenetre.blit(BNLmenu,(291,350))
                if position_selecteur == 420:
                    fenetre.blit(Lounge_menu,(300,420))
                if position_selecteur == 490:
                    fenetre.blit(Intercomm_menu,(300,490))
                if position_selecteur == 560:
                    fenetre.blit(tools_min,(300,560))
                if position_selecteur == 630:
                    fenetre.blit(MO_menu,(300,630))

                pygame.display.flip()

            widget_level_coor = [0,0]
            pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))
            décalage_widget = [0,0]

    # Réassignation des variables images après sélection d'un nouveau thème
    def theme_init():

        global Rouge
        global Bleu
        global Violet
        global Vert
        global Jaune
        global Cyan
        global more_colors
        global more_fonts
        global more_themes
        global more_wallpapers
        global new_wallpapers
        global scroll_bar
        global Selection_menu
        global Selection_soundtrack
        global bouton_Python
        global bouton_C
        global bouton_Abord
        global bouton_OK
        global bouton_search_update
        global bouton_update_python
        global bouton_update_all_python
        global bouton_delete_all_python
        global BNLmenu
        global Soundtrack
        global Soundtrack_menu
        global Autopilot_menu
        global MO_menu
        global Lounge_menu
        global Solar
        global Bonus
        global Autre
        global Infos
        global Infos1
        global Modules
        global Modules1
        global Animations
        global Animations1
        global Fond_paramètres
        global Fond_paramètres1
        global fond_visibilité
        global ON_OFF_maker
        global ON
        global OFF
        global widget_soundtrack_skin
        global widget_soundtrack_miniature
        global widget_soundtrack_lecture
        global widget_soundtrack_pause
        global widget_soundtrack_reculer
        global widget_soundtrack_avancer
        global widget_level_miniature
        global widget_level_skin
        global widget_barre
        global widget_signet_open
        global widget_signet_close
        global Son
        global Lecture
        global Pause
        global Avancer
        global Reculer
        global Lecture1
        global Pause1
        global Avancer1
        global Reculer1
        global Menu1
        global Menu11
        global carr_title_bar
        global carr_level_sun
        global menu_carroussel
        global Intercomm_menu
        global tools_min
        global submenu_wallpapers
        global audio_player_icon_min
        global yt_dlp_icon_min
        global tello_icon_min
        global UP_button
        global UP_button1
        global DOWN_button
        global DOWN_button1
        global Color_menu
        
        Rouge = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Rouge.png").convert_alpha()
        Bleu = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Bleu.png").convert_alpha()
        Violet = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Violet.png").convert_alpha()
        Vert = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Vert.png").convert_alpha()
        Jaune = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Jaune.png").convert_alpha()
        Cyan = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Cyan.png").convert_alpha()
        more_colors = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
        more_themes = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
        more_fonts = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
        more_wallpapers = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
        new_wallpapers = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/More colors.png").convert_alpha()
        scroll_bar = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/scroll_bar.png").convert_alpha()
        Selection_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Selection_menu.png").convert_alpha()
        Selection_soundtrack = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Selection_soundtrack.png").convert_alpha()
        bouton_Python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_bouton.png").convert_alpha()
        bouton_C = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/C#_bouton.png").convert_alpha()
        bouton_Abord = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Annuler_bouton.png").convert_alpha()
        bouton_OK = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Bouton_OK.png").convert_alpha()
        bouton_search_update = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Search_update.png").convert_alpha()
        bouton_update_python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_update.png").convert_alpha()
        bouton_update_all_python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_update_all.png").convert_alpha()
        bouton_delete_all_python = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Python_delete_all.png").convert_alpha()
        BNLmenu= pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Parametres.png").convert_alpha()
        Soundtrack = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Soundtrack.png").convert_alpha()        
        Soundtrack_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Soundtrack_menu.png").convert_alpha()
        Autopilot_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Autopilot.png").convert_alpha()
        MO_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/M-O.png").convert_alpha()
        Lounge_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Lounge.png").convert_alpha()
        Solar = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Solar.png").convert_alpha()
        Bonus = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Bonus.png").convert_alpha()
        Autre = pygame.image.load("Images/Autre.png").convert_alpha()
        Infos= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Infos.png").convert_alpha()
        Infos1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Infos1.png").convert_alpha()
        Modules= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Modules.png").convert_alpha()
        Modules1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Modules1.png").convert_alpha()
        Animations= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Animations.png").convert_alpha()
        Animations1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Animations1.png").convert_alpha()
        touche_vide= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/touche_vide.png").convert_alpha()
        Fond_paramètres= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Fond_parametres.png").convert_alpha()
        Fond_paramètres1= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/Fond_parametres1.png").convert_alpha()
        fond_visibilité = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/fond_visibilite.png").convert_alpha()
        ON_OFF_maker= pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/ON_OFF_maker.png").convert_alpha()
        ON = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/ON.png").convert_alpha()
        OFF = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/OFF.png").convert_alpha()
        widget_soundtrack_skin = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Soundtrack Widget.png")
        widget_soundtrack_miniature = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Soundtrack Widget Miniature.png")
        widget_soundtrack_lecture = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Lecture_widget.png")
        widget_soundtrack_pause = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Pause_widget.png")
        widget_soundtrack_reculer = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Reculer_widget.png")
        widget_soundtrack_avancer = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Avancer_widget.png")
        widget_level_miniature = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Level Widget Miniature.png")
        widget_level_skin = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Level Widget.png")
        widget_barre = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Widgets_barre.png")
        widget_signet_open = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Signet_open.png")
        widget_signet_close = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Widgets/Signet_close.png")
        Son = pygame.image.load("Miniature/Soundtrack.png").convert_alpha()
        Lecture = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Lecture.png").convert_alpha()
        Pause = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Pause.png").convert_alpha()
        Avancer = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Avancer.png").convert_alpha()
        Reculer = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Reculer.png").convert_alpha()
        Lecture1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Lecture1.png").convert_alpha()
        Pause1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Pause1.png").convert_alpha()
        Avancer1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Avancer1.png").convert_alpha()
        Reculer1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Reculer1.png").convert_alpha()        
        Menu1 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Menu.png").convert_alpha()
        Menu11 = pygame.image.load("Images/Theme/"+theme_selected+"/Soundtrack/Menu1.png").convert_alpha()
        carr_title_bar = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Carroussel/title_bar.png")
        carr_level_sun = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Carroussel/solarcharge.png")
        menu_carroussel = Carroussel(["Accueil", "Videos", "Jauge", "Audio_player", "Jeux", "Parametres", "Credits", "Messages", "Quitter"], "Images/Theme/"+theme_selected+"/Menu/Carroussel/","menu_carroussel")
        Intercomm_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Message.png").convert_alpha()
        tools_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Outils.png").convert_alpha()
        submenu_wallpapers.img = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/submenu.png").convert_alpha()
        audio_player_icon_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Audio_player.png").convert_alpha()
        yt_dlp_icon_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/yt_dlp.png").convert_alpha()
        tello_icon_min = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Tello.png").convert_alpha()
        UP_button = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/up.png").convert_alpha()
        UP_button1 = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/up1.png").convert_alpha()
        DOWN_button = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/down.png").convert_alpha()
        DOWN_button1 = pygame.image.load("Images/Theme/"+theme_selected+"/Parametres/down1.png").convert_alpha()
        Color_menu = pygame.image.load("Images/Theme/"+theme_selected+"/Menu/Color_wheel.png").convert_alpha()

    # Définition de la position des thèmes dans le sous-menu (Paramètres --> Personnalisation --> Plus de thèmes)
    def theme_panel_pos():

        x = 250
        y = 20

        for i in range(len(os.listdir("Images//Theme"))):
            globals() ["pos_theme"+str(i)] = theme0.get_rect(topleft=(x,y-scroll_theme.val))
            if x == 850:
                x = 250
                y += 200
            else:
                x += 300

    # Vérification de la sélection d'un thème (Paramètres --> Personnalisation --> Plus de thèmes)
    def theme_is_click():
        global theme_selected
        global data_base

        for i in range(len(os.listdir("Images//Theme"))):
            if eval(f'pos_theme{i}.collidepoint(event.pos)'):
                data_base.update("theme_selected",str(list_themes[i]))
                theme_init()

    # Vérification de la sélection d'une police de caractères (Paramètres --> Personnalisation --> Plus de polices)
    def font_is_click():
        global font_selected

        for i in range(len(os.listdir("Fonts"))):
            if eval(f'pos_font{i}.collidepoint(event.pos)'):
                data_base.update("font_selected","Fonts/"+list_font[i]+"/font.ttf")
                font_init()

    # Définition de la position des polices de caractères dans le sous-menu (Paramètres --> Personnalisation --> Plus de polices)
    def font_panel_pos():

        x = 250
        y = 20

        for i in range(len(os.listdir("Fonts"))):
            globals() ["pos_font"+str(i)] = Overpass.get_rect(topleft=(x,y-scroll_font.val))
            if x == 880:
                x = 250
                y += 123
            else:
                x += 210

    # Définition de la position des fonds d'écran dans le sous-menu (Paramètres --> Personnalisation --> Plus de fonds)
    def wallpapers_panel_pos():

        x = 250
        y = 20

        for i in range(len(os.listdir("Images//Wallpapers"))):
            globals() ["pos_fondmenu"+str(i)] = fondmenu0_a.get_rect(topleft=(x,y-scroll_wallpapers.val))
            if x == 880:
                x = 250
                y += 123
            else:
                x += 210

    # Vérification de la sélection d'un fond d'écran (Paramètres --> Personnalisation --> Plus de fonds)
    def wallpapers_is_click(mode=None):
        global fond_selection
        global wallpapers_use

        if mode == "delete":
            for i in range(len(os.listdir("Images//Wallpapers"))):
                if eval(f'pos_fondmenu{i}.collidepoint(submenu_wallpapers.coor)'):
                    return str(list_wallpapers[i])
            return None
        else:
            for i in range(len(os.listdir("Images//Wallpapers"))):
                if eval(f'pos_fondmenu{i}.collidepoint(event.pos)'):
                    test = str(list_wallpapers[i])
                    test = test.replace("_", "")
                    data_base.update("fond_selection",test)
                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

    # Vérification de la sélection d'une piste audio (Soundtrack)
    def soundtrack_is_click():
        global piste
        global p

        for i in range(38):
            if eval(f'pos_sound_{i}.collidepoint(event.pos)'):
                p = i
                piste = Music_player(i,True)
                audio_reader_proc.lecture()

    # Définition de la position des fonds d'écran dans le sous-menu (Paramètres --> Personnalisation --> Plus de fonds)
    def albums_panel_pos():

        x = 50
        y = 100

        for i in range(len(list_albums)):
            globals() ["pos_album"+str(i)] = audio_player_unknown_min.get_rect(topleft=(x,y-scroll_album.val))
            y += 150

    # Vérification de la sélection d'un fond d'écran (Paramètres --> Personnalisation --> Plus de fonds)
    def albums_is_click():
        global album_init_search
        global music_album_command
        global scroll_album
        global album_selection_stat
        global Audio_player_reader
        global Audio_player_album
        global audio_reader_proc
        global Audio_player_menu

        global music_selected

        for i in range(len(liste_variables_albums)):
            if eval(f'pos_album{i}.collidepoint(event.pos)'):
                if album_selection_stat == 1 or album_selection_stat == 11 or album_selection_stat == 21:
                    music_album_command = f'SELECT Path, Titre FROM Music WHERE Album="{list_albums[i][1]}" ORDER BY Piste'
                    album_init_search = True
                    album_selection_stat += 1
                    scroll_album = Scroll([1230,150],0, False)
                elif album_selection_stat == 2 or album_selection_stat == 12 or album_selection_stat == 22 or album_selection_stat == 113:
                    Audio_player_album = False
                    Audio_player_reader = True
                    scroll_album = Scroll([1230,150],0, False)
                    music_selected = list_albums[i]
                    audio_reader_proc = Music_player(i, True, list_albums)
                    audio_reader_proc.lecture()
                elif album_selection_stat == 10:
                    music_album_command = f'SELECT Path, Album FROM Music WHERE Artiste="{list_albums[i][1]}" GROUP BY Album'
                    album_init_search = True
                    album_selection_stat += 1
                    scroll_album = Scroll([1230,150],0, False)
                elif album_selection_stat == 20:
                    music_album_command = f'SELECT Path, Album FROM Music WHERE Genre="{list_albums[i][1]}" GROUP BY Album'
                    album_init_search = True
                    album_selection_stat += 1
                    scroll_album = Scroll([1230,150],0, False)

    def yt_videos_panel_pos():

        x = 50
        y = 120

        for i in range(len(playlist_list)):
            globals() ["pos_yt_videos"+str(i)] = yt_dlp_check_box.get_rect(topleft=(x,y-scroll_yt_dlp.val))
            y += 80

    def yt_videos_is_click():
        global liste_check_box
        global video_to_download

        for i in range(len(playlist_list)):
            if eval(f'pos_yt_videos{i}.collidepoint(event.pos)'):
                if liste_check_box[i] == yt_dlp_check_box1:
                    liste_check_box[i] = yt_dlp_check_box
                    video_to_download.remove(playlist_list[i][0])
                else:
                    liste_check_box[i] = yt_dlp_check_box1
                    video_to_download.append(playlist_list[i][0])

    # Téléchargement de fichiers relatifs aux mises à jour (Update_check.py, Level mise à niveau.zip)
    def Download_thread(url,name):
        global update_at_quit
        global quit_enable
        global update_web
        update_at_quit = True
        animations_Thread = Thread(target=download_animations_Thread, args=(liste_donwload_animation,))
        animations_Thread.start()
        quit_enable = False
        update_web = True
        gdown.download(url, name, quiet=True)
        update_at_quit = False
        quit_enable = True

    def yt_dlp_infos_thread(url):
        global youtube_yt_dlp
        global youtube_info
        global target
        global Youtube_min
        global search_infos_stat
        global yt_dlp_txt
        global video_to_download
        global playlist_list
        global liste_check_box
        global Youtube_loading_signal

        try:
            Youtube_loading_signal.start_signal()
            search_infos_stat = True
            yt_dlp_txt = "Chargement en cours..."
            youtube_yt_dlp = yt_dlp.YoutubeDL({"quiet" : True, "ignoreerrors" : True})
            youtube_info = youtube_yt_dlp.extract_info(url, download=False)
            try:
                youtube_info["_type"]
                target = "playlist"
                Youtube_min = None

                video_to_download = []
                playlist_list = []
                youtube_info_entries = youtube_info["entries"]
                for elem in youtube_info_entries:
                    if elem != None:
                        video_to_download.append(elem["original_url"])
                        playlist_list.append([elem["original_url"],elem["title"]])

                liste_check_box = []
                for i in range(len(playlist_list)):
                    liste_check_box.append(yt_dlp_check_box1)

            except:
                target = "video"
                r = requests.get(youtube_info["thumbnails"][-1]['url'])
                img = io.BytesIO(r.content)
                Youtube_min = pygame.image.load(img).convert_alpha()
                Youtube_min = pygame.transform.scale(Youtube_min, Image_resize_ratio(Youtube_min,(1280)))

                video_to_download = Console_url_text

            search_infos_stat = False
            yt_dlp_txt = ""

        except Exception as e:
            print(e)
            Youtube_min = None
            search_infos_stat = False
            yt_dlp_txt = langue.yt_dlp_url_error
            pygame.display.flip()
            time.sleep(1)
            
        Youtube_loading_signal.stop_signal()

    # Téléchargement de médias Youtube
    def yt_dlp_download_thread(yt, format, res):
        global yt_dlp_thread_list
        global Youtube_min
        global yt_dlp_running
        global youtube_info
        global Youtube_loading_signal
        
        Youtube_loading_signal.start_signal()

        FFmpegPostProcessor._ffmpeg_location.set(R'ffmpeg-master-latest-win64-gpl/bin/')

        if target == "playlist":
            dir = youtube_info["title"]
            dir_temp = ""
            for i in range(len(dir)):                 
                if dir[i] == '\n':
                    dir_temp += '\0 '
                elif dir[i] == '?' or ord(dir[i]) < 32 or ord(dir[i]) == 127:
                    dir_temp += ''
                elif dir[i] == '"':
                    dir_temp += '\''
                elif dir[i] == ':':
                    dir_temp += '\0 \0-'
                elif dir[i] in '\\/|*<>':
                    dir_temp += '\0_'
                    
                else:
                    dir_temp += dir[i]
            
            dir = dir_temp                
        else:
            dir = ""

        if target == "video":
            yt = [yt]

        yt_dlp_running = True

        for element in yt:
            if type_out == "video":
                type = 'best[ext=mp4]'
            else:
                type= 'bestaudio/best'

            if format == "mp4":
                options = {'windowsfilenames' : True, 'format' : type, "quiet" : True, "outtmpl" : f"Youtube\\{dir}\\%(title)s.%(ext)s", "noprogress" : True}
            elif type_out == "video":
                options = {'windowsfilenames' : True, 'format' : type, "quiet" : True, "outtmpl" : f"Youtube\\{dir}\\%(title)s.%(ext)s", "noprogress" : True,
                'postprocessors': [{'key': 'FFmpegVideoConvertor','preferedformat': format}]}
            else:
                options = {'windowsfilenames' : True, 'format' : type, "quiet" : True, "outtmpl" : f"Youtube\\{dir}\\%(title)s.%(ext)s", "noprogress" : True,
                'compat_opts' : {'filename-sanitization' : True},'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': format, "preferredquality" : res}]}

            youtube_yt_dlp = yt_dlp.YoutubeDL(options)
            youtube_info = youtube_yt_dlp.extract_info(element)

            r = requests.get(youtube_info["thumbnails"][-1]['url'])
            img = io.BytesIO(r.content)
            Youtube_min_temp = pygame.image.load(img).convert_alpha()
            Youtube_min_temp = pygame.transform.scale(Youtube_min_temp, Image_resize_ratio(Youtube_min_temp,(1280)))
            Youtube_min = Youtube_min_temp

            try :
                title = youtube_info["title"]
                title_temp = ""
                for i in range(len(title)):                 
                    if title[i] == '\n':
                        title_temp += '\0 '
                    elif title[i] == '?' or ord(title[i]) < 32 or ord(title[i]) == 127:
                        title_temp += ''
                    elif title[i] == '"':
                        title_temp += '\''
                    elif title[i] == ':':
                        title_temp += ' -'
                    elif title[i] in '\\/|*<>':
                        title_temp += '_'
                        
                    else:
                        title_temp += title[i]
                
                title = str(title_temp)

                # chemin de sortie
                youtube_yt_dlp.download(element)
                
                if (yt_set_album_playlist and target == "playlist") or yt_set_title or yt_set_artist:
                    if "—" in title:
                        title_temp = title.replace("—","")
                        os.rename(f"Youtube\\{dir}\\{title}.{format}",f"Youtube\\{title_temp}.{format}")
                        title = title_temp
                    
                    yt_elem_to_set = music_tag.load_file(f"Youtube\\{dir}\\{title}.{format}")
                    
                    if (yt_set_album_playlist and target == "playlist"):
                        yt_elem_to_set["album"] = dir
                        
                    if yt_set_title:
                        yt_elem_to_set["title"] = youtube_info["title"]
                        
                    if yt_set_artist:
                        yt_elem_to_set["artist"] = youtube_info["channel"]
                        
                    yt_elem_to_set.save()

            except Exception as e:
                print(e)
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                fichier=open("log.txt","a")
                if os.stat("log.txt").st_size == 0:
                    fichier.write("________  __     __  __      ___     ________      _____      __  __" + "\n")
                    fichier.write("| |     \ | |\   | | | |    /___/    | |     \    / ___ \     \ \/ /." + "\n")
                    fichier.write("| |     | | | \  | | | |             | |     |   / /   \ \     \ \/.  " + "\n")
                    fichier.write("| |_____/ | |\ \ | | | |             | |_____/  / /     \ \     \ \. " + "\n")
                    fichier.write("| |     \ | | \ \| | | |             | |     \  \ \     / /    / \ \." + "\n")
                    fichier.write("| |     | | |  \   | | |____         | |     |   \ \___/ /    / / \ \." + "\n")
                    fichier.write("|_|_____/ |_|   \__| |______|        |_|_____/    \_____/    /_/   \_\." + "\n")
                    fichier.write("\n")    
                fichier.write(str(dt_string) +"\n")
                fichier.write(str(e)+"\n")
                fichier.write("Url donnee : "+ str(element) +"\n")
                fichier.write("Attributs (MP3/MP4) (LD/HD) : format -> "+ str(format) + " qualité -> " + str(res) +"\n")
                fichier.write(f"Ligne : {str(sys.exc_info()[-1].tb_lineno)}" + "\n")
                try:
                    fichier.write(f"Type d'erreur : {str(type(e).__name__)}" + "\n")
                except:
                    None
                fichier.write("\n")
                fichier.close()

            yt_dlp_thread_list -= 1
            yt_dlp_running = False
            
        Youtube_loading_signal.stop_signal()

    # Réception d'éventuels messages de BNL's Intercomm (utilisé avec un Thread)
    def Intercomm_recv_thread():
        global serv_mess
        global client_mess
        global mail_box_mess
        global mail_box_init
        global socket_server
        global conn
        global comm_running
        global mess_list

        while comm_running:
            try :
                if mail_box_stat == "client":
                    serv_mess_temp = (socket_server.recv(4096**2)).decode()
                    if compatibility_mode == 1:
                        serv_mess_temp = client_crypt.decode_general(serv_mess_temp)
                    else:
                        serv_mess_temp = client_crypt.decode(serv_mess_temp)

                    if serv_mess_temp[0] == "t":
                        serv_mess = serv_mess_temp
                        mess_list.insert(0,server_name + " : " + serv_mess_temp[1:])
                    elif serv_mess_temp[0] == "&":
                        intercomm_transfer(serv_mess_temp[1:])

                else:
                    client_mess_temp = (conn.recv(4096**2)).decode()
                    if compatibility_mode == 1:
                        client_mess_temp = server_crypt.decode_general(client_mess_temp)
                    else:
                        client_mess_temp = server_crypt.decode(client_mess_temp)
                    if client_mess_temp[0] == "t":
                        client_mess = client_mess_temp
                        mess_list.insert(0, client + " : " + client_mess_temp[1:])
                    elif client_mess_temp[0] == "&":
                        intercomm_transfer(client_mess_temp[1:])

            except Exception as e:
                print(e)
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                fichier=open("log.txt","a")
                if os.stat("log.txt").st_size == 0:
                    fichier.write("________  __     __  __      ___     ________      _____      __  __" + "\n")
                    fichier.write("| |     \ | |\   | | | |    /___/    | |     \    / ___ \     \ \/ /." + "\n")
                    fichier.write("| |     | | | \  | | | |             | |     |   / /   \ \     \ \/.  " + "\n")
                    fichier.write("| |_____/ | |\ \ | | | |             | |_____/  / /     \ \     \ \. " + "\n")
                    fichier.write("| |     \ | | \ \| | | |             | |     \  \ \     / /    / \ \." + "\n")
                    fichier.write("| |     | | |  \   | | |____         | |     |   \ \___/ /    / / \ \." + "\n")
                    fichier.write("|_|_____/ |_|   \__| |______|        |_|_____/    \_____/    /_/   \_\." + "\n")
                    fichier.write("\n")    
                fichier.write(str(dt_string) +"\n")
                fichier.write(f"Erreur detectee : {str(e)}" + "\n")
                fichier.write(f"Ligne : {str(sys.exc_info()[-1].tb_lineno)}" + "\n")
                fichier.write(f"Type d'erreur : {str(type(e).__name__)}" + "\n")
                fichier.write("Localisation : BNL's Intercomm, phase de communication"+ "\n")
                fichier.write("\n")
                fichier.close()
                mail_box_mess = False
                mail_box_init = True
                comm_running = False
                if mail_box_stat == "client":
                    socket_server.shutdown(socket.SHUT_RDWR)
                    socket_server.close()
                else:
                    conn.shutdown(socket.SHUT_RDWR)
                    conn.close()

                return

    # Fonction allouée à l'arrondi de la miniature pour fond d'écran
    def add_corners(im, rad): # from : https://stackoverflow.com/questions/11287402/how-to-round-corner-a-logo-without-white-backgroundtransparent-on-it-using-pi
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im

    # Animation d'ouverture du titre de l'onglet (en haut, au centre, composé d'un titre, du sélecteur de Titanium-Widgets, et d'une miniature)
    def onglets_fermeture(text,icon,visibility=False):
        if transition_check:
            for i in range(35):
                if visibility:
                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                fenetre.blit(text, (500,20-i*2))
                fenetre.blit(icon,(755,0-i*2))
                fenetre.blit(Selection_menu,(455,0-i*2))
                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))
                pygame.display.flip()
            if visibility and not(Blur_background):
                for i in range(128):

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité,(0-i*10,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))
                    pygame.display.flip()

    # Animation de fermeture du titre de l'onglet (en haut, au centre, composé d'un titre, du sélecteur de Titanium-Widgets, et d'une miniature)
    def onglets_ouverture(text,icon,visibility=False):
        if transition_check:
            if visibility and not(Blur_background):
                for i in range(128):
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité,(-1280+i*10,0))
                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))
                    pygame.display.flip()
            for i in range(35):
                if visibility and not(Blur_background):
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                fenetre.blit(text, (500,-50+i*2))
                fenetre.blit(icon,(755,-70+i*2))
                fenetre.blit(Selection_menu,(455,-70+i*2))
                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))
                pygame.display.flip()

    # Transfert de fichiers via BNL's Intercomm
    def intercomm_transfer(name):
        global intercomm_transfer_stat
        global my_mess_temp
        BUFFER_SIZE = 4096**2
        my_mess_temp = langue.intercomm_receive_txt + name
        if "Received_files" in name:
            os.makedirs("Received_files",exist_ok=True)
        if mail_box_stat == "client":
            with open(name, "wb") as file:
                while True:
                    serv_mess_temp = (socket_server.recv(BUFFER_SIZE))
                    bytes_read = base64.b64decode((serv_mess_temp))
                    print(bytes_read)
                    if not(bytes_read) or bytes_read == bytes("END_file",'utf-8'):
                        break
                    try:
                        data += bytes_read
                    except:
                        data = bytes_read
                file.write(data)
        else:
            with open(name, "wb") as file:
                while True:
                    client_mess_temp = (conn.recv(BUFFER_SIZE))
                    bytes_read = base64.b64decode((client_mess_temp))
                    print(bytes_read)
                    if not(bytes_read) or bytes_read == bytes("END_file",'utf-8'):
                        break
                    try:
                        data += bytes_read
                    except:
                        data = bytes_read
                file.write(data)

        intercomm_transfer_stat = 0
        my_mess_temp = ""

    # Timer (peut être utilisé avec un Thread, pour éteindre, déconnecter ou rédémarrer l'ordinateur)
    def system_timer(timer, after):
        try:
            time.sleep(timer)
            if after == "shutdown":
                return os.system("shutdown /s /t 1")
            if after == "restart":
                return os.system("shutdown /r /t 1")
            if after == "logout":
                return os.system("shutdown -l")
        except Exception as e:
            print(e)

    # Animation du témoin de téléchargement
    def download_animations_Thread(liste):
        global download_stat_downloading
        i = 0
        while update_at_quit:
            download_stat_downloading = liste[i]
            time.sleep(0.5)
            i += 1
            if i == len(liste):
                i = 0

    # Redimensionnement d'une image en fonction d'une longueur donnée
    def Image_resize_ratio(img, size):
        img_ratio = img.get_rect()[2:4]
        img_ratio_temp = img_ratio[0] / size

        n_size = img_ratio[0] / img_ratio_temp
        n_size2 = img_ratio[1] / img_ratio_temp

        return (int(n_size), int(n_size2))

    def fond_menu_create(path, ext=""):
        if ext != "":
            path_copy = ""
            ext_copy = ""
            for elem in (os.getcwd()+"/"+path):
                if elem == chr(92):
                    path_copy += "/"
                else:
                    path_copy += elem
            for elem in (ext):
                if elem == chr(92):
                    ext_copy += "/"
                else:
                    ext_copy += elem
            os.makedirs(path_copy)
            shutil.copy2(ext_copy, path_copy+"/fondmenu.png")

        im = Image.open(path+"/fondmenu.png").convert("RGB")
        im_def = im.resize((1280,720))
        im_def.save(path+"/fondmenu.png")
        im = Image.open(path+"/fondmenu.png").convert("RGB")
        largeur = im.size[0]
        hauteur = im.size[1]

        im_left_txt = Image.new("RGB", (379, hauteur))
        for lig in range(hauteur):
            for col in range(379):
                (r,g,b) = im.getpixel((col,lig))
                im_left_txt.putpixel((col,lig), (r,g,b))

        im_left_txt.save(path+"/Gauche_txt.png")

        im_left = Image.new("RGB", (largeur//2, hauteur))
        for lig in range(hauteur):
            for col in range(largeur//2):
                (r,g,b) = im.getpixel((col,lig))
                im_left.putpixel((col,lig), (r,g,b))

        im_left.save(path+"/Gauche.png")

        im_min_temp = add_corners(im, 100)

        im_mini = im_min_temp.resize((200,112))
        im_mini.save(path+"/wallpapers_view.png")
        
        im = Image.open(path+"/fondmenu.png").convert("RGB")

        im_right = Image.new("RGB", (largeur//2, hauteur))
        for lig in range(hauteur):
            for col in range(largeur//2,largeur):
                (r,g,b) = im.getpixel((col,lig))
                im_right.putpixel((col-largeur//2,lig), (r,g,b))

        im_right.save(path+"/Droite.png")

        time.sleep(0.5)

        globals() ["fondmenu"+ str(i)] = pygame.image.load(path+"/wallpapers_view.png").convert_alpha()
        
    def wallpapers_search():
        global list_wallpapers
        global liste_variables_wallpapers
        global wallpapers_init_search
            
        list_wallpapers = os.listdir("Images//Wallpapers")

        liste_variables_wallpapers = []

        for i in range(len(list_wallpapers)):
            try:
                globals() ["fondmenu"+ str(i)] = pygame.image.load("Images/Wallpapers/"+list_wallpapers[i]+"/wallpapers_view.png").convert_alpha()
            except:

                list_wallpapers[i] = list_wallpapers[i].replace("_","")
                list_wallpapers[i] = list_wallpapers[i].replace("'","")

                fond_menu_create("Images/Wallpapers/"+list_wallpapers[i])
                
        for i in range(len(list_wallpapers)):
            liste_variables_wallpapers.append(globals() ["fondmenu"+str(i)])
            
        wallpapers_init_search = False
        
    def create_wallpapers_from_img():
        
        global wallpapers_init_search
        global creating_sectionned_wallpapers
        
        filename_fond = str(path.split("\\")[-1])
        filename_fond = filename_fond.split(".")
        filename_fond[0] = filename_fond[0].replace("_","")
        filename_fond[0] = filename_fond[0].replace("'","")
        try:
            fond_menu_create("Images/Wallpapers/"+filename_fond[0], path)
        except FileExistsError:
            shutil.rmtree("Images//Wallpapers//"+filename_fond[0])
            fond_menu_create("Images/Wallpapers/"+filename_fond[0], path)

        wallpapers_init_search = True
        creating_sectionned_wallpapers = False

    def music_data_update(dir, table, stat=""):
        global mdb_progress
        global music_update_txt
        global Audio_player_database_update_proc
        mdb_progress = 0
        music_update_txt = ""
        liste = []
        if stat == "":
            music_data.delete(f"DELETE FROM {table}","")
        liste_ext = [".mp3", ".acc", ".aiff", ".dsf", ".flac", ".m4a", ".ogg", ".opus", ".wav", ".wv"]

        music_update_txt = "Recherche des fichiers en cours..."
        
        music_progress_temp = Thread(target=music_data_update_progress_temp, args=())
        music_progress_temp.start()

        for path, subdirs, files in os.walk(dir):
            for name in files:
                for e in liste_ext:
                    if e in os.path.join(path, name):
                        liste.append(os.path.join(path, name))
                        
        time.sleep(1)

        mdb_progress = 0
        mdb_progress_coeff = 1252/len(liste)

        music_update_txt = "Ajout à la base de données..."

        for elem in liste:
            try:
                music = music_tag.load_file(elem)
                test = [str(music['title']),str(music['artist']),str(music['album']),str(music['year']),str(music['tracknumber']),str(music['genre']),str(music['albumartist']),str(music['composer']),elem]
                test = tuple(test)
                music_data.add(f"INSERT INTO {table} (Titre, Artiste, Album, Annee, Piste, Genre, Interprete, Compositeur, Path) VALUES ",test)

            except Exception as e:
                print(e, elem)

            mdb_progress += mdb_progress_coeff

        mdb_progress = 1252
        music_update_txt = "Mise à jour effectuée..."

        time.sleep(2)

        Audio_player_database_update_proc = False
        
    def music_data_update_progress_temp():
        global mdb_progress
        
        mdb_progress = 0
        while music_update_txt == "Recherche des fichiers en cours..." :
            if mdb_progress < 1252:
                mdb_progress += 4
            else:
                mdb_progress = 0
            time.sleep(0.000001)
        
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    """Début du programme : ensemble de boucle WHILE vérifiées ou non selon les actions de l'utilisateur."""
    
    for event in pygame.event.get():
        None
    étape_programme = "Entrée dans la boucle principale"
    p=0
    lecture=True
    titre=""
    temps=0
    avance=0
    end = False
    Update_at_start_check = True
    piste = Music_player(0,True, music_data.get("SELECT Path, Titre FROM Soundtrack"))
    scroll_first_start = Scroll([1230,150],0, False)
    scroll_changelog = Scroll([1230,150],0, False)
    scroll_bar_decalage = [0,0]
    tello_sys = Tello_system()
    tello_active = False
    # Boucle principale
    while continuer:
        # Affectation de variables
        videos_carroussel.selection = 0
        volume_control_transition_stat = 1
        carr_title_bar_transition_stat = 1
        carr_title_bar_stat = "disable"

        texte_accueil = font.render(langue.title_home, 1, color_menu)
        texte_vidéos = font.render(langue.title_videos, 1, color_menu)
        texte_jauge = font.render(langue.title_level, 1, color_menu)
        texte_audio_player = font.render(langue.title_audio_player, 1, color_menu)
        texte_jeux = font.render(langue.title_games, 1, color_menu)
        texte_paramètres = font.render(langue.title_parameters, 1, color_menu)
        texte_credits = font.render(langue.title_credits, 1, color_menu)
        texte_quitter = font.render(langue.title_quit, 1, color_menu)
        texte_intercomm = font.render(langue.title_intercomm, 1, color_menu)
        texte_tools = font.render(langue.title_tools, 1, color_menu)
        texte_changelog_version = font.render("BNL's Box "+str(Version_Menu), 1, color_menu)
        texte_color = font.render("Couleurs", 1, color_menu)

        pygame.mixer.music.set_volume(volume_BNL/10)

        # Changelog (affiché si la variable "First_start" est égale à 1 : valable lors des premiers démarrages ou mises à jour)
        while First_start == 1:

            étape_programme = "Changelog / First start"

            if Blur_background:
                fenetre.blit(wallpapers_use.blur, (0,0))
            else:
                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(fond_visibilité, (0,0))
            fenetre.blit(Selection_menu,(455,0))
            fenetre.blit(texte_changelog_version, (530, 20))
            fenetre.blit(changelog_logo,(755,4))

            texte = font_popup.render(chlog_t0, 5, (255,255,255))
            fenetre.blit(texte, (100, 150-scroll_first_start.val))
            texte = font_popup.render(chlog_t1, 5, (255,255,255))
            fenetre.blit(texte, (100, 200-scroll_first_start.val))
            texte = font_popup.render(chlog_t2, 5, (255,255,255))
            fenetre.blit(texte, (100, 250-scroll_first_start.val))
            texte = font_popup.render(chlog_t3, 5, (255,255,255))
            fenetre.blit(texte, (100, 300-scroll_first_start.val))
            texte = font_popup.render(chlog_t4, 5, (255,255,255))
            fenetre.blit(texte, (100, 350-scroll_first_start.val))
            texte = font_popup.render(chlog_t5, 5, (255,255,255))
            fenetre.blit(texte, (100, 400-scroll_first_start.val))
            texte = font_popup.render(chlog_t6, 5, (255,255,255))
            fenetre.blit(texte, (100, 450-scroll_first_start.val))
            texte = font_popup.render(chlog_t7, 5, (255,255,255))
            fenetre.blit(texte, (100, 500-scroll_first_start.val))
            texte = font_popup.render(chlog_t8, 5, (255,255,255))
            fenetre.blit(texte, (100, 550-scroll_first_start.val))
            texte = font_popup.render(chlog_t9, 5, (255,255,255))
            fenetre.blit(texte, (100, 600-scroll_first_start.val))
            texte = font_popup.render(chlog_t10, 5, (255,255,255))
            fenetre.blit(texte, (100, 650-scroll_first_start.val))

            texte = font_popup.render(chlog_t11, 5, (255,255,255))
            fenetre.blit(texte, (100, 700-scroll_first_start.val))
            texte = font_popup.render(chlog_t12, 5, (255,255,255))
            fenetre.blit(texte, (100, 750-scroll_first_start.val))
            texte = font_popup.render(chlog_t13, 5, (255,255,255))
            fenetre.blit(texte, (100, 800-scroll_first_start.val))
            texte = font_popup.render(chlog_t14, 5, (255,255,255))
            fenetre.blit(texte, (100, 850-scroll_first_start.val))
            texte = font_popup.render(chlog_t15, 5, (255,255,255))
            fenetre.blit(texte, (100, 900-scroll_first_start.val))
            texte = font_popup.render(chlog_t16, 5, (255,255,255))
            fenetre.blit(texte, (100, 950-scroll_first_start.val))
            texte = font_popup.render(chlog_t17, 5, (255,255,255))
            fenetre.blit(texte, (100, 1000-scroll_first_start.val))
            texte = font_popup.render(chlog_t18, 5, (255,255,255))
            fenetre.blit(texte, (100, 1050-scroll_first_start.val))
            texte = font_popup.render(chlog_t19, 5, (255,255,255))
            fenetre.blit(texte, (100, 1100-scroll_first_start.val))
            texte = font_popup.render(chlog_t20, 5, (255,255,255))
            fenetre.blit(texte, (100, 1150-scroll_first_start.val))
            
            texte = font_popup.render(chlog_t21, 5, (255,255,255))
            fenetre.blit(texte, (100, 1200-scroll_first_start.val))
            texte = font_popup.render(chlog_t22, 5, (255,255,255))
            fenetre.blit(texte, (100, 1250-scroll_first_start.val))
            texte = font_popup.render(chlog_t23, 5, (255,255,255))
            fenetre.blit(texte, (100, 1300-scroll_first_start.val))
            texte = font_popup.render(chlog_t24, 5, (255,255,255))
            fenetre.blit(texte, (100, 1350-scroll_first_start.val))
            texte = font_popup.render(chlog_t25, 5, (255,255,255))
            fenetre.blit(texte, (100, 1400-scroll_first_start.val))
            texte = font_popup.render(chlog_t26, 5, (255,255,255))
            fenetre.blit(texte, (100, 1450-scroll_first_start.val))
            texte = font_popup.render(chlog_t27, 5, (255,255,255))
            fenetre.blit(texte, (100, 1500-scroll_first_start.val))
            texte = font_popup.render(chlog_t28, 5, (255,255,255))
            fenetre.blit(texte, (100, 1550-scroll_first_start.val))
            texte = font_popup.render(chlog_t29, 5, (255,255,255))
            fenetre.blit(texte, (100, 1600-scroll_first_start.val))
            texte = font_popup.render(chlog_t30, 5, (255,255,255))
            fenetre.blit(texte, (100, 1650-scroll_first_start.val))

            texte = font_popup.render(chlog_t31, 5, (255,255,255))
            fenetre.blit(texte, (100, 1700-scroll_first_start.val))
            texte = font_popup.render(chlog_t32, 5, (255,255,255))
            fenetre.blit(texte, (100, 1750-scroll_first_start.val))
            texte = font_popup.render(chlog_t33, 5, (255,255,255))
            fenetre.blit(texte, (100, 1800-scroll_first_start.val))
            texte = font_popup.render(chlog_t34, 5, (255,255,255))
            fenetre.blit(texte, (100, 1850-scroll_first_start.val))
            texte = font_popup.render(chlog_t35, 5, (255,255,255))
            fenetre.blit(texte, (100, 1900-scroll_first_start.val))
            texte = font_popup.render(chlog_t36, 5, (255,255,255))
            fenetre.blit(texte, (100, 1950-scroll_first_start.val))
            texte = font_popup.render(chlog_t37, 5, (255,255,255))
            fenetre.blit(texte, (100, 2000-scroll_first_start.val))
            texte = font_popup.render(chlog_t38, 5, (255,255,255))
            fenetre.blit(texte, (100, 2050-scroll_first_start.val))
            texte = font_popup.render(chlog_t39, 5, (255,255,255))
            fenetre.blit(texte, (100, 2100-scroll_first_start.val))
            texte = font_popup.render(chlog_t40, 5, (255,255,255))
            fenetre.blit(texte, (100, 2150-scroll_first_start.val))

            a,b= pygame.mouse.get_pos ( )
            mouse_stat = pygame.mouse.get_pressed()

            if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_first_start.pos.collidepoint(pygame.mouse.get_pos()):
                if scroll_first_start.coor[1] < b-scroll_bar_decalage[1]:
                    scroll_first_start.val -= (scroll_first_start.coor[1] - (b-scroll_bar_decalage[1]))*4
                elif scroll_first_start.coor[1] > b-scroll_bar_decalage[1]:
                    scroll_first_start.val += -(scroll_first_start.coor[1] - (b-scroll_bar_decalage[1]))*4
                scroll_first_start.coor[1] = b-scroll_bar_decalage[1]
                scroll_first_start.pos = scroll_bar.get_rect(topleft=scroll_first_start.coor)

            fenetre.blit(scroll_bar,scroll_first_start.coor)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_stat = pygame.mouse.get_pressed()
                    if mouse_stat[0]:
                        if scroll_first_start.pos.collidepoint(event.pos):
                            scroll_bar_decalage = [a-scroll_first_start.coor[0],b-scroll_first_start.coor[1]]
                        else:
                            data_base.update("First_start","0")
                            changelog("out","BNL's Box "+str(Version_Menu))
                            if not(Update_at_start):
                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    menu_carroussel.open()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        data_base.update("First_start","0")
                        changelog("out","BNL's Box "+str(Version_Menu))
                        if not(Update_at_start):
                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                menu_carroussel.open()

                if event.type == pygame.MOUSEWHEEL:
                    scroll_first_start.stat = False
                    a = 0
                    b = event.y
                    scroll_bar_decalage = [0,0]

                    if scroll_first_start.coor[1]-b*10 >= 150 and scroll_first_start.coor[1]-b*10 <= 550 :
                        scroll_first_start.val -= b*40
                        scroll_first_start.coor[1] -= b*10
                        scroll_first_start.pos = scroll_bar.get_rect(topleft=scroll_first_start.coor)

                if event.type == QUIT:
                    STOP()

        # Affichage du changelog en cas de disponibilité d'une mise à jour
        if Update_at_start_check and Update_at_start:
            try:
                if Update_check_web:
                    selection_update = True
                    fenetre.blit(download_stat_tem,(475,310))
                    pygame.display.flip()
                    url = "https://drive.google.com/u/1/uc?id=1663LepTTo2f1tb74OMcYscCp7IGf2WCW&export=download"
                    output = "Update_check.py"
                    gdown.download(url, output, quiet=True)

                    url = "https://drive.google.com/u/1/uc?id=1rzJZoe_jGXbFpCTFsWJmuNWRmNOty0sr&export=download"
                    output = "Changelog_txt_up.py"
                    gdown.download(url, output, quiet=True)
                else:
                    with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                        selection_update = True
                        zipObj.extract("Update_check.py")
                        zipObj.extract("Changelog_txt_up.py")

                if True:

                    importlib.reload(Update_check)
                    importlib.reload(Changelog_txt_up)

                    from Update_check import*
                    from Changelog_txt_up import*

                    if Update_Menu == Version_Menu and Update_Update == Version_Update and Update_Level == Version_Level and Update_Intercomm == Version_Intercomm:
                        Update_at_start_check = False
                        if Skin_selected == "Titanium":
                            ouverture_titre(200,1,0)
                        elif Skin_selected == "Carroussel":
                            menu_carroussel.open()

                    else:
                        changelog("entry","BNL's Box "+str(Update_Menu))
                        selection_update = True

                        while selection_update:

                            étape_programme = "Changelog / Update"

                            if Blur_background:
                                fenetre.blit(wallpapers_use.blur, (0,0))
                            else:
                                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                                fenetre.blit(fond_visibilité, (0,0))
                            fenetre.blit(Selection_menu,(455,0))
                            fenetre.blit(font.render("BNL's Box "+str(Update_Menu), 1, color_menu), (530, 20))
                            fenetre.blit(changelog_logo,(755,4))

                            fenetre.blit(bouton_Python, (500,650))
                            fenetre.blit(bouton_Abord, (700,650))

                            texte = font.render("Mise à jour disponible :", 5, (255,255,255))
                            fenetre.blit(texte, (100, 100-scroll_changelog.val))
                            texte = font_popup.render("BNL's Box : " + str(Version_Menu) + "  ->  " + str(Update_Menu), 5, (255,255,255))
                            fenetre.blit(texte, (100, 150-scroll_changelog.val))
                            texte = font_popup.render("BNL's Level : " + str(Version_Level) + "  ->  " + str(Update_Level), 5, (255,255,255))
                            fenetre.blit(texte, (100, 200-scroll_changelog.val))
                            texte = font_popup.render("BNL's Update Utility : " + str(Version_Update) + "  ->  " + str(Update_Update), 5, (255,255,255))
                            fenetre.blit(texte, (100, 250-scroll_changelog.val))
                            texte = font_popup.render("BNL's Intercomm : " + str(Version_Intercomm) + "  ->  " + str(Update_Intercomm), 5, (255,255,255))
                            fenetre.blit(texte, (100, 300-scroll_changelog.val))

                            texte = font_popup.render(chlog_t0, 5, (255,255,255))
                            fenetre.blit(texte, (100, 350-scroll_changelog.val))
                            texte = font_popup.render(chlog_t1, 5, (255,255,255))
                            fenetre.blit(texte, (100, 400-scroll_changelog.val))
                            texte = font_popup.render(chlog_t2, 5, (255,255,255))
                            fenetre.blit(texte, (100, 450-scroll_changelog.val))
                            texte = font_popup.render(chlog_t3, 5, (255,255,255))
                            fenetre.blit(texte, (100, 500-scroll_changelog.val))
                            texte = font_popup.render(chlog_t4, 5, (255,255,255))
                            fenetre.blit(texte, (100, 550-scroll_changelog.val))
                            texte = font_popup.render(chlog_t5, 5, (255,255,255))
                            fenetre.blit(texte, (100, 600-scroll_changelog.val))
                            texte = font_popup.render(chlog_t6, 5, (255,255,255))
                            fenetre.blit(texte, (100, 650-scroll_changelog.val))
                            texte = font_popup.render(chlog_t7, 5, (255,255,255))
                            fenetre.blit(texte, (100, 700-scroll_changelog.val))
                            texte = font_popup.render(chlog_t8, 5, (255,255,255))
                            fenetre.blit(texte, (100, 750-scroll_changelog.val))
                            texte = font_popup.render(chlog_t9, 5, (255,255,255))
                            fenetre.blit(texte, (100, 800-scroll_changelog.val))
                            texte = font_popup.render(chlog_t10, 5, (255,255,255))
                            fenetre.blit(texte, (100, 850-scroll_changelog.val))

                            texte = font_popup.render(chlog_t11, 5, (255,255,255))
                            fenetre.blit(texte, (100, 900-scroll_changelog.val))
                            texte = font_popup.render(chlog_t12, 5, (255,255,255))
                            fenetre.blit(texte, (100, 950-scroll_changelog.val))
                            texte = font_popup.render(chlog_t13, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1000-scroll_changelog.val))
                            texte = font_popup.render(chlog_t14, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1050-scroll_changelog.val))
                            texte = font_popup.render(chlog_t15, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1100-scroll_changelog.val))
                            texte = font_popup.render(chlog_t16, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1150-scroll_changelog.val))
                            texte = font_popup.render(chlog_t17, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1200-scroll_changelog.val))
                            texte = font_popup.render(chlog_t18, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1250-scroll_changelog.val))
                            texte = font_popup.render(chlog_t19, 5, (255,255,255))
                            fenetre.blit(texte, (100, 1300-scroll_changelog.val))
                            texte = font_popup.render(chlog_t20, 5, (255,255,255))

                            a,b= pygame.mouse.get_pos ( )
                            mouse_stat = pygame.mouse.get_pressed()

                            if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_changelog.pos.collidepoint(pygame.mouse.get_pos()):
                                if scroll_changelog.coor[1] < b-scroll_bar_decalage[1]:
                                    scroll_changelog.val -= (scroll_changelog.coor[1] - (b-scroll_bar_decalage[1]))*4
                                elif scroll_changelog.coor[1] > b-scroll_bar_decalage[1]:
                                    scroll_changelog.val += -(scroll_changelog.coor[1] - (b-scroll_bar_decalage[1]))*4
                                scroll_changelog.coor[1] = b-scroll_bar_decalage[1]
                                scroll_changelog.pos = scroll_bar.get_rect(topleft=scroll_changelog.coor)

                            fenetre.blit(scroll_bar,scroll_changelog.coor)

                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_stat = pygame.mouse.get_pressed()
                                    if mouse_stat[0]:
                                        if pos_bouton_Python.collidepoint(event.pos):
                                            if Update_check_web:
                                                download_thread = Thread(target=Download_thread, args=("https://drive.google.com/u/1/uc?id="+update_file_link+"&export=download","Level mise à niveau.zip"))
                                                download_thread.start()
                                                changelog("out","BNL's Box "+str(Update_Menu))
                                                selection_update = False
                                                Update_at_start_check = False
                                                if Skin_selected == "Titanium":
                                                    menu_continuer=True
                                                    ouverture_titre(200,2,0)
                                                elif Skin_selected == "Carroussel":
                                                    Menu_skin2 = True
                                                    menu_carroussel.open()
                                            else:
                                                continuer=False
                                                selection_update = False
                                                STOP("Update.bat")
                                        if pos_bouton_Abord.collidepoint(event.pos):
                                            changelog("out","BNL's Box "+str(Update_Menu))
                                            selection_update = False
                                            Update_at_start_check = False
                                            if Skin_selected == "Titanium":
                                                menu_continuer=True
                                                ouverture_titre(200,2,0)
                                            elif Skin_selected == "Carroussel":
                                                Menu_skin2 = True
                                                menu_carroussel.open()
                                        if scroll_changelog.pos.collidepoint(event.pos):
                                            scroll_bar_decalage = [a-scroll_changelog.coor[0],b-scroll_changelog.coor[1]]

                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE :
                                        changelog("out","BNL's Box "+str(Update_Menu))
                                        selection_update = False
                                        Update_at_start_check = False
                                        if Skin_selected == "Titanium":
                                            menu_continuer=True
                                            ouverture_titre(200,2,0)
                                        elif Skin_selected == "Carroussel":
                                            Menu_skin2 = True
                                            menu_carroussel.open()

                                if event.type == pygame.MOUSEWHEEL:
                                    scroll_changelog.stat = False
                                    a = 0
                                    b = event.y
                                    scroll_bar_decalage = [0,0]

                                    if scroll_changelog.coor[1]-b*10 >= 150 and scroll_changelog.coor[1]-b*10 <= 550 :
                                        scroll_changelog.val -= b*40
                                        scroll_changelog.coor[1] -= b*10
                                        scroll_changelog.pos = scroll_bar.get_rect(topleft=scroll_changelog.coor)

                                if event.type == QUIT:
                                    STOP()

            except:
                None

        # Menu principal (Titanium and widgets skin)
        while menu_continuer:
            étape_programme = "Menu Titanium-Widgets"

            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            fenetre.blit(wallpapers_use.wallpaper, (0,0))

            if widget_soundtrack:
                fenetre.blit(widget_soundtrack_skin,(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))
                texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                fenetre.blit(texte, (widget_soundtrack_coor[0]+15, widget_soundtrack_coor[1]+33))
                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_pause,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                fenetre.blit(widget_soundtrack_reculer,(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))
                fenetre.blit(widget_soundtrack_avancer,(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                fenetre.blit(Curseur, (widget_soundtrack_coor[0]+9+avance, widget_soundtrack_coor[1]+103))

                fenetre.blit(audio_reader_proc.min,(widget_soundtrack_coor[0]+240,widget_soundtrack_coor[1]+70))

            if widget_level:
                fenetre.blit(widget_level_skin,(widget_level_coor[0],widget_level_coor[1]))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,0,0)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        afficher_batons(n,0,0)

                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(widget_level_coor[0]+125, widget_level_coor[1]+280, 150, 30))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (widget_level_coor[0]+150, widget_level_coor[1]+285))

                except:
                    texte = font.render("ERROR", 1, (255,0,0))
                    fenetre.blit(texte, (widget_level_coor[0]+155,widget_level_coor[1]+155))

            if widget_signet :
                fenetre.blit(widget_barre,(1180,0))
                fenetre.blit(widget_signet_open,(1152,500))
                if not(widget_soundtrack) :
                    fenetre.blit(widget_soundtrack_miniature,(1190,50))
                if not(widget_level):
                    fenetre.blit(widget_level_miniature,(1190,130))
            else :
                fenetre.blit(widget_signet_close,(1252,500))

            fenetre.blit(Selection_menu,(0,position_selecteur))

            fenetre.blit(texte_accueil, (20, 20))

            fenetre.blit(texte_vidéos, (20, 90))

            fenetre.blit(texte_jauge, (20, 160))

            fenetre.blit(texte_audio_player, (20, 230))

            fenetre.blit(texte_jeux, (20, 300))

            fenetre.blit(texte_paramètres, (20, 370))

            fenetre.blit(texte_credits, (20, 440))

            fenetre.blit(texte_intercomm, (20, 510))

            fenetre.blit(texte_tools, (20, 580))

            fenetre.blit(texte_quitter, (20, 650))

            if update_at_quit:
                fenetre.blit(download_stat_downloading,(400,5))

            if position_selecteur == 70:
                fenetre.blit(Bonus,(300,70))
            if position_selecteur == 140:
                fenetre.blit(Solar,(291,140))
            if position_selecteur == 210:
                fenetre.blit(audio_player_icon_min,(291,210))
            if position_selecteur == 280:
                fenetre.blit(Autopilot_menu,(300,280))
            if position_selecteur == 350:
                fenetre.blit(BNLmenu,(291,350))
            if position_selecteur == 420:
                fenetre.blit(Lounge_menu,(300,420))
            if position_selecteur == 490:
                fenetre.blit(Intercomm_menu,(300,490))
            if position_selecteur == 560:
                fenetre.blit(tools_min,(300,560))
            if position_selecteur == 630:
                fenetre.blit(MO_menu,(300,630))

            pygame.display.flip()
            r=0
            a,b= pygame.mouse.get_pos ( )

            if widget_soundtrack :

                a_string=pygame.mixer.music.get_pos()/1000
                float_str = float(a_string)
                test= int(float_str)
                pygame.display.flip()

                temps = 200/audio_reader_proc.time
                if pygame.mixer.music.get_busy():
                    avance=temps*test
                pygame.display.flip()

            for event in pygame.event.get():
                c=0

                if event.type == pygame.KEYDOWN and menu_continuer:
                    if event.key == pygame.K_DOWN:
                        sélecteur("DOWN")

                    if event.key == pygame.K_UP:
                        sélecteur("UP")

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        if position_selecteur == 0:
                            menu_continuer = False
                            veille = True
                            fermeture_titre(200,2,0)

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        if position_selecteur == 70:
                            menu_continuer=False
                            video=True
                            fermeture_titre(200,2,0)
                            videos_carroussel.open()

                        if position_selecteur == 140:
                            fermeture_titre(200,2,0)
                            STOP("Level.bat")

                        if position_selecteur == 210:
                            menu_continuer=False
                            Audio_player = True
                            Audio_player_menu = True
                            fermeture_titre(200,2,0)
                            onglets_ouverture(texte_audio_player,audio_player_icon_min)

                        if position_selecteur == 280:
                            menu_continuer = False
                            jeux = True
                            jeux_menu = True
                            fermeture_titre(200,2,0)
                            onglets_ouverture(texte_jeux, Autopilot_menu)
                            menu_games.open()

                        if position_selecteur == 350:
                            paramètres=True
                            menu_continuer=False
                            fermeture_titre(200,2,0)
                            Tuiles_ouverture()

                        if position_selecteur == 420:
                            credits = True
                            credits_menu = True
                            menu_continuer=False
                            fermeture_titre(200,2,0)
                            onglets_ouverture(texte_credits, Lounge_menu,True)

                        if position_selecteur == 490:
                            fermeture_titre(200,2,0)
                            menu_continuer = False
                            mail_box = True
                            mail_box_init = True
                            onglets_ouverture(texte_intercomm,Intercomm_menu)

                        if position_selecteur == 560:
                            fermeture_titre(200,2,0)
                            menu_continuer = False
                            tools = True
                            tools_selection = True
                            onglets_ouverture(texte_tools,tools_min)

                        if position_selecteur == 630:
                            if quit_enable and not(update_web):
                                fermeture_titre(200,2,0)
                                STOP()
                            elif quit_enable and update_web:
                                fermeture_titre(200,2,0)
                                STOP("Update.bat")

                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

                a,b= pygame.mouse.get_pos ( )

                if event.type == pygame.MOUSEBUTTONDOWN and menu_continuer:
                    mouse_stat = pygame.mouse.get_pressed()
                    if mouse_stat[0]:
                        if pos_widget_soundtrack_skin.collidepoint(event.pos) and not(pos_widget_soundtrack_pause.collidepoint(event.pos) or pos_widget_soundtrack_avancer.collidepoint(event.pos) or pos_widget_soundtrack_reculer.collidepoint(event.pos)) and not(déplacement_widget_level) and widget_soundtrack:
                            if déplacement_widget_soundtrack:
                                déplacement_widget_soundtrack = False
                            else :
                                déplacement_widget_soundtrack = True
                                décalage_widget = [a-widget_soundtrack_coor[0],b-widget_soundtrack_coor[1]]

                        if pos_widget_level_skin.collidepoint(event.pos) and not(déplacement_widget_soundtrack) and widget_level:
                            if déplacement_widget_level:
                                déplacement_widget_level = False
                            else :
                                déplacement_widget_level = True
                                décalage_widget = [a-widget_level_coor[0],b-widget_level_coor[1]]

                        if pos_widget_signet_open.collidepoint(event.pos) and widget_signet:
                            widget_signet = False
                            widget_barre_transition(2)
                        if pos_widget_signet_close.collidepoint(event.pos) and not(widget_signet):
                            widget_signet = True
                            widget_barre_transition(1)
                        if pos_widget_soundtrack_miniature.collidepoint(event.pos) and not(widget_soundtrack) and widget_signet:
                            widget_soundtrack = True
                            widget_animation("soundtrack",1)

                        if pos_widget_level_miniature.collidepoint(event.pos) and not(widget_level) and widget_signet:
                            widget_level = True
                            widget_animation("level",1)

                        if pos_widget_soundtrack_pause.collidepoint(event.pos) and widget_soundtrack:
                            if pygame.mixer.music.get_busy():
                                audio_reader_proc.pause()
                            else:
                                audio_reader_proc.lecture()

                        if pos_widget_soundtrack_avancer.collidepoint(event.pos) and widget_soundtrack:
                            audio_reader_proc.avancer()

                        if pos_widget_soundtrack_reculer.collidepoint(event.pos) and widget_soundtrack:
                            audio_reader_proc.reculer()

                        if b >= 0 and b <= 70 and a <= 371:
                            if position_selecteur >= 70 :
                                while position_selecteur != 0 :
                                    sélecteur("UP")
                            menu_continuer = False
                            veille = True
                            fermeture_titre(200,2,0)

                        if b > 70 and b <= 140 and a <= 371:
                            if position_selecteur > 70 :
                                while position_selecteur != 70 :
                                    sélecteur("UP")
                            if position_selecteur < 70 :
                                while position_selecteur != 70 :
                                    sélecteur("DOWN")

                            menu_continuer=False
                            video=True
                            fermeture_titre(200,2,0)
                            videos_carroussel.open()

                        if b > 140 and b <= 210 and a <= 371:
                            if position_selecteur > 140 :
                                while position_selecteur != 140 :
                                    sélecteur("UP")
                            if position_selecteur < 140 :
                                while position_selecteur != 140 :
                                    sélecteur("DOWN")
                            fermeture_titre(200,2,0)
                            STOP("Level.bat")

                        if b > 210 and b <= 280 and a <= 371:
                            if position_selecteur > 210 :
                                while position_selecteur != 210 :
                                    sélecteur("UP")
                            if position_selecteur < 210 :
                                while position_selecteur != 210 :
                                    sélecteur("DOWN")
                            Audio_player = True
                            Audio_player_menu = True
                            menu_continuer=False
                            fermeture_titre(200,2,0)
                            onglets_ouverture(texte_audio_player,audio_player_icon_min)

                        if b > 280 and b <= 350 and a <= 371:
                            if position_selecteur > 280 :
                                while position_selecteur != 280 :
                                    sélecteur("UP")
                            if position_selecteur < 280 :
                                while position_selecteur != 280 :
                                    sélecteur("DOWN")
                            menu_continuer = False
                            jeux = True
                            jeux_menu = True
                            fermeture_titre(200,2,0)
                            onglets_ouverture(texte_jeux, Autopilot_menu)
                            menu_games.open()

                        if b > 350 and b <= 420 and a <= 371:
                            if position_selecteur > 350 :
                                while position_selecteur != 350 :
                                    sélecteur("UP")
                            if position_selecteur < 350 :
                                while position_selecteur != 350 :
                                    sélecteur("DOWN")

                            paramètres=True
                            menu_continuer=False
                            fermeture_titre(200,2,0)
                            Tuiles_ouverture()

                        if b > 420 and b <= 490 and a <= 371:
                            if position_selecteur > 420 :
                                while position_selecteur != 420 :
                                    sélecteur("UP")
                            if position_selecteur < 420 :
                                while position_selecteur != 420 :
                                    sélecteur("DOWN")
                            credits = True
                            credits_menu = True
                            menu_continuer=False
                            fermeture_titre(200,2,0)
                            onglets_ouverture(texte_credits, Lounge_menu,True)

                        if b > 490 and b <= 560 and a <= 371:
                            if position_selecteur > 490 :
                                while position_selecteur != 490 :
                                    sélecteur("UP")
                            if position_selecteur < 490 :
                                while position_selecteur != 490 :
                                    sélecteur("DOWN")
                            fermeture_titre(200,2,0)
                            menu_continuer = False
                            mail_box = True
                            mail_box_init = True
                            onglets_ouverture(texte_intercomm,Intercomm_menu)

                        if b > 560 and b <= 630 and a <= 371:
                            if position_selecteur > 560 :
                                while position_selecteur != 560 :
                                    sélecteur("UP")
                            if position_selecteur < 560 :
                                while position_selecteur != 560 :
                                    sélecteur("DOWN")
                            fermeture_titre(200,2,0)
                            menu_continuer = False
                            tools = True
                            tools_selection = True
                            onglets_ouverture(texte_tools,tools_min)


                        if b > 630 and b <= 700 and a <= 371:
                            if position_selecteur > 630 :
                                while position_selecteur != 630 :
                                    sélecteur("UP")
                            if position_selecteur < 630 :
                                while position_selecteur != 630 :
                                    sélecteur("DOWN")
                            if quit_enable and not(update_web):
                                fermeture_titre(200,2,0)
                                STOP()
                            elif quit_enable and update_web:
                                fermeture_titre(200,2,0)
                                STOP("Update.bat")

            a,b= pygame.mouse.get_pos ( )

            while b >= 0 and b <= 70 and a <= 371 and position_selecteur != 0  and menu_continuer:

                if position_selecteur > 0 :
                    while position_selecteur != 0 :
                        sélecteur("UP")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 70 and b <= 140 and a <= 371 and position_selecteur != 70  and menu_continuer:

                if position_selecteur > 70 :
                    while position_selecteur != 70 :
                        sélecteur("UP")
                if position_selecteur < 70 :
                    while position_selecteur != 70 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 140 and b <= 210 and a <= 371 and position_selecteur != 140  and menu_continuer:

                if position_selecteur > 140 :
                    while position_selecteur != 140 :
                        sélecteur("UP")
                if position_selecteur < 140 :
                    while position_selecteur != 140 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 210 and b <= 280 and a <= 371 and position_selecteur != 210  and menu_continuer:

                if position_selecteur > 210 :
                    while position_selecteur != 210 :
                        sélecteur("UP")
                if position_selecteur < 210 :
                    while position_selecteur != 210 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 280 and b <= 350 and a <= 371 and position_selecteur != 280  and menu_continuer:

                if position_selecteur > 280 :
                    while position_selecteur != 280 :
                        sélecteur("UP")
                if position_selecteur < 280 :
                    while position_selecteur != 280 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 350 and b <= 420 and a <= 371 and position_selecteur != 350  and menu_continuer:

                if position_selecteur > 350 :
                    while position_selecteur != 350 :
                        sélecteur("UP")
                if position_selecteur < 350 :
                    while position_selecteur != 350 :
                        sélecteur("DOWN")
                a,b= pygame.mouse.get_pos ( )

            while b > 420 and b <= 490 and a <= 371 and position_selecteur != 420  and menu_continuer:

                if position_selecteur > 420 :
                        while position_selecteur != 420 :
                            sélecteur("UP")
                if position_selecteur < 420 :
                    while position_selecteur != 420 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            a,b= pygame.mouse.get_pos ( )

            while b > 490 and b <= 560 and a <= 371 and position_selecteur != 490  and menu_continuer:

                if position_selecteur > 490 :
                    while position_selecteur != 490 :
                        sélecteur("UP")
                if position_selecteur < 490 :
                    while position_selecteur != 490 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            while b > 560 and b <= 630 and a <= 371 and position_selecteur != 560  and menu_continuer:

                if position_selecteur > 560 :
                    while position_selecteur != 560 :
                        sélecteur("UP")
                if position_selecteur < 560 :
                    while position_selecteur != 560 :
                        sélecteur("DOWN")

            while b > 630 and b <= 700 and a <= 371 and position_selecteur != 630  and menu_continuer:

                if position_selecteur > 630 :
                    while position_selecteur != 630 :
                        sélecteur("UP")
                if position_selecteur < 630 :
                    while position_selecteur != 630 :
                        sélecteur("DOWN")

                a,b= pygame.mouse.get_pos ( )

            if widget_soundtrack_coor[0]+décalage_widget[0] > 1180 and not(déplacement_widget_soundtrack) and widget_signet  and menu_continuer:
                widget_soundtrack = False
                widget_animation("soundtrack",2)

            if widget_level_coor[0]+décalage_widget[0] > 1180 and not(déplacement_widget_level) and widget_signet  and menu_continuer:
                widget_level = False
                widget_animation("level",2)

            a,b= pygame.mouse.get_pos ( )

            if déplacement_widget_soundtrack  and menu_continuer:
                n_coord = [a-décalage_widget[0],b-décalage_widget[1]]

                if n_coord[0] > 380 and (n_coord[1] > 10 and n_coord[1] < 490):
                    n_coord = [a-décalage_widget[0],b-décalage_widget[1]]
                    widget_soundtrack_coor = n_coord
                    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                elif n_coord[0] < 380 and (n_coord[1] > 10 and n_coord[1] < 490):
                    n_coord = [widget_soundtrack_coor[0],b-décalage_widget[1]]
                    widget_soundtrack_coor = n_coord
                    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))
                elif n_coord[0] > 380 and (n_coord[1] < 10 or n_coord[1] > 490):
                    n_coord = [a-décalage_widget[0],widget_soundtrack_coor[1]]
                    widget_soundtrack_coor = n_coord
                    pos_widget_soundtrack_skin = widget_soundtrack_skin.get_rect(topleft=(widget_soundtrack_coor[0],widget_soundtrack_coor[1]))

                    pos_widget_soundtrack_pause = widget_soundtrack_pause.get_rect(topleft=(widget_soundtrack_coor[0]+95,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_reculer = widget_soundtrack_reculer.get_rect(topleft=(widget_soundtrack_coor[0]+15,widget_soundtrack_coor[1]+152))

                    pos_widget_soundtrack_avancer = widget_soundtrack_avancer.get_rect(topleft=(widget_soundtrack_coor[0]+175,widget_soundtrack_coor[1]+152))

            if déplacement_widget_level  and menu_continuer:
                n_coord = [a-décalage_widget[0],b-décalage_widget[1]]

                if n_coord[0] > 380 and (n_coord[1] > 10 and n_coord[1] < 372):
                    n_coord = [a-décalage_widget[0],b-décalage_widget[1]]
                    widget_level_coor = n_coord
                    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

                elif n_coord[0] < 380 and (n_coord[1] > 10 and n_coord[1] < 372):
                    n_coord = [widget_level_coor[0],b-décalage_widget[1]]
                    widget_level_coor = n_coord
                    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

                elif n_coord[0] > 380 and (n_coord[1] < 10 or n_coord[1] > 372):
                    n_coord = [a-décalage_widget[0],widget_level_coor[1]]
                    widget_level_coor = n_coord
                    pos_widget_level_skin = widget_level_skin.get_rect(topleft=(widget_level_coor[0],widget_level_coor[1]))

        # Menu principal (Old Style skin, Legacy : le premier menu présent dans la Level 2.0, ancien nom de la BNL's Box)
        while Menu_skin1 :

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            étape_programme = "Menu principal (legacy)"
            BNLmenu_old = pygame.image.load("Images/Old/BNLmenu.png").convert_alpha()
            DVD_old = pygame.image.load("Images/Old/DVD.png").convert_alpha()
            Soundtrack_old = pygame.image.load("Images/Old/Soundtrack.png").convert_alpha()
            Solar_old = pygame.image.load("Solar/DVD0.png").convert_alpha()
            Bonus_old = pygame.image.load("Images/Old/Bonus.png").convert_alpha()
            Autre_old = pygame.image.load("Images/Old/Autre.png").convert_alpha()

            """Définition de la position des images précédement chargées"""

            pos_Solar_old = Solar_old.get_rect(topleft=(50,450))
            pos_BNLmenu_old = BNLmenu_old.get_rect(topleft=(970,20))
            pos_Soundtrack_old = Soundtrack_old.get_rect(topleft=(500,450))
            pos_Bonus_old = Bonus_old.get_rect(topleft=(50,20))
            pos_Autre_old = Autre_old.get_rect(topleft=(400,20))
            pos_DVD_old = DVD_old.get_rect(topleft=(1000,450))

            fenetre.blit(wallpapers_use.wallpaper,(0,0))
            fenetre.blit(DVD_old,(1000,450))
            fenetre.blit(BNLmenu_old,(970,20))
            fenetre.blit(Soundtrack_old,(500,450))
            fenetre.blit(Solar_old,(50,450))
            fenetre.blit(Bonus_old,(50,20))
            fenetre.blit(Autre_old,(400,20))
            font_old = pygame.font.Font(font_selected, 30)
            texte = font_old.render(langue.old_bonus, 1, (255,255,255))
            fenetre.blit(texte, (100, 330))
            texte = font_old.render(langue.old_soundtrack, 1, (255,255,255))
            fenetre.blit(texte, (500, 420))
            texte = font_old.render(langue.old_parameters, 1, (255,255,255))
            fenetre.blit(texte, (970, 145))
            if update_at_quit:
                fenetre.blit(download_stat_downloading,(400,5))
            pygame.display.flip()
            r=0
            a,b= pygame.mouse.get_pos ( )

            while pos_Solar_old.collidepoint(a,b) and r<=93:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        x, y = event.pos
                        if mouse_stat[0]:
                            x, y = event.pos
                            if pos_Solar_old.collidepoint(event.pos):
                                os.startfile("Level.bat")
                        pass
                text="Solar/DVD"+str(r)+".png"
                SolarG = pygame.image.load(text).convert_alpha()
                fenetre.blit(SolarG,(50,450))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            for event in pygame.event.get():
                c=0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_stat = pygame.mouse.get_pressed()
                    x, y = event.pos
                    if mouse_stat[0]:
                        if pos_Soundtrack_old.collidepoint(event.pos):
                            Audio_player = True
                            Audio_player_menu = True
                            Menu_skin1=False
                            onglets_ouverture(texte_audio_player,audio_player_icon_min)

                        if pos_Bonus_old.collidepoint(event.pos):
                            Menu_skin1=False
                            video_old=True

                            # Chargement des icônes du menu Bonus
                            PUB = pygame.image.load("Images/Old/Miniature/PUB.png").convert_alpha()
                            Truck= pygame.image.load("Images/Old/Miniature/Truck.png").convert_alpha()
                            Floor= pygame.image.load("Images/Old/Miniature/Floor.png").convert_alpha()
                            Deck= pygame.image.load("Images/Old/Miniature/Deck.png").convert_alpha()
                            Dock= pygame.image.load("Images/Old/Miniature/Dock.png").convert_alpha()
                            Captain= pygame.image.load("Images/Old/Miniature/Captain.png").convert_alpha()
                            Pool= pygame.image.load("Images/Old/Miniature/Pool.png").convert_alpha()
                            Earth= pygame.image.load("Images/Old/Miniature/Earth.png").convert_alpha()
                            Axiom= pygame.image.load("Images/Old/Miniature/Axiom.png").convert_alpha()
                            Preview= pygame.image.load("Images/Old/Miniature/Preview.png").convert_alpha()
                            Trash= pygame.image.load("Images/Old/Miniature/Trash.png").convert_alpha()
                            # Initialisation des positions des icônes du menu Bonus
                            pos_PUB = PUB.get_rect(topleft=(20, 20))
                            pos_Truck = Truck.get_rect(topleft=(240, 20))
                            pos_Earth = Earth.get_rect(topleft=(460, 20))
                            pos_Deck = Deck.get_rect(topleft=(680, 20))
                            pos_Dock = Dock.get_rect(topleft=(900, 20))
                            pos_Floor = Floor.get_rect(topleft=(20, 250))
                            pos_Captain = Captain.get_rect(topleft=(240, 250))
                            pos_Pool = Pool.get_rect(topleft=(460, 250))
                            pos_Preview = Preview.get_rect(topleft=(680, 250))
                            pos_Axiom = Axiom.get_rect(topleft=(900, 250))
                            pos_Trash = Trash.get_rect(topleft=(20, 500))

                            for i in range(88):
                                text="Bonus/Bonus"+str(c)+".png"
                                fond1 = pygame.image.load(text).convert_alpha()
                                fenetre.blit(fond1,(0,0))
                                pygame.display.flip()
                                c+=1
                                time.sleep(0.02)

                        elif pos_BNLmenu_old.collidepoint(event.pos):
                            paramètres=True
                            Menu_skin1=False

                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

        #Menu principal (Carroussel skin)
        while Menu_skin2:
            étape_programme = "Menu Carroussel"

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            if menu_carroussel.selection == 0 :
                menu_carroussel.selection_temp1 = len(menu_carroussel.liste)-1
                menu_carroussel.selection_temp2 = len(menu_carroussel.liste)-2
                menu_carroussel.selection_temp3 = menu_carroussel.selection+1
                menu_carroussel.selection_temp4 = menu_carroussel.selection+2

            elif menu_carroussel.selection == 1 :
                menu_carroussel.selection_temp1 = 0
                menu_carroussel.selection_temp2 = len(menu_carroussel.liste)-1
                menu_carroussel.selection_temp3 = menu_carroussel.selection+1
                menu_carroussel.selection_temp4 = menu_carroussel.selection+2

            elif menu_carroussel.selection == len(menu_carroussel.liste)-1 :
                menu_carroussel.selection_temp1 = menu_carroussel.selection-1
                menu_carroussel.selection_temp2 = menu_carroussel.selection-2
                menu_carroussel.selection_temp3 = 0
                menu_carroussel.selection_temp4 = 1
            elif menu_carroussel.selection == len(menu_carroussel.liste)-2 :
                menu_carroussel.selection_temp1 = menu_carroussel.selection-1
                menu_carroussel.selection_temp2 = menu_carroussel.selection-2
                menu_carroussel.selection_temp3 = len(menu_carroussel.liste)-1
                menu_carroussel.selection_temp4 = 0
            else :
                menu_carroussel.selection_temp1 = menu_carroussel.selection-1
                menu_carroussel.selection_temp2 = menu_carroussel.selection-2
                menu_carroussel.selection_temp3 = menu_carroussel.selection+1
                menu_carroussel.selection_temp4 = menu_carroussel.selection+2

            vignette_1 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp2]+".png").convert_alpha()
            vignette_5 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp4]+".png").convert_alpha()

            vignette_3 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection]+".png").convert_alpha()

            vignette_2 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp1]+".png").convert_alpha()
            vignette_4 = pygame.image.load(menu_carroussel.path+menu_carroussel.liste[menu_carroussel.selection_temp3]+".png").convert_alpha()

            vignette_1 = pygame.transform.scale(vignette_1, (300,169))
            vignette_5 = pygame.transform.scale(vignette_5, (300,169))

            vignette_2 = pygame.transform.scale(vignette_2, (400,225))
            vignette_4 = pygame.transform.scale(vignette_4, (400,225))

            pos_video_bonus = vignette_3.get_rect(topleft=(340, 191))

            fenetre.blit(wallpapers_use.wallpaper,(0,0))

            fenetre.blit(vignette_1,(100,275))
            fenetre.blit(vignette_5,(880,275))

            fenetre.blit(vignette_2,(200,247))
            fenetre.blit(vignette_4,(680,247))

            fenetre.blit(vignette_3,(299,168))

            fenetre.blit(Gauche_video2,(60,500))
            fenetre.blit(Droite_video2,(1189,500))

            if carr_title_bar_stat == "enable":
                fenetre.blit(carr_title_bar,(0,606))
                texte = font.render(carr_lang_translate[menu_carroussel.liste[menu_carroussel.selection]], 1, color_menu)
                fenetre.blit(texte, (20, 650))
                fenetre.blit(carr_level_sun,(1070, 630))

                try :
                    battery = psutil.sensors_battery()
                    level= battery.percent
                    plugged = battery.power_plugged
                    a_string = level/10
                    float_str = float(a_string)
                    test= int(float_str)
                    if level>=10 and level<100:
                        n=test
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                        afficher_batons_carr(n,1150,630)
                    elif level==100:
                        n=9
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                        afficher_batons_carr(n,1150,630)
                    elif plugged and level<10:
                        n=0
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                    elif level<10 and not(plugged):
                        pygame.draw.rect(fenetre, color_level, pygame.Rect(1135, 630,10, 60))
                        texte = font.render("WARNING", 1, (0,0,0))
                        fenetre.blit(texte, (1130, 650))

                except:
                    texte = font.render("ERROR", 1, (255,0,0))
                    fenetre.blit(texte, (1130,650))

                fenetre.blit(widget_soundtrack_reculer,(600,650))
                fenetre.blit(widget_soundtrack_avancer,(780,650))

                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_pause,(690,650))
                elif not(pygame.mixer.music.get_busy()):
                    fenetre.blit(widget_soundtrack_lecture,(690,650))

                texte = font_widget.render(audio_reader_proc.title_widget, 1, (255,255,255))
                fenetre.blit(texte, (600,620))

                fenetre.blit(audio_reader_proc.min,(490,613))

            a,b= pygame.mouse.get_pos ( )

            if b > 606 :
                if carr_title_bar_transition_stat == 1 :
                    carr_title_bar_transition_stat = 0
                    carr_title_bar_transition("entry",0)
                carr_title_bar_stat = "enable"
            else :
                if carr_title_bar_transition_stat == 0 :
                    carr_title_bar_transition_stat = 1
                    carr_title_bar_transition("out",0)
                carr_title_bar_stat = "disable"

            if update_at_quit:
                fenetre.blit(download_stat_downloading,(400,5))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        menu_carroussel.selection_old = menu_carroussel.selection
                        if menu_carroussel.selection < len(menu_carroussel.liste)-1 :
                            menu_carroussel.selection += 1
                        else :
                            menu_carroussel.selection = 0

                        if menu_carroussel.selection == len(menu_carroussel.liste)-3 :
                            menu_carroussel.selection_trans = len(menu_carroussel.liste)-1
                        elif menu_carroussel.selection == len(menu_carroussel.liste)-2 :
                            menu_carroussel.selection_trans = 0
                        elif menu_carroussel.selection == len(menu_carroussel.liste)-1 :
                            menu_carroussel.selection_trans = 1
                        else :
                            menu_carroussel.selection_trans = menu_carroussel.selection+2

                        menu_carroussel.right()

                    if event.key == pygame.K_LEFT:
                        menu_carroussel.selection_old = menu_carroussel.selection
                        if menu_carroussel.selection > 0 :
                            menu_carroussel.selection -= 1
                        else :
                            menu_carroussel.selection = len(menu_carroussel.liste)-1

                        if menu_carroussel.selection == 0 :
                            menu_carroussel.selection_trans = len(menu_carroussel.liste)-2
                        elif menu_carroussel.selection == 1:
                            menu_carroussel.selection_trans = len(menu_carroussel.liste)-1
                        else :
                            menu_carroussel.selection_trans = menu_carroussel.selection-2

                        menu_carroussel.left()

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        if menu_carroussel.liste[menu_carroussel.selection] == "Accueil":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            veille = True
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Audio_player":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            Audio_player = True
                            Audio_player_menu = True
                            onglets_ouverture(texte_audio_player,audio_player_icon_min)
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Jeux":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            jeux = True
                            jeux_menu = True
                            onglets_ouverture(texte_jeux, Autopilot_menu)
                            menu_games.open()
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Credits":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            credits = True
                            credits_menu = True
                            onglets_ouverture(texte_credits, Lounge_menu,True)

                        elif menu_carroussel.liste[menu_carroussel.selection] == "Quitter":
                            if quit_enable and not(update_web):
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                STOP()
                            elif quit_enable and update_web:
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                STOP("Update.bat")

                        elif menu_carroussel.liste[menu_carroussel.selection] == "Videos":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            video=True
                            videos_carroussel.open()
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Jauge":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            STOP("Level.bat")
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Parametres":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            paramètres=True
                            Tuiles_ouverture()
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Messages":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            mail_box = True
                            mail_box_init = True
                            onglets_ouverture(texte_intercomm,Intercomm_menu)
                        elif menu_carroussel.liste[menu_carroussel.selection] == "Outils":
                            Menu_skin2 = False
                            if carr_title_bar_stat == "enable":
                                carr_title_bar_transition("out",0)
                            menu_carroussel.close()
                            tools = True
                            tools_selection = True
                            onglets_ouverture(texte_tools,tools_min)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_stat = pygame.mouse.get_pressed()
                    if mouse_stat[0]:
                        if pos_video_bonus.collidepoint(event.pos):
                            if menu_carroussel.liste[menu_carroussel.selection] == "Accueil":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                veille = True
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Audio_player":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                Audio_player = True
                                Audio_player_menu = True
                                onglets_ouverture(texte_audio_player,audio_player_icon_min)
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Jeux":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                jeux = True
                                jeux_menu = True
                                onglets_ouverture(texte_jeux, Autopilot_menu)
                                menu_games.open()
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Credits":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                credits = True
                                credits_menu = True
                                onglets_ouverture(texte_credits, Lounge_menu,True)

                            elif menu_carroussel.liste[menu_carroussel.selection] == "Quitter":
                                if quit_enable and not(update_web):
                                    Menu_skin2 = False
                                    if carr_title_bar_stat == "enable":
                                        carr_title_bar_transition("out",0)
                                    menu_carroussel.close()
                                    STOP()
                                elif quit_enable and update_web:
                                    Menu_skin2 = False
                                    if carr_title_bar_stat == "enable":
                                        carr_title_bar_transition("out",0)
                                    menu_carroussel.close()
                                    STOP("Update.bat")

                            elif menu_carroussel.liste[menu_carroussel.selection] == "Videos":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                video=True
                                videos_carroussel.open()
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Jauge":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                STOP("Level.bat")
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Parametres":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                paramètres=True
                                Tuiles_ouverture()
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Messages":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                mail_box = True
                                mail_box_init = True
                                onglets_ouverture(texte_intercomm,Intercomm_menu)
                            elif menu_carroussel.liste[menu_carroussel.selection] == "Outils":
                                Menu_skin2 = False
                                if carr_title_bar_stat == "enable":
                                    carr_title_bar_transition("out",0)
                                menu_carroussel.close()
                                tools = True
                                tools_selection = True
                                onglets_ouverture(texte_tools,tools_min)

                        if pos_Gauche_video.collidepoint(event.pos):
                            menu_carroussel.selection_old = menu_carroussel.selection
                            if menu_carroussel.selection > 0 :
                                menu_carroussel.selection -= 1
                            else :
                                menu_carroussel.selection = len(menu_carroussel.liste)-1

                            if menu_carroussel.selection == 0 :
                                menu_carroussel.selection_trans = len(menu_carroussel.liste)-2
                            elif menu_carroussel.selection == 1:
                                menu_carroussel.selection_trans = len(menu_carroussel.liste)-1
                            else :
                                menu_carroussel.selection_trans = menu_carroussel.selection-2

                            menu_carroussel.left()

                        if pos_Droite_video.collidepoint(event.pos):
                            menu_carroussel.selection_old = menu_carroussel.selection
                            if menu_carroussel.selection < len(menu_carroussel.liste)-1 :
                                menu_carroussel.selection += 1
                            else :
                                menu_carroussel.selection = 0

                            if menu_carroussel.selection == len(menu_carroussel.liste)-3 :
                                menu_carroussel.selection_trans = len(menu_carroussel.liste)-1
                            elif menu_carroussel.selection == len(menu_carroussel.liste)-2 :
                                menu_carroussel.selection_trans = 0
                            elif menu_carroussel.selection == len(menu_carroussel.liste)-1 :
                                menu_carroussel.selection_trans = 1
                            else :
                                menu_carroussel.selection_trans = menu_carroussel.selection+2

                            menu_carroussel.right()

                        if pos_carr_soundtrack_pause.collidepoint(event.pos):
                            if pygame.mixer.music.get_busy():
                                audio_reader_proc.pause()
                            else:
                                audio_reader_proc.lecture()

                        if pos_carr_soundtrack_avancer.collidepoint(event.pos):
                            audio_reader_proc.avancer()

                        if pos_carr_soundtrack_reculer.collidepoint(event.pos):
                            audio_reader_proc.reculer()

                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

        # Menu vidéos (Old Style skin, Legacy : apparut depuis Level 1.5, retiré du service avec la BNL's Box 4.1)
        while video_old:
            étape_programme = "Bonus (legacy)"
            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            fenetre.blit(PUB,(20,20))
            fenetre.blit(Truck,(240,20))
            fenetre.blit(Earth,(460,20))
            fenetre.blit(Deck,(680,20))
            fenetre.blit(Dock,(900,20))
            fenetre.blit(Floor,(20,250))
            fenetre.blit(Captain,(240,250))
            fenetre.blit(Pool,(460,250))
            fenetre.blit(Preview,(680,250))
            fenetre.blit(Axiom,(900,250))
            fenetre.blit(Trash,(20,500))
            fenetre.blit(Menu,(1150,20))

            if update_at_quit:
                fenetre.blit(download_stat_downloading,(900,500))

            pygame.display.flip()
            r=0
            a,b= pygame.mouse.get_pos ( )

            while pos_PUB.collidepoint(a,b) and r<=208:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_PUB.collidepoint(event.pos):
                            os.startfile("Videos\\PUB.mp4")
                    pass
                text="Images/Old/GIF Miniatures/PUB/PUB"+str(r)+".png"
                PUBG = pygame.image.load(text).convert_alpha()
                fenetre.blit(PUBG,(20,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Trash.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Trash.collidepoint(event.pos):
                            os.startfile("Videos\\Trash.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Trash/PUB"+str(r)+".png"
                TrashG = pygame.image.load(text).convert_alpha()
                fenetre.blit(TrashG,(20,500))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Floor.collidepoint(a,b) and r<=91:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Floor.collidepoint(event.pos):
                            os.startfile("Videos\\Floor.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Floor/PUB"+str(r)+".png"
                FloorG = pygame.image.load(text).convert_alpha()
                fenetre.blit(FloorG,(20,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Deck.collidepoint(a,b) and r<=97:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Deck.collidepoint(event.pos):
                            os.startfile("Videos\\Deck.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Deck/PUB"+str(r)+".png"
                DeckG = pygame.image.load(text).convert_alpha()
                fenetre.blit(DeckG,(680,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Dock.collidepoint(a,b) and r<=98:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Dock.collidepoint(event.pos):
                            os.startfile("Videos\\Dock.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Dock/PUB"+str(r)+".png"
                DockG = pygame.image.load(text).convert_alpha()
                fenetre.blit(DockG,(900,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Preview.collidepoint(a,b) and r<=115:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Preview.collidepoint(event.pos):
                            os.startfile("Videos\\Preview.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Preview/PUB"+str(r)+".png"
                PreviewG = pygame.image.load(text).convert_alpha()
                fenetre.blit(PreviewG,(680,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Axiom.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Axiom.collidepoint(event.pos):
                            os.startfile("Videos\\Axiom.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Axiom/PUB"+str(r)+".png"
                AxiomG = pygame.image.load(text).convert_alpha()
                fenetre.blit(AxiomG,(900,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Earth.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Earth.collidepoint(event.pos):
                            os.startfile("Videos\\Earth.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Earth/PUB"+str(r)+".png"
                EarthG = pygame.image.load(text).convert_alpha()
                fenetre.blit(EarthG,(460,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Truck.collidepoint(a,b) and r<=138:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Truck.collidepoint(event.pos):
                            os.startfile("Videos\\Truck.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Truck/PUB"+str(r)+".png"
                TruckG = pygame.image.load(text).convert_alpha()
                fenetre.blit(TruckG,(240,20))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Pool.collidepoint(a,b) and r<=99:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Pool.collidepoint(event.pos):
                            os.startfile("Videos\\Pool.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Pool/PUB"+str(r)+".png"
                PoolG = pygame.image.load(text).convert_alpha()
                fenetre.blit(PoolG,(460,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0

            while pos_Captain.collidepoint(a,b) and r<=79:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                        x, y = event.pos
                        if pos_Captain.collidepoint(event.pos):
                            os.startfile("Videos\\Captain.mp4")
                    pass
                text="Images/Old/GIF Miniatures/Captain/PUB"+str(r)+".png"
                CaptainG = pygame.image.load(text).convert_alpha()
                fenetre.blit(CaptainG,(240,250))
                pygame.display.flip()
                r+=1
                time.sleep(0.02)
                a,b= pygame.mouse.get_pos ( )

            r=0
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pos_Menu.collidepoint(event.pos):
                    video_old = False
                    Menu_skin1 = True
                    menu_continuer = False
                    transition_ouverture(322)

            for event in pygame.event.get():
                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

        # Menu vidéos
        while video:
            étape_programme = "Vidéos"

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            if videos_carroussel.selection == 0 :
                videos_carroussel.selection_temp1 = len(videos_carroussel.liste)-1
                videos_carroussel.selection_temp2 = len(videos_carroussel.liste)-2
                videos_carroussel.selection_temp3 = videos_carroussel.selection+1
                videos_carroussel.selection_temp4 = videos_carroussel.selection+2

            elif videos_carroussel.selection == 1 :
                videos_carroussel.selection_temp1 = 0
                videos_carroussel.selection_temp2 = len(videos_carroussel.liste)-1
                videos_carroussel.selection_temp3 = videos_carroussel.selection+1
                videos_carroussel.selection_temp4 = videos_carroussel.selection+2

            elif videos_carroussel.selection == len(videos_carroussel.liste)-1 :
                videos_carroussel.selection_temp1 = videos_carroussel.selection-1
                videos_carroussel.selection_temp2 = videos_carroussel.selection-2
                videos_carroussel.selection_temp3 = 0
                videos_carroussel.selection_temp4 = 1
            elif videos_carroussel.selection == len(videos_carroussel.liste)-2 :
                videos_carroussel.selection_temp1 = videos_carroussel.selection-1
                videos_carroussel.selection_temp2 = videos_carroussel.selection-2
                videos_carroussel.selection_temp3 = len(videos_carroussel.liste)-1
                videos_carroussel.selection_temp4 = 0
            else :
                videos_carroussel.selection_temp1 = videos_carroussel.selection-1
                videos_carroussel.selection_temp2 = videos_carroussel.selection-2
                videos_carroussel.selection_temp3 = videos_carroussel.selection+1
                videos_carroussel.selection_temp4 = videos_carroussel.selection+2

            vignette_1 = pygame.image.load(videos_carroussel.path+videos_carroussel.liste[videos_carroussel.selection_temp2]+".png").convert_alpha()
            vignette_5 = pygame.image.load(videos_carroussel.path+videos_carroussel.liste[videos_carroussel.selection_temp4]+".png").convert_alpha()

            vignette_3 = pygame.image.load(videos_carroussel.path+videos_carroussel.liste[videos_carroussel.selection]+".png").convert_alpha()

            vignette_2 = pygame.image.load(videos_carroussel.path+videos_carroussel.liste[videos_carroussel.selection_temp1]+".png").convert_alpha()
            vignette_4 = pygame.image.load(videos_carroussel.path+videos_carroussel.liste[videos_carroussel.selection_temp3]+".png").convert_alpha()

            vignette_1 = pygame.transform.scale(vignette_1, (300,169))
            vignette_5 = pygame.transform.scale(vignette_5, (300,169))

            vignette_2 = pygame.transform.scale(vignette_2, (400,225))
            vignette_4 = pygame.transform.scale(vignette_4, (400,225))

            pos_video_bonus = vignette_3.get_rect(topleft=(340, 191))

            fenetre.blit(wallpapers_use.wallpaper,(0,0))

            fenetre.blit(vignette_1,(100,275))
            fenetre.blit(vignette_5,(880,275))

            fenetre.blit(vignette_2,(200,247))
            fenetre.blit(vignette_4,(680,247))

            fenetre.blit(vignette_3,(299,168))

            fenetre.blit(Menu,(1150,20))
            fenetre.blit(Gauche_video2,(60,500))
            fenetre.blit(Droite_video2,(1189,500))

            if update_at_quit:
                fenetre.blit(download_stat_downloading,(400,5))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        videos_carroussel.selection_old = videos_carroussel.selection
                        if videos_carroussel.selection < len(videos_carroussel.liste)-1 :
                            videos_carroussel.selection += 1
                        else :
                            videos_carroussel.selection = 0

                        if videos_carroussel.selection == len(videos_carroussel.liste)-3 :
                            videos_carroussel.selection_trans = len(videos_carroussel.liste)-1
                        elif videos_carroussel.selection == len(videos_carroussel.liste)-2 :
                            videos_carroussel.selection_trans = 0
                        elif videos_carroussel.selection == len(videos_carroussel.liste)-1 :
                            videos_carroussel.selection_trans = 1
                        else :
                            videos_carroussel.selection_trans = videos_carroussel.selection+2

                        videos_carroussel.right()

                    if event.key == pygame.K_LEFT:
                        videos_carroussel.selection_old = videos_carroussel.selection
                        if videos_carroussel.selection > 0 :
                            videos_carroussel.selection -= 1
                        else :
                            videos_carroussel.selection = len(videos_carroussel.liste)-1

                        if videos_carroussel.selection == 0 :
                            videos_carroussel.selection_trans = len(videos_carroussel.liste)-2
                        elif videos_carroussel.selection == 1:
                            videos_carroussel.selection_trans = len(videos_carroussel.liste)-1
                        else :
                            videos_carroussel.selection_trans = videos_carroussel.selection-2

                        videos_carroussel.left()

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                        os.startfile("Videos\\"+videos_carroussel.liste[videos_carroussel.selection]+".mp4")
                    if event.key == K_ESCAPE:
                        video = False
                        if Skin_selected == "Titanium":
                            menu_continuer=True
                            videos_carroussel.close()
                            ouverture_titre(200,2,0)
                        elif Skin_selected == "Carroussel":
                            Menu_skin2 = True
                            videos_carroussel.close()
                            menu_carroussel.open()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_stat = pygame.mouse.get_pressed()
                    if mouse_stat[0]:
                        if pos_video_bonus.collidepoint(event.pos):
                            os.startfile("Videos\\"+videos_carroussel.liste[videos_carroussel.selection]+".mp4")
                        if pos_Gauche_video.collidepoint(event.pos):
                            videos_carroussel.selection_old = videos_carroussel.selection
                            if videos_carroussel.selection > 0 :
                                videos_carroussel.selection -= 1
                            else :
                                videos_carroussel.selection = len(videos_carroussel.liste)-1

                            if videos_carroussel.selection == 0 :
                                videos_carroussel.selection_trans = len(videos_carroussel.liste)-2
                            elif videos_carroussel.selection == 1:
                                videos_carroussel.selection_trans = len(videos_carroussel.liste)-1
                            else :
                                videos_carroussel.selection_trans = videos_carroussel.selection-2

                            videos_carroussel.left()

                        if pos_Droite_video.collidepoint(event.pos):
                            videos_carroussel.selection_old = videos_carroussel.selection
                            if videos_carroussel.selection < len(videos_carroussel.liste)-1 :
                                videos_carroussel.selection += 1
                            else :
                                videos_carroussel.selection = 0

                            if videos_carroussel.selection == len(videos_carroussel.liste)-3 :
                                videos_carroussel.selection_trans = len(videos_carroussel.liste)-1
                            elif videos_carroussel.selection == len(videos_carroussel.liste)-2 :
                                videos_carroussel.selection_trans = 0
                            elif videos_carroussel.selection == len(videos_carroussel.liste)-1 :
                                videos_carroussel.selection_trans = 1
                            else :
                                videos_carroussel.selection_trans = videos_carroussel.selection+2

                            videos_carroussel.right()
                        if pos_Menu.collidepoint(event.pos):
                            video = False
                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                videos_carroussel.close()
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                videos_carroussel.close()
                                menu_carroussel.open()

                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

        while Audio_player:
            scroll_album = Scroll([1230,150],0, False)
            while Audio_player_menu:

                étape_programme = "Lecteur multimédia / Menu"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_audio_player, (500, 20))
                fenetre.blit(audio_player_icon_min,(755,0))

                fenetre.blit(audio_player_reader_icon,(1000,20))

                fenetre.blit(audio_player_album, (50,200))
                fenetre.blit(audio_player_artist, (300,200))
                fenetre.blit(audio_player_genre, (550,200))
                fenetre.blit(audio_player_soundtrack, (1000,200))

                fenetre.blit(audio_player_update_button_menu,(1000,600))

                pygame.display.flip()

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                Audio_player_menu = False
                                Audio_player = False
                                onglets_fermeture(texte_audio_player,audio_player_icon_min)
                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    transition_ouverture(322)
                            if pos_audio_player_update_menu_button.collidepoint(event.pos):
                                Audio_player_menu = False
                                Audio_player_database_update = True
                                Audio_player_database_update_proc = False
                            if pos_audio_player_album.collidepoint(event.pos):
                                Audio_player_menu = False
                                Audio_player_album = True
                                album_init_search = True
                                music_album_command = "SELECT Path, Album FROM Music GROUP BY Album"
                                album_selection_stat = 1

                            if pos_audio_player_soundtrack.collidepoint(event.pos):
                                Audio_player_menu = False
                                Audio_player_album = True
                                album_init_search = True
                                music_album_command = "SELECT Path, Titre FROM Soundtrack ORDER BY Piste"
                                album_selection_stat = 113

                            if pos_audio_player_artist.collidepoint(event.pos):
                                Audio_player_menu = False
                                Audio_player_album = True
                                album_init_search = True
                                music_album_command = "SELECT Path, Artiste FROM Music GROUP BY Artiste"
                                album_selection_stat = 10

                            if pos_audio_player_genre.collidepoint(event.pos):
                                Audio_player_menu = False
                                Audio_player_album = True
                                album_init_search = True
                                music_album_command = "SELECT Path, Genre FROM Music GROUP BY Genre"
                                album_selection_stat = 20

                            if pos_audio_player_reader_icon.collidepoint(event.pos) and audio_reader_proc.playlist != []:
                                Audio_player_menu = False
                                Audio_player_reader = True

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if event.key == pygame.K_ESCAPE :
                            Audio_player_menu = False
                            Audio_player = False
                            onglets_fermeture(texte_audio_player,audio_player_icon_min)
                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                transition_ouverture(322)

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while Audio_player_database_update:

                étape_programme = "Lecteur multimédia / Mise à jour de la base de données"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_audio_player, (500, 20))
                fenetre.blit(audio_player_icon_min,(755,0))

                if not(Audio_player_database_update_proc):
                    music_update_txt = "En attente..."
                    mdb_progress = 0
                    fenetre.blit(audio_player_dir_button,(1100,650))
                    fenetre.blit(audio_player_dir_add_button,(1200,650))
                else:
                    fenetre.blit(audio_player_dir_button1,(1100,650))
                    fenetre.blit(audio_player_dir_add_button,(1200,650))

                texte = font_widget.render(music_update_txt, 1, (255,255,255))
                fenetre.blit(texte, (40, 406))

                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(10,400,1260, 30),2,0)
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(10,450,1260, 50),2,0)

                pygame.draw.rect(fenetre, color_aux, pygame.Rect(14,454,mdb_progress, 42))

                pygame.display.flip()

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos) and not(Audio_player_database_update_proc):
                                Audio_player_menu = True
                                Audio_player_database_update = False
                            if pos_audio_player_update_button.collidepoint(event.pos) and not(Audio_player_database_update_proc):
                                root = easygui.diropenbox()
                                if root != None:
                                    music_update_process = Thread(target=music_data_update, args=(root,"Music"))
                                    music_update_process.start()
                                    Audio_player_database_update_proc = True
                            if pos_audio_player_add_button.collidepoint(event.pos) and not(Audio_player_database_update_proc):
                                root = easygui.diropenbox()
                                if root != None:
                                    music_update_process = Thread(target=music_data_update, args=(root,"Music","add"))
                                    music_update_process.start()
                                    Audio_player_database_update_proc = True

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if event.key == pygame.K_ESCAPE and not(Audio_player_database_update_proc):
                            Audio_player_menu = True
                            Audio_player_database_update = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while Audio_player_album:

                étape_programme = "Lecteur multimédia / Affichage des albums, genres, artistes, etc."

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_audio_player, (500, 20))
                if album_selection_stat == 1 or album_selection_stat == 2:
                    fenetre.blit(audio_player_album_min,(755,0))
                elif album_selection_stat == 10 or album_selection_stat == 11 or album_selection_stat == 12:
                    fenetre.blit(audio_player_artist_min,(755,0))
                elif album_selection_stat == 20 or album_selection_stat == 21 or album_selection_stat == 22:
                    fenetre.blit(audio_player_genre_min,(755,0))

                fenetre.blit(audio_player_reader_icon,(1000,20))
                fenetre.blit(audio_player_menu_icon,(900,20))

                if album_init_search :
                    
                    albums_listing_Thread = Thread(target=albums_listing, args=())
                    albums_listing_Thread.start()
                    Audio_player_loading_signal.start_signal()
                    
                    while album_init_search:
                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        if Blur_background:
                            fenetre.blit(wallpapers_use.blur, (0,0))
                        else:
                            fenetre.blit(wallpapers_use.wallpaper, (0,0))
                            fenetre.blit(fond_visibilité, (0,0))
                        fenetre.blit(Menu,(1150,20))
                        fenetre.blit(Selection_menu,(455,0))
                        fenetre.blit(texte_audio_player, (500, 20))
                        if album_selection_stat == 1 or album_selection_stat == 2:
                            fenetre.blit(audio_player_album_min,(755,0))
                        elif album_selection_stat == 10 or album_selection_stat == 11 or album_selection_stat == 12:
                            fenetre.blit(audio_player_artist_min,(755,0))
                        elif album_selection_stat == 20 or album_selection_stat == 21 or album_selection_stat == 22:
                            fenetre.blit(audio_player_genre_min,(755,0))

                        fenetre.blit(audio_player_reader_icon,(1000,20))
                        fenetre.blit(audio_player_menu_icon,(900,20))
                        
                        fenetre.blit(Audio_player_loading_signal.img_in_use, Audio_player_loading_signal.coor)
                        pygame.display.flip()
                        
                        for event in pygame.event.get():
                            None
                        
                    Audio_player_loading_signal.stop_signal()

                albums_listing_lat_decalage = 0
                albums_listing_long_decalage = 0

                albums_panel_pos()

                for i in range(len(liste_variables_albums)):
                    coor_pos_temp_album = (50+albums_listing_long_decalage,100+albums_listing_lat_decalage-scroll_album.val)
                    fenetre.blit(liste_variables_albums[i],coor_pos_temp_album)

                    if list_albums[i][1] == "":
                        if album_selection_stat == 2:
                            album_title = list_albums[i][0]
                            album_title = album_title.split("\\")
                            album_title = album_title[-1].split(".")
                            album_title = album_title[-2]
                        else:
                            if album_selection_stat == 1:
                                album_title = "Album inconnu"
                            elif album_selection_stat == 10:
                                album_title = "Artiste inconnu"
                            elif album_selection_stat == 20:
                                album_title = "Genre inconnu"
                    else:
                        album_title = list_albums[i][1]

                    fenetre.blit(font.render(album_title, 5, color_txt), (200+albums_listing_long_decalage,125+albums_listing_lat_decalage-scroll_album.val))

                    albums_listing_lat_decalage += 150

                a,b= pygame.mouse.get_pos ( )
                mouse_stat = pygame.mouse.get_pressed()

                if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_album.pos.collidepoint(pygame.mouse.get_pos()):
                    if scroll_album.coor[1] < b-scroll_bar_decalage[1]:
                        scroll_album.val -= (scroll_album.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_albums))//2)
                    elif scroll_album.coor[1] > b-scroll_bar_decalage[1]:
                        scroll_album.val += -(scroll_album.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_albums))//2)
                    scroll_album.coor[1] = b-scroll_bar_decalage[1]
                    scroll_album.pos = scroll_bar.get_rect(topleft=scroll_album.coor)

                fenetre.blit(scroll_bar,scroll_album.coor)

                pygame.display.flip()

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            albums_is_click()

                            if pos_Menu.collidepoint(event.pos):
                                if album_selection_stat == 1:
                                    Audio_player_menu = True
                                    Audio_player_album = False
                                    scroll_album = Scroll([1230,150],0, False)
                                elif album_selection_stat == 2:
                                    album_init_search = True
                                    music_album_command = "SELECT Path, Album FROM Music GROUP BY Album"
                                    album_selection_stat -= 1
                                    scroll_album = Scroll([1230,150],0, False)
                                elif album_selection_stat == 114 or album_selection_stat == 113:
                                    Audio_player_menu = True
                                    Audio_player_album = False
                                elif album_selection_stat == 11:
                                    album_init_search = True
                                    music_album_command = "SELECT Path, Artiste FROM Music GROUP BY Artiste"
                                    album_selection_stat -= 1
                                    scroll_album = Scroll([1230,150],0, False)
                                elif album_selection_stat == 12:
                                    album_init_search = True
                                    artist_temp = music_tag.load_file(list_albums[i][0])
                                    artist_temp = str(artist_temp["artist"])
                                    music_album_command = f'SELECT Path, Album FROM Music WHERE Artiste="{artist_temp}" GROUP BY Album'
                                    album_selection_stat -= 1
                                    scroll_album = Scroll([1230,150],0, False)

                                elif album_selection_stat == 21:
                                    album_init_search = True
                                    music_album_command = "SELECT Path, Genre FROM Music GROUP BY Genre"
                                    album_selection_stat -= 1
                                    scroll_album = Scroll([1230,150],0, False)
                                elif album_selection_stat == 22:
                                    album_init_search = True
                                    genre_temp = music_tag.load_file(list_albums[i][0])
                                    genre_temp = str(genre_temp["genre"])
                                    music_album_command = f'SELECT Path, Album FROM Music WHERE Genre="{genre_temp}" GROUP BY Album'
                                    album_selection_stat -= 1
                                    scroll_album = Scroll([1230,150],0, False)
                                else:
                                    Audio_player_menu = True
                                    Audio_player_album = False

                            if scroll_album.pos.collidepoint(event.pos):
                                scroll_bar_decalage = [a-scroll_album.coor[0],b-scroll_album.coor[1]]

                            if pos_audio_player_reader_icon.collidepoint(event.pos) and audio_reader_proc.playlist != []:
                                Audio_player_album = False
                                Audio_player_reader = True

                            if pos_audio_player_menu_icon.collidepoint(event.pos):
                                Audio_player_album = False
                                Audio_player_menu = True

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if event.key == pygame.K_ESCAPE :
                            if album_selection_stat == 1:
                                Audio_player_menu = True
                                Audio_player_album = False
                                scroll_album = Scroll([1230,150],0, False)
                            elif album_selection_stat == 2:
                                album_init_search = True
                                music_album_command = "SELECT Path, Album FROM Music GROUP BY Album"
                                album_selection_stat -= 1
                                scroll_album = Scroll([1230,150],0, False)
                            elif album_selection_stat == 114 or album_selection_stat == 113:
                                Audio_player_menu = True
                                Audio_player_album = False
                            elif album_selection_stat == 11:
                                album_init_search = True
                                music_album_command = "SELECT Path, Artiste FROM Music GROUP BY Artiste"
                                album_selection_stat -= 1
                                scroll_album = Scroll([1230,150],0, False)
                            elif album_selection_stat == 12:
                                album_init_search = True
                                artist_temp = music_tag.load_file(list_albums[i][0])
                                artist_temp = str(artist_temp["artist"])
                                music_album_command = f'SELECT Path, Album FROM Music WHERE Artiste="{artist_temp}" GROUP BY Album'
                                album_selection_stat -= 1
                                scroll_album = Scroll([1230,150],0, False)

                            elif album_selection_stat == 21:
                                album_init_search = True
                                music_album_command = "SELECT Path, Genre FROM Music GROUP BY Genre"
                                album_selection_stat -= 1
                                scroll_album = Scroll([1230,150],0, False)
                            elif album_selection_stat == 22:
                                album_init_search = True
                                genre_temp = music_tag.load_file(list_albums[i][0])
                                genre_temp = str(genre_temp["genre"])
                                music_album_command = f'SELECT Path, Album FROM Music WHERE Genre="{genre_temp}" GROUP BY Album'
                                album_selection_stat -= 1
                                scroll_album = Scroll([1230,150],0, False)
                            else:
                                Audio_player_menu = True
                                Audio_player_album = False
                    if event.type == pygame.MOUSEWHEEL:
                        scroll_album.stat = False
                        a = 0
                        b = scroll_album.coor[1]-event.y
                        scroll_bar_decalage = [0,0]

                        if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550:
                            if scroll_album.coor[1] < b-scroll_bar_decalage[1]:
                                scroll_album.val -= (scroll_album.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_albums))//2)
                            elif scroll_album.coor[1] > b-scroll_bar_decalage[1]:
                                scroll_album.val += -(scroll_album.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_albums))//2)
                            scroll_album.coor[1] = b-scroll_bar_decalage[1]
                            scroll_album.pos = scroll_bar.get_rect(topleft=scroll_album.coor)

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while Audio_player_reader:

                étape_programme = "Lecteur multimédia / Lecteur"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_audio_player, (500, 20))

                album_temp_data = music_tag.load_file(audio_reader_proc.playlist[audio_reader_proc.id][0])

                fenetre.blit(audio_player_menu_icon,(900,20))

                try:
                    album_temp = io.BytesIO(album_temp_data['artwork'].first.data)
                    album_temp = pygame.image.load(album_temp).convert_alpha()
                except:
                    album_temp = audio_player_unknown

                album_temp_min = pygame.transform.scale(album_temp, (70,70))
                album_temp = pygame.transform.scale(album_temp, (400,400))

                fenetre.blit(album_temp_min,(755,0))
                fenetre.blit(album_temp,(50,200))

                fenetre.blit(sound_down, (60, 610))
                fenetre.blit(sound_up, (360, 610))
                sound_viewer_pos = pygame.mixer.music.get_volume()*200
                fenetre.blit(sound_viewer_general,(140+sound_viewer_pos,610))

                a_string=pygame.mixer.music.get_pos()/1000
                float_str = float(a_string)
                test= int(float_str)
                temps = 726/(int(float(str(album_temp_data['#length']))))
                avance=temps*test

                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(500,500,730, 15),1,0)

                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(502,502,avance, 11))

                fenetre.blit(font_audio_reader.render("Titre : " + audio_reader_proc.title_reader, 5, color_txt), (500,300))

                fenetre.blit(font_audio_reader.render("Album : " + audio_reader_proc.album, 5, color_txt), (500,350))

                fenetre.blit(widget_soundtrack_reculer,(700,550))
                if pygame.mixer.music.get_busy():
                    fenetre.blit(widget_soundtrack_pause,(800,550))
                else:
                    fenetre.blit(widget_soundtrack_lecture,(800,550))
                fenetre.blit(widget_soundtrack_avancer,(900,550))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                if album_selection_stat == 113:
                                    Audio_player_reader = False
                                    Audio_player_album = True
                                    album_init_search = True
                                    music_album_command = "SELECT Path, Titre FROM Soundtrack ORDER BY Piste"

                                else:
                                    Audio_player_reader = False
                                    Audio_player_album = True
                                    album_init_search = True
                                    temp = str(album_temp_data['album'])
                                    music_album_command = f'SELECT Path, Titre FROM Music WHERE Album="{temp}" ORDER BY Piste'
                                    scroll_album = Scroll([1230,150],0, False)

                            if pos_audio_player_menu_icon.collidepoint(event.pos):
                                Audio_player_reader = False
                                Audio_player_menu = True

                            if pos_audio_reculer.collidepoint(event.pos):
                                audio_reader_proc.reculer()
                            if pos_audio_play.collidepoint(event.pos):
                                if pygame.mixer.music.get_busy():
                                    audio_reader_proc.pause()
                                else:
                                    audio_reader_proc.lecture()
                            if pos_audio_avancer.collidepoint(event.pos):
                                audio_reader_proc.avancer()

                            if pos_sound_up_audio_player.collidepoint(event.pos) and volume_BNL < 10:
                                fenetre.blit(sound_up1, (360,610))
                                pygame.display.flip()
                                volume_BNL += 1
                                data_base.update("volume_BNL", str(volume_BNL))
                                time.sleep(0.1)
                                pygame.mixer.music.set_volume(volume_BNL/10)

                            if pos_sound_down_audio_player.collidepoint(event.pos) and volume_BNL > 0 :
                                fenetre.blit(sound_down1, (60,610))
                                pygame.display.flip()
                                volume_BNL -= 1
                                data_base.update("volume_BNL", str(volume_BNL))
                                time.sleep(0.1)
                                pygame.mixer.music.set_volume(volume_BNL/10)
                                
                            """
                            if event.pos[0] >= 502 and event.pos[0] <= 1228 and event.pos[1] >= 502 and event.pos[1] <= 513:
                                audio_reader_proc.go_to_time((event.pos[0]-502)//temps)
                            """

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if event.key == pygame.K_ESCAPE :
                            if album_selection_stat == 113:
                                Audio_player_reader = False
                                Audio_player_album = True
                                album_init_search = True
                                music_album_command = "SELECT Path, Titre FROM Soundtrack ORDER BY Piste"

                            else:
                                Audio_player_reader = False
                                Audio_player_album = True
                                album_init_search = True
                                temp = str(album_temp_data['album'])
                                music_album_command = f'SELECT Path, Titre FROM Music WHERE Album="{temp}" ORDER BY Piste'
                                scroll_album = Scroll([1230,150],0, False)

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

        # Menu paramètres (présent depuis le cycle 2.0)
        while paramètres:

            étape_programme = "Paramètres"

            scroll_fond = Scroll([1230,150],0, False)
            scroll_theme = Scroll([1230,150],0, False)
            scroll_wallpapers = Scroll([1230,150],0, False)
            scroll_font = Scroll([1230,150],0, False)
            scroll_animations = Scroll([1230,150],0, False)
            scroll_version = Scroll([1230,150],0, False)

            submenu_wallpapers = Submenu("Images/Theme/"+theme_selected+"/Parametres/submenu.png", [0,0], "Supprimer", False)

            étape_programme = "Paramètres"

            scroll_bar_decalage = [0,0]

            fond_page = 1

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            if AdaptoRAM_check:
                if psutil.virtual_memory()[1] < RAM_free:
                    animations = False
                    transition_check = False

            if Blur_background:
                fenetre.blit(wallpapers_use.blur, (0,0))
            else:
                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(fond_visibilité, (0,0))

            fenetre.blit(Animations,(0,360))
            fenetre.blit(Infos,(0,0))
            fenetre.blit(Modules,(0,180))
            fenetre.blit(Fond_paramètres,(0,540))
            fenetre.blit(Menu,(1150,20))

            if update_at_quit:
                fenetre.blit(download_stat_downloading,(400,5))

            pygame.display.flip()

            Console_s = 0
            Console_t = ""

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_stat = pygame.mouse.get_pressed()
                    if mouse_stat[0]:
                        if pos_Infos.collidepoint(event.pos):
                            fenetre.blit(Infos1,(0,0))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=True
                            pygame.display.flip()

                        if pos_Animations.collidepoint(event.pos):
                            fenetre.blit(Animations1,(0,360))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            fond_écran=False
                            animations_continuer=True
                            paramètres=True
                            upgrade_continuer=False
                            version_continuer=False
                            pygame.display.flip()

                        if pos_Modules.collidepoint(event.pos):
                            fenetre.blit(Modules1,(0,180))
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            upgrade_continuer=True
                            fond_écran=False
                            animations_continuer=False
                            version_continuer=False
                            pygame.display.flip()

                        if pos_Menu.collidepoint(event.pos):
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False

                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(322)

                        if pos_Fond_paramètres.collidepoint(event.pos):
                            paramètres=True
                            menu_continuer=False
                            soundtrack=False
                            bonus_continuer=False
                            animations_continuer=False
                            fond_écran=True
                            upgrade_continuer=False
                            version_continuer=False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_DOWN:
                        fenetre.blit(Infos1,(0,0))
                        soundtrack=False
                        menu_continuer=False
                        bonus_continuer=False
                        paramètres=True
                        animations_continuer=False
                        fond_écran=False
                        upgrade_continuer=False
                        version_continuer=True
                        pygame.display.flip()

                    if event.key == K_ESCAPE:
                        paramètres=False
                        animations_continuer=False
                        fond_écran=False
                        upgrade_continuer=False
                        version_continuer=False

                        if Skin_selected == "Titanium":
                            menu_continuer=True
                            fenetre.blit(wallpapers_use.wallpaper,(0,0))
                            Tuiles_fermeture()
                            ouverture_titre(200,2,0)
                        elif Skin_selected == "Carroussel":
                            Menu_skin2 = True
                            fenetre.blit(wallpapers_use.wallpaper,(0,0))
                            Tuiles_fermeture()
                            menu_carroussel.open()
                        elif Skin_selected == "Legacy":
                            Menu_skin1 = True
                            menu_continuer = False
                            Tuiles_fermeture()
                            transition_ouverture(322)
                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

            # Menu paramètres (onglet version et mise à jour du système)
            while version_continuer:

                étape_programme = "Paramètres / Versions et mise à jour de BNL's Box"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Infos1,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))
                
                texte = font_underline.render("Versions installées :", 1, (color_txt))
                fenetre.blit(texte, (250, 140))

                texte = font.render("BNL's Box -> "+str(Version_Menu), 1, (color_txt))
                fenetre.blit(texte, (250, 200))
                texte = font.render("BNL's Update Utility -> "+str(Version_Update), 1, (color_txt))
                fenetre.blit(texte, (250, 250))
                texte = font.render("BNL's Level -> "+str(Version_Level), 1, (color_txt))
                fenetre.blit(texte, (250, 300))
                texte = font.render("ID Intercomm -> "+str(Version_Intercomm), 1, (color_txt))
                fenetre.blit(texte, (250, 400))

                fenetre.blit(bouton_search_update,(250,502))

                texte = font.render(langue.param_auto_update, 1, (color_txt))
                fenetre.blit(texte, (250, 600))
                texte = font.render(langue.param_update_web, 1, (color_txt))
                fenetre.blit(texte, (250, 650))

                fenetre.blit(ON_OFF_maker,(850,600))
                fenetre.blit(ON_OFF_maker,(850,650))

                if Update_at_start:
                    fenetre.blit(ON,(855,605))
                else:
                    fenetre.blit(OFF,(885,605))

                if Update_check_web:
                    fenetre.blit(ON,(855,655))
                else:
                    fenetre.blit(OFF,(885,655))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))
                    texte = font.render(langue.param_downloading_running, 1, (color_txt))
                    fenetre.blit(texte, (700, 510))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            x, y = event.pos
                            if pos_bouton_search_update.collidepoint(event.pos) and not(update_at_quit):
                                try:
                                    if Update_check_web:
                                        selection_update = True
                                        fenetre.blit(download_stat_tem,(475,310))
                                        pygame.display.flip()
                                        url = "https://drive.google.com/u/1/uc?id=1663LepTTo2f1tb74OMcYscCp7IGf2WCW&export=download"
                                        output = "Update_check.py"
                                        gdown.download(url, output, quiet=True)

                                        url = "https://drive.google.com/u/1/uc?id=1rzJZoe_jGXbFpCTFsWJmuNWRmNOty0sr&export=download"
                                        output = "Changelog_txt_up.py"
                                        gdown.download(url, output, quiet=True)
                                    else:
                                        with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                                            selection_update = True
                                            zipObj.extract("Update_check.py")
                                            zipObj.extract("Changelog_txt_up.py")

                                    importlib.reload(Update_check)
                                    importlib.reload(Changelog_txt_up)

                                    from Update_check import*
                                    from Changelog_txt_up import*

                                    if Update_Menu == Version_Menu and Update_Update == Version_Update and Update_Level == Version_Level and Update_Intercomm == Version_Intercomm:
                                        Tuiles_fermeture()
                                        changelog("entry","BNL's Box "+str(Version_Menu))

                                        while selection_update:

                                            étape_programme = "Changelog / Update"

                                            if audio_reader_proc.is_finish():
                                                audio_reader_proc.avancer()

                                            if Blur_background:
                                                fenetre.blit(wallpapers_use.blur, (0,0))
                                            else:
                                                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                                                fenetre.blit(fond_visibilité, (0,0))
                                            fenetre.blit(Selection_menu,(455,0))
                                            fenetre.blit(font.render("BNL's Box "+str(Version_Menu), 1, color_menu), (530, 20))
                                            fenetre.blit(changelog_logo,(755,4))

                                            fenetre.blit(bouton_Python, (500,650))
                                            fenetre.blit(bouton_Abord, (700,650))

                                            texte = font.render("Aucune mise à jour trouvée...", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 100))
                                            texte = font_popup.render("Voulez-vous effectuer une réinitialisation/réparation ?", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 150))
                                            texte = font_popup.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 200))
                                            texte = font_popup.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 250))
                                            texte = font_popup.render("ATTENTION : toutes les données de la BNL's Box seront réinitialisées.", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 300))
                                            texte = font_popup.render("Si vous êtes développeur, pensez à enregistrer vos modifications dans Level mise à niveau.zip !", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 350))
                                            texte = font_popup.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 400))
                                            texte = font.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 450))
                                            texte = font_popup.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 500))
                                            texte = font.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 550))
                                            texte = font_popup.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 600))
                                            texte = font_popup.render("", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 650))

                                            pygame.display.flip()

                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_stat = pygame.mouse.get_pressed()
                                                    if mouse_stat[0]:
                                                        if pos_bouton_Python.collidepoint(event.pos):
                                                            fichier=open("Update_check.py","w")
                                                            fichier.write('import os'+"\n")
                                                            fichier.write('update_del = os.listdir()'+"\n")
                                                            fichier.write("update_unzip = 'all'"+"\n")
                                                            fichier.write('update_process = ["Update.delete(update_del)", "Update.unzip(update_unzip)"]'+"\n")
                                                            fichier.write('update_stat = ("","")'+"\n")
                                                            fichier.write('after_update = "Menu"'+"\n")
                                                            fichier.close()

                                                            if Update_check_web:
                                                                download_thread = Thread(target=Download_thread, args=("https://drive.google.com/u/1/uc?id="+update_file_link+"&export=download","Level mise à niveau.zip"))
                                                                download_thread.start()
                                                                changelog("out","BNL's Box "+str(Version_Menu))
                                                                Tuiles_ouverture()

                                                                selection_update = False
                                                            else:
                                                                continuer=False
                                                                selection_update = False
                                                                STOP("Update.bat")
                                                        if pos_bouton_Abord.collidepoint(event.pos):
                                                            changelog("out","BNL's Box "+str(Version_Menu))
                                                            Tuiles_ouverture()
                                                            selection_update = False

                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_ESCAPE :
                                                        changelog("out","BNL's Box "+str(Version_Menu))
                                                        Tuiles_ouverture()
                                                        selection_update = False

                                                if event.type == QUIT:
                                                    if quit_enable and not(update_web):
                                                        STOP()
                                                    elif quit_enable and update_web:
                                                        STOP("Update.bat")

                                    else :

                                        Tuiles_fermeture()
                                        changelog("entry","BNL's Box "+str(Update_Menu))
                                        scroll_changelog = Scroll([1230,150],0, False)

                                        while selection_update:

                                            étape_programme = "Changelog / Update"

                                            if audio_reader_proc.is_finish():
                                                audio_reader_proc.avancer()

                                            if Blur_background:
                                                fenetre.blit(wallpapers_use.blur, (0,0))
                                            else:
                                                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                                                fenetre.blit(fond_visibilité, (0,0))
                                            fenetre.blit(Selection_menu,(455,0))
                                            fenetre.blit(font.render("BNL's Box "+str(Update_Menu), 1, color_menu), (530, 20))
                                            fenetre.blit(changelog_logo,(755,4))

                                            fenetre.blit(bouton_Python, (500,650))
                                            fenetre.blit(bouton_Abord, (700,650))

                                            texte = font.render("Mise à jour disponible :", 5, (255,255,255))
                                            fenetre.blit(texte, (100, 100-scroll_changelog.val))
                                            texte = font_popup.render("BNL's Box : " + str(Version_Menu) + "  ->  " + str(Update_Menu), 5, (255,255,255))
                                            fenetre.blit(texte, (100, 150-scroll_changelog.val))
                                            texte = font_popup.render("BNL's Level : " + str(Version_Level) + "  ->  " + str(Update_Level), 5, (255,255,255))
                                            fenetre.blit(texte, (100, 200-scroll_changelog.val))
                                            texte = font_popup.render("BNL's Update Utility : " + str(Version_Update) + "  ->  " + str(Update_Update), 5, (255,255,255))
                                            fenetre.blit(texte, (100, 250-scroll_changelog.val))
                                            texte = font_popup.render("BNL's Intercomm : " + str(Version_Intercomm) + "  ->  " + str(Update_Intercomm), 5, (255,255,255))
                                            fenetre.blit(texte, (100, 300-scroll_changelog.val))

                                            texte = font_popup.render(chlog_t0, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 350-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t1, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 400-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t2, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 450-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t3, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 500-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t4, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 550-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t5, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 600-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t6, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 650-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t7, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 700-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t8, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 750-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t9, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 800-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t10, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 850-scroll_changelog.val))

                                            texte = font_popup.render(chlog_t11, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 900-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t12, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 950-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t13, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1000-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t14, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1050-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t15, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1100-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t16, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1150-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t17, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1200-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t18, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1250-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t19, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1300-scroll_changelog.val))
                                            texte = font_popup.render(chlog_t20, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1350-scroll_changelog.val))
                                            
                                            texte = font_popup.render(chlog_t21, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1400-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t22, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1450-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t23, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1500-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t24, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1550-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t25, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1600-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t26, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1650-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t27, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1700-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t28, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1750-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t29, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1800-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t30, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1850-scroll_first_start.val))

                                            texte = font_popup.render(chlog_t31, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1900-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t32, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 1950-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t33, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2000-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t34, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2050-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t35, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2100-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t36, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2150-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t37, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2200-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t38, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2250-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t39, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2300-scroll_first_start.val))
                                            texte = font_popup.render(chlog_t40, 5, (255,255,255))
                                            fenetre.blit(texte, (100, 2350-scroll_first_start.val))

                                            a,b= pygame.mouse.get_pos ( )
                                            mouse_stat = pygame.mouse.get_pressed()

                                            if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_changelog.pos.collidepoint(pygame.mouse.get_pos()):
                                                if scroll_changelog.coor[1] < b-scroll_bar_decalage[1]:
                                                    scroll_changelog.val -= (scroll_changelog.coor[1] - (b-scroll_bar_decalage[1]))*4
                                                elif scroll_changelog.coor[1] > b-scroll_bar_decalage[1]:
                                                    scroll_changelog.val += -(scroll_changelog.coor[1] - (b-scroll_bar_decalage[1]))*4
                                                scroll_changelog.coor[1] = b-scroll_bar_decalage[1]
                                                scroll_changelog.pos = scroll_bar.get_rect(topleft=scroll_changelog.coor)

                                            fenetre.blit(scroll_bar,scroll_changelog.coor)

                                            pygame.display.flip()

                                            for event in pygame.event.get():
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_stat = pygame.mouse.get_pressed()
                                                    if mouse_stat[0]:
                                                        if pos_bouton_Python.collidepoint(event.pos):
                                                            if Update_check_web:
                                                                download_thread = Thread(target=Download_thread, args=("https://drive.google.com/u/1/uc?id="+update_file_link+"&export=download","Level mise à niveau.zip"))
                                                                download_thread.start()
                                                                changelog("out","BNL's Box "+str(Update_Menu))
                                                                Tuiles_ouverture()
                                                                selection_update = False
                                                            else:
                                                                continuer=False
                                                                selection_update = False
                                                                STOP("Update.bat")
                                                        if pos_bouton_Abord.collidepoint(event.pos):
                                                            changelog("out","BNL's Box "+str(Update_Menu))
                                                            Tuiles_ouverture()
                                                            selection_update = False
                                                        if scroll_changelog.pos.collidepoint(event.pos):
                                                            scroll_bar_decalage = [a-scroll_changelog.coor[0],b-scroll_changelog.coor[1]]

                                                if event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                                        changelog("out","BNL's Box "+str(Update_Menu))
                                                        Tuiles_ouverture()
                                                        selection_update = False

                                                if event.type == pygame.MOUSEWHEEL:
                                                    scroll_changelog.stat = False
                                                    a = 0
                                                    b = event.y
                                                    scroll_bar_decalage = [0,0]

                                                    if scroll_changelog.coor[1]-b*10 >= 150 and scroll_changelog.coor[1]-b*10 <= 550 :
                                                        scroll_changelog.val -= b*40
                                                        scroll_changelog.coor[1] -= b*10
                                                        scroll_changelog.pos = scroll_bar.get_rect(topleft=scroll_changelog.coor)

                                                if event.type == QUIT:
                                                    if quit_enable and not(update_web):
                                                        STOP()
                                                    elif quit_enable and update_web:
                                                        STOP("Update.bat")

                                except FileNotFoundError:
                                    texte = font.render("Aucun fichier de mise à niveau trouvé", 1, (color_txt))
                                    fenetre.blit(texte, (700, 502))
                                    pygame.display.flip()
                                    time.sleep(3)
                                except Exception as e:
                                    print(e)
                                    fenetre.blit(texte, (700, 502))
                                    pygame.display.flip()
                                    time.sleep(3)

                            if pos_ON_OFF_update.collidepoint(event.pos):
                                if Update_at_start :
                                    data_base.update("Update_at_start","0")
                                else :
                                    data_base.update("Update_at_start","1")

                            if pos_ON_OFF_update_web.collidepoint(event.pos):
                                if Update_check_web :
                                    data_base.update("Update_check_web","0")
                                else :
                                    data_base.update("Update_check_web","1")

                            if pos_Menu.collidepoint(event.pos):
                                paramètres=False
                                animations_continuer=False
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False

                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    Tuiles_fermeture()
                                    transition_ouverture(322)

                            if pos_Infos.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                paramètres=True
                                fond_écran=False
                                upgrade_continuer=False
                                animations_continuer=False
                                version_continuer=True

                            if pos_Fond_paramètres.collidepoint(event.pos):
                                paramètres=True
                                menu_continuer=False
                                soundtrack=False
                                bonus_continuer=False
                                animations_continuer=False
                                fond_écran=True
                                upgrade_continuer=False
                                version_continuer=False

                            if pos_Modules.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                paramètres=True
                                fond_écran=False
                                animations_continuer=False
                                upgrade_continuer=True
                                version_continuer=False

                            if pos_Animations.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                animations_continuer=True
                                fond_écran=False
                                paramètres=True
                                upgrade_continuer=False
                                version_continuer=False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_DOWN:
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False

                        if event.key == K_ESCAPE:
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False

                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(322)
                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            # Menu paramètres (onglet version et mise à jour des modules)
            while upgrade_continuer:
                étape_programme = "Paramètres / Versions et mise à jour des modules"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                pos_ON_OFF_modules_prew = ON_OFF_maker.get_rect(topleft=(850,950-scroll_version.val))
                pos_bouton_update_all_python = bouton_update_all_python.get_rect(topleft=(250,850-scroll_version.val))
                pos_bouton_delete_all_python = bouton_delete_all_python.get_rect(topleft=(500,850-scroll_version.val))

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules1,(0,180))
                fenetre.blit(Animations,(0,360))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))
                
                texte = font_underline.render("Modules installés :", 1, (color_txt))
                fenetre.blit(texte, (250, 100-scroll_version.val))

                texte = font.render("Version Pip -> "+str(pip.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 200-scroll_version.val))
                texte = font.render("Version Psutil -> "+str(psutil.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 250-scroll_version.val))
                texte = font.render("Version Pygame -> "+str(pygame.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 300-scroll_version.val))
                texte = font.render("Version Music_tag -> "+str(music_tag.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 350-scroll_version.val))
                texte = font.render("Version Pillow -> "+str(PIL.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 400-scroll_version.val))
                texte = font.render("Version Pyperclip -> "+str(pyperclip.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 450-scroll_version.val))
                texte = font.render("Version Gdown -> "+str(gdown.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 500-scroll_version.val))
                texte = font.render("Version Yt-dlp -> "+str(yt_dlp.version.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 550-scroll_version.val))
                texte = font.render("Version Easygui -> "+str(easygui.egversion), 1, (color_txt))
                fenetre.blit(texte, (250, 600-scroll_version.val))
                texte = font.render("Version Djitellopy -> Non communiqué", 1, (color_txt))
                fenetre.blit(texte, (250, 650-scroll_version.val))
                texte = font.render("Version Cv2 -> "+str(cv2.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 700-scroll_version.val))
                texte = font.render("Version Numpy -> "+str(numpy.__version__), 1, (color_txt))
                fenetre.blit(texte, (250, 750-scroll_version.val))

                fenetre.blit(bouton_update_all_python, (250, 850-scroll_version.val))
                fenetre.blit(bouton_delete_all_python, (500, 850-scroll_version.val))

                texte = font.render(langue.param_preview_module, 1, (color_txt))
                fenetre.blit(texte, (250, 950-scroll_version.val))

                fenetre.blit(ON_OFF_maker,(850,950-scroll_version.val))

                if Modules_preview:
                    fenetre.blit(ON,(855,955-scroll_version.val))
                else:
                    fenetre.blit(OFF,(885,955-scroll_version.val))

                a,b= pygame.mouse.get_pos ()

                mouse_stat = pygame.mouse.get_pressed()

                if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_version.pos.collidepoint(pygame.mouse.get_pos()) :
                    if scroll_version.coor[1] < b-scroll_bar_decalage[1]:
                        scroll_version.val -= (scroll_version.coor[1] - (b-scroll_bar_decalage[1]))*2
                    elif scroll_version.coor[1] > b-scroll_bar_decalage[1]:
                        scroll_version.val += -(scroll_version.coor[1] - (b-scroll_bar_decalage[1]))*2
                    scroll_version.coor[1] = b-scroll_bar_decalage[1]
                    scroll_version.pos = scroll_bar.get_rect(topleft=scroll_version.coor)

                fenetre.blit(scroll_bar,scroll_version.coor)

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_bouton_update_all_python.collidepoint(event.pos):
                                continuer = False
                                if Modules_preview:
                                    STOP("Update all(preview)")
                                else:
                                    STOP("Update all")
                            if pos_bouton_delete_all_python.collidepoint(event.pos):
                                continuer = False
                                STOP("Delete all")

                            if pos_ON_OFF_modules_prew.collidepoint(event.pos):
                                if Modules_preview :
                                    data_base.update("Modules_preview","0")
                                else :
                                    data_base.update("Modules_preview","1")

                            if pos_Menu.collidepoint(event.pos):
                                paramètres=False
                                animations_continuer=False
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False

                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    Tuiles_fermeture()
                                    transition_ouverture(322)

                            if pos_Infos.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                paramètres=True
                                fond_écran=False
                                animations_continuer=False
                                upgrade_continuer=False
                                version_continuer=True

                            if pos_Animations.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                animations_continuer=True
                                fond_écran=False
                                paramètres=False
                                upgrade_continuer=False
                                version_continuer=False

                            if pos_Fond_paramètres.collidepoint(event.pos):
                                paramètres=True
                                menu_continuer=False
                                soundtrack=False
                                bonus_continuer=False
                                animations_continuer=False
                                fond_écran=True
                                upgrade_continuer=False
                                version_continuer=False
                            if scroll_version.pos.collidepoint(event.pos):
                                scroll_bar_decalage = [a-scroll_version.coor[0],b-scroll_version.coor[1]]

                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_DOWN:
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            animations_continuer=True
                            fond_écran=False
                            paramètres=False
                            upgrade_continuer=False
                            version_continuer=False
                        if event.key == pygame.K_UP:
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=True

                        if event.key == K_ESCAPE:
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False

                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(322)

                    if event.type == pygame.MOUSEWHEEL:
                        scroll_version.stat = False
                        a = 0
                        b = scroll_version.coor[1]-event.y
                        scroll_bar_decalage = [0,0]

                        if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 :
                            if scroll_version.coor[1] < b-scroll_bar_decalage[1]:
                                scroll_version.val -= (scroll_version.coor[1] - (b-scroll_bar_decalage[1]))*2
                            elif scroll_version.coor[1] > b-scroll_bar_decalage[1]:
                                scroll_version.val += -(scroll_version.coor[1] - (b-scroll_bar_decalage[1]))*2
                            scroll_version.coor[1] = b-scroll_bar_decalage[1]
                            scroll_version.pos = scroll_bar.get_rect(topleft=scroll_version.coor)

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            # Menu paramètres (onglet gestion du système : animations, transitions, AdaptoRAM, console, volume, etc.)
            while animations_continuer:
                étape_programme = "Paramètres / Avancés et console"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                a,b= pygame.mouse.get_pos ( )

                pos_ON_OFF_full_screen = ON_OFF_maker.get_rect(topleft=(850,167-scroll_animations.val))
                pos_ON_OFF_animations = ON_OFF_maker.get_rect(topleft=(850,207-scroll_animations.val))
                pos_ON_OFF_transitions = ON_OFF_maker.get_rect(topleft=(850,247-scroll_animations.val))
                pos_ON_OFF_AdaptoRAM = ON_OFF_maker.get_rect(topleft=(850,287-scroll_animations.val))
                pos_sound_up_general = sound_up.get_rect(topleft=(1050,490-scroll_animations.val))
                pos_sound_down_general = sound_down.get_rect(topleft=(750,490-scroll_animations.val))
                pos_ON_OFF_blur_background = ON_OFF_maker.get_rect(topleft=(850,600-scroll_animations.val))

                pos_DOWN_blur = DOWN_button.get_rect(topleft=(950,600-scroll_animations.val))
                pos_UP_blur = UP_button.get_rect(topleft=(1050,600-scroll_animations.val))

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Infos,(0,0))
                fenetre.blit(Modules,(0,180))
                fenetre.blit(Animations1,(0,360))
                fenetre.blit(Fond_paramètres,(0,540))
                fenetre.blit(Menu,(1150,20))

                texte = font_underline.render("Paramètres avancés :", 1, (color_txt))
                fenetre.blit(texte, (250, 100-scroll_animations.val))

                fenetre.blit(ON_OFF_maker,(850,167-scroll_animations.val))
                fenetre.blit(ON_OFF_maker,(850,207-scroll_animations.val))
                fenetre.blit(ON_OFF_maker,(850,247-scroll_animations.val))
                fenetre.blit(ON_OFF_maker,(850,287-scroll_animations.val))
                fenetre.blit(ON_OFF_maker,(850,600-scroll_animations.val))

                if Blur_background:
                    fenetre.blit(DOWN_button, (950,600-scroll_animations.val))
                    texte = font_widget.render(str(Blur_radius), 1, (color_txt))
                    fenetre.blit(texte, (1000, 605-scroll_animations.val))
                    fenetre.blit(UP_button, (1050,600-scroll_animations.val))

                if full_screen:
                    fenetre.blit(ON,(855,172-scroll_animations.val))
                else:
                    fenetre.blit(OFF,(885,172-scroll_animations.val))

                if animations:
                    fenetre.blit(ON,(855,212-scroll_animations.val))
                else:
                    fenetre.blit(OFF,(885,212-scroll_animations.val))

                if transition_check:
                    fenetre.blit(ON,(855,252-scroll_animations.val))
                else:
                    fenetre.blit(OFF,(885,252-scroll_animations.val))

                if AdaptoRAM_check:
                    fenetre.blit(ON,(855,292-scroll_animations.val))
                else:
                    fenetre.blit(OFF,(885,292-scroll_animations.val))

                if Blur_background:
                    fenetre.blit(ON,(855,605-scroll_animations.val))
                else:
                    fenetre.blit(OFF,(885,605-scroll_animations.val))

                texte = font.render(langue.param_full_screen, 1, (color_txt))
                fenetre.blit(texte, (250, 167-scroll_animations.val))
                texte = font.render(langue.param_animations, 1, (color_txt))
                fenetre.blit(texte, (250, 207-scroll_animations.val))
                texte = font.render(langue.param_transitions, 1, (color_txt))
                fenetre.blit(texte, (250, 247-scroll_animations.val))
                texte = font.render(langue.param_adaptoRAM, 1, (color_txt))
                fenetre.blit(texte, (250, 287-scroll_animations.val))
                texte = font.render(langue.param_RAM_free+ str(int((psutil.virtual_memory()[1])/1000000))+" Mo", 1, (color_txt))
                fenetre.blit(texte, (250, 327-scroll_animations.val))

                if Console_s == 0 :
                    if Console_t == "":
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(250,447-scroll_animations.val,510, 30),2,50)
                    else:
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                else :
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)

                texte = font.render(langue.param_console, 1, (color_txt))
                fenetre.blit(texte, (250, 407-scroll_animations.val))
                texte = font_popup.render(Console_t, 1, (0,0,0))
                fenetre.blit(texte, (255, 449-scroll_animations.val))
                texte = font.render(langue.param_sound_volume, 1, (color_txt))
                fenetre.blit(texte, (250, 515-scroll_animations.val))
                fenetre.blit(sound_down, (750, 490-scroll_animations.val))
                fenetre.blit(sound_up, (1050, 490-scroll_animations.val))
                sound_viewer_pos = pygame.mixer.music.get_volume()*200
                fenetre.blit(sound_viewer_general,(830+sound_viewer_pos,490-scroll_animations.val))

                texte = font.render(langue.param_blur_background, 1, (color_txt))
                fenetre.blit(texte, (250, 600-scroll_animations.val))

                mouse_stat = pygame.mouse.get_pressed()

                if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_animations.pos.collidepoint(pygame.mouse.get_pos()) :
                    if scroll_animations.coor[1] < b-scroll_bar_decalage[1]:
                        scroll_animations.val -= (scroll_animations.coor[1] - (b-scroll_bar_decalage[1]))*2
                    elif scroll_animations.coor[1] > b-scroll_bar_decalage[1]:
                        scroll_animations.val += -(scroll_animations.coor[1] - (b-scroll_bar_decalage[1]))*2
                    scroll_animations.coor[1] = b-scroll_bar_decalage[1]
                    scroll_animations.pos = scroll_bar.get_rect(topleft=scroll_animations.coor)

                fenetre.blit(scroll_bar,scroll_animations.coor)

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(400,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if event.pos[0] >= 250 and event.pos[0] <= 760 and event.pos[1] >= 449-scroll_animations.val and event.pos[1] <= 479-scroll_animations.val :
                                Console_s = 1
                            else :
                                Console_s = 0

                            if pos_Menu.collidepoint(event.pos):
                                paramètres=False
                                animations_continuer=False
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False

                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    Tuiles_fermeture()
                                    transition_ouverture(322)

                            if pos_Infos.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                paramètres=True
                                fond_écran=False
                                upgrade_continuer=False
                                animations_continuer=False
                                version_continuer=True

                            if pos_Modules.collidepoint(event.pos):
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                paramètres=True
                                fond_écran=False
                                animations_continuer=False
                                upgrade_continuer=True
                                version_continuer=False

                            if pos_Fond_paramètres.collidepoint(event.pos):
                                paramètres=False
                                menu_continuer=False
                                soundtrack=False
                                bonus_continuer=False
                                animations_continuer=False
                                fond_écran=True
                                upgrade_continuer=False
                                version_continuer=False

                            if pos_ON_OFF_full_screen.collidepoint(event.pos):
                                if full_screen :
                                    data_base.update("full_screen","0")
                                    fenetre = pygame.display.set_mode((1280,720))
                                else :
                                    data_base.update("full_screen","1")
                                    flags = FULLSCREEN
                                    fenetre = pygame.display.set_mode(taille, flags)

                            if pos_ON_OFF_animations.collidepoint(event.pos):
                                if animations :
                                    data_base.update("animations","0")
                                else :
                                    data_base.update("animations","1")

                            if pos_ON_OFF_transitions.collidepoint(event.pos):
                                if transition_check:
                                    data_base.update("transition_check","0")
                                else:
                                    data_base.update("transition_check","1")

                            if pos_ON_OFF_AdaptoRAM.collidepoint(event.pos):
                                if AdaptoRAM_check:
                                    data_base.update("AdaptoRAM_check","0")
                                else:
                                    data_base.update("AdaptoRAM_check","1")

                            if pos_sound_up_general.collidepoint(event.pos) and volume_BNL < 10:
                                fenetre.blit(sound_up1, (1050, 490-scroll_animations.val))
                                pygame.display.flip()
                                volume_BNL += 1
                                data_base.update("volume_BNL", str(volume_BNL))
                                time.sleep(0.1)
                                pygame.mixer.music.set_volume(volume_BNL/10)

                            if pos_sound_down_general.collidepoint(event.pos) and volume_BNL > 0 :
                                fenetre.blit(sound_down1, (750, 490-scroll_animations.val))
                                pygame.display.flip()
                                volume_BNL -= 1
                                data_base.update("volume_BNL", str(volume_BNL))
                                time.sleep(0.1)
                                pygame.mixer.music.set_volume(volume_BNL/10)

                            if pos_ON_OFF_blur_background.collidepoint(event.pos):
                                if Blur_background :
                                    data_base.update("Blur_background","0")
                                else :
                                    data_base.update("Blur_background","1")

                            if pos_UP_blur.collidepoint(event.pos) and Blur_radius < 50 and Blur_background:
                                fenetre.blit(UP_button1, (1050, 600-scroll_animations.val))
                                Blur_radius += 2
                                pygame.display.flip()
                                data_base.update("Blur_radius", str(Blur_radius))
                                time.sleep(0.1)
                                wallpapers_use.create_blur(Blur_radius)

                            if pos_DOWN_blur.collidepoint(event.pos) and Blur_radius > 0 and Blur_background:
                                fenetre.blit(DOWN_button1, (950, 600-scroll_animations.val))
                                Blur_radius -= 2
                                pygame.display.flip()
                                data_base.update("Blur_radius", str(Blur_radius))
                                time.sleep(0.1)
                                wallpapers_use.create_blur(Blur_radius)

                            if scroll_animations.pos.collidepoint(event.pos):
                                scroll_bar_decalage = [a-scroll_animations.coor[0],b-scroll_animations.coor[1]]

                    if event.type == pygame.KEYDOWN :
                        key = pygame.key.get_pressed()
                        if event.key == pygame.K_DOWN:
                            paramètres=False
                            menu_continuer=False
                            soundtrack=False
                            bonus_continuer=False
                            animations_continuer=False
                            fond_écran=True
                            upgrade_continuer=False
                            version_continuer=False
                        if event.key == pygame.K_UP:
                            soundtrack=False
                            menu_continuer=False
                            bonus_continuer=False
                            paramètres=True
                            fond_écran=False
                            animations_continuer=False
                            upgrade_continuer=True
                            version_continuer=False

                        elif key[pygame.K_LCTRL] and key[pygame.K_v]:
                            if (len(Console_t) + len(pyperclip.paste())) < 56:
                                Console_t += pyperclip.paste()

                        if event.key == K_ESCAPE:
                            paramètres=False
                            animations_continuer=False
                            fond_écran=False
                            upgrade_continuer=False
                            version_continuer=False

                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                Tuiles_fermeture()
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                Tuiles_fermeture()
                                transition_ouverture(322)

                        if Console_s == 1:
                            if event.key == pygame.K_SPACE :
                                Console_t += " "
                            elif event.key == pygame.K_BACKSPACE :
                                Console_t = Console_t[:-1]
                            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                                if Console_t.upper() == "STOP":
                                    STOP()
                                elif Console_t.upper() == "RESTART":
                                    STOP("Menu.bat")
                                elif Console_t.upper() == "Update/":
                                    STOP("Update.bat")
                                elif Console_t == "Update/all":
                                    fichier=open("Update_check.py","w")
                                    fichier.write('import os'+"\n")
                                    fichier.write('update_del = os.listdir()'+"\n")
                                    fichier.write("update_unzip = 'all'"+"\n")
                                    fichier.write('update_process = ["Update.delete(update_del)", "Update.unzip(update_unzip)"]'+"\n")
                                    fichier.close()
                                    STOP("Update.bat")

                                elif Console_t == "file_list/update":
                                    file_list_temp = os.listdir()
                                    file_list = []

                                    for i in file_list_temp:
                                        if not("__pycache__" in i):
                                            if os.path.isfile(i):
                                                file_list.append(i)
                                            else :
                                                for (dirpath, dirnames, filenames) in os.walk(i):
                                                    file_list += [os.path.join(dirpath, file) for file in filenames if not("__pycache__" in os.path.join(dirpath, file)) ]

                                    fichier=open("file_list.py","w")
                                    fichier.write("file_list = " + str(file_list))
                                    fichier.close()
                                    Console_t = langue.param_console_checking_file
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                    texte = font_popup.render(Console_t, 1, (0,0,0))
                                    fenetre.blit(texte, (255, 449-scroll_animations.val))
                                    pygame.display.flip()
                                    time.sleep(1)
                                    try:
                                        from file_list import*
                                        Console_t = langue.param_console_done
                                    except:
                                        Console_t = langue.param_console_failed
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                    texte = font_popup.render(Console_t, 1, (0,0,0))
                                    fenetre.blit(texte, (255, 449-scroll_animations.val))
                                    pygame.display.flip()
                                    time.sleep(1)


                                elif Console_t == "error/":
                                    animations_continuer = False
                                    paramètres = False
                                    continuer = False
                                    erreur_report = True
                                    data_base.exit()

                                elif Console_t == "log/read":
                                    os.startfile("log.txt")

                                elif Console_t == "log/erase":
                                    fichier = open("log.txt","w")
                                    fichier.close()
                                    Console_t = langue.param_console_done
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                    texte = font_popup.render(Console_t, 1, (0,0,0))
                                    fenetre.blit(texte, (255, 449-scroll_animations.val))
                                    pygame.display.flip()
                                    time.sleep(1)
                                elif Console_t.startswith("data_base"):
                                    try :
                                        eval(Console_t)
                                        Console_t = langue.param_console_done
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                        texte = font_popup.render(Console_t, 1, (0,0,0))
                                        fenetre.blit(texte, (255, 449-scroll_animations.val))
                                        pygame.display.flip()
                                        time.sleep(1)
                                    except:
                                        Console_t = langue.param_console_unknown_command
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                        texte = font_popup.render(Console_t, 1, (0,0,0))
                                        fenetre.blit(texte, (255, 449-scroll_animations.val))
                                        pygame.display.flip()
                                        time.sleep(1)
                                elif Console_t.startswith("system_timer("):
                                    try :
                                        timer_temp = Console_t.partition("system_timer(")[2][:-1]
                                        timer_temp1 = int(timer_temp.split(",", 1)[0])
                                        action = timer_temp.split(",", 1)[1]
                                        system_timer_thread = Thread(target=system_timer, args=(timer_temp1,action))
                                        system_timer_thread.start()
                                        Console_t = langue.param_console_done
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                        texte = font_popup.render(Console_t, 1, (0,0,0))
                                        fenetre.blit(texte, (255, 449-scroll_animations.val))
                                        pygame.display.flip()
                                        time.sleep(1)
                                    except Exception as e:
                                        print(e)
                                        Console_t = langue.param_console_unknown_command
                                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                        texte = font_popup.render(Console_t, 1, (0,0,0))
                                        fenetre.blit(texte, (255, 449-scroll_animations.val))
                                        pygame.display.flip()
                                        time.sleep(1)
                                else :
                                    Console_t = langue.param_console_unknown_command
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(250,447-scroll_animations.val,510, 30),15,50)
                                    texte = font_popup.render(Console_t, 1, (0,0,0))
                                    fenetre.blit(texte, (255, 449-scroll_animations.val))
                                    pygame.display.flip()
                                    time.sleep(1)
                                Console_t = ""
                            elif len(Console_t) > 55 :
                                Console_t = ""

                            else :
                                Console_t += event.unicode

                    if event.type == pygame.MOUSEWHEEL:
                        scroll_animations.stat = False
                        a = 0
                        b = scroll_animations.coor[1]-event.y
                        scroll_bar_decalage = [0,0]

                        if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 :
                            if scroll_animations.coor[1] < b-scroll_bar_decalage[1]:
                                scroll_animations.val -= (scroll_animations.coor[1] - (b-scroll_bar_decalage[1]))*2
                            elif scroll_animations.coor[1] > b-scroll_bar_decalage[1]:
                                scroll_animations.val += -(scroll_animations.coor[1] - (b-scroll_bar_decalage[1]))*2
                            scroll_animations.coor[1] = b-scroll_bar_decalage[1]
                            scroll_animations.pos = scroll_bar.get_rect(topleft=scroll_animations.coor)

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            # Menu paramètres (onglet personnalisation du système : fond, couleur, skin, thèmes, etc.)
            while fond_écran:
                theme_init_search = True
                wallpapers_init_search = True
                font_init_search = True
                while fond_page == 1 :
                    a,b= pygame.mouse.get_pos ( )
                    étape_programme = "Paramètres / Personnalisation"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if AdaptoRAM_check:
                        if psutil.virtual_memory()[1] < RAM_free:
                            animations = False
                            transition_check = False

                    pos_fondmenu0_a = fondmenu0_a.get_rect(topleft=(250,200-scroll_fond.val))
                    pos_fondmenu1_a = fondmenu1_a.get_rect(topleft=(460,200-scroll_fond.val))
                    pos_fondmenu2_a = fondmenu1_a.get_rect(topleft=(670,200-scroll_fond.val))
                    pos_fondmenu3_a = fondmenu3_a.get_rect(topleft=(880,200-scroll_fond.val))
                    pos_fondmenu4_a = fondmenu4_a.get_rect(topleft=(250,323-scroll_fond.val))
                    pos_fondmenu5_a = fondmenu5_a.get_rect(topleft=(460,323-scroll_fond.val))
                    pos_fondmenu6_a = fondmenu6_a.get_rect(topleft=(670,323-scroll_fond.val))
                    pos_fondmenu7_a = fondmenu7_a.get_rect(topleft=(880,323-scroll_fond.val))

                    pos_titanium_widgets_BNL = titanium_widgets_BNL.get_rect(topleft=(250,650-scroll_fond.val))
                    pos_old_style = old_style.get_rect(topleft=(550,650-scroll_fond.val))
                    pos_carroussel_skin = carroussel_skin.get_rect(topleft=(850,650-scroll_fond.val))
                    pos_MINI_Picture_original = MINI_Picture_original.get_rect(topleft=(250,900-scroll_fond.val))
                    pos_MINI_Picture_original_black_theme = MINI_Picture_original_black_theme.get_rect(topleft=(550,900-scroll_fond.val))
                    pos_MINI_Picture_original_alpha_theme = MINI_Picture_original_alpha_theme.get_rect(topleft=(850,900-scroll_fond.val))

                    pos_Violet = Violet.get_rect(topleft=(540,450-scroll_fond.val))
                    pos_Jaune = Jaune.get_rect(topleft=(580,450-scroll_fond.val))
                    pos_Rouge = Rouge.get_rect(topleft=(620,450-scroll_fond.val))
                    pos_Vert = Vert.get_rect(topleft=(660,450-scroll_fond.val))
                    pos_Cyan = Cyan.get_rect(topleft=(700,450-scroll_fond.val))
                    pos_Bleu = Bleu.get_rect(topleft=(740,450-scroll_fond.val))
                    pos_Violet_r = Violet.get_rect(topleft=(540,500-scroll_fond.val))
                    pos_Jaune_r = Jaune.get_rect(topleft=(580,500-scroll_fond.val))
                    pos_Rouge_r = Rouge.get_rect(topleft=(620,500-scroll_fond.val))
                    pos_Vert_r = Vert.get_rect(topleft=(660,500-scroll_fond.val))
                    pos_Cyan_r = Cyan.get_rect(topleft=(700,500-scroll_fond.val))
                    pos_Bleu_r = Bleu.get_rect(topleft=(740,500-scroll_fond.val))

                    pos_more_colors = more_colors.get_rect(topleft=(250,540-scroll_fond.val))
                    pos_more_themes = more_themes.get_rect(topleft=(250,1060-scroll_fond.val))
                    pos_more_wallpapers = more_wallpapers.get_rect(topleft=(1090,200-scroll_fond.val))
                    pos_more_fonts = more_fonts.get_rect(topleft=(250,1320-scroll_fond.val))

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                    fenetre.blit(Infos,(0,0))
                    fenetre.blit(Modules,(0,180))
                    fenetre.blit(Animations,(0,360))
                    fenetre.blit(Fond_paramètres1,(0,540))
                    fenetre.blit(Menu,(1150,20))

                    texte = font_underline.render("Personnalisation :", 1, (color_txt))
                    fenetre.blit(texte, (250, 100-scroll_fond.val))
                    
                    fenetre.blit(fondmenu0_a,(250,200-scroll_fond.val))
                    fenetre.blit(fondmenu1_a,(460,200-scroll_fond.val))
                    fenetre.blit(fondmenu2_a,(670,200-scroll_fond.val))
                    fenetre.blit(fondmenu3_a,(880,200-scroll_fond.val))
                    fenetre.blit(fondmenu4_a,(250,323-scroll_fond.val))
                    fenetre.blit(fondmenu5_a,(460,323-scroll_fond.val))
                    fenetre.blit(fondmenu6_a,(670,323-scroll_fond.val))
                    fenetre.blit(fondmenu7_a,(880,323-scroll_fond.val))
                    fenetre.blit(more_wallpapers,(1090,200-scroll_fond.val))

                    texte = font.render(langue.param_wallpapers, 1, (color_txt))
                    fenetre.blit(texte, (250, 150-scroll_fond.val))

                    texte = font.render(langue.param_color_text, 1, (color_txt))
                    fenetre.blit(texte, (250, 450-scroll_fond.val))
                    pygame.draw.rect(fenetre, color_aux, pygame.Rect(250,495-scroll_fond.val,270, 35))
                    texte = font.render(langue.param_color_aux, 1, (0,0,0))
                    fenetre.blit(texte, (250, 500-scroll_fond.val))
                    texte = font.render(langue.param_skin, 1, color_txt)
                    fenetre.blit(texte, (250, 600-scroll_fond.val))
                    fenetre.blit(titanium_widgets_BNL,(250,650-scroll_fond.val))
                    fenetre.blit(old_style,(550,650-scroll_fond.val))
                    fenetre.blit(carroussel_skin,(850,650-scroll_fond.val))
                    texte = font.render(langue.param_theme, 1, color_txt)
                    fenetre.blit(texte, (250, 850-scroll_fond.val))
                    fenetre.blit(MINI_Picture_original,(250,900-scroll_fond.val))
                    fenetre.blit(MINI_Picture_original_black_theme,(550,900-scroll_fond.val))
                    fenetre.blit(MINI_Picture_original_alpha_theme,(850,900-scroll_fond.val))
                    fenetre.blit(more_themes,(250,1060-scroll_fond.val))

                    texte = font.render(langue.param_auto_theme, 1, (color_txt))
                    fenetre.blit(texte, (420, 1065-scroll_fond.val))
                    fenetre.blit(ON_OFF_maker,(850,1065-scroll_fond.val))
                    pos_ON_OFF_Auto_theme = ON_OFF_maker.get_rect(topleft=(850,1065-scroll_fond.val))

                    if Auto_theme:
                        fenetre.blit(ON,(855,1070-scroll_fond.val))
                    else:
                        fenetre.blit(OFF,(885,1070-scroll_fond.val))

                    texte = font.render(langue.param_fonts, 1, color_txt)
                    fenetre.blit(texte, (250, 1150-scroll_fond.val))
                    fenetre.blit(Overpass,(250,1200-scroll_fond.val))
                    fenetre.blit(DynaPuff,(460,1200-scroll_fond.val))
                    fenetre.blit(SourceSansPro,(670,1200-scroll_fond.val))
                    fenetre.blit(Great_Vibes,(880,1200-scroll_fond.val))
                    fenetre.blit(more_fonts,(250,1320-scroll_fond.val))

                    pos_font0_a = Overpass.get_rect(topleft=(250,1200-scroll_fond.val))
                    pos_font1_a = DynaPuff.get_rect(topleft=(460,1200-scroll_fond.val))
                    pos_font2_a = SourceSansPro.get_rect(topleft=(670,1200-scroll_fond.val))
                    pos_font3_a = Great_Vibes.get_rect(topleft=(880, 1200-scroll_fond.val))

                    texte = font.render(langue.param_lang, 1, (color_txt))
                    fenetre.blit(texte, (250, 1400-scroll_fond.val))
                    fenetre.blit(french_lang,(250,1450-scroll_fond.val))
                    fenetre.blit(english_lang,(460,1450-scroll_fond.val))
                    fenetre.blit(spanish_lang,(670,1450-scroll_fond.val))

                    pos_french = french_lang.get_rect(topleft=(250,1450-scroll_fond.val))
                    pos_english = english_lang.get_rect(topleft=(460,1450-scroll_fond.val))
                    pos_spanish = english_lang.get_rect(topleft=(670,1450-scroll_fond.val))

                    if color_txt == (255,0,255):
                        pygame.draw.rect(fenetre, color_txt, pygame.Rect(535,445-scroll_fond.val,40, 40))
                    elif color_txt == (255,255,0):
                        pygame.draw.rect(fenetre, color_txt, pygame.Rect(575,445-scroll_fond.val,40, 40))
                    elif color_txt == (255,0,0):
                        pygame.draw.rect(fenetre, color_txt, pygame.Rect(615,445-scroll_fond.val,40, 40))
                    elif color_txt == (0,255,0):
                        pygame.draw.rect(fenetre, color_txt, pygame.Rect(655,445-scroll_fond.val,40, 40))
                    elif color_txt == (0,255,255):
                        pygame.draw.rect(fenetre, color_txt, pygame.Rect(695,445-scroll_fond.val,40, 40))
                    elif color_txt == (0,0,255):
                        pygame.draw.rect(fenetre, color_txt, pygame.Rect(735,445-scroll_fond.val,40, 40))

                    if color_aux == (255,0,255):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(535,495-scroll_fond.val,40, 40))
                    elif color_aux == (255,255,0):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(575,495-scroll_fond.val,40, 40))
                    elif color_aux == (255,0,0):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(615,495-scroll_fond.val,40, 40))
                    elif color_aux == (0,255,0):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(655,495-scroll_fond.val,40, 40))
                    elif color_aux == (0,255,255):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(695,495-scroll_fond.val,40, 40))
                    elif color_aux == (0,0,255):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(735,495-scroll_fond.val,40, 40))

                    fenetre.blit(Violet,(540,450-scroll_fond.val))
                    fenetre.blit(Jaune,(580,450-scroll_fond.val))
                    fenetre.blit(Rouge,(620,450-scroll_fond.val))
                    fenetre.blit(Vert,(660,450-scroll_fond.val))
                    fenetre.blit(Cyan,(700,450-scroll_fond.val))
                    fenetre.blit(Bleu,(740,450-scroll_fond.val))
                    fenetre.blit(Violet,(540,500-scroll_fond.val))
                    fenetre.blit(Jaune,(580,500-scroll_fond.val))
                    fenetre.blit(Rouge,(620,500-scroll_fond.val))
                    fenetre.blit(Vert,(660,500-scroll_fond.val))
                    fenetre.blit(Cyan,(700,500-scroll_fond.val))
                    fenetre.blit(Bleu,(740,500-scroll_fond.val))

                    fenetre.blit(more_colors,(250,540-scroll_fond.val))

                    if fond_selection=="fondmenu0":
                        fenetre.blit(Selection,(245,200-scroll_fond.val))
                    elif fond_selection=="fondmenu1":
                        fenetre.blit(Selection,(455,200-scroll_fond.val))
                    elif fond_selection=="fondmenu2":
                        fenetre.blit(Selection,(665,200-scroll_fond.val))
                    elif fond_selection=="fondmenu3":
                        fenetre.blit(Selection,(875,200-scroll_fond.val))
                    elif fond_selection=="fondmenu4":
                        fenetre.blit(Selection,(245,323-scroll_fond.val))
                    elif fond_selection=="fondmenu5":
                        fenetre.blit(Selection,(455,323-scroll_fond.val))
                    elif fond_selection=="fondmenu6":
                        fenetre.blit(Selection,(665,323-scroll_fond.val))
                    elif fond_selection=="fondmenu7":
                        fenetre.blit(Selection,(875,323-scroll_fond.val))
                    else:
                        fenetre.blit(Selection,(1085,200-scroll_fond.val))

                    if Skin_selected == "Titanium":
                        fenetre.blit(Selection,(245,650-scroll_fond.val))
                    elif Skin_selected == "Legacy":
                        fenetre.blit(Selection,(545,650-scroll_fond.val))
                    elif Skin_selected == "Carroussel":
                        fenetre.blit(Selection,(845,650-scroll_fond.val))

                    if theme_selected == "MINI_Picture_original":
                        fenetre.blit(Selection,(245,900-scroll_fond.val))
                    elif theme_selected == "MINI_Picture_original_black_theme":
                        fenetre.blit(Selection,(545,900-scroll_fond.val))
                    elif theme_selected == "MINI_Picture_original_alpha_theme":
                        fenetre.blit(Selection,(845,900-scroll_fond.val))
                    else:
                        fenetre.blit(Selection,(245,1060-scroll_fond.val))

                    if font_selected=='Fonts/font0/font.ttf':
                        fenetre.blit(Selection,(245,1200-scroll_fond.val))
                    elif font_selected=='Fonts/font1/font.ttf':
                        fenetre.blit(Selection,(455,1200-scroll_fond.val))
                    elif font_selected=='Fonts/font2/font.ttf':
                        fenetre.blit(Selection,(665,1200-scroll_fond.val))
                    elif font_selected=='Fonts/font3/font.ttf':
                        fenetre.blit(Selection,(875,1200-scroll_fond.val))
                    else:
                        fenetre.blit(Selection,(245,1320-scroll_fond.val))

                    if Lang_selected == "french":
                        fenetre.blit(Selection,(245,1450-scroll_fond.val))
                    elif Lang_selected == "english":
                        fenetre.blit(Selection,(455,1450-scroll_fond.val))
                    elif Lang_selected == "spanish":
                        fenetre.blit(Selection,(665,1450-scroll_fond.val))

                    mouse_stat = pygame.mouse.get_pressed()

                    if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_fond.pos.collidepoint(pygame.mouse.get_pos()) :
                        if scroll_fond.coor[1] < b-scroll_bar_decalage[1]:
                            scroll_fond.val -= (scroll_fond.coor[1] - (b-scroll_bar_decalage[1]))*3
                        elif scroll_fond.coor[1] > b-scroll_bar_decalage[1]:
                            scroll_fond.val += -(scroll_fond.coor[1] - (b-scroll_bar_decalage[1]))*3
                        scroll_fond.coor[1] = b-scroll_bar_decalage[1]
                        scroll_fond.pos = scroll_bar.get_rect(topleft=scroll_fond.coor)

                    fenetre.blit(scroll_bar,scroll_fond.coor)

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    paramètres=False
                                    animations_continuer=False
                                    fond_écran=False
                                    upgrade_continuer=False
                                    version_continuer=False
                                    fond_page = 0

                                    if Skin_selected == "Titanium":
                                        menu_continuer=True
                                        fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                        Tuiles_fermeture()
                                        ouverture_titre(200,2,0)
                                    elif Skin_selected == "Carroussel":
                                        Menu_skin2 = True
                                        fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                        Tuiles_fermeture()
                                        menu_carroussel.open()
                                    elif Skin_selected == "Legacy":
                                        Menu_skin1 = True
                                        menu_continuer = False
                                        Tuiles_fermeture()
                                        transition_ouverture(322)

                                if pos_Infos.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    animations_continuer=False
                                    version_continuer=True
                                    fond_page = 0

                                if pos_Modules.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    animations_continuer=False
                                    upgrade_continuer=True
                                    version_continuer=False
                                    fond_page = 0

                                if pos_Animations.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    animations_continuer=True
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    version_continuer=False
                                    fond_page = 0

                                if pos_fondmenu0_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu0")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu1_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu1")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu2_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu2")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu3_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu3")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu4_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu4")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu5_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu5")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu6_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu6")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_fondmenu7_a.collidepoint(event.pos):
                                    data_base.update("fond_selection","fondmenu7")
                                    wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                if pos_titanium_widgets_BNL.collidepoint(event.pos):
                                    data_base.update("Skin_selected","Titanium")
                                if pos_old_style.collidepoint(event.pos):
                                    data_base.update("Skin_selected","Legacy")
                                    data_base.update("theme_selected","MINI_Picture_original_legacy_theme")
                                    theme_init()
                                if pos_carroussel_skin.collidepoint(event.pos):
                                    data_base.update("Skin_selected","Carroussel")

                                if pos_Violet.collidepoint(event.pos):
                                    data_base.update("color_txt","(255,0,255)")

                                if pos_Rouge.collidepoint(event.pos):
                                    data_base.update("color_txt","(255,0,0)")

                                if pos_Cyan.collidepoint(event.pos):
                                    data_base.update("color_txt","(0,255,255)")

                                if pos_Bleu.collidepoint(event.pos):
                                    data_base.update("color_txt","(0,0,255)")

                                if pos_Vert.collidepoint(event.pos):
                                    data_base.update("color_txt","(0,255,0)")

                                if pos_Jaune.collidepoint(event.pos):
                                    data_base.update("color_txt","(255,255,0)")

                                if pos_Violet_r.collidepoint(event.pos):
                                    data_base.update("color_aux","(255,0,255)")

                                if pos_Rouge_r.collidepoint(event.pos):
                                   data_base.update("color_aux","(255,0,0)")

                                if pos_Cyan_r.collidepoint(event.pos):
                                   data_base.update("color_aux","(0,255,255)")

                                if pos_Bleu_r.collidepoint(event.pos):
                                   data_base.update("color_aux","(0,0,255)")

                                if pos_Vert_r.collidepoint(event.pos):
                                   data_base.update("color_aux","(0,255,0)")

                                if pos_Jaune_r.collidepoint(event.pos):
                                   data_base.update("color_aux","(255,255,0)")

                                if pos_MINI_Picture_original.collidepoint(event.pos):
                                    data_base.update("theme_selected","MINI_Picture_original")
                                    theme_init()
                                if pos_MINI_Picture_original_black_theme.collidepoint(event.pos):
                                    data_base.update("theme_selected","MINI_Picture_original_black_theme")
                                    theme_init()
                                if pos_MINI_Picture_original_alpha_theme.collidepoint(event.pos):
                                    data_base.update("theme_selected","MINI_Picture_original_alpha_theme")
                                    theme_init()

                                if pos_font0_a.collidepoint(event.pos):
                                    data_base.update("font_selected","Fonts/font0/font.ttf")
                                    font_init()

                                if pos_font1_a.collidepoint(event.pos):
                                    data_base.update("font_selected","Fonts/font1/font.ttf")
                                    font_init()

                                if pos_font2_a.collidepoint(event.pos):
                                    data_base.update("font_selected","Fonts/font2/font.ttf")
                                    font_init()

                                if pos_font3_a.collidepoint(event.pos):
                                    data_base.update("font_selected","Fonts/font3/font.ttf")
                                    font_init()

                                if pos_ON_OFF_Auto_theme.collidepoint(event.pos):
                                    if Auto_theme:
                                        data_base.update("Auto_theme","0")
                                        theme_init()

                                    else:
                                        now = datetime.datetime.now()
                                        data_base.update("Auto_theme","1")
                                        if now.month == 12 and now.day < 29 and now.day > 10:
                                            theme_selected = "MINI_Picture_original_christmas_theme"
                                            data_base.update("Auto_theme","1")
                                            theme_init()
                                        """
                                        if now.month == 7 and now.day == 14:
                                            theme_selected = "MINI_Picture_original_Bastille_day"
                                            data_base.update("Auto_theme","1")
                                            theme_init()

                                        if now.month == 1 and now.day == 1:
                                            theme_selected = "MINI_Picture_original_New_Year"
                                            data_base.update("Auto_theme","1")
                                            theme_init()
                                        """
                                            
                                if pos_french.collidepoint(event.pos):
                                    data_base.update("Lang_selected","french")
                                    theme_init()
                                    importlib.import_module(f".{Lang_selected}", "Lang")
                                    langue = eval(f"Lang.{Lang_selected}")

                                if pos_english.collidepoint(event.pos):
                                    data_base.update("Lang_selected","english")
                                    theme_init()
                                    importlib.import_module(f".{Lang_selected}", "Lang")
                                    langue = eval(f"Lang.{Lang_selected}")

                                if pos_spanish.collidepoint(event.pos):
                                    data_base.update("Lang_selected","spanish")
                                    theme_init()
                                    importlib.import_module(f".{Lang_selected}", "Lang")
                                    langue = eval(f"Lang.{Lang_selected}")

                                if pos_more_colors.collidepoint(event.pos):
                                    color_selection = True
                                    color_list_selection = []
                                    color_temp = ["255","255","255"]
                                    color_temp_f = (255,255,255)        

                                    color_input_r_s = False
                                    color_input_g_s = False
                                    color_input_b_s = False

                                    fond_écran = False
                                    paramètres = False
                                    fond_page = 0
                                if pos_more_themes.collidepoint(event.pos):
                                    scroll_fond.stat = False
                                    fond_page = 2
                                if pos_more_wallpapers.collidepoint(event.pos):
                                    scroll_fond.stat = False
                                    fond_page = 3
                                if scroll_fond.pos.collidepoint(event.pos):
                                    scroll_bar_decalage = [a-scroll_fond.coor[0],b-scroll_fond.coor[1]]
                                if pos_more_fonts.collidepoint(event.pos):
                                    scroll_fond.stat = False
                                    fond_page = 4

                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_UP:
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                animations_continuer=True
                                paramètres=True
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False
                                fond_page = 0

                            if event.key == K_ESCAPE:
                                paramètres=False
                                animations_continuer=False
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False
                                fond_page = 0

                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    Tuiles_fermeture()
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    Tuiles_fermeture()
                                    transition_ouverture(322)
                        if event.type == pygame.MOUSEWHEEL:
                            scroll_fond.stat = False
                            a = 0
                            b = scroll_fond.coor[1]-event.y
                            scroll_bar_decalage = [0,0]

                            if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 :
                                if scroll_fond.coor[1] < b-scroll_bar_decalage[1]:
                                    scroll_fond.val -= (scroll_fond.coor[1] - (b-scroll_bar_decalage[1]))*3
                                elif scroll_fond.coor[1] > b-scroll_bar_decalage[1]:
                                    scroll_fond.val += -(scroll_fond.coor[1] - (b-scroll_bar_decalage[1]))*3
                                scroll_fond.coor[1] = b-scroll_bar_decalage[1]
                                scroll_fond.pos = scroll_bar.get_rect(topleft=scroll_fond.coor)

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while fond_page == 2 :
                    a,b= pygame.mouse.get_pos ( )
                    étape_programme = "Paramètres / Personnalisation / Thèmes"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if AdaptoRAM_check:
                        if psutil.virtual_memory()[1] < RAM_free:
                            animations = False
                            transition_check = False

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                    fenetre.blit(Infos,(0,0))
                    fenetre.blit(Modules,(0,180))
                    fenetre.blit(Animations,(0,360))
                    fenetre.blit(Fond_paramètres1,(0,540))
                    fenetre.blit(Menu,(1150,20))

                    if theme_init_search :
                        list_themes = os.listdir("Images//Theme")

                        liste_variables_themes = []

                        for i in range(len(list_themes)):
                            globals() ["theme"+ str(i)] = pygame.image.load("Images/Theme/"+list_themes[i]+"/Theme_view.png").convert_alpha()

                        for i in range(len(list_themes)):
                            liste_variables_themes.append(globals() ["theme"+str(i)])

                        themes_listing_lat_decalage = 0
                        themes_listing_long_decalage = 0

                        for i in liste_variables_themes:
                            coor_pos_temp_theme = (250+themes_listing_long_decalage,20+themes_listing_lat_decalage-scroll_theme.val)
                            fenetre.blit(i,coor_pos_temp_theme)

                            if themes_listing_long_decalage < 600:
                                themes_listing_long_decalage += 300
                            elif themes_listing_long_decalage == 600:
                                themes_listing_long_decalage = 0
                                themes_listing_lat_decalage += 200

                        theme_init_search = False

                    themes_listing_lat_decalage = 0
                    themes_listing_long_decalage = 0

                    for i in liste_variables_themes:
                        coor_pos_temp_theme = (250+themes_listing_long_decalage,20+themes_listing_lat_decalage-scroll_theme.val)
                        fenetre.blit(i,coor_pos_temp_theme)

                        if themes_listing_long_decalage < 600:
                            themes_listing_long_decalage += 300
                        elif themes_listing_long_decalage == 600:
                            themes_listing_long_decalage = 0
                            themes_listing_lat_decalage += 200

                    mouse_stat = pygame.mouse.get_pressed()

                    if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_theme.pos.collidepoint(pygame.mouse.get_pos()):
                        if scroll_theme.coor[1] < b-scroll_bar_decalage[1]:
                            scroll_theme.val -= (scroll_theme.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_themes)//9)*1.5
                        elif scroll_theme.coor[1] > b-scroll_bar_decalage[1]:
                            scroll_theme.val += -(scroll_theme.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_themes)//9)*1.5
                        scroll_theme.coor[1] = b-scroll_bar_decalage[1]
                        scroll_theme.pos = scroll_bar.get_rect(topleft=scroll_theme.coor)

                    fenetre.blit(scroll_bar,scroll_theme.coor)

                    theme_panel_pos()

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:

                                theme_is_click()

                                if pos_Menu.collidepoint(event.pos):
                                    scroll_theme.stat = False
                                    fond_page = 1

                                if pos_Infos.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    animations_continuer=False
                                    version_continuer=True
                                    fond_page = 0

                                if pos_Modules.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    animations_continuer=False
                                    upgrade_continuer=True
                                    version_continuer=False
                                    fond_page = 0

                                if pos_Animations.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    animations_continuer=True
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    version_continuer=False
                                    fond_page = 0

                                if scroll_theme.pos.collidepoint(event.pos):
                                    scroll_bar_decalage = [a-scroll_theme.coor[0],b-scroll_theme.coor[1]]

                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_UP:
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                animations_continuer=True
                                paramètres=True
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False
                                fond_page = 0

                            if event.key == K_ESCAPE:
                                scroll_theme.stat = False
                                fond_page = 1
                        if event.type == pygame.MOUSEWHEEL:
                            scroll_theme.stat = False
                            a = 0
                            b = scroll_theme.coor[1]-event.y
                            scroll_bar_decalage = [0,0]

                            if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550:
                                if scroll_theme.coor[1] < b-scroll_bar_decalage[1]:
                                    scroll_theme.val -= (scroll_theme.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_themes)//9)*1.5
                                elif scroll_theme.coor[1] > b-scroll_bar_decalage[1]:
                                    scroll_theme.val += -(scroll_theme.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_themes)//9)*1.5
                                scroll_theme.coor[1] = b-scroll_bar_decalage[1]
                                scroll_theme.pos = scroll_bar.get_rect(topleft=scroll_theme.coor)

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while fond_page == 3 :
                    a,b= pygame.mouse.get_pos ( )
                    étape_programme = "Paramètres / Personnalisation / fonds d'écran"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if AdaptoRAM_check:
                        if psutil.virtual_memory()[1] < RAM_free:
                            animations = False
                            transition_check = False

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                    fenetre.blit(Infos,(0,0))
                    fenetre.blit(Modules,(0,180))
                    fenetre.blit(Animations,(0,360))
                    fenetre.blit(Fond_paramètres1,(0,540))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(new_wallpapers,(1150,150))

                    if wallpapers_init_search :
                        Wallpapers_loading_signal.start_signal()
                        
                        wallpapers_search_thread = Thread(target=wallpapers_search, args=())
                        wallpapers_search_thread.start()
                        
                        while wallpapers_init_search:
                            if Blur_background:
                                fenetre.blit(wallpapers_use.blur, (0,0))
                            else:
                                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                                fenetre.blit(fond_visibilité, (0,0))
                            fenetre.blit(Infos,(0,0))
                            fenetre.blit(Modules,(0,180))
                            fenetre.blit(Animations,(0,360))
                            fenetre.blit(Fond_paramètres1,(0,540))
                            fenetre.blit(Menu,(1150,20))
                            fenetre.blit(Wallpapers_loading_signal.img_in_use, Wallpapers_loading_signal.coor)
                            pygame.display.flip()
                            
                            for event in pygame.event.get():
                                None
                                
                        Wallpapers_loading_signal.stop_signal()

                    wallpapers_listing_lat_decalage = 0
                    wallpapers_listing_long_decalage = 0

                    for i in liste_variables_wallpapers:
                        coor_pos_temp_wallpapers = (250+wallpapers_listing_long_decalage,20+wallpapers_listing_lat_decalage-scroll_wallpapers.val)
                        fenetre.blit(i,coor_pos_temp_wallpapers)

                        if wallpapers_listing_long_decalage < 630:
                            wallpapers_listing_long_decalage += 210
                        elif wallpapers_listing_long_decalage == 630:
                            wallpapers_listing_long_decalage = 0
                            wallpapers_listing_lat_decalage += 123

                    if submenu_wallpapers.stat:
                        fenetre.blit(submenu_wallpapers.img, submenu_wallpapers.coor)
                        fenetre.blit(submenu_wallpapers.txt, submenu_wallpapers.coor_txt)

                    mouse_stat = pygame.mouse.get_pressed()

                    if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_wallpapers.pos.collidepoint(pygame.mouse.get_pos()):
                        if scroll_wallpapers.coor[1] < b-scroll_bar_decalage[1]:
                            scroll_wallpapers.val -= (scroll_wallpapers.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_wallpapers))//20)*1.5
                        elif scroll_wallpapers.coor[1] > b-scroll_bar_decalage[1]:
                            scroll_wallpapers.val += -(scroll_wallpapers.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_wallpapers))//20)*1.5
                        scroll_wallpapers.coor[1] = b-scroll_bar_decalage[1]
                        scroll_wallpapers.pos = scroll_bar.get_rect(topleft=scroll_wallpapers.coor)

                    fenetre.blit(scroll_bar,scroll_wallpapers.coor)

                    wallpapers_panel_pos()

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:

                                if not(submenu_wallpapers.stat):
                                    wallpapers_is_click()

                                if pos_Menu.collidepoint(event.pos):
                                    scroll_wallpapers.stat = False
                                    fond_page = 1

                                elif pos_Infos.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    animations_continuer=False
                                    version_continuer=True
                                    fond_page = 0

                                elif pos_Modules.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    animations_continuer=False
                                    upgrade_continuer=True
                                    version_continuer=False
                                    fond_page = 0

                                elif pos_Animations.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    animations_continuer=True
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    version_continuer=False
                                    fond_page = 0

                                elif scroll_wallpapers.pos.collidepoint(event.pos):
                                    scroll_bar_decalage = [a-scroll_wallpapers.coor[0],b-scroll_wallpapers.coor[1]]

                                elif pos_new_wallpapers.collidepoint(event.pos):
                                    path = easygui.fileopenbox()
                                    
                                    if path != None:
                                        
                                        Wallpapers_loading_signal.start_signal()
                                        
                                        wallpapers_create_thread = Thread(target=create_wallpapers_from_img, args=())
                                        wallpapers_create_thread.start()
                                        
                                        creating_sectionned_wallpapers = True
                                        
                                        while creating_sectionned_wallpapers:
                                            if Blur_background:
                                                fenetre.blit(wallpapers_use.blur, (0,0))
                                            else:
                                                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                                                fenetre.blit(fond_visibilité, (0,0))
                                            fenetre.blit(Infos,(0,0))
                                            fenetre.blit(Modules,(0,180))
                                            fenetre.blit(Animations,(0,360))
                                            fenetre.blit(Fond_paramètres1,(0,540))
                                            fenetre.blit(Menu,(1150,20))
                                            fenetre.blit(Wallpapers_loading_signal.img_in_use, Wallpapers_loading_signal.coor)
                                            pygame.display.flip()
                                            
                                            for event in pygame.event.get():
                                                None
                                        
                                        Wallpapers_loading_signal.stop_signal()
                                        
                                elif submenu_wallpapers.pos.collidepoint(event.pos) and submenu_wallpapers.stat:
                                    if submenu_wallpapers.selection not in ['fondmenu0', 'fondmenu1', 'fondmenu10', 'fondmenu2', 'fondmenu3', 'fondmenu4', 'fondmenu5', 'fondmenu6', 'fondmenu7', 'fondmenu8', 'fondmenu9']:
                                        try:
                                            shutil.rmtree("Images//Wallpapers//"+submenu_wallpapers.selection)
                                        except:
                                            None
                                        wallpapers_init_search = True
                                        submenu_wallpapers.stat = False
                                        if str(submenu_wallpapers.selection) == str(fond_selection):
                                            data_base.update("fond_selection","fondmenu0")
                                            wallpapers_use = Wallpapers(fond_selection,(1280,720), Blur_radius)

                                else:
                                    submenu_wallpapers.stat = False

                            if mouse_stat[2]:
                                submenu_wallpapers.set_pos([a,b])
                                submenu_wallpapers.selection = wallpapers_is_click(mode="delete")
                                if submenu_wallpapers.selection != None:
                                    submenu_wallpapers.stat = True
                                else:
                                    submenu_wallpapers.stat = False

                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_UP:
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                animations_continuer=True
                                paramètres=True
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False
                                fond_page = 0

                            if event.key == K_ESCAPE:
                                scroll_wallpapers.stat = False
                                fond_page = 1
                        if event.type == pygame.MOUSEWHEEL:
                            scroll_wallpapers.stat = False
                            a = 0
                            b = scroll_wallpapers.coor[1]-event.y
                            scroll_bar_decalage = [0,0]

                            if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550:
                                if scroll_wallpapers.coor[1] < b-scroll_bar_decalage[1]:
                                    scroll_wallpapers.val -= (scroll_wallpapers.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_wallpapers))//20)*1.5
                                elif scroll_wallpapers.coor[1] > b-scroll_bar_decalage[1]:
                                    scroll_wallpapers.val += -(scroll_wallpapers.coor[1] - (b-scroll_bar_decalage[1]))*((len(list_wallpapers))//20)*1.5
                                scroll_wallpapers.coor[1] = b-scroll_bar_decalage[1]
                                scroll_wallpapers.pos = scroll_bar.get_rect(topleft=scroll_wallpapers.coor)

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while fond_page == 4 :
                    a,b= pygame.mouse.get_pos ( )
                    étape_programme = "Paramètres / Personnalisation / polices de caractère"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if AdaptoRAM_check:
                        if psutil.virtual_memory()[1] < RAM_free:
                            animations = False
                            transition_check = False

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                    fenetre.blit(Infos,(0,0))
                    fenetre.blit(Modules,(0,180))
                    fenetre.blit(Animations,(0,360))
                    fenetre.blit(Fond_paramètres1,(0,540))
                    fenetre.blit(Menu,(1150,20))

                    if font_init_search :
                        list_font = os.listdir("Fonts")

                        liste_variables_font = []

                        for i in range(len(list_font)):
                            globals() ["font"+ str(i)] = pygame.image.load("Fonts/"+list_font[i]+"/font_view.png").convert_alpha()

                        for i in range(len(list_font)):
                            liste_variables_font.append(globals() ["font"+str(i)])

                        font_listing_lat_decalage = 0
                        font_listing_long_decalage = 0

                        for i in liste_variables_font:
                            coor_pos_temp_font = (250+font_listing_long_decalage,20+font_listing_lat_decalage-scroll_font.val)
                            fenetre.blit(i,coor_pos_temp_font)

                            if font_listing_long_decalage < 630:
                                font_listing_long_decalage += 210
                            elif font_listing_long_decalage == 630:
                                font_listing_long_decalage = 0
                                font_listing_lat_decalage += 123

                        font_init_search = False

                    font_listing_lat_decalage = 0
                    font_listing_long_decalage = 0

                    for i in liste_variables_font:
                        coor_pos_temp_font = (250+font_listing_long_decalage,20+font_listing_lat_decalage-scroll_font.val)
                        fenetre.blit(i,coor_pos_temp_font)

                        if font_listing_long_decalage < 630:
                            font_listing_long_decalage += 210
                        elif font_listing_long_decalage == 630:
                            font_listing_long_decalage = 0
                            font_listing_lat_decalage += 123

                    mouse_stat = pygame.mouse.get_pressed()

                    if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_font.pos.collidepoint(pygame.mouse.get_pos()):
                        if scroll_font.coor[1] < b-scroll_bar_decalage[1]:
                            scroll_font.val -= (scroll_font.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_font)//20)*1.5
                        elif scroll_font.coor[1] > b-scroll_bar_decalage[1]:
                            scroll_font.val += -(scroll_font.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_font)//20)*1.5
                        scroll_font.coor[1] = b-scroll_bar_decalage[1]
                        scroll_font.pos = scroll_bar.get_rect(topleft=scroll_font.coor)

                    fenetre.blit(scroll_bar,scroll_font.coor)

                    font_panel_pos()

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(400,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:

                                font_is_click()

                                if pos_Menu.collidepoint(event.pos):
                                    scroll_font.stat = False
                                    fond_page = 1

                                if pos_Infos.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    animations_continuer=False
                                    version_continuer=True
                                    fond_page = 0

                                if pos_Modules.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    paramètres=True
                                    fond_écran=False
                                    animations_continuer=False
                                    upgrade_continuer=True
                                    version_continuer=False
                                    fond_page = 0

                                if pos_Animations.collidepoint(event.pos):
                                    soundtrack=False
                                    menu_continuer=False
                                    bonus_continuer=False
                                    animations_continuer=True
                                    paramètres=True
                                    fond_écran=False
                                    upgrade_continuer=False
                                    version_continuer=False
                                    fond_page = 0

                                if scroll_font.pos.collidepoint(event.pos):
                                    scroll_bar_decalage = [a-scroll_font.coor[0],b-scroll_font.coor[1]]

                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_UP:
                                soundtrack=False
                                menu_continuer=False
                                bonus_continuer=False
                                animations_continuer=True
                                paramètres=True
                                fond_écran=False
                                upgrade_continuer=False
                                version_continuer=False
                                fond_page = 0

                            if event.key == K_ESCAPE:
                                scroll_font.stat = False
                                fond_page = 1
                        if event.type == pygame.MOUSEWHEEL:
                            scroll_font.stat = False
                            a = 0
                            b = scroll_font.coor[1]-event.y
                            scroll_bar_decalage = [0,0]

                            if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550:
                                if scroll_font.coor[1] < b-scroll_bar_decalage[1]:
                                    scroll_font.val -= (scroll_font.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_font)//20)*1.5
                                elif scroll_font.coor[1] > b-scroll_bar_decalage[1]:
                                    scroll_font.val += -(scroll_font.coor[1] - (b-scroll_bar_decalage[1]))*(len(list_font)//20)*1.5
                                scroll_font.coor[1] = b-scroll_bar_decalage[1]
                                scroll_font.pos = scroll_bar.get_rect(topleft=scroll_font.coor)

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

        # Menu "A propos"
        while credits:
            scroll_credits_history = Scroll([1230,150],0, False)
            scroll_bar_decalage = [0,0]
            while credits_menu:
                étape_programme = "A propos"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_credits, (500, 20))
                fenetre.blit(Lounge_menu,(755,0))
                fenetre.blit(Menu,(1150,20))

                fenetre.blit(Credits_history_picture,(100,200))
                texte = font.render(langue.credits_history_title, 1, (color_txt))
                fenetre.blit(texte, (130, 400))

                fenetre.blit(Credits_changelog_picture,(400,200))
                texte = font.render(langue.credits_project_title, 1, (color_txt))
                fenetre.blit(texte, (430, 400))

                fenetre.blit(Credits_help_picture,(700,200))
                texte = font.render(langue.credits_help_title, 1, (color_txt))
                fenetre.blit(texte, (740, 400))

                fenetre.blit(Credits_about_picture,(1000,200))
                texte = font.render(langue.credits_legals_title, 1, (color_txt))
                fenetre.blit(texte, (980, 400))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                credits = False
                                credits_menu = False
                                transition_ouverture(322)

                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                            if pos_Credits_history_picture.collidepoint(event.pos):
                                credits_menu = False
                                credits_history = True
                            if pos_Credits_changelog_picture.collidepoint(event.pos):
                                credits_menu = False
                                credits_changelog = True
                            if pos_Credits_help_picture.collidepoint(event.pos):
                                credits_menu = False
                                credits_help = True
                            if pos_Credits_about_picture.collidepoint(event.pos):
                                credits_menu = False
                                credits_about = True
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE:
                            credits = False
                            credits_menu = False
                            transition_ouverture(322)

                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while credits_history:
                étape_programme = "A propos / Histoire"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))

                texte = font.render("Level 1.x", 1, (color_txt))
                fenetre.blit(texte, (600, 100-scroll_credits_history.val))
                fenetre.blit(Credits_history_Level_1x, (556,150-scroll_credits_history.val))

                texte = font_credits.render(langue.credits_history_Level1x_1, 1, (color_txt))
                fenetre.blit(texte, (10, 380-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level1x_2, 1, (color_txt))
                fenetre.blit(texte, (10, 400-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level1x_3, 1, (color_txt))
                fenetre.blit(texte, (10, 420-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level1x_4, 1, (color_txt))
                fenetre.blit(texte, (10, 440-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level1x_5, 1, (color_txt))
                fenetre.blit(texte, (10, 460-scroll_credits_history.val))

                texte = font.render("Level 2.x", 1, (color_txt))
                fenetre.blit(texte, (600, 600-scroll_credits_history.val))
                fenetre.blit(Credits_history_Level_2x1, (60,650-scroll_credits_history.val))
                fenetre.blit(Credits_history_Level_2x, (460,650-scroll_credits_history.val))
                fenetre.blit(Credits_history_Level_2x2, (860,650-scroll_credits_history.val))

                texte = font_credits.render(langue.credits_history_Level2x_1, 1, (color_txt))
                fenetre.blit(texte, (10, 880-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_2, 1, (color_txt))
                fenetre.blit(texte, (10, 900-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_3, 1, (color_txt))
                fenetre.blit(texte, (10, 920-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_4, 1, (color_txt))
                fenetre.blit(texte, (10, 940-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_5, 1, (color_txt))
                fenetre.blit(texte, (10, 960-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_6, 1, (color_txt))
                fenetre.blit(texte, (10, 980-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_7, 1, (color_txt))
                fenetre.blit(texte, (10, 1000-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_Level2x_8, 1, (color_txt))
                fenetre.blit(texte, (10, 1020-scroll_credits_history.val))

                texte = font.render("BNL's Box 3.x", 1, (color_txt))
                fenetre.blit(texte, (550, 1100-scroll_credits_history.val))
                fenetre.blit(Credits_history_BNLBox_3x1, (60,1150-scroll_credits_history.val))
                fenetre.blit(Credits_history_BNLBox_3x, (460,1150-scroll_credits_history.val))
                fenetre.blit(Credits_history_BNLBox_3x2, (860, 1150-scroll_credits_history.val))

                texte = font_credits.render(langue.credits_history_BNL3x_1, 1, (color_txt))
                fenetre.blit(texte, (10, 1380-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_2, 1, (color_txt))
                fenetre.blit(texte, (10, 1400-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_3, 1, (color_txt))
                fenetre.blit(texte, (10, 1420-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_4, 1, (color_txt))
                fenetre.blit(texte, (10, 1440-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_5, 1, (color_txt))
                fenetre.blit(texte, (10, 1460-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_6, 1, (color_txt))
                fenetre.blit(texte, (10, 1480-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_7, 1, (color_txt))
                fenetre.blit(texte, (10, 1500-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_8, 1, (color_txt))
                fenetre.blit(texte, (10, 1520-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL3x_9, 1, (color_txt))
                fenetre.blit(texte, (10, 1540-scroll_credits_history.val))

                texte = font.render("BNL's Box 4.x", 1, (color_txt))
                fenetre.blit(texte, (550, 1600-scroll_credits_history.val))
                fenetre.blit(Credits_history_BNLBox_4x1, (60,1650-scroll_credits_history.val))
                fenetre.blit(Credits_history_BNLBox_4x, (460,1650-scroll_credits_history.val))
                fenetre.blit(Credits_history_BNLBox_4x2, (860,1650-scroll_credits_history.val))

                texte = font_credits.render(langue.credits_history_BNL4x_1, 1, (color_txt))
                fenetre.blit(texte, (10, 1880-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_2, 1, (color_txt))
                fenetre.blit(texte, (10, 1900-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_3, 1, (color_txt))
                fenetre.blit(texte, (10, 1920-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_4, 1, (color_txt))
                fenetre.blit(texte, (10, 1940-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_5, 1, (color_txt))
                fenetre.blit(texte, (10, 1960-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_6, 1, (color_txt))
                fenetre.blit(texte, (10, 1980-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_7, 1, (color_txt))
                fenetre.blit(texte, (10, 2000-scroll_credits_history.val))
                texte = font_credits.render(langue.credits_history_BNL4x_8, 1, (color_txt))
                fenetre.blit(texte, (10, 2020-scroll_credits_history.val))
                texte = font_credits.render("", 1, (color_txt))
                fenetre.blit(texte, (10, 2040-scroll_credits_history.val))

                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_credits, (500, 20))
                fenetre.blit(Credits_history_picture_min,(755,0))
                fenetre.blit(Menu,(1150,20))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                a,b= pygame.mouse.get_pos ( )
                mouse_stat = pygame.mouse.get_pressed()

                if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_credits_history.pos.collidepoint(pygame.mouse.get_pos()):
                    if scroll_credits_history.coor[1] < b-scroll_bar_decalage[1]:
                        scroll_credits_history.val -= (scroll_credits_history.coor[1] - (b-scroll_bar_decalage[1]))*4
                    elif scroll_credits_history.coor[1] > b-scroll_bar_decalage[1]:
                        scroll_credits_history.val += -(scroll_credits_history.coor[1] - (b-scroll_bar_decalage[1]))*4
                    scroll_credits_history.coor[1] = b-scroll_bar_decalage[1]
                    scroll_credits_history.pos = scroll_bar.get_rect(topleft=scroll_credits_history.coor)

                fenetre.blit(scroll_bar,scroll_credits_history.coor)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                credits_menu = True
                                credits_history = False
                            if scroll_credits_history.pos.collidepoint(event.pos):
                                scroll_bar_decalage = [a-scroll_credits_history.coor[0],b-scroll_credits_history.coor[1]]
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE:
                            credits_menu = True
                            credits_history = False

                    if event.type == pygame.MOUSEWHEEL:
                        scroll_credits_history.stat = False
                        a = 0
                        b = scroll_credits_history.coor[1]-event.y
                        scroll_bar_decalage = [0,0]

                        if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550:
                            if scroll_credits_history.coor[1] < b-scroll_bar_decalage[1]:
                                scroll_credits_history.val -= (scroll_credits_history.coor[1] - (b-scroll_bar_decalage[1]))*4
                            elif scroll_credits_history.coor[1] > b-scroll_bar_decalage[1]:
                                scroll_credits_history.val += -(scroll_credits_history.coor[1] - (b-scroll_bar_decalage[1]))*4
                            scroll_credits_history.coor[1] = b-scroll_bar_decalage[1]
                            scroll_credits_history.pos = scroll_bar.get_rect(topleft=scroll_credits_history.coor)

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while credits_changelog:
                étape_programme = "A propos / Projets"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_credits, (500, 20))
                fenetre.blit(Credits_changelog_picture_min,(755,0))
                fenetre.blit(Menu,(1150,20))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                credits_menu = True
                                credits_changelog = False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE:
                            credits_menu = True
                            credits_changelog = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while credits_help:
                étape_programme = "A propos / Aide"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_credits, (500, 20))
                fenetre.blit(Credits_help_picture_min,(755,0))
                fenetre.blit(Menu,(1150,20))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                credits_menu = True
                                credits_help = False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE:
                            credits_menu = True
                            credits_help = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while credits_about:
                étape_programme = "A propos / Mentions légales"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))

                texte = font_credits.render(langue.credits_legals_1, 1, (color_txt))
                fenetre.blit(texte, (10, 100))
                texte = font_credits.render(langue.credits_legals_2, 1, (color_txt))
                fenetre.blit(texte, (10, 150))
                texte = font_credits.render(langue.credits_legals_3, 1, (color_txt))
                fenetre.blit(texte, (10, 200))
                texte = font_credits.render(langue.credits_legals_4, 1, (color_txt))
                fenetre.blit(texte, (10, 220))
                texte = font_credits.render(langue.credits_legals_5, 1, (color_txt))
                fenetre.blit(texte, (10, 240))
                texte = font_credits.render(langue.credits_legals_6, 1, (color_txt))
                fenetre.blit(texte, (10, 260))
                texte = font_credits.render(langue.credits_legals_7, 1, (color_txt))
                fenetre.blit(texte, (10, 280))
                texte = font_credits.render(langue.credits_legals_8, 1, (color_txt))
                fenetre.blit(texte, (10, 310))
                texte = font_credits.render(langue.credits_legals_9, 1, (color_txt))
                fenetre.blit(texte, (10, 330))
                texte = font_credits.render(langue.credits_legals_10, 1, (color_txt))
                fenetre.blit(texte, (10, 350))
                texte = font_credits.render(langue.credits_legals_11, 1, (color_txt))
                fenetre.blit(texte, (10, 370))
                texte = font_credits.render(langue.credits_legals_12, 1, (color_txt))
                fenetre.blit(texte, (10, 390))
                texte = font_credits.render(langue.credits_legals_13, 1, (color_txt))
                fenetre.blit(texte, (10, 410))
                texte = font_credits.render(langue.credits_legals_14, 1, (color_txt))
                fenetre.blit(texte, (10, 440))
                texte = font_credits.render(langue.credits_legals_15, 1, (color_txt))
                fenetre.blit(texte, (10, 460))
                texte = font_credits.render(langue.credits_legals_16, 1, (color_txt))
                fenetre.blit(texte, (10, 480))
                texte = font_credits.render(langue.credits_legals_17, 1, (color_txt))
                fenetre.blit(texte, (10, 500))
                texte = font_credits.render(langue.credits_legals_18, 1, (color_txt))
                fenetre.blit(texte, (10, 520))
                texte = font_credits.render(langue.credits_legals_19, 1, (color_txt))
                fenetre.blit(texte, (10, 550))
                texte = font_credits.render(langue.credits_legals_20, 1, (color_txt))
                fenetre.blit(texte, (10, 600))

                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_credits, (500, 20))
                fenetre.blit(Credits_about_picture_min,(755,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Credits_logo,(980,100))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                credits_menu = True
                                credits_about = False
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_ESCAPE:
                            credits_menu = True
                            credits_about = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

        # Onglet jeux
        while jeux :
            jeux_liste = ["P4","C","P4_M","Tetris","Jump", "Minesweeper"]
            pos_logo_jeu = Puissance4_logo.get_rect(topleft=(553,250))

            # Menu jeux
            while jeux_menu :

                étape_programme = "Jeux"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if AdaptoRAM_check:
                    if psutil.virtual_memory()[1] < RAM_free:
                        animations = False
                        transition_check = False

                if menu_games.selection == 0 :
                    menu_games.selection_temp1 = len(menu_games.liste)-1
                    menu_games.selection_temp2 = len(menu_games.liste)-2
                    menu_games.selection_temp3 = menu_games.selection+1
                    menu_games.selection_temp4 = menu_games.selection+2

                elif menu_games.selection == 1 :
                    menu_games.selection_temp1 = 0
                    menu_games.selection_temp2 = len(menu_games.liste)-1
                    menu_games.selection_temp3 = menu_games.selection+1
                    menu_games.selection_temp4 = menu_games.selection+2

                elif menu_games.selection == len(menu_games.liste)-1 :
                    menu_games.selection_temp1 = menu_games.selection-1
                    menu_games.selection_temp2 = menu_games.selection-2
                    menu_games.selection_temp3 = 0
                    menu_games.selection_temp4 = 1
                elif menu_games.selection == len(menu_games.liste)-2 :
                    menu_games.selection_temp1 = menu_games.selection-1
                    menu_games.selection_temp2 = menu_games.selection-2
                    menu_games.selection_temp3 = len(menu_games.liste)-1
                    menu_games.selection_temp4 = 0
                else :
                    menu_games.selection_temp1 = menu_games.selection-1
                    menu_games.selection_temp2 = menu_games.selection-2
                    menu_games.selection_temp3 = menu_games.selection+1
                    menu_games.selection_temp4 = menu_games.selection+2

                vignette_1 = pygame.image.load(menu_games.path+menu_games.liste[menu_games.selection_temp2]+".png").convert_alpha()
                vignette_5 = pygame.image.load(menu_games.path+menu_games.liste[menu_games.selection_temp4]+".png").convert_alpha()

                vignette_3 = pygame.image.load(menu_games.path+menu_games.liste[menu_games.selection]+".png").convert_alpha()

                vignette_2 = pygame.image.load(menu_games.path+menu_games.liste[menu_games.selection_temp1]+".png").convert_alpha()
                vignette_4 = pygame.image.load(menu_games.path+menu_games.liste[menu_games.selection_temp3]+".png").convert_alpha()

                vignette_1 = pygame.transform.scale(vignette_1, (300,169))
                vignette_5 = pygame.transform.scale(vignette_5, (300,169))

                vignette_2 = pygame.transform.scale(vignette_2, (400,225))
                vignette_4 = pygame.transform.scale(vignette_4, (400,225))

                pos_video_bonus = vignette_3.get_rect(topleft=(340, 191))

                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_jeux, (500, 20))
                fenetre.blit(Autopilot_menu,(755,0))
                fenetre.blit(Menu,(1150,20))

                fenetre.blit(vignette_1,(100,275))
                fenetre.blit(vignette_5,(880,275))

                fenetre.blit(vignette_2,(200,247))
                fenetre.blit(vignette_4,(680,247))

                fenetre.blit(vignette_3,(299,168))

                fenetre.blit(Gauche_video2,(60,500))
                fenetre.blit(Droite_video2,(1189,500))

                if menu_games.liste[menu_games.selection] == "P4_R" :

                    texte = font_games_menu.render(langue.game_p4_r0, 1, (color_txt))
                    fenetre.blit(texte, (10, 570))
                    texte = font_games_menu.render(langue.game_p4_r1, 1, (color_txt))
                    fenetre.blit(texte, (10, 600))
                    texte = font_games_menu.render(langue.game_p4_r2, 1, (color_txt))
                    fenetre.blit(texte, (10, 630))

                elif menu_games.liste[menu_games.selection] == "Memory_Cards" :

                    texte = font_games_menu.render(langue.game_c_0, 1, (color_txt))
                    fenetre.blit(texte, (10, 570))
                    texte = font_games_menu.render(langue.game_c_1, 1, (color_txt))
                    fenetre.blit(texte, (10, 600))
                    texte = font_games_menu.render(langue.game_c_2, 1, (color_txt))
                    fenetre.blit(texte, (10, 630))

                elif menu_games.liste[menu_games.selection] == "P4_M" :

                    texte = font_games_menu.render(langue.game_p4_m0, 1, (color_txt))
                    fenetre.blit(texte, (10, 570))
                    texte = font_games_menu.render(langue.game_p4_m1, 1, (color_txt))
                    fenetre.blit(texte, (10, 600))
                    texte = font_games_menu.render(langue.game_p4_m2, 1, (color_txt))
                    fenetre.blit(texte, (10, 630))

                elif menu_games.liste[menu_games.selection] == "Tetros" :

                    texte = font_games_menu.render(langue.game_tet_0, 1, (color_txt))
                    fenetre.blit(texte, (10, 570))
                    texte = font_games_menu.render(langue.game_tet_1, 1, (color_txt))
                    fenetre.blit(texte, (10, 600))
                    texte = font_games_menu.render(langue.game_tet_2, 1, (color_txt))
                    fenetre.blit(texte, (10, 630))

                elif menu_games.liste[menu_games.selection] == "WALL-E's_Jump" :

                    texte = font_games_menu.render(langue.game_j_0, 1, (color_txt))
                    fenetre.blit(texte, (10, 570))
                    texte = font_games_menu.render(langue.game_j_1, 1, (color_txt))
                    fenetre.blit(texte, (10, 600))
                    texte = font_games_menu.render(langue.game_j_2, 1, (color_txt))
                    fenetre.blit(texte, (10, 630))

                elif menu_games.liste[menu_games.selection] == "T.A.N.K.S" :

                    texte = font_games_menu.render(langue.game_tank_0, 1, (color_txt))
                    fenetre.blit(texte, (10, 570))
                    texte = font_games_menu.render(langue.game_tank_1, 1, (color_txt))
                    fenetre.blit(texte, (10, 600))
                    texte = font_games_menu.render(langue.game_tank_2, 1, (color_txt))
                    fenetre.blit(texte, (10, 630))

                elif menu_games.liste[menu_games.selection] == "Minesweeper" :
                    None

                a,b= pygame.mouse.get_pos ( )

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_RIGHT:
                            menu_games.selection_old = menu_games.selection
                            if menu_games.selection < len(menu_games.liste)-1 :
                                menu_games.selection += 1
                            else :
                                menu_games.selection = 0

                            if menu_games.selection == len(menu_games.liste)-3 :
                                menu_games.selection_trans = len(menu_games.liste)-1
                            elif menu_games.selection == len(menu_games.liste)-2 :
                                menu_games.selection_trans = 0
                            elif menu_games.selection == len(menu_games.liste)-1 :
                                menu_games.selection_trans = 1
                            else :
                                menu_games.selection_trans = menu_games.selection+2

                            menu_games.right()

                        if event.key == pygame.K_LEFT:
                            menu_games.selection_old = menu_games.selection
                            if menu_games.selection > 0 :
                                menu_games.selection -= 1
                            else :
                                menu_games.selection = len(menu_games.liste)-1

                            if menu_games.selection == 0 :
                                menu_games.selection_trans = len(menu_games.liste)-2
                            elif menu_games.selection == 1:
                                menu_games.selection_trans = len(menu_games.liste)-1
                            else :
                                menu_games.selection_trans = menu_games.selection-2

                            menu_games.left()

                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            if menu_games.liste[menu_games.selection] == "P4_R":
                                jeux_menu = False
                                Puissance4 = True
                            elif menu_games.liste[menu_games.selection] == "Memory_Cards":
                                jeux_menu = False
                                Cartes = True
                                reset_cartes()
                                compte = 0
                            elif menu_games.liste[menu_games.selection] == "P4_M":
                                jeux_menu = False
                                Puissance4_by_Maxime = True
                            elif menu_games.liste[menu_games.selection] == "Tetros":
                                if Preview_access:
                                    jeux_menu = False
                                    Tetros = True
                                    Tetros_menu = True
                                else:
                                    pop_up()
                                    texte = font_games_menu.render(langue.game_advert, 5, (255,255,255))
                                    fenetre.blit(texte, (560, 190))
                                    texte = font_games_menu.render("", 1, (255,255,255))
                                    fenetre.blit(texte, (450, 250))
                                    texte = font_games_menu.render(langue.game_in_dev, 1, (255,255,255))
                                    fenetre.blit(texte, (480, 280))
                                    texte = font_games_menu.render("", 1, (255,255,255))
                                    fenetre.blit(texte, (450, 310))
                                    texte = font_games_menu.render(f"{langue.game_out}2023", 1, (255,255,255))
                                    fenetre.blit(texte, (550, 340))
                                    texte = font_games_menu.render("", 1, (255,255,255))
                                    fenetre.blit(texte, (450, 370))
                                    texte = font_games_menu.render("", 1, (255,255,255))
                                    fenetre.blit(texte, (450, 400))
                                    texte = font_games_menu.render("", 1, (255,255,255))
                                    fenetre.blit(texte, (450, 430))
                                    texte = font_games_menu.render("", 1, (255,255,255))
                                    fenetre.blit(texte, (450, 460))
                                    pygame.display.flip()
                                    time.sleep(4)

                            elif menu_games.liste[menu_games.selection] == "WALL-E's_Jump":
                                jeux_menu = False
                                Jump = True
                                Jump_menu = True
                                Jump_check = False
                                Jump_play = True
                                Jump_avance = 0
                                Jump_init = True

                            elif menu_games.liste[menu_games.selection] == "T.A.N.K.S":
                                jeux_menu = False
                                TANK_M = True

                            elif menu_games.liste[menu_games.selection] == "Minesweeper":
                               jeux_menu = False
                               Minesweeper = True
                               Minesweeper_menu = True
                               
                            elif menu_games.liste[menu_games.selection] == "Vilallongue_chroni":
                               jeux_menu = False
                               Vilallongue_chroni_game = True

                        if event.key == K_ESCAPE:
                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                menu_games.close()
                                onglets_fermeture(texte_jeux,Autopilot_menu)
                                jeux_menu = False
                                jeux = False
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                menu_games.close()
                                onglets_fermeture(texte_jeux,Autopilot_menu)
                                jeux_menu = False
                                jeux = False
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                menu_games.close()
                                onglets_fermeture(texte_jeux,Autopilot_menu)
                                jeux_menu = False
                                jeux = False
                                Menu_skin1 = True
                                menu_continuer = False
                                transition_ouverture(322)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    menu_games.close()
                                    onglets_fermeture(texte_jeux,Autopilot_menu)
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    menu_games.close()
                                    onglets_fermeture(texte_jeux,Autopilot_menu)
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    menu_games.close()
                                    onglets_fermeture(texte_jeux,Autopilot_menu)
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    transition_ouverture(322)
                                jeux_menu = False
                                jeux = False

                            elif pos_Gauche_video.collidepoint(event.pos):
                                menu_games.selection_old = menu_games.selection
                                if menu_games.selection > 0 :
                                    menu_games.selection -= 1
                                else :
                                    menu_games.selection = len(menu_games.liste)-1

                                if menu_games.selection == 0 :
                                    menu_games.selection_trans = len(menu_games.liste)-2
                                elif menu_games.selection == 1:
                                    menu_games.selection_trans = len(menu_games.liste)-1
                                else :
                                    menu_games.selection_trans = menu_games.selection-2

                                menu_games.left()

                            elif pos_Droite_video.collidepoint(event.pos):
                                menu_games.selection_old = menu_games.selection
                                if menu_games.selection < len(menu_games.liste)-1 :
                                    menu_games.selection += 1
                                else :
                                    menu_games.selection = 0

                                if menu_games.selection == len(menu_games.liste)-3 :
                                    menu_games.selection_trans = len(menu_games.liste)-1
                                elif menu_games.selection == len(menu_games.liste)-2 :
                                    menu_games.selection_trans = 0
                                elif menu_games.selection == len(menu_games.liste)-1 :
                                    menu_games.selection_trans = 1
                                else :
                                    menu_games.selection_trans = menu_games.selection+2

                                menu_games.right()

                            else:
                                if menu_games.liste[menu_games.selection] == "P4_R":
                                    jeux_menu = False
                                    Puissance4 = True
                                elif menu_games.liste[menu_games.selection] == "Memory_Cards":
                                    jeux_menu = False
                                    Cartes = True
                                    reset_cartes()
                                    compte = 0
                                elif menu_games.liste[menu_games.selection] == "P4_M":
                                    jeux_menu = False
                                    Puissance4_by_Maxime = True
                                elif menu_games.liste[menu_games.selection] == "Tetros":
                                    if Preview_access:
                                        jeux_menu = False
                                        Tetros = True
                                        Tetros_menu = True
                                    else:
                                        pop_up()
                                        texte = font_games_menu.render(langue.game_advert, 5, (255,255,255))
                                        fenetre.blit(texte, (560, 190))
                                        texte = font_games_menu.render("", 1, (255,255,255))
                                        fenetre.blit(texte, (450, 250))
                                        texte = font_games_menu.render(langue.game_in_dev, 1, (255,255,255))
                                        fenetre.blit(texte, (480, 280))
                                        texte = font_games_menu.render("", 1, (255,255,255))
                                        fenetre.blit(texte, (450, 310))
                                        texte = font_games_menu.render(f"{langue.game_out}2023", 1, (255,255,255))
                                        fenetre.blit(texte, (550, 340))
                                        texte = font_games_menu.render("", 1, (255,255,255))
                                        fenetre.blit(texte, (450, 370))
                                        texte = font_games_menu.render("", 1, (255,255,255))
                                        fenetre.blit(texte, (450, 400))
                                        texte = font_games_menu.render("", 1, (255,255,255))
                                        fenetre.blit(texte, (450, 430))
                                        texte = font_games_menu.render("", 1, (255,255,255))
                                        fenetre.blit(texte, (450, 460))
                                        pygame.display.flip()
                                        time.sleep(4)
                                elif menu_games.liste[menu_games.selection] == "WALL-E's_Jump":
                                    jeux_menu = False
                                    Jump = True
                                    Jump_menu = True
                                    Jump_check = False
                                    Jump_play = True
                                    Jump_avance = 0
                                    Jump_init = True

                                elif menu_games.liste[menu_games.selection] == "T.A.N.K.S":
                                    jeux_menu = False
                                    TANK_M = True

                                elif menu_games.liste[menu_games.selection] == "Minesweeper":
                                    jeux_menu = False
                                    Minesweeper = True
                                    Minesweeper_menu = True
                                    
                                elif menu_games.liste[menu_games.selection] == "Vilallongue_chroni":
                                    jeux_menu = False
                                    Vilallongue_chroni_game = True

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while Puissance4 :

                étape_programme = "Jeux / Puissance 4 by Raphaël Picture"

                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(Menu,(1150,20))

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                # Jeux : Puissance 4 avec l'aimable autorisation de Raphaël Bobille ( alias Raphaël Picture )
                # Des modifications ont cependant été effectuées afin de le rendre compatible avec BNL's Box...

                import json
                from random import randint

                def aide():
                    global jeux_menu
                    global Puissance4

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/help.png").convert_alpha(), (316,58))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()
                    while Puissance4:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                if quit_enable and not(update_web):
                                    STOP()
                                elif quit_enable and update_web:
                                    STOP("Update.bat")
                            if event.type == KEYDOWN:
                                return
                            if event.type == MOUSEBUTTONDOWN:
                                mouse_stat = pygame.mouse.get_pressed()
                                if mouse_stat[0]:
                                    if pos_Menu.collidepoint(event.pos):
                                        return
                def menu():
                    global jeux_menu
                    global Puissance4

                    time.sleep(1.5)
                    menu = pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/menu.png").convert_alpha()

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(menu, (506,340))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()
                    while Puissance4:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                if quit_enable and not(update_web):
                                    STOP()
                                elif quit_enable and update_web:
                                    STOP("Update.bat")
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    if 200 < event.pos[1] < 239:
                                        if 230+316 < event.pos[0] < 364+316:
                                            return
                                        if 364+316 < event.pos[0] < 498+316:
                                            puissance4()

                                if pos_Menu.collidepoint(event.pos):
                                    return

                            if event.type == KEYDOWN:
                                if event.key == K_KP0:
                                    return
                                if event.key == K_KP1:
                                    puissance4()
                                if event.key == K_ESCAPE:
                                    return

                def puissance4():
                    n = 0
                    global jeux_menu
                    global Puissance4

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/grille.png").convert_alpha(), (316,58))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()
                    background = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
                    w = 0
                    plein = 0
                    player = randint(1,2)
                    tyellow = pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/tyellow.png").convert_alpha()
                    tred = pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/tred.png").convert_alpha()
                    while Puissance4:
                        while Puissance4:
                            if n > 41:
                                fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/equality.png").convert_alpha(), (563, 327))

                                pygame.display.flip()
                                menu()
                                return
                            if player == 1:
                                fenetre.blit(tyellow, (100, 300))
                                pygame.display.flip()
                            else:
                                fenetre.blit(tred, (100, 300))
                                pygame.display.flip()
                            col = selectcol()

                            if col == 7 :
                                return

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
                                return

                def selectcol():

                    global Puissance4
                    global jeux_menu

                    while Puissance4:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                if quit_enable and not(update_web):
                                    STOP()
                                elif quit_enable and update_web:
                                    STOP("Update.bat")
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    if 10+58 < event.pos[1] < 525+58:
                                        if 31+316 < event.pos[0] < 103+316:
                                            return 0
                                        if 118+316 < event.pos[0] < 187+316:
                                            return 1
                                        if 202+316 < event.pos[0] < 272+316:
                                            return 2
                                        if 287+316 < event.pos[0] < 357+316:
                                            return 3
                                        if 373+316 < event.pos[0] < 443+316:
                                            return 4
                                        if 457+316 < event.pos[0] < 527+316:
                                            return 5
                                        if 542+316 < event.pos[0] < 612+316:
                                            return 6

                                if pos_Menu.collidepoint(event.pos):
                                    return 7

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
                                if event.key == K_ESCAPE:
                                    return 7

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
                        pionj = pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/pionj.png").convert_alpha()
                        fenetre.blit(pionj, (c[1]+316, c[0]+58))
                    else:
                        pionr = pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/pionr.png").convert_alpha()
                        fenetre.blit(pionr, (c[1]+316, c[0]+58))
                    pygame.display.flip()

                def résultat(b, k1, c1, k2, c2, k3, c3, k4, c4):

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/grille.png").convert_alpha(), (316,58))
                    c = b[k1][c1]
                    grille(c1, k1, c)
                    grille(c2, k2, c)
                    grille(c3, k3, c)
                    grille(c4, k4, c)
                    if b[k1][c1] == 1:
                        fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/jaune.png").convert_alpha(), (407, 324))
                    else:
                        fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/rouge.png").convert_alpha(), (407, 324))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()

                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(Menu,(1150,20))

                fenetre.blit(pygame.image.load("Games/Raphael Picture/Puissance_4.2/images/start.png").convert_alpha(), (316,58))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(5,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if 489+58 > event.pos[1] and 648+316 > event.pos[0] and 316 < event.pos[0]:
                                puissance4()
                            if 488+58 < event.pos[1] and 648+316 > event.pos[0] and 316 < event.pos[0]:
                                aide()
                            if event.type == KEYDOWN:
                                puissance4()

                        if pos_Menu.collidepoint(event.pos):
                            Puissance4 = False
                            jeux_menu = True

                    if event.type==KEYDOWN:
                        if event.key == K_ESCAPE:
                            Puissance4 = False
                            jeux_menu = True

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            # Jeu WALL-E's Memory by MINI Picture
            while Cartes :

                étape_programme = "Jeux / WALL-E's Memory by MINI Picture"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(score_reset,(1100,500))
                fenetre.blit(card_reset,(1100,600))

                """ Chargement des cartes (dos) """

                liste_cartes_statut = [carte1,carte2,carte3,carte4,carte5,carte6,carte7,carte8,carte9]
                liste_cartes_statut1 = [carte1_bis,carte2_bis,carte3_bis,carte4_bis,carte5_bis,carte6_bis,carte7_bis,carte8_bis,carte9_bis]

                for e in liste_cartes_statut:
                    e.check_stat()
                for e in liste_cartes_statut1:
                    e.check_stat()

                fenetre.blit(carte1.img,carte1.coor)
                fenetre.blit(carte2.img,carte2.coor)
                fenetre.blit(carte3.img,carte3.coor)
                fenetre.blit(carte4.img,carte4.coor)
                fenetre.blit(carte5.img,carte5.coor)
                fenetre.blit(carte6.img,carte6.coor)

                fenetre.blit(carte1_bis.img,carte1_bis.coor)
                fenetre.blit(carte2_bis.img,carte2_bis.coor)
                fenetre.blit(carte3_bis.img,carte3_bis.coor)
                fenetre.blit(carte4_bis.img,carte4_bis.coor)
                fenetre.blit(carte5_bis.img,carte5_bis.coor)
                fenetre.blit(carte6_bis.img,carte6_bis.coor)

                fenetre.blit(carte7.img,carte7.coor)
                fenetre.blit(carte8.img,carte8.coor)
                fenetre.blit(carte9.img,carte9.coor)
                fenetre.blit(carte7_bis.img,carte7_bis.coor)
                fenetre.blit(carte8_bis.img,carte8_bis.coor)
                fenetre.blit(carte9_bis.img,carte9_bis.coor)

                texte = font_score.render(langue.game_c_score, 5, (color_txt))
                fenetre.blit(texte, (1100, 250))
                texte = font_score.render(str(score_card), 5, (color_txt))
                fenetre.blit(texte, (1100, 300))
                texte = font_score.render(langue.game_c_best_score, 5, (color_txt))
                fenetre.blit(texte, (1100, 400))
                texte = font_score.render(str(best_score_card), 5, (color_txt))
                fenetre.blit(texte, (1100, 450))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                # Système de comparaison
                if sélection_carte1 != 0 and sélection_carte2 != 0 :
                    for i in range(len(liste_cartes_statut)) :
                        if sélection_carte1 == liste_cartes_statut[i].id:
                            if sélection_carte2 == liste_cartes_statut1[i].id:
                                liste_cartes_statut[i].stat = 2
                                liste_cartes_statut1[i].stat = 2
                                sélection_carte1 = 0
                                sélection_carte2 = 0
                                compte += 1
                                score_card += 100
                            else :
                                for j in range(len(liste_cartes_statut1)) :
                                    if liste_cartes_statut1[j].stat == 1 :
                                        liste_cartes_statut1[j].stat = 0
                                for j in range(len(liste_cartes_statut)) :
                                    if liste_cartes_statut[j].stat == 1 :
                                        liste_cartes_statut[j].stat = 0

                                sélection_carte1 = 0
                                sélection_carte2 = 0

                                if score_card >= 100 :
                                    score_card -= 50
                                else :
                                    score_card = 0

                    time.sleep(1)

                if compte == 9 :
                    pop_up()
                    if best_score_card < score_card:
                        best_score_card = score_card
                    texte = font_big.render(langue.game_c_win, 5, (color_txt))
                    fenetre.blit(texte, (550, 250))
                    pygame.display.flip()
                    reset_cartes()
                    compte = 0
                    data_base.update("best_score_card",str(best_score_card))
                    data_base.refresh()

                    time.sleep(2)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if (carte1.pos).collidepoint(event.pos):
                                carte1.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte1.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte1.id

                            if (carte2.pos).collidepoint(event.pos):
                                carte2.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte2.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte2.id

                            if (carte3.pos).collidepoint(event.pos):
                                carte3.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte3.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte3.id

                            if (carte4.pos).collidepoint(event.pos):
                                carte4.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte4.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte4.id

                            if (carte5.pos).collidepoint(event.pos):
                                carte5.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte5.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte5.id

                            if (carte6.pos).collidepoint(event.pos):
                                carte6.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte6.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte6.id

                            if (carte7.pos).collidepoint(event.pos):
                                carte7.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte7.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte7.id

                            if (carte8.pos).collidepoint(event.pos):
                                carte8.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte8.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte8.id

                            if (carte9.pos).collidepoint(event.pos):
                                carte9.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte9.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte9.id


                            if (carte1_bis.pos).collidepoint(event.pos):
                                carte1_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte1_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte1_bis.id

                            if (carte2_bis.pos).collidepoint(event.pos):
                                carte2_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte2_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte2_bis.id

                            if (carte3_bis.pos).collidepoint(event.pos):
                                carte3_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte3_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte3_bis.id

                            if (carte4_bis.pos).collidepoint(event.pos):
                                carte4_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte4_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte4_bis.id

                            if (carte5_bis.pos).collidepoint(event.pos):
                                carte5_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte5_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte5_bis.id

                            if (carte6_bis.pos).collidepoint(event.pos):
                                carte6_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte6_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte6_bis.id

                            if (carte7_bis.pos).collidepoint(event.pos):
                                carte7_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte7_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte7_bis.id

                            if (carte8_bis.pos).collidepoint(event.pos):
                                carte8_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte8_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte8_bis.id

                            if (carte9_bis.pos).collidepoint(event.pos):
                                carte9_bis.stat = 1
                                if sélection_carte1 == 0 and sélection_carte2 == 0 :
                                    sélection_carte1 = carte9_bis.id
                                elif sélection_carte1 != 0 and sélection_carte2 == 0 :
                                    sélection_carte2 = carte9_bis.id

                            if pos_score_card_reset.collidepoint(event.pos):
                                fenetre.blit(score_reset1,(1100,500))
                                pygame.display.flip()
                                reset_cartes()
                                compte = 0
                                best_score_card = 0
                                data_base.update("best_score_card",str(best_score_card))
                                data_base.refresh()
                                time.sleep(0.1)

                            if pos_card_reset.collidepoint(event.pos):
                                fenetre.blit(card_reset1,(1100,600))
                                pygame.display.flip()
                                reset_cartes()
                                compte = 0
                                time.sleep(0.1)

                            if pos_Menu.collidepoint(event.pos):
                                jeux_menu = True
                                compte = 0
                                reset_cartes()
                                Cartes = False

                    if event.type==KEYDOWN :
                        if event.key == K_ESCAPE:
                            jeux_menu = True
                            compte = 0
                            reset_cartes()
                            Cartes = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            while Puissance4_by_Maxime :
                étape_programme = "Jeux / Puissance 4 by Maxime Picture"
                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(Menu,(1150,20))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(5,5))

                # Jeux : Puissance 4 avec l'aimable autorisation de Maxime Banuls ( alias Maxime Picture )
                # Des modifications ont cependant été effectuées afin de le rendre compatible avec BNL's Box...

                #Début bibliothèque
                import pygame
                import math
                import random
                from pygame.locals import *

                #Préparation du chargement
                def chargement(nom_chargement):
                    '''Taille de la police'''
                    font_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 10)
                    '''Taille de la fenêtre'''
                    global fenetre
                    global color_correction_max
                    fenêtre = fenetre
                    '''Couleurs'''
                    couleur_fond_chargement=(0,0,0)
                    couleur_chargement=(255,255,255)
                    if color_P4_stat == "BNLs Box":
                        if color_aux == (255,0,0) or color_aux == (255,255,0):
                            color_correction_max = (255,160,0)
                        else :
                            color_correction_max = color_aux
                        couleur_barre=color_aux
                    elif color_P4_stat == "Maxime original":
                        couleur_barre=(0,150,255)
                        color_correction_max = color_aux

                    '''Barre vide + fond'''
                    pygame.draw.rect(fenêtre,couleur_fond_chargement,pygame.Rect(490,310,300,100))
                    pygame.draw.rect(fenêtre,couleur_chargement,pygame.Rect(49+490,29+310,202,42))
                    pygame.draw.rect(fenêtre,couleur_fond_chargement,pygame.Rect(52+490,32+310,196,36))
                    '''Texte du chargement pour tous'''
                    texte_chargement= font_p4_m.render("Chargement", 1, (255,255,255))
                    '''Précision du chargement'''
                    texte_chargement2= font_p4_m.render(nom_chargement, 1, (255,255,255))
                    '''Affichage du fond et du texte'''
                    fenêtre.blit(texte_chargement,(490+55,310+5))
                    fenêtre.blit(texte_chargement2,(135+490,5+310))
                    '''Rafraîchisement de l'écran'''
                    pygame.display.flip()
                    '''Coordonées X du début de la barre'''
                    charge_barre=52+490
                    '''Boucle du remplissage de la barre'''
                    for i in range(196):
                        '''Chargement'''
                        pygame.draw.rect(fenêtre,couleur_barre,pygame.Rect(charge_barre,32+310,1,36))
                        '''Rafraîchisement de l'écran'''
                        pygame.display.flip()
                        '''Avancement de la barre'''
                        charge_barre+=1
                        '''Délai du chargement'''
                        pygame.time.delay(random.randint(0,5))

                #Menu principal
                def Menu_principal():

                    d = 190
                    d1 = 60

                    global fenetre
                    fenêtre = fenetre
                    global Puissance4_by_Maxime
                    global jeux_menu

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    '''Variables'''
                    Menu_principal_actif=True
                    selection=1
                    Validation=False
                    changement=True
                    '''Couleur contours'''
                    if color_P4_stat == "BNLs Box":
                        couleur_contours=color_aux
                    elif color_P4_stat == "Maxime original":
                        couleur_contours=(0,150,255)

                    '''Hitboxes boutons'''
                    Bouton_puissance=Rect(((25+d,45+d1),(260,50)))
                    Bouton_parameters=Rect(((25+d,135+d1),(260,50)))
                    Bouton_quitter=Rect(((25+d,225+d1),(260,50)))
                    chargement(" du menu principal...")

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()
                    Fond_puissance=pygame.image.load("Games/Maxime Picture/Multi-game/Fond_puissance.png").convert_alpha()
                    Fond_parameters=pygame.image.load("Games/Maxime Picture/Multi-game/Fond_parameters.png").convert_alpha()
                    Fond_quitter=pygame.image.load("Games/Maxime Picture/Multi-game/Fond_quitter.png").convert_alpha()
                    font_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 30)
                    #actions
                    while Menu_principal_actif==True:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        for event in pygame.event.get():
                            if event.type==KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Menu_principal_actif = False
                                    jeux_menu = True
                                    Puissance4_by_Maxime = False
                                    Menu_principal_actif = False
                                    return
                                if event.key == K_DOWN:
                                    if selection!=3:
                                        selection+=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_UP:
                                    if selection!=1:
                                        selection-=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_RETURN or event.key == K_SPACE:
                                    Validation=True
                            elif event.type == pygame.MOUSEMOTION:
                                if Bouton_quitter.collidepoint(event.pos):
                                    selection=3
                                    changement=True
                                if Bouton_parameters.collidepoint(event.pos):
                                    selection=2
                                    changement=True
                                if Bouton_puissance.collidepoint(event.pos):
                                    selection=1
                                    changement=True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_stat = pygame.mouse.get_pressed()
                                if mouse_stat[0]:

                                    if Bouton_quitter.collidepoint(event.pos):
                                        Validation=True
                                    elif Bouton_parameters.collidepoint(event.pos):
                                        Validation=True
                                    elif Bouton_puissance.collidepoint(event.pos):
                                        Validation=True
                                    elif pos_Menu.collidepoint(event.pos):
                                        jeux_menu = True
                                        Puissance4_by_Maxime = False
                                        Menu_principal_actif = False
                                        return
                            elif event.type == QUIT:
                                if quit_enable and not(update_web):
                                    STOP()
                                elif quit_enable and update_web:
                                    STOP("Update.bat")
                        if Validation==True and selection==1:
                            Menu_principal_actif = False
                            puissance4(couleur_contours)
                        elif Validation==True and selection==2:
                            Menu_principal_actif = False
                            parameters_P4M(couleur_contours)
                        elif Validation==True and selection==3:
                            Menu_principal_actif = False
                            jeux_menu = True
                            Puissance4_by_Maxime = False
                            Menu_principal_actif = False
                            return
                        if changement==True:
                            changement=False
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0+d,0+d1,300,600))
                            if color_P4_stat == "BNLs Box":
                                pygame.draw.rect(fenêtre,color_aux,pygame.Rect(300+d,0+d1,600,600))
                            if color_P4_stat == "Maxime original":
                                pygame.draw.rect(fenêtre,(255,255,255),pygame.Rect(300+d,0+d1,600,600))
                            pygame.draw.rect(fenêtre,couleur_contours,pygame.Rect(20+d,-30+d1+70*selection,260,60))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(25+d,-25+d1+70*selection,250,50))
                            texte_menu1=font_p4_m.render("Puissance 4", 1, (255,255,255))
                            texte_menu_parameters=font_p4_m.render("Options", 1, (255,255,255))
                            texte_menu2=font_p4_m.render("Quitter", 1, (255,255,255))
                            fenêtre.blit(texte_menu1,(45+d,55+d1))
                            fenêtre.blit(texte_menu_parameters,(45+d,125+d1))
                            fenêtre.blit(texte_menu2,(45+d,195+d1))
                            if selection==1:
                                fenêtre.blit(Fond_puissance,(350+d,45+d1))
                            if selection==2:
                                fenêtre.blit(Fond_parameters,(350+d,50+d1))
                            if selection==3:
                                fenêtre.blit(Fond_quitter,(325+d,0+d1))

                            if update_at_quit:
                                fenetre.blit(download_stat_downloading,(5,5))

                            pygame.display.flip()

                def parameters_P4M(c1):

                    global fenetre
                    fenêtre = fenetre
                    global Puissance4_by_Maxime
                    global jeux_menu
                    global color_P4_stat

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    dis = 170
                    dis2 = 160
                    dis1 = 10

                    chargement("chargement des options")
                    Menu_parameters=True
                    selection=2
                    Jeu=False
                    fin=False
                    Validation=False
                    changement=True
                    Bouton_puissance_commencer=Rect(((300+dis,400-dis1),(370,80)))
                    Bouton_puissance_quitter=Rect(((360+dis,550-dis1),(260,80)))

                    check_box_activate=pygame.image.load("Games/Maxime Picture/Multi-game/parameters_check_box_activate.png").convert_alpha()
                    check_box_desactivate=pygame.image.load("Games/Maxime Picture/Multi-game/parameters_check_box_desactivate.png").convert_alpha()
                    pos_check_box = check_box_activate.get_rect(topleft=(550+dis,250-dis1))

                    font_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 10)
                    couleur1=(255,0,0)
                    couleur2=(255,255,0)
                    couleur_ligne_de_4=(0,0,0)
                    font_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 10)
                    font_titre_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 50)
                    font2_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 30)
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(360,20-dis1,560,700))
                    pygame.draw.rect(fenêtre,c1,pygame.Rect(365,25-dis1,550,690))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,30-dis1,540,680))
                    titre=font_titre_p4_m.render("Puissance 4", 1, (255,255,255))
                    t1=font2_p4_m.render("Options", 1, (255,255,255))
                    t2=font2_p4_m.render("Couleur du Puissance 4 :", 1, (255,255,255))
                    BNL_Puissance4 = font2_p4_m.render("BNL's Box :", 1, (255,255,255))
                    t3=font_titre_p4_m.render("Quitter", 1, (255,255,255))
                    fenêtre.blit(titre,(300+dis,50))
                    fenêtre.blit(t1,(400+dis,150-dis1))
                    fenêtre.blit(t2,(275+dis,200-dis1))
                    fenêtre.blit(BNL_Puissance4,(250+dis,250-dis1))
                    fenêtre.blit(t3,(380+dis,550-dis1))
                    if color_P4_stat == "BNLs Box":
                        fenêtre.blit(check_box_activate,(550+dis,250-dis1))
                    elif color_P4_stat == "Maxime original":
                        fenêtre.blit(check_box_desactivate,(550+dis,250-dis1))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()

                    while Menu_parameters==True:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        for event in pygame.event.get():
                            #quitter
                            if event.type==KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Menu_parameters = False
                                    Menu_principal()
                                if event.key == K_RETURN or event.key == K_SPACE:
                                    Validation=True
                            elif event.type == pygame.MOUSEMOTION:
                                if Bouton_puissance_quitter.collidepoint(event.pos):
                                    selection=2
                                    changement=True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_stat = pygame.mouse.get_pressed()
                                if mouse_stat[0]:
                                    if Bouton_puissance_quitter.collidepoint(event.pos):
                                        Validation=True
                                    elif pos_Menu.collidepoint(event.pos):
                                        jeux_menu = True
                                        Puissance4_by_Maxime = False
                                        return
                                    elif pos_check_box.collidepoint(event.pos):
                                        if color_P4_stat == "BNLs Box":
                                            color_P4_stat = "Maxime original"
                                            fenêtre.blit(check_box_desactivate,(550+dis,250-dis1))
                                        elif color_P4_stat == "Maxime original":
                                            color_P4_stat = "BNLs Box"
                                            fenêtre.blit(check_box_activate,(550+dis,250-dis1))

                                        data_base.update("color_P4_stat",str(color_P4_stat))

                            elif event.type == QUIT:
                                if quit_enable and not(update_web):
                                    STOP()
                                elif quit_enable and update_web:
                                    STOP("Update.bat")
                            if Validation==True and selection==1:
                                Menu_parameters = False
                                Jeu=True
                            if Validation==True and selection==2:
                                Menu_parameters = False
                                Menu_principal()
                            if changement==True:
                                changement=False

                        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(360,20-dis1,560,700))
                        pygame.draw.rect(fenêtre,c1,pygame.Rect(365,25-dis1,550,690))
                        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,30-dis1,540,680))
                        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,230-dis1,540,400))
                        if selection==2:
                            pygame.draw.rect(fenêtre,c1,pygame.Rect(360+dis,550-dis1,260,80))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(365+dis,555-dis1,250,70))
                        fenêtre.blit(titre,(300+dis,50))
                        fenêtre.blit(t1,(400+dis,150-dis1))
                        fenêtre.blit(t2,(275+dis,200-dis1))
                        fenêtre.blit(BNL_Puissance4,(250+dis,250-dis1))
                        fenêtre.blit(t3,(380+dis,550-dis1))
                        if color_P4_stat == "BNLs Box":
                            fenêtre.blit(check_box_activate,(550+dis,250-dis1))
                            c1 = color_aux
                        elif color_P4_stat == "Maxime original":
                            fenêtre.blit(check_box_desactivate,(550+dis,250-dis1))
                            c1 = (0,150,255)

                        if update_at_quit:
                            fenetre.blit(download_stat_downloading,(5,5))

                        pygame.display.flip()

                def puissance4(c1):

                    global fenetre
                    fenêtre = fenetre
                    global Puissance4_by_Maxime
                    global jeux_menu

                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(Menu,(1150,20))

                    dis = 170
                    dis2 = 160
                    dis1 = 10

                    chargement("du puissance 4")
                    Menu_puissance=True
                    selection=1
                    selection2=1
                    Jeu=False
                    fin=False
                    Validation=False
                    changement=True
                    Bouton_puissance_commencer=Rect(((300+dis,400-dis1),(370,80)))
                    Bouton_puissance_quitter=Rect(((360+dis,550-dis1),(260,80)))
                    Boutonj1=Rect(((280+dis,230-dis1),(140,140)))
                    Boutonj2=Rect(((530+dis,230-dis1),(140,140)))
                    font_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 10)
                    couleur1=(255,0,0)
                    couleur2=(255,255,0)
                    couleur_ligne_de_4=(0,0,0)
                    font_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 10)
                    font_titre_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 50)
                    font2_p4_m = pygame.font.Font("Games/Maxime Picture/Multi-game/police.ttf", 30)
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(360,20-dis1,560,700))
                    pygame.draw.rect(fenêtre,c1,pygame.Rect(365,25-dis1,550,690))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,30-dis1,540,680))
                    titre=font_titre_p4_m.render("Puissance 4", 1, (255,255,255))
                    t1=font2_p4_m.render("Qui commence ?", 1, (255,255,255))
                    t2=font_titre_p4_m.render("Commencer", 1, (255,255,255))
                    t3=font_titre_p4_m.render("Quitter", 1, (255,255,255))
                    t4=font_titre_p4_m.render("Victoire", 1, (255,255,255))
                    t5=font_titre_p4_m.render("du Joueur", 1, (255,255,255))
                    v1=font_titre_p4_m.render("1", 1, (255,255,255))
                    v2=font_titre_p4_m.render("2", 1, (255,255,255))
                    v3=font_titre_p4_m.render("Egalité", 1, (255,255,255))
                    fenêtre.blit(titre,(300+dis,50))
                    fenêtre.blit(t1,(350+dis,150-dis1))
                    fenêtre.blit(t2,(320+dis,400-dis1))
                    fenêtre.blit(t3,(380+dis,550-dis1))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(5,5))

                    pygame.display.flip()

                    while Menu_puissance==True:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        for event in pygame.event.get():
                            #quitter
                            if event.type==KEYDOWN:
                                if event.key == K_ESCAPE:
                                    Menu_puissance = False
                                    Menu_principal()
                                if event.key == K_DOWN:
                                    if selection!=2:
                                        selection+=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_UP:
                                    if selection!=1:
                                        selection-=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_LEFT:
                                    if selection2!=1:
                                        selection2-=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_RIGHT:
                                    if selection2!=2:
                                        selection2+=1
                                        changement=True
                                        pygame.time.delay(50)
                                if event.key == K_RETURN or event.key == K_SPACE:
                                    Validation=True
                            elif event.type == pygame.MOUSEMOTION:
                                if Bouton_puissance_commencer.collidepoint(event.pos):
                                    selection=1
                                    changement=True
                                if Bouton_puissance_quitter.collidepoint(event.pos):
                                    selection=2
                                    changement=True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_stat = pygame.mouse.get_pressed()
                                if mouse_stat[0]:
                                    if Bouton_puissance_commencer.collidepoint(event.pos):
                                        Validation=True
                                    elif Bouton_puissance_quitter.collidepoint(event.pos):
                                        Validation=True
                                    elif Boutonj1.collidepoint(event.pos):
                                        changement=True
                                        selection2=1
                                    elif Boutonj2.collidepoint(event.pos):
                                        changement=True
                                        selection2=2
                                    elif pos_Menu.collidepoint(event.pos):
                                        jeux_menu = True
                                        Puissance4_by_Maxime = False
                                        return
                            elif event.type == QUIT:
                                if quit_enable and not(update_web):
                                    STOP()
                                elif quit_enable and update_web:
                                    STOP("Update.bat")
                            if Validation==True and selection==1:
                                Menu_puissance = False
                                Jeu=True
                            if Validation==True and selection==2:
                                Menu_puissance = False
                                Menu_principal()
                            if changement==True:
                                changement=False
                                pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(370,230-dis1,540,400))
                                if selection2==1:
                                    pygame.draw.rect(fenêtre,c1,pygame.Rect(280+dis,230-dis1,140,140))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(285+dis,235-dis1,130,130))
                                    joueur=1
                                elif selection2==2:
                                    pygame.draw.rect(fenêtre,c1,pygame.Rect(530+dis,230-dis1,140,140))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(535+dis,235-dis1,130,130))
                                    joueur=2
                                if selection==1:
                                    pygame.draw.rect(fenêtre,c1,pygame.Rect(300+dis,400-dis1,370,80))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(305+dis,405-dis1,360,70))
                                elif selection==2:
                                    pygame.draw.rect(fenêtre,c1,pygame.Rect(360+dis,550-dis1,260,80))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(365+dis,555-dis1,250,70))

                                pygame.draw.circle(fenêtre,couleur1, (350+dis,300-dis1),50,0)
                                pygame.draw.circle(fenêtre,couleur2, (600+dis,300-dis1),50,0)
                                fenêtre.blit(t2,(320+dis,400-dis1))
                                fenêtre.blit(t3,(380+dis,550-dis1))
                                pygame.display.flip()

                    m1,m2=0,0
                    if Jeu==True:
                        changement_puissance=True
                        selection_puissance=38
                        case=3
                        b=5
                        victoire=0
                        c=False
                        d=0
                        bouge=True
                        épaisseur_trait=15
                        emplacements=[5,5,5,5,5,5,5]
                        grille=[[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0]]
                        Colone1=Rect(((60+dis2,0),(120,740)))
                        Colone2=Rect(((180+dis2,0),(120,740)))
                        Colone3=Rect(((300+dis2,0),(120,740)))
                        Colone4=Rect(((420+dis2,0),(120,740)))
                        Colone5=Rect(((540+dis2,0),(120,740)))
                        Colone6=Rect(((660+dis2,0),(120,740)))
                        Colone7=Rect(((780+dis2,0),(120,740)))

                        while Jeu==True:

                            if audio_reader_proc.is_finish():
                                audio_reader_proc.avancer()

                            for event in pygame.event.get():
                                if event.type==KEYDOWN:
                                    if event.key == K_ESCAPE:
                                        Jeu=False
                                        puissance4(c1)
                                    if event.key == K_LEFT:
                                        if case!=0:
                                            a=[]
                                            bouge=True
                                            for i in range(case):
                                                if emplacements[case-1-i]!=-1:
                                                    a.append(case-1-i)
                                            if a!=[]:
                                                case=a[0]
                                            changement_puissance=True
                                            pygame.time.delay(50)
                                    if event.key == K_RIGHT:
                                        if case!=6:
                                            a=[]
                                            bouge=True
                                            for i in range(6-case):
                                                if emplacements[case+1+i]!=-1:
                                                    a.append(case+1+i)
                                            if a!=[]:
                                                case=a[0]
                                            changement_puissance=True
                                            pygame.time.delay(50)
                                    if event.key == K_RETURN or event.key == K_SPACE:
                                        if joueur==1:
                                            grille[b][case]=1
                                            joueur=2
                                        else:
                                            grille[b][case]=5
                                            joueur=1
                                        bouge=True
                                        if emplacements[case]>=0:
                                                emplacements[case]-=1
                                        pygame.time.delay(50)
                                        changement_puissance=True
                                elif event.type == pygame.MOUSEMOTION:
                                    if Colone1.collidepoint(event.pos):
                                        case=0
                                        changement_puissance=True
                                    elif Colone2.collidepoint(event.pos):
                                        case=1
                                        changement_puissance=True
                                    elif Colone3.collidepoint(event.pos):
                                        case=2
                                        changement_puissance=True
                                    elif Colone4.collidepoint(event.pos):
                                        case=3
                                        changement_puissance=True
                                    elif Colone5.collidepoint(event.pos):
                                        case=4
                                        changement_puissance=True
                                    elif Colone6.collidepoint(event.pos):
                                        case=5
                                        changement_puissance=True
                                    elif Colone7.collidepoint(event.pos):
                                        case=6
                                        changement_puissance=True
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_stat = pygame.mouse.get_pressed()
                                    if mouse_stat[0]:
                                        if joueur==1:
                                            grille[b][case]=1
                                            joueur=2
                                        else:
                                            grille[b][case]=5
                                            joueur=1
                                        bouge=True
                                        if emplacements[case]>=0:
                                                emplacements[case]-=1
                                        pygame.time.delay(50)
                                        changement_puissance=True
                                        if pos_Menu.collidepoint(event.pos):
                                            jeux_menu = True
                                            Puissance4_by_Maxime = False
                                            return
                                elif event.type == QUIT:
                                    if quit_enable and not(update_web):
                                        STOP()
                                    elif quit_enable and update_web:
                                        STOP("Update.bat")
                            if changement_puissance==True:
                                changement_puissance=False
                                pygame.draw.rect(fenêtre,(0,0,255),pygame.Rect(0+dis2,0,960,740))
                                for i in range(7):
                                    for i in range(6):
                                     for j in range(7):
                                            if grille[i][j]==0:
                                                pygame.draw.circle(fenêtre,(255,255,255), (120+j*120+dis2,70+i*120),50,0)
                                            elif grille[i][j]==1:
                                                pygame.draw.circle(fenêtre,(255,0,0), (120+j*120+dis2,70+i*120),50,0)
                                            elif grille[i][j]==5:
                                                pygame.draw.circle(fenêtre,(255,255,0), (120+j*120+dis2,70+i*120),50,0)

                                b=emplacements[case]
                                if b!=-1:
                                    pygame.draw.circle(fenêtre,color_correction_max, (120+case*120+dis2,70+b*120),25,0)
                                    if joueur==1:
                                        pygame.draw.circle(fenêtre,couleur1, (120+case*120+dis2,70+b*120),15,0)
                                    else:
                                        pygame.draw.circle(fenêtre,couleur2, (120+case*120+dis2,70+b*120),15,0)
                                else:
                                    c=True
                                    d=0
                                    while c==True:
                                        if emplacements[case]!=-1:
                                            c=False
                                        elif case!=6:
                                            case+=1
                                        else:
                                            case=0
                                        d+=1
                                        if d==10:
                                            c=False
                                    b=emplacements[case]
                                    pygame.draw.circle(fenêtre,color_correction_max, (120+case*120+dis2,70+b*120),25,0)
                                    if joueur==1:
                                        pygame.draw.circle(fenêtre,couleur1, (120+case*120+dis2,70+b*120),15,0)
                                    else:
                                        pygame.draw.circle(fenêtre,couleur2, (120+case*120+dis2,70+b*120),15,0)
                                if bouge==True:
                                    pygame.mouse.set_pos((120+120*case+dis2,70+120*b))
                                bouge=False
                                pygame.display.flip()
                                for i in range(6):
                                    for j in range(4):
                                        if grille[i][j]+grille[i][j+1]+grille[i][j+2]+grille[i][j+3]==4:
                                            victoire=1
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*(j+3)+dis2,70+120*i),épaisseur_trait)
                                            fin=True
                                        elif grille[i][j]+grille[i][j+1]+grille[i][j+2]+grille[i][j+3]==20:
                                            victoire=2
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*(j+3)+dis2,70+120*i),épaisseur_trait)
                                            fin=True
                                for i in range(3):
                                    for j in range(7):
                                        if grille[i][j]+grille[i+1][j]+grille[i+2][j]+grille[i+3][j]==4:
                                            victoire=1
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*j+dis2,70+120*(i+3)),épaisseur_trait)
                                            fin=True
                                        elif grille[i][j]+grille[i+1][j]+grille[i+2][j]+grille[i+3][j]==20:
                                            victoire=2
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*j+dis2,70+120*(i+3)),épaisseur_trait)
                                            fin=True
                                for i in range(3):
                                    for j in range(4):
                                        if grille[i][j]+grille[i+1][j+1]+grille[i+2][j+2]+grille[i+3][j+3]==4:
                                            victoire=1
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*(j+3)+dis2,70+120*(i+3)),épaisseur_trait)
                                            fin=True
                                        elif grille[i][j]+grille[i+1][j+1]+grille[i+2][j+2]+grille[i+3][j+3]==20:
                                            victoire=2
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*(j+3)+dis2,70+120*(i+3)),épaisseur_trait)
                                            fin=True
                                for i in range(3):
                                    for j in range(3,7):
                                        if grille[i][j]+grille[i+1][j-1]+grille[i+2][j-2]+grille[i+3][j-3]==4:
                                            victoire=1
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*(j-3)+dis2,70+120*(i+3)),épaisseur_trait)
                                            fin=True
                                        elif grille[i][j]+grille[i+1][j-1]+grille[i+2][j-2]+grille[i+3][j-3]==20:
                                            victoire=2
                                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j+dis2,70+120*i),(120+120*(j-3)+dis2,70+120*(i+3)),épaisseur_trait)
                                            fin=True
                                if emplacements==[-1,-1,-1,-1,-1,-1,-1]:
                                    victoire=3
                                    fin=True
                                if fin==True:
                                    pygame.display.flip()
                                    pygame.time.delay(1000)
                                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(205+dis,25-dis1,550,690))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(210+dis,30-dis1,540,680))
                                    if victoire==1:
                                        fenêtre.blit(t4,(350+dis,150-dis1))
                                        fenêtre.blit(t5,(320+dis,200-dis1))
                                        fenêtre.blit(v1,(600+dis,200-dis1))
                                        pygame.draw.circle(fenêtre,(255,0,0), (480+dis,370-dis1),50,0)
                                    elif victoire==2:
                                        fenêtre.blit(t4,(350+dis,150-dis1))
                                        fenêtre.blit(t5,(320+dis,200-dis1))
                                        fenêtre.blit(v2,(600+dis,200-dis1))
                                        pygame.draw.circle(fenêtre,(255,255,0), (480+dis,370-dis1),50,0)
                                    elif victoire==3:
                                        fenêtre.blit(v3,(320+dis+20,200-dis1))
                                    pygame.display.flip()
                                    pygame.time.delay(2000)
                                    Jeu=False
                                    puissance4(c1)

                if Puissance4_by_Maxime:
                    Menu_principal()

            while Jump:

                while Jump_menu:
                    étape_programme = "Jeux / WALL-E's Jump by MINI Picture / Menu"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    fenetre.blit(Jump_landscape,(0,-100))
                    fenetre.blit(Jump_dirt1,(0,650))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Jump_menu_alpha,(0,0))
                    fenetre.blit(Jump_menu_play_button,(50,250))
                    fenetre.blit(Jump_menu_settings_button,(50,300))
                    fenetre.blit(Jump_menu_help_button,(50,350))
                    fenetre.blit(Jump_menu_quit_button,(50,400))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Jump_menu = False
                                    jeux_menu = True
                                    Jump = False
                                    Jump_active = False
                                if pos_Jump_menu_play_button.collidepoint(event.pos):
                                    Jump_menu = False
                                    Jump_active = True
                                if pos_Jump_menu_quit_button.collidepoint(event.pos):
                                    Jump_menu = False
                                    jeux_menu = True
                                    Jump = False
                                    Jump_active = False

                        if event.type==KEYDOWN :
                            if event.key == K_ESCAPE:
                                Jump_menu = False
                                jeux_menu = True
                                Jump = False
                                Jump_active = False

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while Jump_active:
                    étape_programme = "Jeux / WALL-E's Jump by MINI Picture / Jeu"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    liste_obstacles = [Jump_obstacle1, Jump_obstacle2, Jump_obstacle3]
                    liste_clouds = [Jump_cloud1,Jump_cloud2,Jump_cloud3,Jump_cloud4]

                    if Jump_init:
                        
                        jump_ratio = 15                     
                        obstacle1 = random.choice(liste_obstacles)
                        obstacle2 = random.choice(liste_obstacles)
                        obstacle3 = random.choice(liste_obstacles)
                        obstacle4 = random.choice(liste_obstacles)

                        player_dec = 600-Jump_player.get_height()+50
                        obstacle1_dec = 600-obstacle1.get_height()+50
                        obstacle2_dec = 600-obstacle2.get_height()+50
                        obstacle3_dec = 600-obstacle3.get_height()+50
                        obstacle4_dec = 600-obstacle4.get_height()+50

                        obstacle1_coor = [random.randint(1280,1500),obstacle1_dec]
                        obstacle2_coor = [random.randint(obstacle1_coor[0]+obstacle1.get_width(),obstacle1_coor[0]+obstacle1.get_width()+500)+500,obstacle2_dec]
                        obstacle3_coor = [random.randint(obstacle2_coor[0]+obstacle2.get_width(),obstacle2_coor[0]+obstacle2.get_width()+500)+500,obstacle3_dec]
                        obstacle4_coor = [random.randint(obstacle3_coor[0]+obstacle3.get_width(),obstacle3_coor[0]+obstacle3.get_width()+500)+500,obstacle4_dec]
                        dirt1_coor = [0,650]
                        dirt2_coor = [1280,650]

                        cloud1 = random.choice(liste_clouds)
                        cloud2 = random.choice(liste_clouds)
                        cloud3 = random.choice(liste_clouds)
                        cloud4 = random.choice(liste_clouds)

                        cloud1_coor = [random.randint(0,1280),random.randint(100,300)]
                        cloud2_coor = [random.randint(0,1280),random.randint(100,300)]
                        cloud3_coor = [random.randint(0,1280),random.randint(100,300)]
                        cloud4_coor = [random.randint(0,1280),random.randint(100,300)]

                        Jump_avance1 = 0
                        Jump_avance2 = 0
                        Jump_avance3 = 0
                        Jump_avance4 = 0
                        Jump_avance_dirt = 0

                        Jump_avance_cloud1 = 0
                        Jump_avance_cloud2 = 0
                        Jump_avance_cloud3 = 0
                        Jump_avance_cloud4 = 0

                        score_jump = 0

                        Jump_init = False

                        Jump_player_count = 0

                        Jump_player_use = Jump_player

                        Jump_cube = False

                    if Jump_play:
                        Jump_avance1 += 10
                        Jump_avance2 += 10
                        Jump_avance3 += 10
                        Jump_avance4 += 10
                        Jump_avance_dirt += 10
                        Jump_player_count += 1
                        Jump_avance_cloud1 += 1
                        Jump_avance_cloud2 += 1
                        Jump_avance_cloud3 += 1
                        Jump_avance_cloud4 += 1

                        score_jump += 1
                        if score_jump > best_score_jump:
                            best_score_jump = score_jump

                    if obstacle4_coor[0]-Jump_avance4 < -200:
                        Jump_avance4 = 0
                        obstacle4 = random.choice(liste_obstacles)
                        obstacle4_dec = 600-obstacle4.get_height()+50
                        obstacle4_coor = [random.randint(obstacle3_coor[0]+obstacle3.get_width(),obstacle3_coor[0]+obstacle3.get_width()+500)+500,obstacle4_dec]
                    if obstacle3_coor[0]-Jump_avance3 < -200:
                        Jump_avance3 = 0
                        obstacle3 = random.choice(liste_obstacles)
                        obstacle3_dec = 600-obstacle3.get_height()+50
                        obstacle3_coor = [random.randint(obstacle2_coor[0]+obstacle2.get_width(),obstacle2_coor[0]+obstacle2.get_width()+500)+500,obstacle3_dec]
                    if obstacle2_coor[0]-Jump_avance2 < -200:
                        Jump_avance2 = 0
                        obstacle2 = random.choice(liste_obstacles)
                        obstacle2_dec = 600-obstacle2.get_height()+50
                        obstacle2_coor = [random.randint(obstacle1_coor[0]+obstacle1.get_width(),obstacle1_coor[0]+obstacle1.get_width()+500)+500,obstacle2_dec]
                    if obstacle1_coor[0]-Jump_avance1 < -200:
                        Jump_avance1 = 0
                        obstacle1 = random.choice(liste_obstacles)
                        obstacle1_dec = 600-obstacle1.get_height()+50
                        obstacle1_coor = [random.randint(1280,1500),obstacle1_dec]

                    if cloud1_coor[0]-Jump_avance_cloud1 < -(cloud1.get_width()):
                        Jump_avance_cloud1 = 0
                        cloud1 = random.choice(liste_clouds)
                        cloud1_coor = [random.randint(1280,2000),random.randint(100,300)]
                    if cloud2_coor[0]-Jump_avance_cloud2 < -(cloud2.get_width()):
                        Jump_avance_cloud2 = 0
                        cloud2 = random.choice(liste_clouds)
                        cloud2_coor = [random.randint(1280,2000),random.randint(100,300)]
                    if cloud3_coor[0]-Jump_avance_cloud3 < -(cloud3.get_width()):
                        Jump_avance_cloud3 = 0
                        cloud3 = random.choice(liste_clouds)
                        cloud3_coor = [random.randint(1280,2000),random.randint(100,300)]
                    if cloud4_coor[0]-Jump_avance_cloud4 < -(cloud4.get_width()):
                        Jump_avance_cloud4 = 0
                        cloud4 = random.choice(liste_clouds)
                        cloud4_coor = [random.randint(1280,2000),random.randint(100,300)]

                    if Jump_player_count == 0 and not(Jump_cube):
                        Jump_player_use = Jump_player
                    elif Jump_player_count == 25 and not(Jump_cube):
                        Jump_player_use = Jump_player1
                    elif Jump_player_count == 50 and not(Jump_cube):
                        Jump_player_count = -1

                    fenetre.blit(Jump_landscape,(0,-100))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Jump_dirt1,(dirt1_coor[0]-Jump_avance_dirt,dirt1_coor[1]))
                    fenetre.blit(Jump_dirt1,(dirt2_coor[0]-Jump_avance_dirt,dirt2_coor[1]))
                    if Jump_avance_dirt > 1280:
                        Jump_avance_dirt = 0

                    texte = font.render(langue.game_c_score, 5, (color_txt))
                    fenetre.blit(texte, (100, 100))
                    texte = font.render(str(score_jump), 5, (color_txt))
                    fenetre.blit(texte, (180, 100))
                    texte = font.render(langue.game_c_best_score, 5, (color_txt))
                    fenetre.blit(texte, (600, 100))
                    texte = font.render(str(best_score_jump), 5, (color_txt))
                    fenetre.blit(texte, (730, 100))

                    if Jump_check and Jump_play:
                        player_coor[1] -= jump_ratio
                        jump_ratio -= 0.5
                        if player_coor[1] > 600-Jump_player_use.get_height()+50:
                            Jump_check = False
                            player_coor[1] = 600-Jump_player_use.get_height()+50

                    elif not(Jump_check) and Jump_play:
                        jump_ratio = 15
                        player_coor = [100,600-Jump_player_use.get_height()+50]

                    fenetre.blit(cloud1,(cloud1_coor[0]-Jump_avance_cloud1,cloud1_coor[1]))
                    fenetre.blit(cloud2,(cloud2_coor[0]-Jump_avance_cloud2,cloud2_coor[1]))
                    fenetre.blit(cloud3,(cloud3_coor[0]-Jump_avance_cloud3,cloud3_coor[1]))
                    fenetre.blit(cloud4,(cloud4_coor[0]-Jump_avance_cloud4,cloud4_coor[1]))

                    fenetre.blit(Jump_player_use,player_coor)

                    fenetre.blit(obstacle1,(obstacle1_coor[0]-Jump_avance1,obstacle1_dec))
                    fenetre.blit(obstacle2,(obstacle2_coor[0]-Jump_avance2,obstacle2_dec))
                    fenetre.blit(obstacle3,(obstacle3_coor[0]-Jump_avance3,obstacle3_dec))
                    fenetre.blit(obstacle4,(obstacle4_coor[0]-Jump_avance4,obstacle4_dec))

                    pos_Jump_player = Jump_player_use.get_rect(topleft=player_coor)

                    pos_Jump_obstacle1 = obstacle1.get_rect(topleft=(obstacle1_coor[0]-Jump_avance1,obstacle1_dec))
                    pos_Jump_obstacle2 = obstacle2.get_rect(topleft=(obstacle2_coor[0]-Jump_avance2,obstacle2_dec))
                    pos_Jump_obstacle3 = obstacle3.get_rect(topleft=(obstacle3_coor[0]-Jump_avance3,obstacle3_dec))
                    pos_Jump_obstacle4 = obstacle4.get_rect(topleft=(obstacle4_coor[0]-Jump_avance4,obstacle4_dec))

                    if not(Jump_play):
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(638-200,358-200,4+200*2, 4+200*2))
                        pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(640-200,360-200,1+200*2, 1+200*2))
                        texte = font_big.render("PERDU !", 5, (color_txt))
                        fenetre.blit(texte, (540, 250))

                    time.sleep(0.01)

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    pygame.display.flip()

                    if (pos_Jump_player.colliderect(pos_Jump_obstacle1) or pos_Jump_player.colliderect(pos_Jump_obstacle2) or pos_Jump_player.colliderect(pos_Jump_obstacle3) or pos_Jump_player.colliderect(pos_Jump_obstacle4)) and Jump_play:
                        Jump_play = False
                        pop_up()

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Jump_menu = True
                                    Jump_active = False
                                    data_base.update("best_score_jump",str(best_score_jump))
                                    data_base.refresh()

                        if event.type==KEYDOWN :
                            if event.key == K_SPACE and not(Jump_check):
                                Jump_check = True
                                Jump_cube = False
                                Jump_player_count = -1
                                Jump_player_use = Jump_player
                                player_coor = [100,600-Jump_player_use.get_height()+50]

                            if event.key == K_ESCAPE:
                                Jump_menu = True
                                Jump_active = False
                                data_base.update("best_score_jump",str(best_score_jump))
                                data_base.refresh()

                            if (event.key == pygame.K_c) and Jump_play:
                                if not(Jump_cube):
                                    Jump_cube = True
                                    Jump_player_use = Jump_player_cube
                                else:
                                    Jump_cube = False
                                    Jump_player_count = -1

                            if (event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN) and not(Jump_play):
                                Jump_play = True
                                Jump_check = False
                                Jump_up = False
                                player_coor = [615,600]
                                obstacle_coor = [1280,600]
                                Jump_avance = 0
                                Jump_init = True
                                data_base.update("best_score_jump",str(best_score_jump))
                                data_base.refresh()

                        if event.type == QUIT:
                            data_base.update("best_score_jump",str(best_score_jump))
                            data_base.refresh()
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

            while TANK_M :
                étape_programme = "Jeux / T.A.N.K.S by Maxime Picture"
                """
                T.A.N.K.S : production de Maxime Picture, tous droits réservés... Des modifications à des fins de compatibilités ont toutefois été effectuées,
                afin de l'intégrer à la BNL's Box
                """

                #Project T.A.N.K.S.
                ##########################################################################
                #bibliothèques

                import random as rn

                ###########################################################################
                #Tank
                #[vitesse de déplacement,vitesse de rotation,vie maximale,munitions max, dégats, vitesse_balles,vitesse de rechargement]
                class Tank:
                    #données du tank
                    def __init__(self,x,y,dir,spr,id,vit,vit_rot,vie,max_ammo,deg,vit_bul,vit_rech,f):
                        self.fe=f
                        self.x=x
                        self.y=y
                        self.dir=dir
                        self.spr2=spr
                        self.spr=pygame.transform.rotate(self.spr2,self.dir)
                        self.rec=self.spr.get_rect(center=(self.x, self.y))
                        self.id=id
                        self.vit=vit
                        self.vit_rot=vit_rot
                        self.vie=vie
                        self.vieleft=vie
                        self.ammo=max_ammo
                        self.max_ammo=max_ammo
                        self.deg=deg
                        self.vit_bul=vit_bul
                        self.vit_rech=vit_rech
                        self.classe="None"

                    #tourner
                    def tourner(self,x):
                        self.dir+=x
                        self.spr=pygame.transform.rotate(self.spr2,self.dir)
                        self.rec=self.spr.get_rect(center = self.spr.get_rect(center = (self.x, self.y)).center)
                        if self.rec[0]<5 or self.rec[0]>1275-self.rec[2] or self.rec[1]<5 or self.rec[1]>715-self.rec[3]:
                            self.dir-=x
                            self.spr=pygame.transform.rotate(self.spr2,self.dir)
                            self.rec=self.spr.get_rect(center = self.spr.get_rect(center = (self.x, self.y)).center)
                    #avancer
                    def avancer(self,x):
                        dx = x *cos((self.dir+90)*pi/180)
                        dy = - x *sin((self.dir+90)*pi/180)
                        self.x += dx
                        self.y += dy
                        self.rec=self.spr.get_rect(center = self.spr.get_rect(center = (self.x, self.y)).center)
                        if self.rec[0]<5 or self.rec[0]>1275-self.rec[2] or self.rec[1]<5 or self.rec[1]>715-self.rec[3]:
                            dx = -x *cos((self.dir+90)*pi/180)
                            dy = x *sin((self.dir+90)*pi/180)
                            self.x += dx
                            self.y += dy
                            self.rec=self.spr.get_rect(center = self.spr.get_rect(center = (self.x, self.y)).center)
                    #tirer
                    def tirer(self):
                        if self.id==1 and self.ammo!=0:
                            balle=Bullet(pygame.image.load("Games/Maxime Picture/Tanks/bullet_r.png").convert_alpha(),self.rec[0]+self.rec[2]/2-4,self.rec[1]+self.rec[3]/2-4,self.dir,1,self.vit_bul,self.fe)
                            self.ammo-=1
                            bullets.append(balle)
                        elif self.id==2 and self.ammo!=0:
                            balle=Bullet(pygame.image.load("Games/Maxime Picture/Tanks/bullet_b.png").convert_alpha(),self.rec[0]+self.rec[2]/2-4,self.rec[1]+self.rec[3]/2-4,self.dir,2,self.vit_bul,self.fe)
                            self.ammo-=1
                            bullets.append(balle)
                ##################################################################################################################
                #Balles
                bullets=[]
                class Bullet():
                    #Données balles
                    def __init__(self,spr,x,y,dir,id,vit,f):
                        self.fe=f
                        self.spr=pygame.transform.rotate(spr,dir)
                        self.x=x
                        self.y=y
                        self.dir=dir
                        self.rec=self.spr.get_rect()
                        self.rec[0],self.rec[1]=self.x,self.y
                        self.id=id
                        self.vit=vit
                    #déplacement balles
                    def avancer(self,l,t1,t2):
                        if self.id==1 and pygame.Rect.colliderect(self.rec,t2.rec):
                            t2.vieleft-=t1.deg
                            for _ in range(50):
                                s=particles("Games/Maxime Picture/Tanks/par_2.png",self.x,self.y,self.fe)
                                particules.append(s)
                            bullets.pop(l)
                        if self.id==2 and pygame.Rect.colliderect(self.rec,t1.rec):
                            for _ in range(50):
                                s=particles("Games/Maxime Picture/Tanks/par_1.png",self.x,self.y,self.fe)
                                particules.append(s)
                            t1.vieleft-=t2.deg
                            bullets.pop(l)
                        if self.rec[0]>5 and self.rec[0]<1275-self.rec[2] and self.rec[1]>5 and self.rec[1]<715-self.rec[3]:
                            dx = self.vit *cos((self.dir+90)*pi/180)
                            dy = - self.vit *sin((self.dir+90)*pi/180)
                            self.x += dx
                            self.y += dy
                            self.rec=self.spr.get_rect(center = self.spr.get_rect(center = (self.x, self.y)).center)
                        else:
                            for _ in range(50):
                                s=particles("Games/Maxime Picture/Tanks/par_0.png",self.x,self.y,self.fe)
                                particules.append(s)
                            bullets.pop(l)



                #############################################################################################################
                particules=[]
                class particles():
                    def __init__(self,spr,x,y,f):
                        self.fe=f
                        self.x=x
                        self.y=y
                        self.vit=rn.randint(1,7)/10
                        self.size=rn.randint(1,5)
                        self.dir=rn.randint(-179,180)
                        self.lifetime=rn.randint(60,180)
                        self.rec=pygame.image.load(spr).convert_alpha()
                        self.rec=pygame.transform.scale(self.rec,(self.size,self.size))
                        self.rec=pygame.transform.rotate(self.rec,rn.randint(0,45))
                    def move(self):
                        self.lifetime-=1
                        self.x+= self.vit *cos((self.dir+90)*pi/180)
                        self.y+= - self.vit *sin((self.dir+90)*pi/180)
                ################################################################################################
                def upgrade(tank,fenêtre):
                    global TANK_M
                    global jeux_menu
                    list_up=["Games/Maxime Picture/Tanks/Santé.png","Games/Maxime Picture/Tanks/deg.png","Games/Maxime Picture/Tanks/Vroum.png"]
                    l_up=[]
                    touches=[K_s,K_DOWN,K_q,K_d,K_LEFT,K_a,K_RIGHT]
                    selec=1
                    for _ in range(3):
                        up=rn.randint(0,2)
                        l_up.append(up)
                    fenêtre.blit(pygame.image.load("Games/Maxime Picture/Tanks/Fond_Menu.png").convert_alpha(),(5,5))
                    fenêtre.blit(pygame.image.load(list_up[l_up[1]]).convert_alpha(),(490,100))
                    pygame.display.flip()
                    time.sleep(1)
                    fenêtre.blit(pygame.image.load(list_up[l_up[0]]).convert_alpha(),(95,100))
                    pygame.display.flip()
                    time.sleep(1)
                    fenêtre.blit(pygame.image.load(list_up[l_up[2]]).convert_alpha(),(885,100))
                    pygame.display.flip()
                    time.sleep(1)
                    upgrade_en_cours=True
                    while upgrade_en_cours:
                        fenêtre.blit(pygame.image.load("Games/Maxime Picture/Tanks/Fond_Menu.png").convert_alpha(),(5,5))
                        fenêtre.blit(pygame.image.load(list_up[l_up[0]]).convert_alpha(),(95,100))
                        fenêtre.blit(pygame.image.load(list_up[l_up[1]]).convert_alpha(),(490,100))
                        fenêtre.blit(pygame.image.load(list_up[l_up[2]]).convert_alpha(),(885,100))
                        fenêtre.blit(pygame.image.load("Games/Maxime Picture/Tanks/curseur.png").convert_alpha(),(selec*395+225,25))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type==KEYDOWN:
                                if event.key==touches[tank.id-1]:
                                    upgrade_en_cours=False
                                    if list_up[l_up[selec]]=="Games/Maxime Picture/Tanks/Santé.png":
                                        tank.vie = tank.vie*2
                                    elif list_up[l_up[selec]]=="Games/Maxime Picture/Tanks/deg.png":
                                        tank.deg = tank.deg*1.7
                                    elif list_up[l_up[selec]]=="Games/Maxime Picture/Tanks/Vroum.png":
                                        tank.vit = tank.vit*1.3
                                        tank.vit_rot = tank.vit_rot*0.8
                                if event.key==touches[tank.id*2] or (tank.id==1 and touches[5]==event.key):
                                    if selec!=0:
                                        selec-=1
                                if event.key==touches[tank.id*3]:
                                    if selec!=2:
                                        selec+=1
                            if event.type==QUIT:
                                STOP(None)
                ################################################################################################
                #Menu

                def menu():
                    global fenetre
                    global TANK_M
                    global jeux_menu
                    fenêtre = fenetre
                    #initialisation fenêtre
                    Stats_base=lecture("Games/Maxime Picture/Tanks/Valeurs")
                    fullscreen=False
                    nb_manche=5
                    selection_menu=0
                    menu_en_cours=True
                    #pygame.init()
                    font_tanks_m = pygame.font.Font("Games/Maxime Picture/Tanks/police.ttf", 50)
                    couleur_menu=(0,150,250)
                    fond=pygame.image.load("Games/Maxime Picture/Tanks/Fond_menu.png").convert_alpha()
                    pygame.mouse.set_visible(True)
                    #boucle menu
                    while menu_en_cours:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
                        fenêtre.blit(fond,(5,5))
                        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(380,240+selection_menu*100,485,5))
                        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(380,328+selection_menu*100,485,5))
                        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(380,240+selection_menu*100,5,93))
                        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(865,240+selection_menu*100,5,93))
                        fenêtre.blit(font_tanks_m.render("Jouer en Local",1,(0,0,0)),(410,250))
                        fenêtre.blit(font_tanks_m.render("Jouer en Réseau",1,(0,0,0)),(390,350))
                        fenêtre.blit(font_tanks_m.render("Paramètres",1,(0,0,0)),(450,450))
                        fenêtre.blit(font_tanks_m.render("Quitter",1,(0,0,0)),(500,550))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                ecriture("Games/Maxime Picture/Tanks/Valeurs",Stats_base)
                                STOP(None)
                            if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                    jeux_menu = True
                                    TANK_M = False
                                    menu_en_cours=False
                                    ecriture("Games/Maxime Picture/Tanks/Valeurs",Stats_base)
                                    return
                                if event.key==K_w or event.key==K_z:
                                    if selection_menu!=0:
                                        selection_menu-=1
                                elif event.key==K_s:
                                    if selection_menu!=3:
                                        selection_menu+=1
                                if event.key==K_SPACE:
                                    if selection_menu==0:
                                        jeu(fullscreen,fenêtre)
                                    elif selection_menu==1:
                                        print("jouer2")
                                    elif selection_menu==2:
                                        options(fullscreen,fenêtre)
                                    elif selection_menu==3:
                                        jeux_menu = True
                                        TANK_M = False
                                        menu_en_cours=False
                                        ecriture("Games/Maxime Picture/Tanks/Valeurs",Stats_base)
                                        return
                                """
                                if event.key==K_F11:
                                    if not fullscreen:
                                        fenêtre=pygame.display.set_mode((1280,720),FULLSCREEN)
                                        fullscreen=True
                                    else:
                                        fenêtre=pygame.display.set_mode((1280,720))
                                        fullscreen=False
                                """
                ##########################################################################################################
                #Paramètres
                def options(full,fenêtre):
                    global TANK_M
                    global jeux_menu
                    stats=lecture("Games/Maxime Picture/Tanks/Valeurs")
                    option_en_cours=True
                    fond=pygame.image.load("Games/Maxime Picture/Tanks/Fond_menu.png").convert_alpha()
                    font_tanks_m = pygame.font.Font("Games/Maxime Picture/Tanks/police.ttf", 50)
                    pygame.mouse.set_visible(True)
                    while option_en_cours:

                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
                        fenêtre.blit(fond,(5,5))
                        fenêtre.blit(font_tanks_m.render("Manches :  "+str(stats[0]),1,(0,0,0)),(10,10))
                        fenêtre.blit(font_tanks_m.render("Vit déplacements :  "+str(stats[1]),1,(0,0,0)),(10,70))
                        fenêtre.blit(font_tanks_m.render("Vit rotation :  "+str(stats[2]),1,(0,0,0)),(10,130))
                        fenêtre.blit(font_tanks_m.render("Vie :  "+str(stats[3]),1,(0,0,0)),(10,190))
                        fenêtre.blit(font_tanks_m.render("Munitions :  "+str(stats[4]),1,(0,0,0)),(10,250))
                        fenêtre.blit(font_tanks_m.render("Dégats :  "+str(stats[5]),1,(0,0,0)),(10,320))
                        fenêtre.blit(font_tanks_m.render("Vit balles :  "+str(stats[6]),1,(0,0,0)),(10,390))
                        fenêtre.blit(font_tanks_m.render("Vit rechargement :  "+str(stats[7]),1,(0,0,0)),(10,460))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type==QUIT:
                                STOP(None)
                            if event.type==KEYDOWN:
                                if event.key==K_ESCAPE:
                                    option_en_cours=False
                    pygame.mouse.set_visible(True)
                    ecriture("Games/Maxime Picture/Tanks/Valeurs",stats)

                #########################################################################################################
                #Stockage valeurs paramètres
                def ecriture(nom_fichier,stats):
                    with open(nom_fichier,'w', encoding='utf8') as f :
                        for i in range(8):
                            f.write(str(stats[i])+"\n")
                def lecture(nom_fichier):
                    l=[]
                    with open(nom_fichier,'r', encoding='utf8') as f :
                        for i in f:
                            i=i.replace("\n","")
                            l.append(float(i))
                        return l
                #######################################################################################################

                #boucle jeu
                def jeu(full,fenêtre):
                    global TANK_M
                    global jeux_menu
                    score=[0,0]
                    partie=True
                    fond=pygame.image.load("Games/Maxime Picture/Tanks/Fond_3.png").convert_alpha()
                    cd1=time.time()
                    cd2=time.time()
                    properties=lecture("Games/Maxime Picture/Tanks/Valeurs")
                    font_tanks_m = pygame.font.Font("Games/Maxime Picture/Tanks/police.ttf", 20)
                    buisson=pygame.image.load("Games/Maxime Picture/Tanks/buisson.png").convert_alpha()
                    sapin=pygame.image.load("Games/Maxime Picture/Tanks/sapin.png").convert_alpha()
                    clock = pygame.time.Clock()
                    #variables
                    full=not(full)
                    end=0
                    """
                    if not full:
                        fenêtre=pygame.display.set_mode((1280,720),FULLSCREEN)
                        full=True
                    else:
                        fenêtre=pygame.display.set_mode((1280,720))
                        full=False
                    """
                    #création tank
                    tank1=Tank(100,100,-90,pygame.image.load("Games/Maxime Picture/Tanks/char_r.png").convert_alpha(),1,properties[1],properties[2],properties[3],properties[4],properties[5],properties[6],properties[7],fenêtre)
                    tank2=Tank(1180,620,90,pygame.image.load("Games/Maxime Picture/Tanks/char_b.png").convert_alpha(),2,properties[1],properties[2],properties[3],properties[4],properties[5],properties[6],properties[7],fenêtre)
                    while partie:
                        print(score)
                        en_cours=True
                        while en_cours:

                            if audio_reader_proc.is_finish():
                                audio_reader_proc.avancer()

                            #vie
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
                            fenêtre.blit(fond,(5,5))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,690,102,1))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,690,102,1))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,709,102,1))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,709,102,1))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,690,1,20))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,690,1,20))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(111,690,1,20))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1269,690,1,20))
                            v=round(tank1.vieleft/tank1.vie*100)
                            v2=round(tank2.vieleft/tank2.vie*100)
                            if v>0:
                                pygame.draw.rect(fenêtre,(255,0,0),pygame.Rect(11,691,v,18))
                            else:
                                end=1
                            if v2>0:
                                pygame.draw.rect(fenêtre,(0,0,255),pygame.Rect(1169,691,v2,18))
                            else:
                                end=2
                            l=-1
                            #balles
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(20,684,82,1))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1178,684,82,1))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(20,684,1,7))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1178,684,1,7))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(101,684,1,7))
                            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1259,684,1,7))
                            fenêtre.blit(pygame.transform.scale(pygame.image.load("Games/Maxime Picture/Tanks/bullet_r.png").convert_alpha(),(10,24)),(30,660))
                            fenêtre.blit(font_tanks_m.render("X",1,(0,0,0)),(42,655))
                            fenêtre.blit(font_tanks_m.render(str(int(tank1.ammo)),1,(0,0,0)),(60,655))
                            fenêtre.blit(pygame.transform.scale(pygame.image.load("Games/Maxime Picture/Tanks/bullet_b.png").convert_alpha(),(10,24)),(1185,660))
                            fenêtre.blit(font_tanks_m.render("X",1,(0,0,0)),(1197,655))
                            fenêtre.blit(font_tanks_m.render(str(int(tank2.ammo)),1,(0,0,0)),(1215,655))
                            #recharge
                            if tank1.ammo<tank1.max_ammo:
                                if cd1+tank1.vit_rech<time.time():
                                    cd1=time.time()
                                    tank1.ammo+=1
                            if tank2.ammo<tank2.max_ammo:
                                if cd2+tank2.vit_rech<time.time():
                                    cd2=time.time()
                                    tank2.ammo+=1
                            #dep_balles
                            rem_par=[]
                            for i in bullets:
                                l+=1
                                i.avancer(l,tank1,tank2)
                                fenêtre.blit(i.spr,(i.x,i.y))
                            for i in range(len(particules)):
                                if particules[i].lifetime==0:
                                    rem_par.append(i)
                                else:
                                    particules[i].move()
                                    fenêtre.blit(particules[i].rec,(particules[i].x,particules[i].y))
                            for i in range(len(rem_par)):
                                particules.pop(rem_par[-1])
                                rem_par.pop(-1)
                            fenêtre.blit(tank1.spr,tank1.rec)
                            fenêtre.blit(tank2.spr,tank2.rec)
                            fenêtre.blit(buisson,(900,100))
                            fenêtre.blit(sapin,(100,500))
                            fenêtre.blit(sapin,(170,400))
                            fenêtre.blit(sapin,(280,500))
                            pygame.display.flip()
                            #actions tanks
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_a] or keys[pygame.K_q]:
                                tank1.tourner(tank1.vit_rot)
                            elif keys[pygame.K_d]:
                                tank1.tourner(-tank1.vit_rot)
                            if keys[pygame.K_w] or keys[pygame.K_z]:
                                tank1.avancer(tank1.vit)
                            elif keys[pygame.K_s]:
                                tank1.avancer(-tank1.vit)
                            if keys[pygame.K_LEFT]:
                                tank2.tourner(tank2.vit_rot)
                            elif keys[pygame.K_RIGHT]:
                                tank2.tourner(-tank2.vit_rot)
                            if keys[pygame.K_UP]:
                                tank2.avancer(tank2.vit)
                            if keys[pygame.K_DOWN]:
                                tank2.avancer(-tank2.vit)
                            #contrôles
                            for event in pygame.event.get():
                                if event.type==QUIT:
                                    ecriture("Games/Maxime Picture/Tanks/Valeurs",lecture("Games/Maxime Picture/Tanks/Valeurs"))
                                    STOP(None)
                                if event.type==KEYDOWN:
                                    if event.key==K_ESCAPE:
                                        ecriture("Games/Maxime Picture/Tanks/Valeurs",lecture("Games/Maxime Picture/Tanks/Valeurs"))
                                        en_cours=False
                                        partie=False
                                    """
                                    if event.key==K_F11:
                                        if not full:
                                            fenêtre=pygame.display.set_mode((1280,720),FULLSCREEN)
                                            full=True
                                        else:
                                            fenêtre=pygame.display.set_mode((1280,720))
                                            full=False
                                    """
                                    if event.key==K_SPACE:
                                        tank1.tirer()
                                    if event.key==K_KP0:
                                        tank2.tirer()
                            if end==1:
                                #end1
                                while particules!=[]:
                                    #décors
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
                                    fenêtre.blit(fond,(5,5))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,690,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,690,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,709,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,709,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,690,1,20))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,690,1,20))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(111,690,1,20))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1269,690,1,20))
                                    v=round(tank1.vieleft/tank1.vie*100)
                                    v2=round(tank2.vieleft/tank2.vie*100)
                                    if v>0:
                                        pygame.draw.rect(fenêtre,(255,0,0),pygame.Rect(11,691,v,18))
                                    else:
                                        end=1
                                    if v2>0:
                                        pygame.draw.rect(fenêtre,(0,0,255),pygame.Rect(1169,691,v2,18))
                                    else:
                                        end=2
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(20,684,82,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1178,684,82,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(20,684,1,7))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1178,684,1,7))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(101,684,1,7))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1259,684,1,7))
                                    fenêtre.blit(pygame.transform.scale(pygame.image.load("Games/Maxime Picture/Tanks/bullet_r.png").convert_alpha(),(10,24)),(30,660))
                                    fenêtre.blit(font_tanks_m.render("X",1,(0,0,0)),(42,655))
                                    fenêtre.blit(font_tanks_m.render(str(int(tank1.ammo)),1,(0,0,0)),(60,655))
                                    fenêtre.blit(pygame.transform.scale(pygame.image.load("Games/Maxime Picture/Tanks/bullet_b.png").convert_alpha(),(10,24)),(1185,660))
                                    fenêtre.blit(font_tanks_m.render("X",1,(0,0,0)),(1197,655))
                                    fenêtre.blit(font_tanks_m.render(str(int(tank2.ammo)),1,(0,0,0)),(1215,655))
                                    fenêtre.blit(tank1.spr,tank1.rec)
                                    fenêtre.blit(tank2.spr,tank2.rec)
                                    fenêtre.blit(buisson,(900,100))
                                    fenêtre.blit(sapin,(100,500))
                                    fenêtre.blit(sapin,(170,400))
                                    fenêtre.blit(sapin,(280,500))
                                    l=-1
                                    rem_par=[]
                                    for i in bullets:
                                        l+=1
                                        i.avancer(l,tank1,tank2)
                                        fenêtre.blit(i.spr,(i.x,i.y))
                                    for i in range(len(particules)):
                                        if particules[i].lifetime==0:
                                            rem_par.append(i)
                                        else:
                                            particules[i].move()
                                            fenêtre.blit(particules[i].rec,(particules[i].x,particules[i].y))
                                    for i in range(len(rem_par)):
                                        particules.pop(rem_par[-1])
                                        rem_par.pop(-1)
                                    pygame.display.flip()
                                score[1]+=1
                                rem_par=[]
                                for _ in range(100):
                                    particules.append(particles("Games/Maxime Picture/Tanks/par_3.png",tank1.x,tank1.y,fenêtre))
                                for _ in range(100):
                                    particules.append(particles("Games/Maxime Picture/Tanks/par_4.png",tank1.x,tank1.y,fenêtre))
                                for _ in range(100):
                                    particules.append(particles("Games/Maxime Picture/Tanks/par_5.png",tank1.x,tank1.y,fenêtre))
                                for _ in range(200):
                                    for i in range(len(particules)):
                                        if particules[i].lifetime==0:
                                            rem_par.append(i)
                                        else:
                                            particules[i].move()
                                            fenêtre.blit(particules[i].rec,(particules[i].x,particules[i].y))
                                    for i in range(len(rem_par)):
                                        particules.pop(rem_par[-1])
                                        rem_par.pop(-1)
                                    time.sleep(0.01)
                                    pygame.display.flip()
                                upgrade(tank1,fenêtre)
                                tank1.x=100
                                tank1.y=100
                                tank2.x=1180
                                tank2.y=620
                                tank1.vieleft=tank1.vie
                                tank2.vieleft=tank2.vie
                                tank1.rec=tank1.spr.get_rect(center=(tank1.x, tank1.y))
                                tank2.rec=tank2.spr.get_rect(center=(tank2.x, tank2.y))
                                end=0
                                en_cours=False
                            elif end==2:
                                #end2
                                while particules!=[]:
                                    #décors
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
                                    fenêtre.blit(fond,(5,5))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,690,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,690,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,709,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,709,102,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(10,690,1,20))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1168,690,1,20))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(111,690,1,20))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1269,690,1,20))
                                    v=round(tank1.vieleft/tank1.vie*100)
                                    v2=round(tank2.vieleft/tank2.vie*100)
                                    if v>0:
                                        pygame.draw.rect(fenêtre,(255,0,0),pygame.Rect(11,691,v,18))
                                    else:
                                        end=1
                                    if v2>0:
                                        pygame.draw.rect(fenêtre,(0,0,255),pygame.Rect(1169,691,v2,18))
                                    else:
                                        end=2
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(20,684,82,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1178,684,82,1))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(20,684,1,7))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1178,684,1,7))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(101,684,1,7))
                                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(1259,684,1,7))
                                    fenêtre.blit(pygame.transform.scale(pygame.image.load("Games/Maxime Picture/Tanks/bullet_r.png").convert_alpha(),(10,24)),(30,660))
                                    fenêtre.blit(font_tanks_m.render("X",1,(0,0,0)),(42,655))
                                    fenêtre.blit(font_tanks_m.render(str(int(tank1.ammo)),1,(0,0,0)),(60,655))
                                    fenêtre.blit(pygame.transform.scale(pygame.image.load("Games/Maxime Picture/Tanks/bullet_b.png").convert_alpha(),(10,24)),(1185,660))
                                    fenêtre.blit(font_tanks_m.render("X",1,(0,0,0)),(1197,655))
                                    fenêtre.blit(font_tanks_m.render(str(int(tank2.ammo)),1,(0,0,0)),(1215,655))
                                    fenêtre.blit(tank1.spr,tank1.rec)
                                    fenêtre.blit(tank2.spr,tank2.rec)
                                    fenêtre.blit(buisson,(900,100))
                                    fenêtre.blit(sapin,(100,500))
                                    fenêtre.blit(sapin,(170,400))
                                    fenêtre.blit(sapin,(280,500))
                                    l=-1
                                    rem_par=[]
                                    for i in bullets:
                                        l+=1
                                        i.avancer(l,tank1,tank2)
                                        fenêtre.blit(i.spr,(i.x,i.y))
                                    for i in range(len(particules)):
                                        if particules[i].lifetime==0:
                                            rem_par.append(i)
                                        else:
                                            particules[i].move()
                                            fenêtre.blit(particules[i].rec,(particules[i].x,particules[i].y))
                                    for i in range(len(rem_par)):
                                        particules.pop(rem_par[-1])
                                        rem_par.pop(-1)
                                    pygame.display.flip()
                                score[0]+=1
                                rem_par=[]
                                for _ in range(100):
                                    particules.append(particles("Games/Maxime Picture/Tanks/par_3.png",tank2.x,tank2.y,fenêtre))
                                for _ in range(100):
                                    particules.append(particles("Games/Maxime Picture/Tanks/par_4.png",tank2.x,tank2.y,fenêtre))
                                for _ in range(100):
                                    particules.append(particles("Games/Maxime Picture/Tanks/par_5.png",tank2.x,tank2.y,fenêtre))
                                for _ in range(200):
                                    for i in range(len(particules)):
                                        if particules[i].lifetime==0:
                                            rem_par.append(i)
                                        else:
                                            particules[i].move()
                                            fenêtre.blit(particules[i].rec,(particules[i].x,particules[i].y))
                                    for i in range(len(rem_par)):
                                        particules.pop(rem_par[-1])
                                        rem_par.pop(-1)
                                    time.sleep(0.01)
                                    pygame.display.flip()
                                upgrade(tank2,fenêtre)
                                tank1.x=100
                                tank1.y=100
                                tank2.x=1180
                                tank2.y=620
                                tank1.vieleft=tank1.vie
                                tank2.vieleft=tank2.vie
                                tank1.rec=tank1.spr.get_rect(center=(tank1.x, tank1.y))
                                tank2.rec=tank2.spr.get_rect(center=(tank2.x, tank2.y))
                                end=0
                                en_cours=False
                            if score[0]==properties[0] or score[1]==properties[0]:
                                ecriture("Games/Maxime Picture/Tanks/Valeurs",lecture("Games/Maxime Picture/Tanks/Valeurs"))
                                partie=False
                                en_cours=False
                        clock.tick(60)
                ########################################################################################################
                menu()

            while Tetros:
                Tetros_selector_pos = (50,235)
                while Tetros_menu:
                    étape_programme = "Tetros menu"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    fenetre.blit(Tetros_fond,(0,0))
                    fenetre.blit(Tetros_alpha,(0,0))

                    fenetre.blit(Tetros_selector,Tetros_selector_pos)

                    texte = font_games_menu.render("Jouer", 5, (255,255,255))
                    fenetre.blit(texte, (100, 250))
                    texte = font_games_menu.render("Options", 5, (255,255,255))
                    fenetre.blit(texte, (120, 300))
                    texte = font_games_menu.render("Aide", 5, (255,255,255))
                    fenetre.blit(texte, (140, 350))
                    texte = font_games_menu.render("Quitter", 5, (255,255,255))
                    fenetre.blit(texte, (160, 400))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    a,b= pygame.mouse.get_pos ()

                    if (a > 50 and a < 315) and (b > 235 and b < 285):
                        Tetros_selector_pos = (50,235)
                    if (a > 70 and a < 335) and (b > 285 and b < 335):
                        Tetros_selector_pos = (70,285)
                    if (a > 90 and a < 355) and (b > 335 and b < 385):
                        Tetros_selector_pos = (90,335)
                    if (a > 110 and a < 375) and (b > 385 and b < 435):
                        Tetros_selector_pos = (110,385)

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            a,b= pygame.mouse.get_pos ()
                            if mouse_stat[0]:
                                if (a > 110 and a < 375) and (b > 385 and b < 435):
                                    Tetros_menu = False
                                    Tetros = False
                                    jeux_menu = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE :
                                Tetros_menu = False
                                Tetros = False
                                jeux_menu = True

                            if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and Tetros_selector_pos[1] == 385:
                                Tetros_menu = False
                                Tetros = False
                                jeux_menu = True

                            if event.key == pygame.K_UP and Tetros_selector_pos[1] > 235:
                                Tetros_selector_pos = (Tetros_selector_pos[0]-20, Tetros_selector_pos[1]-50)
                            if event.key == pygame.K_DOWN and Tetros_selector_pos[1] < 345:
                                Tetros_selector_pos = (Tetros_selector_pos[0]+20, Tetros_selector_pos[1]+50)

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

            while Minesweeper:
                
                Minesweeper_selector_pos = (50,235)
                while Minesweeper_menu:
                    étape_programme = "Minesweeper menu"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    fenetre.blit(Minesweeper_fond,(0,0))
                    fenetre.blit(Minesweeper_alpha,(0,0))

                    fenetre.blit(Minesweeper_selector,Minesweeper_selector_pos)

                    texte = font_games_menu.render(langue.game_minesweeper_play_menu, 5, (255,255,255))
                    fenetre.blit(texte, (100, 250))
                    texte = font_games_menu.render(langue.game_minesweeper_settings_menu, 5, (255,255,255))
                    fenetre.blit(texte, (120, 300))
                    texte = font_games_menu.render(langue.game_minesweeper_help_menu, 5, (255,255,255))
                    fenetre.blit(texte, (140, 350))
                    texte = font_games_menu.render(langue.game_minesweeper_quit_menu, 5, (255,255,255))
                    fenetre.blit(texte, (160, 400))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    a,b= pygame.mouse.get_pos ()

                    if (a > 50 and a < 315) and (b > 235 and b < 285):
                        Minesweeper_selector_pos = (50,235)
                    if (a > 70 and a < 335) and (b > 285 and b < 335):
                        Minesweeper_selector_pos = (70,285)
                    if (a > 90 and a < 355) and (b > 335 and b < 385):
                        Minesweeper_selector_pos = (90,335)
                    if (a > 110 and a < 375) and (b > 385 and b < 435):
                        Minesweeper_selector_pos = (110,385)

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            a,b= pygame.mouse.get_pos ()
                            if mouse_stat[0]:
                                if (a > 50 and a < 315) and (b > 235 and b < 285):
                                    Minesweeper_selector_pos = (50,235)
                                    Minesweeper_menu = False
                                    Minesweeper_game = True
                                    Minesweeper_init = True
                                    
                                if (a > 70 and a < 335) and (b > 285 and b < 335):
                                    Minesweeper_menu = False
                                    Minesweeper_settings = True
                                    
                                if (a > 90 and a < 355) and (b > 335 and b < 385):
                                    None
                                    
                                if (a > 110 and a < 375) and (b > 385 and b < 435):
                                    Minesweeper_menu = False
                                    Minesweeper = False
                                    jeux_menu = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE :
                                Minesweeper_menu = False
                                Minesweeper = False
                                jeux_menu = True

                            if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                                if Minesweeper_selector_pos[1] == 235:
                                    Minesweeper_menu = False
                                    Minesweeper_game = True
                                    Minesweeper_init = True  
                                    
                                if Minesweeper_selector_pos[1] == 285:  
                                    Minesweeper_menu = False
                                    Minesweeper_settings = True
                                    
                                elif Minesweeper_selector_pos[1] == 385:
                                    Minesweeper_menu = False
                                    Minesweeper = False
                                    jeux_menu = True

                            if event.key == pygame.K_UP and Minesweeper_selector_pos[1] > 235:
                                Minesweeper_selector_pos = (Minesweeper_selector_pos[0]-20, Minesweeper_selector_pos[1]-50)
                            if event.key == pygame.K_DOWN and Minesweeper_selector_pos[1] < 345:
                                Minesweeper_selector_pos = (Minesweeper_selector_pos[0]+20, Minesweeper_selector_pos[1]+50)

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")
                                
                while Minesweeper_settings:
                    étape_programme = "Minesweeper settings"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    fenetre.blit(Minesweeper_fond,(0,0))
                    fenetre.blit(Minesweeper_alpha,(0,0))

                    fenetre.blit(Minesweeper_selector,(110,385))

                    texte = font_games_menu.render(langue.game_minesweeper_settings_menu, 5, (255,255,255))
                    fenetre.blit(texte, (100, 250))
                    texte = font_games_menu.render(langue.game_minesweeper_return, 5, (255,255,255))
                    fenetre.blit(texte, (160, 400))
                    
                    texte = font_games_menu.render(langue.game_minesweeper_settings_prop_mine, 5, (255,255,255))
                    fenetre.blit(texte, (500, 250))
                    
                    fenetre.blit(DOWN_button, (950,250))
                    texte = font_widget.render(f"1/{Minesweeper_mine_prop}", 1, (color_txt))
                    fenetre.blit(texte, (1000, 255))
                    fenetre.blit(UP_button, (1050,250))
                    
                    texte = font_games_menu.render(langue.game_minesweeper_settings_lenght, 5, (255,255,255))
                    fenetre.blit(texte, (500, 300))
                    
                    fenetre.blit(DOWN_button, (950,300))
                    texte = font_widget.render(str(Minesweeper_size[0]), 1, (color_txt))
                    fenetre.blit(texte, (1000, 305))
                    fenetre.blit(UP_button, (1050,300))
                    
                    texte = font_games_menu.render(langue.game_minesweeper_settings_height, 5, (255,255,255))
                    fenetre.blit(texte, (500, 350))
                    
                    fenetre.blit(DOWN_button, (950,350))
                    texte = font_widget.render(str(Minesweeper_size[1]), 1, (color_txt))
                    fenetre.blit(texte, (1000, 355))
                    fenetre.blit(UP_button, (1050,350))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    a,b= pygame.mouse.get_pos ()

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            a,b= pygame.mouse.get_pos ()
                            if mouse_stat[0]:
                                if (a > 110 and a < 375) and (b > 385 and b < 435):
                                    Minesweeper_settings = False
                                    Minesweeper_menu = True
                                    
                                if pos_UP_Minesweeper_mine.collidepoint(event.pos) and Minesweeper_mine_prop > 2:
                                    data_base.update("Minesweeper_mine_prop", str(Minesweeper_mine_prop-1))
                                if pos_DOWN_Minesweeper_mine.collidepoint(event.pos) and Minesweeper_mine_prop < 7:
                                    data_base.update("Minesweeper_mine_prop", str(Minesweeper_mine_prop+1))
                                    
                                if pos_DOWN_Minesweeper_width.collidepoint(event.pos) and Minesweeper_size[0] > 8:
                                    Minesweeper_size = (Minesweeper_size[0]-1,Minesweeper_size[1])
                                    data_base.update("Minesweeper_size", str(Minesweeper_size))
                                if pos_UP_Minesweeper_width.collidepoint(event.pos) and Minesweeper_size[0] < 15:
                                    Minesweeper_size = (Minesweeper_size[0]+1,Minesweeper_size[1])
                                    data_base.update("Minesweeper_size", str(Minesweeper_size))
                                    
                                if pos_DOWN_Minesweeper_height.collidepoint(event.pos) and Minesweeper_size[1] > 7:
                                    Minesweeper_size = (Minesweeper_size[0],Minesweeper_size[1]-1)
                                    data_base.update("Minesweeper_size", str(Minesweeper_size))
                                if pos_UP_Minesweeper_height.collidepoint(event.pos) and Minesweeper_size[1] < 10:
                                    Minesweeper_size = (Minesweeper_size[0],Minesweeper_size[1]+1)
                                    data_base.update("Minesweeper_size", str(Minesweeper_size))
                                    
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE :
                                Minesweeper_settings = False
                                Minesweeper_menu = True

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")
                
                while Minesweeper_game:
                
                    étape_programme = "Minesweeper"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                    fenetre.blit(Menu,(1150,20))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    if Minesweeper_init:
                        Minesweeper_game = Minesweeper_class(0,Minesweeper_size, Minesweeper_mine_prop, "Games/Mini Picture Original/Wall-E Minesweeper/img_base.png",
                        "Games/Mini Picture Original/Wall-E Minesweeper/img_mine.png",
                        "Games/Mini Picture Original/Wall-E Minesweeper/img_reveal.png",
                        "Games/Mini Picture Original/Wall-E Minesweeper/img_flag.png", (72,72), (0,0))
                        Minesweeper_game.create_grille()
                        Minesweeper_game.create_pos()

                        Minesweeper_init = False

                    Minesweeper_game.draw_grille()

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if Minesweeper_game.stat == "game":
                                    Minesweeper_game.mine_is_click(event.pos)
                                if pos_Menu.collidepoint(event.pos):
                                    Minesweeper_menu = True
                                    Minesweeper_game = False
                            if mouse_stat[2]:
                                if Minesweeper_game.stat == "game":
                                    Minesweeper_game.mine_is_click(event.pos, flag=True)

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                                if Minesweeper_game.stat == "lose":
                                    Minesweeper_init = True
                            if event.key == pygame.K_ESCAPE :
                                Minesweeper_menu = True
                                Minesweeper_game = False

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")
                            
            while Vilallongue_chroni_game:
                étape_programme = "Vilallongue_chroni"
                """
                Initialisation des constantes
                """
                LARGEUR_FENETRE = 1200
                HAUTEUR_FENETRE = 563
                BLACK = (0, 0, 0)
                WHITE = (255, 255, 255)
                RED = (255, 0, 0)
                
                BLACK_BNL = BLACK

                """
                Définition des fonctions
                """
                def construction_listes(liste_de_paquets):
                    liste = []
                    for paquet in liste_de_paquets:
                        nom_paquet = 'Games/Vilallongue Picture/appli_dates/paquets/chroni/' + paquet
                        with open(nom_paquet, 'r', encoding='utf8') as fichier:
                            while True:
                                txt = fichier.readline()
                                if txt == '':
                                    break
                                liste.append(txt[:-1].split(";")+[paquet[:-4]]) # on ajoute le nom du paquet sans l'extension .csv
                    return liste

                def mise_en_forme_date(liste_de_listes):
                    for e in liste_de_listes:
                        e[0] = int(e[0].replace(" ","").replace("Vers","").split(',')[0])
                    return liste_de_listes

                def construit_paquet_de_cartes(liste_de_listes):
                    paquet = PaquetDeCartes()
                    for e in liste_de_listes:
                        carte = Carte(e[0], e[1], e[2])
                        paquet.ajoute(carte)
                    return paquet

                def construit_paquet_joueur(paquet, nb_cartes):
                    new_paquet = PaquetDeCartes()
                    for i in range(nb_cartes):
                        new_paquet.ajoute(paquet.pioche_carte())
                    return new_paquet

                def afficher_texte(texte_str, color, abscisse, ordonnee, largeur_texte) :
                    liste_splitee = texte_str.split()
                    nb_mots = len(liste_splitee)
                    i = 0 # indice du mot
                    chaine = ""
                    while i < nb_mots :
                        if audio_reader_proc.is_finish():
                            audio_reader_proc.avancer()

                        chaine_sans_dernier_mot = chaine
                        longueur = font_Vilallongue.size(chaine)[0]
                        while longueur < largeur_texte and i < nb_mots :
                            chaine_sans_dernier_mot = chaine
                            chaine = chaine + " " + liste_splitee[i]
                            longueur = font_Vilallongue.size(chaine)[0]
                            i += 1
                        if longueur < largeur_texte :
                            texte = font_Vilallongue.render(chaine.lstrip(), 1, color)
                            fenetre.blit(texte, (abscisse+40, ordonnee+157))
                            chaine = ""
                        else :
                            texte = font_Vilallongue.render(chaine_sans_dernier_mot.lstrip(), 1, color)
                            chaine = liste_splitee[i-1]
                            fenetre.blit(texte, (abscisse+40, ordonnee+157))
                        ordonnee += font_Vilallongue.get_height()
                        if i == nb_mots :
                            texte = font_Vilallongue.render(chaine, 1, color)
                            fenetre.blit(texte, (abscisse+40, ordonnee+157))

                def affiche_jeu_central(jeu, y_énoncé, i):
                    """ Affichage concernant le jeu central
                    """
                    global zc1, zc2, bouton_prev_jeu_central, pos_bouton_prev_jeu_central, bouton_next_jeu_central, pos_bouton_next_jeu_central, zc_c, zc_g, zc_d
                    largeur_zone_cliquable = 70
                    hauteur_zone_cliquable = 40
                    y_date = y_énoncé + 150
                    if len(jeu.contenu) == 1:
                        carte = jeu.contenu[i]
                        date, énoncé = str(carte.date), carte.énoncé
                        x = LARGEUR_FENETRE / 2 - Carte.largeur / 2
                        # affichage carte

                        pygame.draw.rect(fenetre, Carte.couleur, (x+40, y_énoncé+157, Carte.largeur, Carte.hauteur))
                        pygame.draw.rect(fenetre, Carte.couleur_bord, (x+40, y_énoncé+157, Carte.largeur, Carte.hauteur), 5)
                        afficher_texte(énoncé, Carte.couleur_texte, x+10, y_énoncé, Carte.largeur)
                        afficher_texte(date, Carte.couleur_texte, x+Carte.largeur-75, y_date, Carte.largeur)
                        # affichage de zone cliquables
                        zc1 = pygame.draw.rect(fenetre, RED, ((LARGEUR_FENETRE/2-Carte.largeur/2)/2 - largeur_zone_cliquable/2 +40, y_énoncé + Carte.hauteur - hauteur_zone_cliquable+157, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
                        zc2 = pygame.draw.rect(fenetre, RED, ((LARGEUR_FENETRE/2+Carte.largeur/2+LARGEUR_FENETRE)/2 - largeur_zone_cliquable/2 +40, y_énoncé + Carte.hauteur - hauteur_zone_cliquable+157, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
                    else: # deux cartes ou plus dans le jeu
                        carte = jeu.contenu[i]
                        carte2 = jeu.contenu[i+1]
                        date, énoncé = str(carte.date), carte.énoncé
                        date2, énoncé2 = str(carte2.date), carte2.énoncé
                        x1 = (LARGEUR_FENETRE - 2 * Carte.largeur) / 3
                        x2 = 2 * (LARGEUR_FENETRE - 2 * Carte.largeur) / 3 + Carte.largeur
                        
                        # affichage carte 1
                        pygame.draw.rect(fenetre, Carte.couleur, (x1+40, y_énoncé+157, Carte.largeur, Carte.hauteur))
                        pygame.draw.rect(fenetre, Carte.couleur_bord, (x1+40, y_énoncé+157, Carte.largeur, Carte.hauteur), 5)
                        afficher_texte(énoncé, Carte.couleur_texte, x1+10, y_énoncé, Carte.largeur)
                        afficher_texte(date, Carte.couleur_texte, x1+Carte.largeur-75, y_date, Carte.largeur)
                        # affichage carte 2
                        pygame.draw.rect(fenetre, Carte.couleur, (x2+40, y_énoncé+157, Carte.largeur, Carte.hauteur))
                        pygame.draw.rect(fenetre, Carte.couleur_bord, (x2+40, y_énoncé+157, Carte.largeur, Carte.hauteur), 5)
                        afficher_texte(énoncé2, Carte.couleur_texte, x2+10, y_énoncé, Carte.largeur)
                        afficher_texte(date2, Carte.couleur_texte, x2+Carte.largeur-75, y_date, Carte.largeur)
                        # affichage zone cliquable centrale
                        zc_c = pygame.draw.rect(fenetre, RED, (LARGEUR_FENETRE/2- largeur_zone_cliquable/2 +40, y_énoncé + Carte.hauteur - hauteur_zone_cliquable+157, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
                        if i == 0:
                            # affichage à gauche d'une zone cliquable
                            zc_g = pygame.draw.rect(fenetre, RED, (x1/2 - largeur_zone_cliquable/2 +40, y_énoncé + Carte.hauteur - hauteur_zone_cliquable+157, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
                        else:
                            # affichage à gauche un bouton
                            largeur_bouton = 50
                            hauteur_bouton =  50
                            bouton_prev_jeu_central = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/prev.png").convert_alpha()
                            pos_bouton_prev_jeu_central = bouton_prev_jeu_central.get_rect(topleft=(x1/2 - largeur_zone_cliquable/2 +40, y_énoncé + Carte.hauteur/2 - hauteur_bouton/2 +157))
                            fenetre.blit(bouton_prev_jeu_central, pos_bouton_prev_jeu_central)
                        if i == jeu.get_nb_cartes() - 2 :
                            # affichage à droite d'une zone cliquable
                            zc_d = pygame.draw.rect(fenetre, RED, ((x2 + Carte.largeur + LARGEUR_FENETRE)/2 - largeur_zone_cliquable/2 +40, y_énoncé + Carte.hauteur - hauteur_zone_cliquable+157, largeur_zone_cliquable, hauteur_zone_cliquable), 5)
                        else:
                            # affichage à droite un bouton
                            largeur_bouton = 50
                            hauteur_bouton =  50
                            bouton_next_jeu_central = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/next.png").convert_alpha()
                            pos_bouton_next_jeu_central = bouton_next_jeu_central.get_rect(topleft=((x2 + Carte.largeur + LARGEUR_FENETRE)/2 - largeur_bouton/2 +40, y_énoncé + Carte.hauteur/2 - hauteur_bouton/2 +157))
                            fenetre.blit(bouton_next_jeu_central, pos_bouton_next_jeu_central)

                def affiche_jeu_joueur(jeu, y_énoncé, i):
                    """ Affichage concernant un joueur
                        Affiche la ième carte
                    """
                    global bouton_prev_joueur, pos_bouton_prev_joueur, bouton_next_joueur, pos_bouton_next_joueur
                    y_date = y_énoncé + 150
                    if len(jeu.contenu) >= 1:
                        carte = jeu.contenu[i]
                        date, énoncé = str(carte.date), carte.énoncé
                        x = LARGEUR_FENETRE / 2 - Carte.largeur / 2
                        # affichage carte
                        
                        pygame.draw.rect(fenetre, Carte.couleur, (x+40, y_énoncé+157, Carte.largeur, Carte.hauteur))
                        pygame.draw.rect(fenetre, Carte.couleur_bord, (x+40, y_énoncé+157, Carte.largeur, Carte.hauteur), 5)
                        afficher_texte(énoncé, Carte.couleur_texte, x+10, y_énoncé, Carte.largeur)
                        #afficher_texte(date, Carte.couleur_texte, x+Carte.largeur-75, y_date, Carte.largeur)
                        # affichage des boutons
                        hauteur_bouton = 50
                        bouton_prev_joueur = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/prev.png").convert_alpha()
                        pos_bouton_prev_joueur = bouton_prev_joueur.get_rect(topleft=(LARGEUR_FENETRE / 4 +40, y_énoncé_joueur_courant + Carte.hauteur/2 - hauteur_bouton/2 +157))
                        bouton_next_joueur = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/next.png").convert_alpha()
                        pos_bouton_next_joueur = bouton_next_joueur.get_rect(topleft=(3 * LARGEUR_FENETRE / 4 +40, y_énoncé_joueur_courant + Carte.hauteur/2 - hauteur_bouton/2 +157))
                        if jeu.get_nb_cartes() > 1:
                            if i != 0:
                                fenetre.blit(bouton_prev_joueur, pos_bouton_prev_joueur)
                            if i != jeu.get_nb_cartes() - 1:
                                fenetre.blit(bouton_next_joueur, pos_bouton_next_joueur)

                """
                Définition des classes
                """
                class Carte():

                    largeur = 350
                    hauteur = 200
                    couleur = (255, 255, 255)
                    couleur_bord = (0, 0, 0)
                    couleur_texte = (0, 0, 0)

                    def __init__(self, date, énoncé, catégorie, sens="recto"):
                        self.date = date
                        self.énoncé = énoncé
                        self.catégorie = catégorie
                        self.sens = sens

                    def retourne(self):
                        if self.sens == "recto":
                            self.sens = "verso"
                        else:
                            self.sens = "recto"

                    def get_date(self):
                        return self.date

                    def get_énoncé(self):
                        return self.énoncé

                    def get_catégorie(self):
                        return self.catégorie

                    def get_sens(self):
                        return self.sens


                class PaquetDeCartes():

                    def __init__(self):
                        self.contenu = []

                    def ajoute(self, carte):
                        self.contenu.append(carte)

                    def ajoute_carte_indice_i(self, i, carte):
                        self.contenu.insert(i, carte)

                    def retire_carte_indice_i(self, i):
                        return self.contenu.pop(i)

                    def get_carte_indice_i(self, i):
                        return self.contenu[i]

                    def filtre_sur_catégorie(self, catégorie):
                        new_contenu = []
                        for carte in self.contenu:
                            if carte.catégorie == catégorie:
                                new_contenu.append(carte)
                        self.contenu = new_contenu

                    def filtre_sur_dates(self, a, b):
                        new_contenu = []
                        for carte in self.contenu:
                            if a <= carte.date <= b:
                                new_contenu.append(carte)
                        self.contenu = new_contenu

                    def pioche_carte(self):
                        nb_cartes = len(self.contenu)
                        x = random.randint(0, nb_cartes - 1)
                        carte = self.contenu[x]
                        del self.contenu[x]
                        return carte

                    def get_nb_cartes(self):
                        return len(self.contenu)


                class Joueur():

                    def __init__(self, nom, paquet):
                        self.nom = nom
                        self.paquet = paquet

                    def get_paquet(self):
                        return self.paquet

                #======================
                # Partie Construction de la liste de liste
                #======================
                ma_liste_de_paquets = ['histoire de france.csv', \
                                        'histoire du monde.csv', \
                                        'histoire de la litterature.csv', \
                                        'histoire des arts.csv', \
                                        'les femmes celebres.csv', \
                                        'les merveilles du monde.csv', \
                                        'les rois et reines de france.csv', \
                                        'les grandes inventions.csv', \
                                        'les monuments de france.csv']
                liste_de_listes = construction_listes(ma_liste_de_paquets)
                liste_de_listes = mise_en_forme_date(liste_de_listes)
                liste_de_listes.sort()

                """
                Initialisation de la fenêtre Pygame
                """
                # Initialisation de la bibliothèque Pygame
                #pygame.init()
                # Création de la fenêtre (note de MINI Picture : supprimé pour l'intégration à la BNL's Box)
                """
                fenetre = pygame.display.set_mode((LARGEUR_FENETRE,HAUTEUR_FENETRE))
                pygame.display.set_icon(pygame.image.load("Games/Vilallongue Picture/appli_dates/images/jblt_80_80.jpg"))
                """
                if Vilallongue_fond_choice < 4:
                    fond = pygame.image.load(f"Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond{Vilallongue_fond_choice}.jpg").convert()

                if Vilallongue_fond_choice == 0:
                    BLACK_BNL = (255,255,255)

                if Vilallongue_fond_choice == 4:
                    BLACK_BNL = (255,255,255)
                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))
                else:                    
                    fenetre.blit(wallpapers_use.wallpaper,(0,0))
                fenetre.blit(Menu,(1150,20))
                
                fenetre.blit(Vilallongue_min0, (40,40))
                fenetre.blit(Vilallongue_min1, (250,40))
                fenetre.blit(Vilallongue_min2, (460,40))
                fenetre.blit(Vilallongue_min3, (670,40))
                fenetre.blit(Vilallongue_min4, (880,40))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))
                    
                if Vilallongue_fond_choice != 4:
                    fenetre.blit(fond,(40,157))
                # Gestion du titre en haut de la fenêtre (note de MINI Picture : supprimé pour l'intégration à la BNL's Box)
                """
                pygame.display.set_caption("Appli")
                """
                #-------------------------------------
                # Pour afficher un texte dans pygame
                #-------------------------------------
                font_Vilallongue = pygame.font.Font("Games/Vilallongue Picture/appli_dates/BradBunR.ttf", 40)

                # Mélange aléatoire des cartes
                #random.seed(0.7) # pour tester en ayant toujours les mêmes jeux

                paquet = construit_paquet_de_cartes(liste_de_listes)
                #paquet.filtre_sur_catégorie("histoire de france")
                #paquet.filtre_sur_dates(1000, 2000)

                joueur1 = Joueur("J1", construit_paquet_joueur(paquet, 10))
                i_joueur1 = 0
                joueur2 = Joueur("J2", construit_paquet_joueur(paquet, 5))
                i_joueur2 = 0

                jeu_central = PaquetDeCartes()
                jeu_central.ajoute(paquet.pioche_carte())

                i_paquet_central = 0

                jeu_joueur_courant = joueur1.paquet
                i_joueur_courant = i_joueur1

                y_énoncé = 50
                y_énoncé_joueur_courant = 350

                texte = font_Vilallongue.render("Jeu central", 1, BLACK_BNL)
                fenetre.blit(texte, (20+40, 0+157))

                zc_c, zc1, zc2 = None, None, None
                affiche_jeu_central(jeu_central, y_énoncé, i_paquet_central)

                texte = font_Vilallongue.render("Jeu joueur "+joueur1.nom, 1, BLACK_BNL)
                fenetre.blit(texte, (20+40, 300+157))
                affiche_jeu_joueur(jeu_joueur_courant, y_énoncé_joueur_courant, i_joueur_courant)

                continuer_Vilallongue = True
                while continuer_Vilallongue :

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    pygame.display.flip() # Rafraichissement

                    # Gestion des événements
                    for event in pygame.event.get():
                        # BNL's Box : pour compatibilité
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    jeux_menu = True
                                    Vilallongue_chroni_game = False
                                    continuer_Vilallongue = False
                                    
                                if pos_Vilallongue_min0.collidepoint(event.pos):
                                    fond = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond0.jpg").convert_alpha()
                                    data_base.update("Vilallongue_fond_choice", "0")
                                    BLACK_BNL = (255,255,255)
                                if pos_Vilallongue_min1.collidepoint(event.pos):
                                    fond = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond1.jpg").convert_alpha()
                                    data_base.update("Vilallongue_fond_choice", "1")
                                    BLACK_BNL = BLACK
                                if pos_Vilallongue_min2.collidepoint(event.pos):
                                    fond = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond2.jpg").convert_alpha()
                                    data_base.update("Vilallongue_fond_choice", "2")
                                    BLACK_BNL = BLACK
                                if pos_Vilallongue_min3.collidepoint(event.pos):
                                    fond = pygame.image.load("Games/Vilallongue Picture/appli_dates/images/Vilallongue_fond3.jpg").convert_alpha()
                                    data_base.update("Vilallongue_fond_choice", "3")
                                    BLACK_BNL = BLACK
                                if pos_Vilallongue_min4.collidepoint(event.pos):
                                    data_base.update("Vilallongue_fond_choice", "4")
                                    BLACK_BNL = (255,255,255)
                                    
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE :
                                jeux_menu = True
                                Vilallongue_chroni_game = False
                                continuer_Vilallongue = False

                        # Evènements liés à la zone centrale
                        # Partie zones cliquables
                        if event.type == pygame.MOUSEBUTTONUP:
                            if jeu_central.get_nb_cartes() == 1 and zc1.collidepoint(event.pos) or \
                                jeu_central.get_nb_cartes() > 1 and i_paquet_central == 0 and zc_g.collidepoint(event.pos):
                                print('clic à gauche')
                                if jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() <= jeu_central.get_carte_indice_i(i_paquet_central).get_date():
                                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                                    jeu_central.ajoute_carte_indice_i(0, carte_jouée)
                                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                                        i_joueur_courant -= 1

                            # ajout à droite avec une seule carte dans le jeu central
                            elif jeu_central.get_nb_cartes() == 1 and zc2.collidepoint(event.pos):
                                print('clic à droite')
                                if jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() >= jeu_central.get_carte_indice_i(i_paquet_central).get_date():
                                    print('cas ok')
                                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                                    jeu_central.ajoute_carte_indice_i(jeu_central.get_nb_cartes(), carte_jouée)
                                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                                        i_joueur_courant -= 1

                            # ajout à droite avec au moins deux cartes dans le jeu central
                            elif jeu_central.get_nb_cartes() > 1 and i_paquet_central == jeu_central.get_nb_cartes() - 2 and zc_d.collidepoint(event.pos):
                                print('clic à droite')
                                if jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() >= jeu_central.get_carte_indice_i(i_paquet_central + 1).get_date():
                                    print('cas ok')
                                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                                    jeu_central.ajoute_carte_indice_i(jeu_central.get_nb_cartes(), carte_jouée)
                                    i_paquet_central += 1
                                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                                        i_joueur_courant -= 1

                            elif jeu_central.get_nb_cartes() > 1 and zc_c.collidepoint(event.pos):
                                print('clic au milieu')
                                if jeu_central.get_carte_indice_i(i_paquet_central).get_date() <= jeu_joueur_courant.get_carte_indice_i(i_joueur_courant).get_date() <= jeu_central.get_carte_indice_i(i_paquet_central+1).get_date():
                                    carte_jouée = jeu_joueur_courant.retire_carte_indice_i(i_joueur_courant)
                                    jeu_central.ajoute_carte_indice_i(i_paquet_central + 1, carte_jouée)
                                    #i_paquet_central += 1
                                    if i_joueur_courant == jeu_joueur_courant.get_nb_cartes():
                                        i_joueur_courant -= 1
                            # Evènements liés à la zone centrale
                            # Partie zones de défilement : previous et next
                            elif jeu_central.get_nb_cartes() > 1 and i_paquet_central != 0 and pos_bouton_prev_jeu_central.collidepoint(event.pos) :
                                i_paquet_central -= 1
                                print(i_paquet_central)
                            elif jeu_central.get_nb_cartes() > 1 and i_paquet_central != jeu_central.get_nb_cartes() - 2 and pos_bouton_next_jeu_central.collidepoint(event.pos) :
                                i_paquet_central += 1
                                print(i_paquet_central)
                            # Evènements liés à la zone du joueur
                            elif pos_bouton_prev_joueur.collidepoint(event.pos) and i_joueur_courant > 0:
                                i_joueur_courant -= 1
                            elif pos_bouton_next_joueur.collidepoint(event.pos) and i_joueur_courant < jeu_joueur_courant.get_nb_cartes()-1:
                                i_joueur_courant += 1

                            if Vilallongue_fond_choice == 4:
                                if Blur_background:
                                    fenetre.blit(wallpapers_use.blur, (0,0))
                                else:
                                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                                    fenetre.blit(fond_visibilité, (0,0))
                            else:                    
                                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                            fenetre.blit(Menu,(1150,20))

                            fenetre.blit(Vilallongue_min0, (40,40))
                            fenetre.blit(Vilallongue_min1, (250,40))
                            fenetre.blit(Vilallongue_min2, (460,40))
                            fenetre.blit(Vilallongue_min3, (670,40))
                            fenetre.blit(Vilallongue_min4, (880,40))

                            if update_at_quit:
                                fenetre.blit(download_stat_downloading,(100,5))

                            if Vilallongue_fond_choice != 4:
                                fenetre.blit(fond,(40,157))
                            texte = font_Vilallongue.render("Jeu central", 1, BLACK_BNL)
                            fenetre.blit(texte, (20+40, 0+157))
                            texte = font_Vilallongue.render("Jeu joueur "+joueur1.nom, 1, BLACK_BNL)
                            fenetre.blit(texte, (20+40, 300+157))

                            print()
                            print(i_paquet_central)
                            print(i_joueur_courant)

                            affiche_jeu_joueur(jeu_joueur_courant, y_énoncé_joueur_courant, i_joueur_courant)
                            affiche_jeu_central(jeu_central, y_énoncé, i_paquet_central)

                        # Pour quitter en fermant la fenêtre
                        """
                        if event.type == QUIT:
                            pygame.quit()
                            continuer = False
                        """
                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")
                    """
                    if jeu_joueur_courant.get_nb_cartes() == 0:
                        pygame.quit()
                        continuer = False
                    """

        # Mode veille (seul le fond d'écran est affiché)
        while veille :
            étape_programme = "Veille"
            fenetre.blit(wallpapers_use.wallpaper, (0,0))

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()

            if update_at_quit:
                fenetre.blit(download_stat_downloading,(400,5))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    veille = False
                    if Skin_selected == "Titanium":
                        menu_continuer = True
                        ouverture_titre(200,2,0)
                    elif Skin_selected == "Carroussel":
                        Menu_skin2 = True
                        menu_carroussel.open()

                if event.type == KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN or event.key == K_ESCAPE :
                        veille = False
                        if Skin_selected == "Titanium":
                            menu_continuer = True
                            ouverture_titre(200,2,0)
                        elif Skin_selected == "Carroussel":
                            Menu_skin2 = True
                            menu_carroussel.open()

                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")

        # Menu de sélection des couleurs (Paramètres --> Personnalisation --> Plus de couleurs)
        while color_selection :
            
            étape_programme = "Utilitaire de personnalisation des couleurs"

            if audio_reader_proc.is_finish():
                audio_reader_proc.avancer()
            
            if Blur_background:
                fenetre.blit(wallpapers_use.blur, (0,0))
            else:
                fenetre.blit(wallpapers_use.wallpaper, (0,0))
                fenetre.blit(fond_visibilité, (0,0))
            fenetre.blit(Menu,(1150,20))
            fenetre.blit(Selection_menu,(455,0))
            fenetre.blit(texte_color, (500, 20))
            fenetre.blit(Color_menu,(755,0)) 
            
            fenetre.blit(Color_wheel, (700,100))
            pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(1196,496,58, 58),2,0)  
            fenetre.blit(color_white, (1200,500))
            pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(1196,596,58, 58),2,0)  
            fenetre.blit(color_black, (1200,600))
            
            texte = font_color.render(langue.mcolor_color_var, 5, (255,255,255))
            fenetre.blit(texte, (10, 100))
            
            texte = font_color.render(langue.mcolor_txt_title, 5, (255,255,255))
            fenetre.blit(texte, (10, 200))
            texte = font_color.render("BNL's Box", 5, color_txt)
            fenetre.blit(texte, (200, 200))
            texte = font_color.render(langue.mcolor_aux, 5, (255,255,255))
            fenetre.blit(texte, (10, 300))
            pygame.draw.rect(fenetre, color_aux, pygame.Rect(200,300,100, 20))
            texte = font_color.render(langue.mcolor_txt_menu_title, 5, (255,255,255))
            fenetre.blit(texte, (10, 400))
            texte = font_color.render("BNL's Box", 5, color_menu)
            fenetre.blit(texte, (200, 400))
            
            texte = font_color.render(langue.mcolor_rgb, 5, color_menu)
            fenetre.blit(texte, (10, 500))
            
            if color_input_r_s:
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(6,546,50, 28))
                texte = font_color.render(str(color_temp[0]), 5, (0,0,0))
                fenetre.blit(texte, (10, 550))
            else:
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(6,546,50, 28),2,0)
                texte = font_color.render(str(color_temp[0]), 5, (255,255,255))
                fenetre.blit(texte, (10, 550))

            if color_input_g_s:
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(66,546,50, 28))
                texte = font_color.render(str(color_temp[1]), 5, (0,0,0))
                fenetre.blit(texte, (70, 550)) 
            else:
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(66,546,50, 28),2,0) 
                texte = font_color.render(str(color_temp[1]), 5, (255,255,255))
                fenetre.blit(texte, (70, 550))
                
            if color_input_b_s:
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(126,546,50, 28)) 
                texte = font_color.render(str(color_temp[2]), 5, (0,0,0))
                fenetre.blit(texte, (130, 550))
            else:
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(126,546,50, 28),2,0) 
                texte = font_color.render(str(color_temp[2]), 5, (255,255,255))
                fenetre.blit(texte, (130, 550))
                
            pygame.draw.rect(fenetre, color_temp_f, pygame.Rect(190,546,28, 28)) 
                            
            fenetre.blit(bouton_OK, (100,650))
            
            pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(296,636,700, 78),2,0)            
            fenetre.blit(Selection_menu,(300,640))
            
            if "text" in color_list_selection:
                fenetre.blit(color_check_box1, (350,185))
                texte = font_color.render("BNL's Box", 1, color_temp_f)
                fenetre.blit(texte, (700, 660))
            else:
                fenetre.blit(color_check_box, (350,185))
                texte = font_color.render("BNL's Box", 1, color_txt)
                fenetre.blit(texte, (700, 660))
            if "aux" in color_list_selection:
                fenetre.blit(color_check_box1, (350,285))
                pygame.draw.rect(fenetre, color_temp_f, pygame.Rect(850,660,100, 20))
            else:
                fenetre.blit(color_check_box, (350,285))
                pygame.draw.rect(fenetre, color_aux, pygame.Rect(850,660,100, 20))
            if "menu" in color_list_selection:
                fenetre.blit(color_check_box1, (350,385))
                texte = font.render("BNL's Box", 1, color_temp_f)
                fenetre.blit(texte, (345, 660))
            else:
                fenetre.blit(color_check_box, (350,385))
                texte = font.render("BNL's Box", 1, color_menu)
                fenetre.blit(texte, (345, 660))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_stat = pygame.mouse.get_pressed()
                    if mouse_stat[0]:
                        if pos_Menu.collidepoint(event.pos):
                            color_selection = False
                            fond_écran = True
                            paramètres = True 
                            
                        if pos_color_text.collidepoint(event.pos):
                            if "text" in color_list_selection:
                                color_list_selection.remove("text")
                            else:
                                color_list_selection.append("text")
                                
                        if pos_color_aux.collidepoint(event.pos):
                            if "aux" in color_list_selection:
                                color_list_selection.remove("aux")
                            else:
                                color_list_selection.append("aux")
                                
                        if pos_color_menu.collidepoint(event.pos):
                            if "menu" in color_list_selection:
                                color_list_selection.remove("menu")
                            else:
                                color_list_selection.append("menu")
                                
                        if pos_color_white.collidepoint(event.pos):
                            color_temp = [255,255,255]
                            color_temp_f = (255,255,255)
                        if pos_color_black.collidepoint(event.pos):
                            color_temp = [0,0,0]
                            color_temp_f = (0,0,0)
                                
                        if pos_bouton_OK.collidepoint(event.pos):
                            color_temp_f = (int(color_temp[0]),int(color_temp[1]),int(color_temp[2]))  
                            for elem in color_list_selection:
                                if elem == "text":
                                    color_txt = color_temp_f
                                    data_base.update("color_txt",str(color_txt))
                                if elem == "aux":
                                    color_aux = color_temp_f
                                    data_base.update("color_aux",str(color_aux))
                                if elem == "menu":
                                    color_menu = color_temp_f
                                    data_base.update("color_menu",str(color_menu))
                                    
                            font_init()

                        if event.pos[0] >= 700 and event.pos[0] <= 1200 and event.pos[1] >= 100 and event.pos[1] <= 600 and not(pos_color_white.collidepoint(event.pos)) and not(pos_color_black.collidepoint(event.pos)):
                            test = pygame.Surface.get_at(Color_wheel, (event.pos[0]-700, event.pos[1]-100))
                            color_temp = [str(test[0]), str(test[1]), str(test[2])]
                            color_temp_f = (int(color_temp[0]),int(color_temp[1]),int(color_temp[2]))  
                                                        
                        if event.pos[0] >= 6 and event.pos[0] <= 56 and event.pos[1] >= 546 and event.pos[1] <= 574 :
                            if color_input_r_s:
                                color_input_r_s = False
                            else:
                                color_input_r_s = True
                        elif event.pos[0] >= 66 and event.pos[0] <= 116 and event.pos[1] >= 546 and event.pos[1] <= 574 :
                            if color_input_g_s:
                                color_input_g_s = False
                            else:
                                color_input_g_s = True
                        elif event.pos[0] >= 116 and event.pos[0] <= 166 and event.pos[1] >= 546 and event.pos[1] <= 574 : 
                            if color_input_b_s:
                                color_input_b_s = False
                            else:
                                color_input_b_s = True   
                                
                        else:
                            color_input_r_s = False 
                            color_input_g_s = False  
                            color_input_b_s = False  
                                         

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE :
                        color_selection = False
                        fond_écran = True
                        paramètres = True
                        
                    if event.key == pygame.K_BACKSPACE :
                        if color_input_r_s :
                            if int(color_temp[0]) > 9:
                                color_temp[0] = color_temp[0][:-1]
                            else:
                                color_temp[0] = "0"
                        if color_input_g_s :
                            if int(color_temp[1]) > 9:
                                color_temp[1] = color_temp[1][:-1]
                            else:
                                color_temp[1] = "0"
                        if color_input_b_s :
                            if int(color_temp[2]) > 9:
                                color_temp[2] = color_temp[2][:-1]
                            else:
                                color_temp[2] = "0"
                        
                        color_temp_f = (int(color_temp[0]),int(color_temp[1]),int(color_temp[2])) 
                            
                    else:                              
                        try:
                            color_test = int(event.unicode)
                            if color_input_r_s:
                                if color_temp[0][0] == "0":
                                    color_temp[0] = event.unicode
                                elif len(color_temp[0]) < 3:
                                    color_temp[0] += event.unicode
                            if color_input_g_s:
                                if color_temp[1][0] == "0":
                                    color_temp[1] = event.unicode
                                elif len(color_temp[1]) < 3:
                                    color_temp[1] += event.unicode
                            if color_input_b_s:
                                if color_temp[2][0] == "0":
                                    color_temp[2] = event.unicode
                                elif len(color_temp[2]) < 3:
                                    color_temp[2] += event.unicode
                            color_temp_f = (int(color_temp[0]),int(color_temp[1]),int(color_temp[2]))  
                        except:
                            None

                if event.type == QUIT:
                    if quit_enable and not(update_web):
                        STOP()
                    elif quit_enable and update_web:
                        STOP("Update.bat")               

        while mail_box:
            Console_ip_s = 0
            Console_ip_t = ""
            Console_pseudo_s = 0
            Console_pseudo_t = BNL_pseudo
            my_pseudo = BNL_pseudo
            other_ip = ""
            my_mess = ""
            mess_list = []
            while mail_box_init:
                étape_programme = "BNL's Intercomm / Menu"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_intercomm, (500, 20))
                fenetre.blit(Intercomm_menu,(755,0))
                texte = font.render(langue.intercomm_init, 1, color_txt)
                fenetre.blit(texte, (20,100))
                texte = font.render(langue.intercomm_select_stat, 1, color_txt)
                fenetre.blit(texte, (20,150))
                fenetre.blit(server_pic,(350, 130))
                fenetre.blit(client_pic,(550, 130))
                fenetre.blit(ON_OFF_maker,(460,150))
                if mail_box_stat == "server":
                    fenetre.blit(ON,(465,155))
                    texte = font.render(langue.intercomm_your_ip + socket.gethostbyname(socket.gethostname()),1,(color_txt))
                    fenetre.blit(texte, (700,150))
                elif mail_box_stat == "":
                    fenetre.blit(OFF,(480,155))
                elif mail_box_stat == "client":
                    fenetre.blit(ON,(495,155))
                    texte = font.render(langue.intercomm_enter_serv_ip, 1, color_txt)
                    fenetre.blit(texte, (20,400))
                texte = font.render(langue.intercomm_enter_pseudo, 1, color_txt)
                fenetre.blit(texte, (20,200))

                if Console_pseudo_s == 0 :
                    if Console_pseudo_t == "":
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(20,250,510, 30),2,50)
                    else:
                        pygame.draw.rect(fenetre, color_aux, pygame.Rect(20,250,510, 30),15,50)
                else :
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(20,250,510, 30),15,50)

                if mail_box_stat == "client":
                    if Console_ip_s == 0 :
                        if Console_ip_t == "":
                            pygame.draw.rect(fenetre, color_aux, pygame.Rect(20,450,510, 30),2,50)
                        else:
                            pygame.draw.rect(fenetre, color_aux, pygame.Rect(20,450,510, 30),15,50)
                    else :
                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(20,450,510, 30),15,50)
                    texte = font.render(Console_ip_t, 1, (0,0,0))
                    fenetre.blit(texte, (25,452))
                    fenetre.blit(intercomm_last_ip, (530,450))

                texte = font.render(Console_pseudo_t, 1, (0,0,0))
                fenetre.blit(texte, (25,252))
                texte = font.render(langue.intercomm_enforced_compatibility, 1, color_txt)
                fenetre.blit(texte, (20,500))
                fenetre.blit(ON_OFF_maker,(460,500))
                if intercomm_compatibility_enforced:
                    fenetre.blit(ON,(465,505))
                else:
                    fenetre.blit(OFF,(495,505))
                
                fenetre.blit(bouton_connexion, (590,650))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if event.pos[0] >= 20 and event.pos[0] <= 530 and event.pos[1] >= 250 and event.pos[1] <= 280 :
                                Console_pseudo_s = 1
                            else :
                                Console_pseudo_s = 0
                            if event.pos[0] >= 20 and event.pos[0] <= 530 and event.pos[1] >= 450 and event.pos[1] <= 480 and mail_box_stat == "client":
                                Console_ip_s = 1
                            else :
                                Console_ip_s = 0
                            if pos_Menu.collidepoint(event.pos):
                                onglets_fermeture(texte_intercomm,Intercomm_menu)
                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    transition_ouverture(322)

                                mail_box = False
                                mail_box_init = False

                            if pos_ON_OFF_intercomm.collidepoint(event.pos):
                                if mail_box_stat == "":
                                    mail_box_stat = "server"
                                elif mail_box_stat == "server":
                                    mail_box_stat = "client"
                                elif mail_box_stat == "client":
                                    mail_box_stat = ""
                            if pos_ON_OFF_compatibility_enforced.collidepoint(event.pos):
                                if intercomm_compatibility_enforced:
                                    data_base.update("intercomm_compatibility_enforced", "0")
                                else:
                                    data_base.update("intercomm_compatibility_enforced", "1")
                            if pos_intercomm_last_ip.collidepoint(event.pos):
                                if Intercomm_last_ip != "None":
                                    Console_ip_t = Intercomm_last_ip
                            if pos_bouton_connexion.collidepoint(event.pos) and my_pseudo != "" :
                                try:
                                    data_base.update("BNL_pseudo",my_pseudo)
                                    if other_ip != "":
                                        data_base.update("Intercomm_last_ip",other_ip)
                                    else:
                                        data_base.update("Intercomm_last_ip","None")
                                    texte = font.render(langue.intercomm_connect, 1, (255,0,0))
                                    fenetre.blit(texte, (720,660))
                                    pygame.display.flip()
                                    serv_mess = " "
                                    client_mess = " "
                                    my_mess_temp = ""
                                    comm_running = True
                                    if mail_box_stat == "client":
                                        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        server_host = socket.gethostname()

                                        client_crypt = intercomm_crypt()

                                        ip = socket.gethostbyname(server_host)

                                        sport = 8080

                                        server_host = other_ip
                                        name = client_crypt.encode_general(my_pseudo)
                                        
                                        socket_server.settimeout(20)
                                        socket_server.connect((server_host, sport))

                                        socket_server.sendall(name.encode())
                                        time.sleep(0.5)
                                        if intercomm_compatibility_enforced:
                                            socket_server.sendall((client_crypt.encode_general("compatibility_mode."+Version_Intercomm)).encode())
                                        else:
                                            socket_server.sendall((client_crypt.encode_general(Version_Intercomm)).encode())

                                        server_name = socket_server.recv(4096**2)
                                        server_name = client_crypt.decode_general(server_name.decode())

                                        client_crypt.other_decode_protocole_assign(client_crypt.decode_general((socket_server.recv(4096**2)).decode()))

                                        if compatibility_mode == 0:
                                            socket_server.sendall((client_crypt.encode_general(client_crypt.my_public_key)).encode())

                                    elif mail_box_stat == "server":
                                        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        host_name = socket.gethostname()
                                        s_ip = socket.gethostbyname(host_name)

                                        server_crypt = intercomm_crypt()

                                        port = 8080
                                        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                        socket_server.bind(('0.0.0.0', port))

                                        name = server_crypt.encode_general(my_pseudo)

                                        socket_server.settimeout(20)
                                        socket_server.listen(1)

                                        conn, add = socket_server.accept()

                                        client = server_crypt.decode_general((conn.recv(4096**2)).decode())

                                        conn.sendall(name.encode())

                                        server_crypt.version_check((conn.recv(4096**2)).decode())

                                        if compatibility_mode == 2:
                                            conn.shutdown(socket.SHUT_RDWR)
                                            conn.close()
                                        elif compatibility_mode == 1:
                                            conn.sendall(server_crypt.encode_general(("compatibility_mode")).encode())
                                            conn.sendall((server_crypt.encode_general(serv_mess)).encode())
                                        else:
                                            conn.sendall(server_crypt.encode_general((server_crypt.my_public_key)).encode())
                                            server_crypt.other_decode_protocole_assign(server_crypt.decode_general((conn.recv(4096**2)).decode()))
                                            conn.sendall((server_crypt.encode(serv_mess)).encode())

                                    socket_server.settimeout(None)
                                    mail_box_init = False
                                    mail_box_mess = True
                                    recv_thread = Thread(target=Intercomm_recv_thread, args=())
                                    recv_thread.start()
                                except Exception as e:
                                    print(e)
                                    now = datetime.datetime.now()
                                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                                    fichier=open("log.txt","a")
                                    if os.stat("log.txt").st_size == 0:
                                        fichier.write("________  __     __  __      ___     ________      _____      __  __" + "\n")
                                        fichier.write("| |     \ | |\   | | | |    /___/    | |     \    / ___ \     \ \/ /." + "\n")
                                        fichier.write("| |     | | | \  | | | |             | |     |   / /   \ \     \ \/.  " + "\n")
                                        fichier.write("| |_____/ | |\ \ | | | |             | |_____/  / /     \ \     \ \. " + "\n")
                                        fichier.write("| |     \ | | \ \| | | |             | |     \  \ \     / /    / \ \." + "\n")
                                        fichier.write("| |     | | |  \   | | |____         | |     |   \ \___/ /    / / \ \." + "\n")
                                        fichier.write("|_|_____/ |_|   \__| |______|        |_|_____/    \_____/    /_/   \_\." + "\n")
                                        fichier.write("\n")    
                                    fichier.write(str(dt_string) +"\n")
                                    fichier.write(f"Erreur detectee : {str(e)}" + "\n")
                                    fichier.write(f"Ligne : {str(sys.exc_info()[-1].tb_lineno)}" + "\n")
                                    fichier.write(f"Type d'erreur : {str(type(e).__name__)}" + "\n")
                                    fichier.write("Localisation : BNL's Intercomm, phase de connexion"+ "\n")
                                    fichier.write("\n")
                                    fichier.close()
                                    texte = font.render(langue.intercomm_failed, 1, (255,0,0))
                                    fenetre.blit(texte, (860,660))
                                    pygame.display.flip()
                                    time.sleep(2)

                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if event.key == pygame.K_ESCAPE :
                            onglets_fermeture(texte_intercomm,Intercomm_menu)
                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                transition_ouverture(322)

                            mail_box = False
                            mail_box_init = False

                        elif event.key == pygame.K_SPACE :
                            if Console_pseudo_s == 1:
                                Console_pseudo_t += " "
                        elif event.key == pygame.K_BACKSPACE :
                            if Console_pseudo_s == 1:
                                Console_pseudo_t = Console_pseudo_t[:-1]
                            if Console_ip_s == 1:
                                Console_ip_t = Console_ip_t[:-1]
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            if Console_pseudo_s == 1:
                                my_pseudo = Console_pseudo_t
                                Console_pseudo_s = 0
                                data_base.update("BNL_pseudo",my_pseudo)
                            if Console_ip_s == 1:
                                other_ip = Console_ip_t
                                Console_ip_s = 0
                        elif key[pygame.K_LCTRL] and key[pygame.K_v]:
                            if Console_pseudo_s == 1:
                                if (len(Console_pseudo_t) + len(pyperclip.paste())) < 56:
                                    Console_pseudo_t += pyperclip.paste()
                            elif Console_ip_s == 1:
                                if (len(Console_ip_t) + len(pyperclip.paste())) < 56:
                                    Console_ip_t += pyperclip.paste()
                        else:
                            if Console_pseudo_s == 1:
                                Console_pseudo_t += event.unicode
                            elif Console_ip_s == 1:
                                Console_ip_t += event.unicode
                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            intercomm_transfer_stat = 0

            while mail_box_mess:

                étape_programme = "BNL's Intercomm / Communication"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                if Blur_background:
                    fenetre.blit(wallpapers_use.blur, (0,0))
                else:
                    fenetre.blit(wallpapers_use.wallpaper, (0,0))
                    fenetre.blit(fond_visibilité, (0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(Intercomm_menu,(755,0))
                fenetre.blit(texte_intercomm, (500, 20))
                pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(20,650,1200, 30),15,50)
                if compatibility_mode != 0:
                    texte = font.render(langue.intercomm_compatibility_mode, 1, color_txt)
                    fenetre.blit(texte, (20,20))

                if intercomm_transfer_stat:
                    fenetre.blit(transfer_min1,(1240,650))
                else:
                    fenetre.blit(transfer_min,(1240,650))

                try:
                    texte = font.render(mess_list[10], 1, color_txt)
                    fenetre.blit(texte, (20,100))
                except:
                    None
                try:
                    texte = font.render(mess_list[9], 1, color_txt)
                    fenetre.blit(texte, (20,150))
                except:
                    None
                try:
                    texte = font.render(mess_list[8], 1, color_txt)
                    fenetre.blit(texte, (20,200))
                except:
                    None
                try:
                    texte = font.render(mess_list[7], 1, color_txt)
                    fenetre.blit(texte, (20,250))
                except:
                    None
                try:
                    texte = font.render(mess_list[6], 1, color_txt)
                    fenetre.blit(texte, (20,300))
                except:
                    None
                try:
                    texte = font.render(mess_list[5], 1, color_txt)
                    fenetre.blit(texte, (20,350))
                except:
                    None
                try:
                    texte = font.render(mess_list[4], 1, color_txt)
                    fenetre.blit(texte, (20,400))
                except:
                    None
                try:
                    texte = font.render(mess_list[3], 1, color_txt)
                    fenetre.blit(texte, (20,450))
                except:
                    None
                try:
                    texte = font.render(mess_list[2], 1, color_txt)
                    fenetre.blit(texte, (20,500))
                except:
                    None
                try:
                    texte = font.render(mess_list[1], 1, color_txt)
                    fenetre.blit(texte, (20,550))
                except:
                    None
                try:
                    texte = font.render(mess_list[0], 1, color_txt)
                    fenetre.blit(texte, (20,600))
                except:
                    None

                texte = font.render(my_mess_temp, 1, (0,0,0))
                fenetre.blit(texte, (22,652))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):

                                if mail_box_stat == "client":
                                    socket_server.shutdown(socket.SHUT_RDWR)
                                    socket_server.close()
                                else:
                                    conn.shutdown(socket.SHUT_RDWR)
                                    conn.close()
                                mail_box = True
                                mail_box_init = True
                                mail_box_mess = False
                                comm_running = False

                            if pos_transfer_min.collidepoint(event.pos):
                                étape_programme = "BNL's Intercomm / Envoi de fichiers"
                                intercomm_transfer_stat = 1
                                path = easygui.fileopenbox()
                                path_to_send = ""
                                if os.stat(path).st_size > 15000000:
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(20,650,1200, 30),15,50)
                                    texte = font.render(langue.intercomm_error_large + path, 1, (0,0,0))
                                    fenetre.blit(texte, (22,652))
                                    path = None
                                    pygame.display.flip()
                                    time.sleep(1)

                                if path != None:
                                    if os.getcwd() in path:
                                        path_to_send = path.replace(os.getcwd(),'')[1:]
                                    else:
                                        path_to_send = "Received_files"+chr(92)+path.split(chr(92))[-1]
                                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(20,650,1200, 30),15,50)
                                    texte = font.render(langue.intercomm_transfer_txt + path, 1, (0,0,0))
                                    fenetre.blit(texte, (22,652))
                                    pygame.display.flip()
                                    if mail_box_stat == "client":
                                        client_mess = "&"+path_to_send
                                        if comm_running:
                                            if compatibility_mode == 1:
                                                mess_send = client_crypt.encode_general(client_mess)
                                            else:
                                                mess_send = client_crypt.encode(client_mess)
                                            socket_server.sendall(mess_send.encode())
                                            BUFFER_SIZE = (4096**2)
                                            with open(path, "rb") as file:
                                                while True:
                                                    bytes_read = base64.b64encode(file.read(BUFFER_SIZE))
                                                    if not(bytes_read):
                                                        break
                                                    client_mess = bytes_read
                                                    if comm_running:
                                                        mess_send = client_mess
                                                        socket_server.sendall(mess_send)
                                                time.sleep(3)
                                                mess_send = bytes("END_file",'utf-8')
                                                socket_server.sendall(base64.b64encode(mess_send))
                                                my_mess_temp = ""
                                                mess_send = ""
                                                client_mess = ""
                                    else:
                                        serv_mess = "&"+path_to_send
                                        if comm_running:
                                            if compatibility_mode == 1:
                                                mess_send = server_crypt.encode_general(serv_mess)
                                            else:
                                                mess_send = server_crypt.encode(serv_mess)
                                            conn.sendall(mess_send.encode())
                                            BUFFER_SIZE = (4096**2)
                                            with open(path, "rb") as file:
                                                while True:
                                                    bytes_read = base64.b64encode(file.read(BUFFER_SIZE))
                                                    if not(bytes_read):
                                                        break
                                                    serv_mess = bytes_read
                                                    print(serv_mess)
                                                    if comm_running:
                                                        mess_send = serv_mess
                                                        conn.sendall(mess_send)
                                                time.sleep(3)
                                                mess_send = bytes("END_file",'utf-8')
                                                conn.sendall(base64.b64encode(mess_send))
                                                my_mess_temp = ""
                                                mess_send = ""
                                                serv_mess = ""

                                intercomm_transfer_stat = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE :
                            if mail_box_stat == "client":
                                socket_server.shutdown(socket.SHUT_RDWR)
                                socket_server.close()
                            else:
                                conn.shutdown(socket.SHUT_RDWR)
                                conn.close()

                            mail_box = True
                            mail_box_init = True
                            mail_box_mess = False
                            comm_running = False

                        elif event.key == pygame.K_SPACE :
                            if len(my_mess_temp) <= 100:
                                my_mess_temp += " "
                        elif event.key == pygame.K_BACKSPACE:
                            if len(my_mess_temp) > 0:
                                my_mess_temp = my_mess_temp[:-1]
                        elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            if mail_box_stat == "client":
                                client_mess = "t"+my_mess_temp
                                if comm_running:
                                    if compatibility_mode == 1:
                                        mess_send = client_crypt.encode_general(client_mess)
                                    else:
                                        mess_send = client_crypt.encode(client_mess)
                                    socket_server.sendall(mess_send.encode())
                                    mess_list.insert(0,my_pseudo + " : " + my_mess_temp)
                            else:
                                serv_mess = "t"+my_mess_temp
                                if comm_running:
                                    if compatibility_mode == 1:
                                        mess_send = server_crypt.encode_general(serv_mess)
                                    else:
                                        mess_send = server_crypt.encode(serv_mess)
                                    conn.sendall(mess_send.encode())
                                    mess_list.insert(0,my_pseudo + " : " + my_mess_temp)
                            my_mess_temp = ""
                        else:
                            if len(my_mess_temp) <= 70:
                                my_mess_temp += event.unicode

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            if mail_box_stat == "client":
                                socket_server.shutdown(socket.SHUT_RDWR)
                                socket_server.close()
                            else:
                                conn.shutdown(socket.SHUT_RDWR)
                                conn.close()

                            mail_box = False
                            mail_box_init = False
                            mail_box_mess = False
                            comm_running = False
                            STOP()
                        elif quit_enable and update_web:
                            if mail_box_stat == "client":
                                socket_server.shutdown(socket.SHUT_RDWR)
                                socket_server.close()
                            else:
                                conn.shutdown(socket.SHUT_RDWR)
                                conn.close()

                            mail_box = False
                            mail_box_init = False
                            mail_box_mess = False
                            comm_running = False
                            STOP("Update.bat")
        while tools :

            while tools_selection:

                étape_programme = "Outils"

                if audio_reader_proc.is_finish():
                    audio_reader_proc.avancer()

                fenetre.blit(wallpapers_use.wallpaper,(0,0))
                fenetre.blit(Menu,(1150,20))
                fenetre.blit(Selection_menu,(455,0))
                fenetre.blit(texte_tools, (500, 20))
                fenetre.blit(tools_min,(755,0))

                fenetre.blit(tello_icon,(80,300))
                fenetre.blit(yt_dlp_icon,(880,300))

                if update_at_quit:
                    fenetre.blit(download_stat_downloading,(100,5))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_stat = pygame.mouse.get_pressed()
                        if mouse_stat[0]:
                            if pos_Menu.collidepoint(event.pos):
                                onglets_fermeture(texte_tools,tools_min)
                                if Skin_selected == "Titanium":
                                    menu_continuer=True
                                    ouverture_titre(200,2,0)
                                elif Skin_selected == "Carroussel":
                                    Menu_skin2 = True
                                    menu_carroussel.open()
                                elif Skin_selected == "Legacy":
                                    Menu_skin1 = True
                                    menu_continuer = False
                                    transition_ouverture(322)
                                tools = False
                                tools_selection = False

                            if pos_yt_dlp_icon.collidepoint(event.pos):
                                tools_selection = False
                                Youtube_downloader = True
                                Youtube_downloader_menu = True

                            if pos_tello_icon.collidepoint(event.pos):
                                tools_selection = False
                                Tello_control = True
                                Tello_control_menu = True

                                if not(tello_active):
                                    tello = Tello()
                                    tello_active = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE :
                            onglets_fermeture(texte_tools,tools_min)
                            if Skin_selected == "Titanium":
                                menu_continuer=True
                                ouverture_titre(200,2,0)
                            elif Skin_selected == "Carroussel":
                                Menu_skin2 = True
                                menu_carroussel.open()
                            elif Skin_selected == "Legacy":
                                Menu_skin1 = True
                                menu_continuer = False
                                transition_ouverture(322)
                            tools = False
                            tools_selection = False

                    if event.type == QUIT:
                        if quit_enable and not(update_web):
                            STOP()
                        elif quit_enable and update_web:
                            STOP("Update.bat")

            if not(yt_dlp_running) and not(search_infos_stat):
                Console_url_stat = 0
                Console_url_text = ""
                res = 0
                format = 0
                target = ""
                type_out = ""
                
            while Youtube_downloader:
                scroll_yt_dlp = Scroll([1230,150],0, False)
                while Youtube_downloader_menu:
                    étape_programme = "Outils / Youtube downloader"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))

                    try:
                        fenetre.blit(Youtube_min, (0,-(Youtube_min.get_height()-720)//2))
                    except:
                        None

                    fenetre.blit(fond_visibilité,(0,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(yt_dlp_settings, (1175,120))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.yt_dlp_title, 5, (255,255,255)), (500, 20))
                    fenetre.blit(yt_dlp_icon_min,(755,0))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    texte = font.render(langue.yt_dlp_url, 1, color_txt)
                    fenetre.blit(texte, (20,200))
                    texte = font.render(langue.yt_dlp_nb_download, 1, color_txt)
                    fenetre.blit(texte, (20,600))
                    texte = font.render(str(yt_dlp_thread_list), 1, color_txt)
                    fenetre.blit(texte, (20,650))

                    if Console_url_stat == 0 :
                        if Console_url_text == "":
                            pygame.draw.rect(fenetre, color_aux, pygame.Rect(20,250,1240, 30),2,50)
                        else:
                            pygame.draw.rect(fenetre, color_aux, pygame.Rect(20,250,1240, 30),15,50)
                    else :
                        pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(20,250,1240, 30),15,50)

                    if len(Console_url_text) > 80:
                        texte = font.render(Console_url_text[:80]+"...", 1, (0,0,0))
                    else:
                        texte = font.render(Console_url_text, 1, (0,0,0))
                    fenetre.blit(texte, (25,253))

                    try :
                        fenetre.blit(font.render(f"{langue.yt_dlp_video_title} {youtube_info['title']}", 1, color_txt),(300,300))
                        fenetre.blit(font.render(f"{langue.yt_dlp_autor} {youtube_info['channel']}", 1, color_txt),(300,350))
                        fenetre.blit(font.render(f"{langue.yt_dlp_lenght} {youtube_info['duration']//3600}h {(youtube_info['duration']%3600)//60}m {(youtube_info['duration']%3600)%60}s", 1, color_txt),(300,400))
                        fenetre.blit(font.render(f"{langue.yt_dlp_views} {youtube_info['view_count']}", 1, color_txt),(300,450))
                    except:
                        None

                    fenetre.blit(yt_dlp_download,(20,500))

                    texte = font.render(yt_dlp_txt, 1, color_txt)
                    fenetre.blit(texte, (300,650))

                    if target == "playlist":
                        fenetre.blit(yt_dlp_playlist_button, (20,300))

                    if format == "mp4":
                        fenetre.blit(MP4_icon2, (120,500))
                    else:
                        fenetre.blit(MP4_icon, (120,500))
                    if format == "mov":
                        fenetre.blit(MOV_icon2, (220,500))
                    else:
                        fenetre.blit(MOV_icon, (220,500))
                    if format == "mkv":
                        fenetre.blit(MKV_icon2, (320,500))
                    else:
                        fenetre.blit(MKV_icon, (320,500))
                    if format == "flv":
                        fenetre.blit(FLV_icon2, (420,500))
                    else:
                        fenetre.blit(FLV_icon, (420,500))
                    if format == "webm":
                        fenetre.blit(WEBM_icon2, (520,500))
                    else:
                        fenetre.blit(WEBM_icon, (520,500))
                    if format == "avi":
                        fenetre.blit(AVI_icon2, (620,500))
                    else:
                        fenetre.blit(AVI_icon, (620,500))

                    if format == "mp3":
                        fenetre.blit(MP3_icon2, (120,550))
                    else:
                        fenetre.blit(MP3_icon, (120,550))
                    if format == "m4a":
                        fenetre.blit(M4A_icon2, (220,550))
                    else:
                        fenetre.blit(M4A_icon, (220,550))
                    if format == "wav":
                        fenetre.blit(WAV_icon2, (320,550))
                    else:
                        fenetre.blit(WAV_icon, (320,550))
                    if format == "flac":
                        fenetre.blit(FLAC_icon2, (420,550))
                    else:
                        fenetre.blit(FLAC_icon, (420,550))
                    if format == "opus":
                        fenetre.blit(OPUS_icon2, (520,550))
                    else:
                        fenetre.blit(OPUS_icon, (520,550))
                    if format == "vorbis":
                        fenetre.blit(OGG_icon2, (620,550))
                    else:
                        fenetre.blit(OGG_icon, (620,550))

                    if type_out == "audio":
                        if res == 64:
                            fenetre.blit(i64kbps_icon2, (820,500))
                        else:
                            fenetre.blit(i64kbps_icon, (820,500))
                        if res == 128:
                            fenetre.blit(i128kbps_icon2, (920,500))
                        else:
                            fenetre.blit(i128kbps_icon, (920,500))
                        if res == 192:
                            fenetre.blit(i192kbps_icon2, (820,550))
                        else:
                            fenetre.blit(i192kbps_icon, (820,550))
                        if res == 320:
                            fenetre.blit(i320kbps_icon2, (920,550))
                        else:
                            fenetre.blit(i320kbps_icon, (920,550))
                        
                    if Youtube_loading_signal.img_in_use != None:    
                        fenetre.blit(Youtube_loading_signal.img_in_use, Youtube_loading_signal.coor)

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Youtube_downloader = False
                                    Youtube_downloader_menu = False
                                    tools_selection = True
                                    
                                if pos_yt_dlp_settings.collidepoint(event.pos) and not(yt_dlp_running):
                                    Youtube_downloader_menu = False
                                    Youtube_downloader_settings = True
                                    
                                elif not(yt_dlp_running) and not(search_infos_stat):

                                    if event.pos[0] >= 20 and event.pos[0] <= 1260 and event.pos[1] >= 250 and event.pos[1] <= 280 :
                                        Console_url_stat = 1
                                    elif Console_url_stat == 1:
                                        Console_url_stat = 0
                                        if Console_url_text != "":
                                            get_infos_thread = Thread(target=yt_dlp_infos_thread, args=(Console_url_text,))
                                            get_infos_thread.start()

                                    if pos_yt_dlp_download.collidepoint(event.pos) and Console_url_text != "" and format != 0 and res != 0 and not(search_infos_stat) and video_to_download != []:
                                        fenetre.blit(yt_dlp_download2,(20,500))
                                        pygame.display.flip()
                                        time.sleep(0.5)
                                        try:

                                            Youtube_thread = Thread(target=yt_dlp_download_thread, args=(video_to_download,format,res))
                                            if target == "playlist" :
                                                yt_dlp_thread_list += len(video_to_download)
                                            else:
                                                yt_dlp_thread_list += 1
                                            Youtube_thread.start()
                                        except Exception as e:
                                            print(e)
                                            Youtube_min = None
                                            yt_dlp_txt = langue.yt_dlp_url_error
                                            pygame.display.flip()
                                            time.sleep(1)

                                    if pos_MP4.collidepoint(event.pos):
                                        format = "mp4"
                                        type_out = "video"
                                        res = "video"
                                    if pos_MOV.collidepoint(event.pos):
                                        format = "mov"
                                        type_out = "video"
                                        res = "video"
                                    if pos_MKV.collidepoint(event.pos):
                                        format = "mkv"
                                        type_out = "video"
                                        res = "video"
                                    if pos_WEBM.collidepoint(event.pos):
                                        format = "webm"
                                        type_out = "video"
                                        res = "video"
                                    if pos_AVI.collidepoint(event.pos):
                                        format = "avi"
                                        type_out = "video"
                                        res = "video"
                                    if pos_FLV.collidepoint(event.pos):
                                        format = "flv"
                                        type_out = "video"
                                        res = "video"

                                    if pos_MP3.collidepoint(event.pos):
                                        format = "mp3"
                                        type_out = "audio"
                                        if res == "video":
                                            res = 0
                                    if pos_FLAC.collidepoint(event.pos):
                                        format = "flac"
                                        type_out = "audio"
                                        if res == "video":
                                            res = 0
                                    if pos_OPUS.collidepoint(event.pos):
                                        format = "opus"
                                        type_out = "audio"
                                        if res == "video":
                                            res = 0
                                    if pos_OGG.collidepoint(event.pos):
                                        format = "vorbis"
                                        type_out = "audio"
                                        if res == "video":
                                            res = 0
                                    if pos_M4A.collidepoint(event.pos):
                                        format = "m4a"
                                        type_out = "audio"
                                        if res == "video":
                                            res = 0
                                    if pos_WAV.collidepoint(event.pos):
                                        format = "wav"
                                        type_out = "audio"
                                        if res == "video":
                                            res = 0

                                    if type_out == "audio":
                                        if pos_64kbps.collidepoint(event.pos):
                                            res = 64
                                        if pos_128kbps.collidepoint(event.pos):
                                            res = 128
                                        if pos_192kbps.collidepoint(event.pos):
                                            res = 192
                                        if pos_320kbps.collidepoint(event.pos):
                                            res = 320

                                    if target == "playlist" and pos_playlist_selection.collidepoint(event.pos):
                                        Youtube_downloader_menu = False
                                        Youtube_downloader_playlist_listing = True
                                        yt_video_init_search = True

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE :
                                Youtube_downloader = False
                                Youtube_downloader_menu = False
                                tools_selection = True

                            if Console_url_stat:
                                if event.key == pygame.K_SPACE :
                                    if len(Console_url_text) <= 70:
                                        Console_url_text += " "
                                elif event.key == pygame.K_BACKSPACE:
                                    if len(Console_url_text) > 0:
                                        Console_url_text = Console_url_text[:-1]
                                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and not(search_infos_stat):
                                    get_infos_thread = Thread(target=yt_dlp_infos_thread, args=(Console_url_text,))
                                    get_infos_thread.start()
                                    Console_url_stat = 0
                                elif event.key == pygame.K_DELETE and Console_url_stat:
                                    Console_url_text = ""
                                elif key[pygame.K_LCTRL] and key[pygame.K_v]:
                                    if (len(Console_url_text) + len(pyperclip.paste())) < 700:
                                        Console_url_text += pyperclip.paste()
                                else:
                                    if len(Console_url_text) <= 700:
                                        Console_url_text += event.unicode

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while Youtube_downloader_playlist_listing:
                    étape_programme = "Outils / Youtube downloader / Playlist selection"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))

                    try:
                        fenetre.blit(Youtube_min, (0,-(Youtube_min.get_height()-720)//2))
                    except:
                        None

                    fenetre.blit(fond_visibilité,(0,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.yt_dlp_title, 5, (255,255,255)), (500, 20))
                    fenetre.blit(yt_dlp_icon_min,(755,0))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    yt_videos_listing_lat_decalage = 0
                    yt_videos_listing_long_decalage = 0

                    yt_videos_panel_pos()

                    for i in range(len(playlist_list)):
                        fenetre.blit(liste_check_box[i], (50+yt_videos_listing_long_decalage,120+yt_videos_listing_lat_decalage-scroll_yt_dlp.val))
                        fenetre.blit(font.render(playlist_list[i][1], 5, color_txt), (200+yt_videos_listing_long_decalage,125+yt_videos_listing_lat_decalage-scroll_yt_dlp.val))

                        yt_videos_listing_lat_decalage += 80


                    a,b= pygame.mouse.get_pos ( )
                    mouse_stat = pygame.mouse.get_pressed()

                    if mouse_stat[0] and b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550 and scroll_yt_dlp.pos.collidepoint(pygame.mouse.get_pos()):
                        if scroll_yt_dlp.coor[1] < b-scroll_bar_decalage[1]:
                            scroll_yt_dlp.val -= (scroll_yt_dlp.coor[1] - (b-scroll_bar_decalage[1]))*((len(playlist_list))//2)
                        elif scroll_yt_dlp.coor[1] > b-scroll_bar_decalage[1]:
                            scroll_yt_dlp.val += -(scroll_yt_dlp.coor[1] - (b-scroll_bar_decalage[1]))*((len(playlist_list))//2)
                        scroll_yt_dlp.coor[1] = b-scroll_bar_decalage[1]
                        scroll_yt_dlp.pos = scroll_bar.get_rect(topleft=scroll_yt_dlp.coor)

                    fenetre.blit(scroll_bar,scroll_yt_dlp.coor)

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                yt_videos_is_click()
                                if pos_Menu.collidepoint(event.pos):
                                    Youtube_downloader_menu = True
                                    Youtube_downloader_playlist_listing = False
                                if scroll_yt_dlp.pos.collidepoint(event.pos):
                                    scroll_bar_decalage = [a-scroll_yt_dlp.coor[0],b-scroll_yt_dlp.coor[1]]

                        if event.type == pygame.MOUSEWHEEL:
                            scroll_yt_dlp.stat = False
                            a = 0
                            b = scroll_yt_dlp.coor[1]-event.y
                            scroll_bar_decalage = [0,0]

                            if b-scroll_bar_decalage[1] >= 150 and b-scroll_bar_decalage[1] <= 550:
                                if scroll_yt_dlp.coor[1] < b-scroll_bar_decalage[1]:
                                    scroll_yt_dlp.val -= (scroll_yt_dlp.coor[1] - (b-scroll_bar_decalage[1]))*((len(playlist_list))//2)
                                elif scroll_yt_dlp.coor[1] > b-scroll_bar_decalage[1]:
                                    scroll_yt_dlp.val += -(scroll_yt_dlp.coor[1] - (b-scroll_bar_decalage[1]))*((len(playlist_list))//2)
                                scroll_yt_dlp.coor[1] = b-scroll_bar_decalage[1]
                                scroll_yt_dlp.pos = scroll_bar.get_rect(topleft=scroll_yt_dlp.coor)

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE :
                                Youtube_downloader_menu = True
                                Youtube_downloader_playlist_listing = False

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")
                                
                while Youtube_downloader_settings:
                    étape_programme = "Outils / Youtube downloader / Settings"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))

                    try:
                        fenetre.blit(Youtube_min, (0,-(Youtube_min.get_height()-720)//2))
                    except:
                        None

                    fenetre.blit(fond_visibilité,(0,0))
                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.yt_dlp_title, 5, (255,255,255)), (500, 20))
                    fenetre.blit(yt_dlp_icon_min,(755,0))
                    
                    fenetre.blit(ON_OFF_maker,(850,167))
                    fenetre.blit(ON_OFF_maker,(850,217))
                    fenetre.blit(ON_OFF_maker,(850,267))

                    if yt_set_album_playlist:
                        fenetre.blit(ON,(855,172))
                    else:
                        fenetre.blit(OFF,(885,172))
                        
                    if yt_set_title:
                        fenetre.blit(ON,(855,222))
                    else:
                        fenetre.blit(OFF,(885,222))
                        
                    if yt_set_artist:
                        fenetre.blit(ON,(855,272))
                    else:
                        fenetre.blit(OFF,(885,272))

                    texte = font.render(langue.yt_dlp_settings_album, 1, (color_txt))
                    fenetre.blit(texte, (150, 167))
                    texte = font.render(langue.yt_dlp_settings_title, 1, (color_txt))
                    fenetre.blit(texte, (150, 217))
                    texte = font.render(langue.yt_dlp_settings_artist, 1, (color_txt))
                    fenetre.blit(texte, (150, 267))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Youtube_downloader_menu = True
                                    Youtube_downloader_settings = False
                                    
                                if pos_ON_OFF_yt_dlp_set_album.collidepoint(event.pos):
                                    data_base.update("yt_set_album_playlist",str(abs(yt_set_album_playlist-1)))
                                if pos_ON_OFF_yt_dlp_set_title.collidepoint(event.pos):
                                    data_base.update("yt_set_title",str(abs(yt_set_title-1)))
                                if pos_ON_OFF_yt_dlp_set_artist.collidepoint(event.pos):
                                    data_base.update("yt_set_artist",str(abs(yt_set_artist-1)))

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE :
                                Youtube_downloader_menu = True
                                Youtube_downloader_settings = False

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

            while Tello_control:
                while Tello_control_menu:
                    étape_programme = "Outils / BNL's Drone Control"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))

                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.tello_title, 5, (255,255,255)), (500, 20))
                    fenetre.blit(tello_icon_min,(755,0))

                    fenetre.blit(font_audio_reader.render(tello_sys.txt_menu, 5, (255,255,255)), (10, 100))
                    fenetre.blit(font_audio_reader.render(tello_sys.txt2_menu, 5, (255,255,255)), (10, 150))

                    fenetre.blit(tello_connexion, (455,500))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    if tello_sys.connected:
                        Tello_control_menu = False
                        Tello_control_before_flight = True

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Tello_control = False
                                    Tello_control_menu = False
                                    tools_selection = True
                                if pos_tello_connexion.collidepoint(event.pos) and not(tello_sys.connexion):
                                    Tello_log = open("Tello_log.txt", "w")
                                    if os.stat("Tello_log.txt").st_size == 0:
                                        fichier.write("________  __     __  __      ___     ________      _____      __  __" + "\n")
                                        fichier.write("| |     \ | |\   | | | |    /___/    | |     \    / ___ \     \ \/ /." + "\n")
                                        fichier.write("| |     | | | \  | | | |             | |     |   / /   \ \     \ \/.  " + "\n")
                                        fichier.write("| |_____/ | |\ \ | | | |             | |_____/  / /     \ \     \ \. " + "\n")
                                        fichier.write("| |     \ | | \ \| | | |             | |     \  \ \     / /    / \ \." + "\n")
                                        fichier.write("| |     | | |  \   | | |____         | |     |   \ \___/ /    / / \ \." + "\n")
                                        fichier.write("|_|_____/ |_|   \__| |______|        |_|_____/    \_____/    /_/   \_\." + "\n")
                                        fichier.write("\n")    
                                    Tello_log.write("Tello control by BNL's Box (a product of MINI Picture)"+"\n")
                                    Tello_log.write("\n")
                                    tello_sys.connect_process()

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE:
                                Tello_control = False
                                Tello_control_menu = False
                                tools_selection = True

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while Tello_control_before_flight:
                    étape_programme = "Outils / BNL's Drone Control / Pré-vol Menu"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))

                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.tello_before_fly, 5, (255,255,255)), (500, 20))
                    fenetre.blit(tello_icon_min,(755,0))

                    fenetre.blit(tello_check,(500,500))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    if not(tello_sys.connected):
                        Tello_control_menu = True
                        Tello_control_before_flight = False

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Tello_control_menu = True
                                    Tello_control_before_flight = False
                                    tello_sys.connected = False
                                if pos_tello_check.collidepoint(event.pos):
                                    Tello_control_check_up = True
                                    Tello_control_before_flight = False

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE:
                                Tello_control_menu = True
                                Tello_control_flight_mode = False
                                tello_sys.connected = False

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while Tello_control_check_up:
                    étape_programme = "Outils / BNL's Drone Control / Vérifications"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))

                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.tello_check_up, 5, (255,255,255)), (500, 20))
                    fenetre.blit(tello_icon_min,(755,0))

                    tello_sys.check_up()

                    fenetre.blit(font_audio_reader.render(f"{langue.tello_battery} : {str(tello_sys.battery)} %", 5, tello_sys.color_check), (10, 100))
                    fenetre.blit(font_audio_reader.render(f"{langue.tello_altimeter} : {str(tello_sys.barometer)} cm", 5, tello_sys.color_check), (10, 150))
                    fenetre.blit(font_audio_reader.render(f"{langue.tello_time_fly} : {str(tello_sys.flight_time)} s", 5, tello_sys.color_check), (10, 200))
                    fenetre.blit(font_audio_reader.render(f"{langue.tello_pitch} : {str(tello_sys.pitch)} deg", 5, tello_sys.color_check), (10, 250))
                    fenetre.blit(font_audio_reader.render(f"{langue.tello_roll} : {str(tello_sys.roll)} deg", 5, tello_sys.color_check), (10, 300))
                    fenetre.blit(font_audio_reader.render(f"{langue.tello_temperature} : {str(tello_sys.temperature)} °C", 5, tello_sys.color_check), (10, 350))
                    fenetre.blit(font_audio_reader.render(f"{langue.tello_altitude} : {str(tello_sys.altitude)} cm", 5, tello_sys.color_check), (10, 400))

                    fenetre.blit(font_audio_reader.render(f"{langue.tello_state} : {str(tello_sys.stat_check)}", 5, tello_sys.color_check), (10, 500))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    if not(tello_sys.connected):
                        Tello_control_menu = True
                        Tello_control_check_up = False

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos):
                                    Tello_control_check_up = False
                                    Tello_control_before_flight = True
                                    now = datetime.datetime.now()
                                    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                                    Tello_log.write(f"{dt_string}   Fin de la séquence de vol...")
                                    Tello_log.close()

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE:
                                Tello_control_check_up = False
                                Tello_control_before_flight = True
                                now = datetime.datetime.now()
                                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                                Tello_log.write(f"{dt_string}   Fin de la séquence de vol...")
                                Tello_log.close()

                            if event.key == pygame.K_t:
                                Tello_control_check_up = False
                                Tello_control_flight_mode = True

                                tello.streamon()
                                tello_wifi_thread = Thread(target=tello_sys.get_wifi, args=(1,))
                                tello_check_up_thread = Thread(target=tello_sys.minimal_check_up, args=(1,))
                                tello_img_thread = Thread(target=tello_sys.get_img, args=(1,))

                                tello_wifi_thread.start()
                                tello_check_up_thread.start()
                                tello_img_thread.start()

                        if event.type == QUIT:
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

                while Tello_control_flight_mode:
                    étape_programme = "Outils / BNL's Drone Control / Mode vol"

                    if audio_reader_proc.is_finish():
                        audio_reader_proc.avancer()

                    if Blur_background:
                        fenetre.blit(wallpapers_use.blur, (0,0))
                    else:
                        fenetre.blit(wallpapers_use.wallpaper, (0,0))
                        fenetre.blit(fond_visibilité, (0,0))

                    try:
                        fenetre.blit(tello_sys.img, (160,0))
                    except:
                        None

                    fenetre.blit(Menu,(1150,20))
                    fenetre.blit(Selection_menu,(455,0))
                    fenetre.blit(font.render(langue.tello_fly, 5, (255,255,255)), (500, 20))
                    fenetre.blit(tello_icon_min,(755,0))

                    fenetre.blit(carr_title_bar,(0,606))

                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(10,620,150, 30),2,0)
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(14,624,((142/100)*int(tello_sys.battery)), 22))

                    fenetre.blit(font_widget.render(str(tello_sys.battery)+" %", 5, (255,255,255)), (165, 625))
                    fenetre.blit(tello_battery_min, (220,620))

                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(10,660,150, 30),2,0)
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(14,664,((142/100)*int(tello_sys.wifi_signal)), 22))

                    fenetre.blit(tello_wifi_min, (165,660))

                    fenetre.blit(tello_move_min, (515,620))
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(550,620,150, 30),2,0)
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(554,624,((142/500)*int(tello_sys.move_n)), 22))

                    fenetre.blit(font_widget.render(str(tello_sys.move_n)+" cm", 5, (255,255,255)), (705, 625))

                    fenetre.blit(tello_rotate_min, (515,660))
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(550,660,150, 30),2,0)
                    pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(554,664,((142/360)*int(tello_sys.rotate_n)), 22))

                    fenetre.blit(font_widget.render(str(tello_sys.rotate_n)+" °", 5, (255,255,255)), (705, 665))

                    fenetre.blit(font_widget.render(f"{langue.tello_altitude} : {tello_sys.altitude} cm", 5, (255,255,255)), (300, 625))

                    fenetre.blit(font_widget.render(f"{langue.tello_state} : {tello_sys.stat}", 5, (255,255,255)), (300, 665))

                    fenetre.blit(tello_picture, (950,610))

                    if tello_sys.takeoff_security_lock:
                        fenetre.blit(tello_lock, (1100,610))
                    else:
                        fenetre.blit(tello_unlock, (1100,610))

                    if tello_sys.record_stat:
                        fenetre.blit(tello_rec_run, (800,610))
                    else:
                        fenetre.blit(tello_rec, (800,610))

                    if update_at_quit:
                        fenetre.blit(download_stat_downloading,(100,5))

                    if not(tello_sys.connected):
                        Tello_control_menu = True
                        Tello_control_flight_mode = False

                        tello.streamoff()

                    pygame.display.flip()

                    key = pygame.key.get_pressed()

                    if key[pygame.K_LCTRL]:
                        if tello_sys.move_n > 20:
                            tello_sys.move_n -= 2

                    if key[pygame.K_LSHIFT]:
                        if tello_sys.move_n < 500:
                            tello_sys.move_n += 2

                    if key[pygame.K_b]:
                        if tello_sys.rotate_n > 1:
                            tello_sys.rotate_n -= 2

                    if key[pygame.K_n]:
                        if tello_sys.rotate_n < 360:
                            tello_sys.rotate_n += 2

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            mouse_stat = pygame.mouse.get_pressed()
                            if mouse_stat[0]:
                                if pos_Menu.collidepoint(event.pos) and tello_sys.safety_quit_check():
                                    Tello_control_flight_mode = False
                                    Tello_control_check_up = True

                                    tello.streamoff()

                                if pos_tello_lock.collidepoint(event.pos) and not(tello_sys.fly):
                                    if tello_sys.takeoff_security_lock:
                                        tello_sys.takeoff_security_lock = False
                                        now = datetime.datetime.now()
                                        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                                        Tello_log.write(f"{dt_string}   Déverouillage de l'appareil..."+"\n")
                                        Tello_log.write("\n")
                                    else:
                                        tello_sys.takeoff_security_lock = True
                                        now = datetime.datetime.now()
                                        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                                        Tello_log.write(f"{dt_string}   Verouillage de l'appareil..."+"\n")
                                        Tello_log.write("\n")

                                if pos_tello_picture.collidepoint(event.pos):
                                    picture_thread = Thread(target=tello_sys.take_picture, args=(1,))
                                    picture_thread.start()

                                if pos_tello_rec.collidepoint(event.pos):
                                    if not(tello_sys.record_stat):
                                        tello_sys.record_stat = True
                                        video_thread = Thread(target=tello_sys.take_video, args=(1,))
                                        video_thread.start()
                                    else:
                                        tello_sys.record_stat = False

                        if event.type == pygame.KEYDOWN:
                            key = pygame.key.get_pressed()
                            if event.key == pygame.K_ESCAPE and tello_sys.safety_quit_check():
                                Tello_control_flight_mode = False
                                Tello_control_check_up = True

                                tello.streamoff()

                            if event.key == pygame.K_t:
                                takeoff_thread = Thread(target=tello_sys.takeoff_security, args=(1,))
                                takeoff_thread.start()

                            if tello_sys.fly:
                                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                                    if not(tello_sys.act):
                                        land_thread = Thread(target=tello_sys.land_protocol, args=(1,))
                                        land_thread.start()

                                if event.key == pygame.K_UP:
                                    if not(tello_sys.act):
                                        forward_thread = Thread(target=tello_sys.forward, args=(1,))
                                        forward_thread.start()

                                if event.key == pygame.K_DOWN:
                                    if not(tello_sys.act):
                                        back_thread = Thread(target=tello_sys.back, args=(1,))
                                        back_thread.start()

                                if event.key == pygame.K_LEFT:
                                    if not(tello_sys.act):
                                        left_thread = Thread(target=tello_sys.left, args=(1,))
                                        left_thread.start()

                                if event.key == pygame.K_RIGHT:
                                    if not(tello_sys.act):
                                        right_thread = Thread(target=tello_sys.right, args=(1,))
                                        right_thread.start()

                                if event.key == pygame.K_a:
                                    if not(tello_sys.act):
                                        up_thread = Thread(target=tello_sys.up, args=(1,))
                                        up_thread.start()

                                if event.key == pygame.K_w:
                                    if not(tello_sys.act):
                                        down_thread = Thread(target=tello_sys.down, args=(1,))
                                        down_thread.start()

                                if event.key == pygame.K_q:
                                    if not(tello_sys.act):
                                        yaw_counter_clock_thread = Thread(target=tello_sys.yaw_counter_clock, args=(1,))
                                        yaw_counter_clock_thread.start()

                                if event.key == pygame.K_s:
                                    if not(tello_sys.act):
                                        yaw_clock_thread = Thread(target=tello_sys.yaw_clock, args=(1,))
                                        yaw_clock_thread.start()

                        if event.type == QUIT and tello_sys.safety_quit_check():
                            tello.streamoff()
                            if quit_enable and not(update_web):
                                STOP()
                            elif quit_enable and update_web:
                                STOP("Update.bat")

# Erreur : en cas d'erreur, le système sautera directement ce qui précède pour en arriver ici : écriture de l'erreur dans le fichier log et activation du BNL's Box Security Mode
except Exception as e:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    fichier=open("log.txt","a")
    if os.stat("log.txt").st_size == 0:
        fichier.write("________  __     __  __      ___     ________      _____      __  __" + "\n")
        fichier.write("| |     \ | |\   | | | |    /___/    | |     \    / ___ \     \ \/ /." + "\n")
        fichier.write("| |     | | | \  | | | |             | |     |   / /   \ \     \ \/.  " + "\n")
        fichier.write("| |_____/ | |\ \ | | | |             | |_____/  / /     \ \     \ \. " + "\n")
        fichier.write("| |     \ | | \ \| | | |             | |     \  \ \     / /    / \ \." + "\n")
        fichier.write("| |     | | |  \   | | |____         | |     |   \ \___/ /    / / \ \." + "\n")
        fichier.write("|_|_____/ |_|   \__| |______|        |_|_____/    \_____/    /_/   \_\." + "\n")
        fichier.write("\n")    
    
    fichier.write(str(dt_string) +"\n")
    fichier.write(f"Erreur detectee : {str(e)}" + "\n")
    fichier.write(f"Ligne : {str(sys.exc_info()[-1].tb_lineno)}" + "\n")
    fichier.write(f"Type d'erreur : {str(type(e).__name__)}" + "\n")
    fichier.write("Localisation : "+ étape_programme +"\n")
    fichier.write("\n")
    fichier.close()
    continuer = False
    erreur_report = True
    erreur_détail = e
    try :
        data_base.exit()
    except:
        None

error_menu = False
error_check = False

def error_download_file(url):
    global download_error
    global download_error_txt
    download_error = True
    try:
        output = "Level mise à niveau.zip"
        gdown.download(url, output, quiet=True)
        with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
            zipObj.extract("file_list.py")
            zipObj.extract("Update_check.py")
            zipObj.extract("file_list.py")

        download_error = False
    except:
        download_error_txt = "Téléchargement en cours : impossible de contacter le serveur / une erreur s'est produite"
        time.sleep(3)
        download_error = False

# Menu sécurisé d'erreur (accueil)
while erreur_report and not(test_error):
    try :
        pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
    except:
        fenetre = pygame.display.set_mode((1280,720))
        pygame.init()
        pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
    try :
        font = pygame.font.Font(font_selected, 25)
    except :
        font = pygame.font.Font(None, 30)
    texte = font.render("BNL's Security mode", 5, (255,255,255))
    fenetre.blit(texte, (530, 10))

    try:
        texte = font.render(langue.error_menu1_1, 1, (255,255,255))
        fenetre.blit(texte, (10, 60))
        texte = font.render(langue.error_menu1_2, 1, (255,255,255))
        fenetre.blit(texte, (10, 100))
        texte = font.render(langue.error_menu1_3, 1, (255,255,255))
        fenetre.blit(texte, (10, 140))
        texte = font.render(langue.error_menu1_4, 1, (255,255,255))
        fenetre.blit(texte, (10, 180))
        texte = font.render(langue.error_menu1_5, 1, (255,255,255))
        fenetre.blit(texte, (10, 220))
        texte = font.render(langue.error_menu1_6, 1, (255,255,255))
        fenetre.blit(texte, (10, 260))
        texte = font.render(langue.error_menu1_7, 1, (255,0,0))
        fenetre.blit(texte, (10, 300))
    except:
        texte = font.render("BNL's Box a rencontré une erreur...", 1, (255,255,255))
        fenetre.blit(texte, (10, 60))
        texte = font.render("L'anomalie peut avoir été engendrée par un fichier manquant, ou un défaut de codage.", 1, (255,255,255))
        fenetre.blit(texte, (10, 100))
        texte = font.render("Dans ce dernier cas, relancez le programme et contactez MINI Picture. Un correctif sera", 1, (255,255,255))
        fenetre.blit(texte, (10, 140))
        texte = font.render("publié dans les plus brefs délais pour corriger le problème.", 1, (255,255,255))
        fenetre.blit(texte, (10, 180))
        texte = font.render("Pensez à consulter le fichier log.txt pour plus d'informations sur l'erreur...", 1, (255,255,255))
        fenetre.blit(texte, (10, 220))
        texte = font.render("Ce dernier devra d'ailleurs être envoyé au développeur pour une meilleure assistance.", 1, (255,255,255))
        fenetre.blit(texte, (10, 260))
        texte = font.render("Appuyez sur ENTER pour plus d'options...", 1, (255,0,0))
        fenetre.blit(texte, (10, 300))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                error_menu = True

        if event.type == QUIT:
            erreur_report = False

            STOP()
    # Menu sécurisé d'erreur (diagnostic)
    while error_menu :
        pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
        try:
            texte = font.render(langue.error_menu2_1, 5, (255,0,0))
            fenetre.blit(texte, (510, 10))
            texte = font.render(langue.error_menu2_2, 5, (255,255,255))
            fenetre.blit(texte, (10, 150))
            texte = font.render(langue.error_menu2_3, 5, (255,255,255))
            fenetre.blit(texte, (10, 250))
            texte = font.render(langue.error_menu2_4, 5, (255,255,255))
            fenetre.blit(texte, (10, 200))
            texte = font.render(langue.error_menu2_5, 5, (255,255,255))
            fenetre.blit(texte, (10, 300))
            texte = font.render(langue.error_menu2_6, 5, (255,255,255))
            fenetre.blit(texte, (10, 350))
            texte = font.render(langue.error_menu2_7, 5, (255,255,255))
            fenetre.blit(texte, (10, 400))
            texte = font.render(langue.error_menu2_8, 5, (255,255,255))
            fenetre.blit(texte, (10, 450))
            texte = font.render(langue.error_menu2_9, 5, (255,255,255))
            fenetre.blit(texte, (10, 600))
            texte = font.render(langue.error_menu2_10, 5, (255,255,255))
            fenetre.blit(texte, (300, 685))
        except:
            texte = font.render("Option d'erreur", 5, (255,0,0))
            fenetre.blit(texte, (510, 10))
            texte = font.render("Redémarrage du programme : press R", 5, (255,255,255))
            fenetre.blit(texte, (10, 150))
            texte = font.render("Utilitaire de réparation (réinitialisation complète) : press U", 5, (255,255,255))
            fenetre.blit(texte, (10, 250))
            texte = font.render("Détail de l'erreur (log file) : press L", 5, (255,255,255))
            fenetre.blit(texte, (10, 200))
            texte = font.render("Outil de vérification : press C", 5, (255,255,255))
            fenetre.blit(texte, (10, 300))
            texte = font.render("Mise à jour forcée des modules : press M (Nominal), press P (Preview)", 5, (255,255,255))
            fenetre.blit(texte, (10, 350))
            texte = font.render("Réinitialisation de la base de données : press D", 5, (255,255,255))
            fenetre.blit(texte, (10, 400))
            texte = font.render("Télécharger le fichier de mise à niveau en ligne : press W", 5, (255,255,255))
            fenetre.blit(texte, (10, 450))
            texte = font.render("Quitter : press ENTER", 5, (255,255,255))
            fenetre.blit(texte, (10, 600))
            texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
            fenetre.blit(texte, (300, 685))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    erreur_report = False
                    error_menu = False
                    STOP("Menu.bat")
                if event.key == pygame.K_u:
                    fichier=open("Update_check.py","w")
                    fichier.write('import os'+"\n")
                    fichier.write('update_del = os.listdir()'+"\n")
                    fichier.write("update_unzip = 'all'"+"\n")
                    fichier.write('update_process = ["Update.delete(update_del)", "Update.unzip(update_unzip)"]'+"\n")
                    fichier.write('update_stat = ("","")'+"\n")
                    fichier.write('after_update = "Menu"'+"\n")
                    fichier.close()
                    erreur_report = False
                    error_menu = False
                    STOP("Update.bat")
                if event.key == pygame.K_l:
                    os.startfile("log.txt")
                if event.key == pygame.K_c:
                    error_menu = False
                    error_check = True
                    check = 1
                if event.key == pygame.K_m:
                    erreur_report = False
                    error_menu = False
                    STOP("Update all.bat")
                if event.key == pygame.K_p:
                    erreur_report = False
                    error_menu = False
                    STOP("Update all(preview).bat")
                if event.key == pygame.K_w:
                    error_Thread = Thread(target=error_download_file, args=("https://drive.google.com/u/1/uc?id=1exJExVL60QBdmIfpuRZ8Bw7spw6PU-u1&export=download",))
                    error_Thread.start()
                    download_error_txt = "Téléchargement en cours..."

                    while download_error :
                        pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                        texte = font.render("Option d'erreur", 5, (255,0,0))
                        fenetre.blit(texte, (510, 10))
                        texte = font.render(download_error_txt, 5, (255,255,255))
                        fenetre.blit(texte, (10, 200))
                        texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
                        fenetre.blit(texte, (300, 685))
                        pygame.display.flip()
                        for event_none in pygame.event.get():
                            None

                if event.key == pygame.K_d:
                    fichier=open("Update_check.py","w")
                    fichier.write('update_del = ["data_base.db","Update_check.py"]'+"\n")
                    fichier.write('update_unzip = ["data_base.db","Update_check.py"]'+"\n")
                    fichier.write('update_process = ["Update.delete(update_del)", "Update.unzip(update_unzip)"]'+"\n")
                    fichier.write('update_stat = ("","")'+"\n")
                    fichier.write('after_update = "Menu"'+"\n")
                    fichier.close()
                    erreur_report = False
                    error_menu = False
                    STOP("Update.bat")

                if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                    erreur_report = False
                    error_menu = False
                    STOP()

            if event.type == QUIT:
                erreur_report = False
                error_menu = False
                STOP()

    while error_check :
        try :
            from file_list import*
            with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                None
        except :
            try:
                with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                    zipObj.extract("file_list.py")
            except :
                pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                texte = font.render("Outil de vérification", 5, (255,0,0))
                fenetre.blit(texte, (500, 10))
                texte = font.render("Analyse/réparation impossible : 'Level mise à niveau' introuvable...", 5, (255,255,255))
                fenetre.blit(texte, (10, 150))

                pygame.display.flip()

                time.sleep(3)
                error_check = False
                error_menu = True
                check = 0
                file_list_temp_c = os.listdir()
                file_list_c = []
                file_error = []
                error_count_f = 0
                error_count_m = 0
                ext_file = []
                stat = ""
                l_m = 0
                l_l = 0
                l_u = 0
                menu_stat = ""
                level_stat = ""
                update_stat = ""

        if check == 1:
            file_list_temp_c = os.listdir()
            file_list_c = []
            file_error = []
            error_count_f = 0
            error_count_m = 0
            ext_file = []
            stat = ""
            l_m = 0
            l_l = 0
            l_u = 0
            menu_stat = ""
            level_stat = ""
            update_stat = ""

            for i in file_list_temp_c:
                if os.path.isfile(i):
                    file_list_c.append(i)

                    pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                    texte = font.render("Outil de vérification", 5, (255,0,0))
                    fenetre.blit(texte, (500, 10))
                    texte = font.render("-> Scan des fichiers actuels", 5, (255,255,255))
                    fenetre.blit(texte, (10, 150))
                    texte = font.render("- Comparaison des fichiers", 5, (255,255,255))
                    fenetre.blit(texte, (10, 200))
                    texte = font.render("- Test des modules", 5, (255,255,255))
                    fenetre.blit(texte, (10, 250))
                    texte = font.render("- Analyse du programme 'Menu'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 300))
                    texte = font.render("", 5, (255,255,255))
                    fenetre.blit(texte, (10, 350))
                    texte = font.render("", 5, (255,255,255))
                    fenetre.blit(texte, (10, 400))
                    texte = font.render("", 5, (255,255,255))
                    fenetre.blit(texte, (10, 450))
                    texte = font.render(str(i), 5, (255,255,255))
                    fenetre.blit(texte, (10, 500))
                    texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
                    fenetre.blit(texte, (300, 685))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            erreur_report = False
                            error_menu = False
                            STOP()

                else :
                    for (dirpath, dirnames, filenames) in os.walk(i):
                        file_list_c += [os.path.join(dirpath, file) for file in filenames]

                        for file in filenames :
                            os.path.join(dirpath, file)

                            pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                            texte = font.render("Outil de vérification", 5, (255,0,0))
                            fenetre.blit(texte, (500, 10))
                            texte = font.render("-> Scan des fichiers actuels", 5, (255,255,255))
                            fenetre.blit(texte, (10, 150))
                            texte = font.render("- Comparaison des fichiers", 5, (255,255,255))
                            fenetre.blit(texte, (10, 200))
                            texte = font.render("- Test des modules", 5, (255,255,255))
                            fenetre.blit(texte, (10, 250))
                            texte = font.render("- Analyse du programme 'Menu'", 5, (255,255,255))
                            fenetre.blit(texte, (10, 300))
                            texte = font.render("- Analyse du programme 'Level'", 5, (255,255,255))
                            fenetre.blit(texte, (10, 350))
                            texte = font.render("- Analyse du programme 'Update'", 5, (255,255,255))
                            fenetre.blit(texte, (10, 400))

                            texte = font.render(str(file), 5, (255,255,255))
                            fenetre.blit(texte, (10, 500))
                            texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
                            fenetre.blit(texte, (300, 685))

                            pygame.display.flip()

                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    erreur_report = False
                                    error_menu = False
                                    STOP()

            try :
                for i in file_list :
                    if i in file_list_c:
                        file_list_c.remove(i)
                    else:
                        file_error.append(i)
                        error_count_f += 1

                    pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                    texte = font.render("Outil de vérification", 5, (255,0,0))
                    fenetre.blit(texte, (500, 10))
                    texte = font.render("- Scan des fichiers actuels", 5, (255,255,255))
                    fenetre.blit(texte, (10, 150))
                    texte = font.render("-> Comparaison des fichiers", 5, (255,255,255))
                    fenetre.blit(texte, (10, 200))

                    texte = font.render("occurence(s) : " + str(error_count_f), 5, (255,255,255))
                    fenetre.blit(texte, (530, 200))

                    texte = font.render("- Test des modules", 5, (255,255,255))
                    fenetre.blit(texte, (10, 250))
                    texte = font.render("- Analyse du programme 'Menu'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 300))
                    texte = font.render("- Analyse du programme 'Level'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 350))
                    texte = font.render("- Analyse du programme 'Update'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 400))

                    texte = font.render(i, 5, (255,255,255))
                    fenetre.blit(texte, (10, 500))

                    texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
                    fenetre.blit(texte, (300, 685))

                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            erreur_report = False
                            error_menu = False
                            STOP()

            except :
                pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                texte = font.render("Outil de vérification", 5, (255,0,0))
                fenetre.blit(texte, (500, 10))
                texte = font.render("Comparaison impossible : le fichier 'file_list.py' va être réinstallé... Réessayez...", 5, (255,255,255))
                fenetre.blit(texte, (10, 150))

                pygame.display.flip()

                time.sleep(3)
                error_check = False
                error_menu = True
                check = 0
                file_list_temp_c = os.listdir()
                file_list_c = []
                file_error = []
                error_count_f = 0
                error_count_m = 0
                ext_file = []
                stat = ""
                l_m = 0
                l_l = 0
                l_u = 0
                menu_stat = ""
                level_stat = ""
                update_stat = ""

                try :
                    with ZipFile('Level mise à niveau.zip', 'r') as zipObj:
                        zipObj.extract("file_list.py")
                except :
                    None
                break

            for file in file_list_temp_c :
                if file.endswith(".py"):
                    file_test = file[:-3]
                    try :
                        __import__(str(file_test))
                        stat = "OK"
                    except:
                        stat = "ERROR"
                        error_count_m += 1
                        file_error.append(file)

                    pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
                    texte = font.render("Outil de vérification", 5, (255,0,0))
                    fenetre.blit(texte, (500, 10))
                    texte = font.render("- Scan des fichiers actuels", 5, (255,255,255))
                    fenetre.blit(texte, (10, 150))
                    texte = font.render("- Comparaison des fichiers", 5, (255,255,255))
                    fenetre.blit(texte, (10, 200))

                    texte = font.render("occurence(s) : " + str(error_count_f), 5, (255,255,255))
                    fenetre.blit(texte, (530, 200))

                    texte = font.render("-> Test des modules", 5, (255,255,255))
                    fenetre.blit(texte, (10, 250))

                    texte = font.render("occurence(s) : " + str(error_count_m), 5, (255,255,255))
                    fenetre.blit(texte, (530, 250))

                    texte = font.render("- Analyse du programme 'Menu'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 300))
                    texte = font.render("- Analyse du programme 'Level'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 350))
                    texte = font.render("- Analyse du programme 'Update'", 5, (255,255,255))
                    fenetre.blit(texte, (10, 400))

                    texte = font.render(str(file), 5, (255,255,255))
                    fenetre.blit(texte, (10, 450))
                    texte = font.render("Statut : " + stat, 5, (255,255,255))
                    fenetre.blit(texte, (10, 500))
                    texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
                    fenetre.blit(texte, (300, 685))

                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        erreur_report = False
                        error_menu = False
                        STOP()

            try :

                with open("Menu_test.pyw", "rb") as f:
                    file_used = hashlib.file_digest(f, "sha256")

                with open("Menu.pyw", "rb") as f:
                    file_ref = hashlib.file_digest(f, "sha256")

                if file_used.hexdigest() != file_ref.hexdigest():
                    menu_stat = "endommagé"
                else:
                    menu_stat = "opérationnel"

            except:
                menu_stat = "inconnu"
                file_error.append("Menu_test.pyw")
                file_error.append("Menu.pyw")

            if menu_stat == "endommagé":
                file_error.append("Menu_test.pyw")
                file_error.append("Menu.pyw")

            try :

                with open("Level_test.pyw", "rb") as f:
                    file_used = hashlib.file_digest(f, "sha256")

                with open("Level.pyw", "rb") as f:
                    file_ref = hashlib.file_digest(f, "sha256")

                if file_used.hexdigest() != file_ref.hexdigest():
                    level_stat = "endommagé"
                else:
                	level_stat = "opérationnel"

            except:
                level_stat = "inconnu"
                file_error.append("Level_test.pyw")
                file_error.append("Level.pyw")

            if level_stat == "endommagé":
                file_error.append("Level_test.pyw")
                file_error.append("Level.pyw")

            try :
                with open("Update_test.pyw", "rb") as f:
                    file_used = hashlib.file_digest(f, "sha256")

                with open("Update.pyw", "rb") as f:
                    file_ref = hashlib.file_digest(f, "sha256")

                if file_used.hexdigest() != file_ref.hexdigest():
                    update_stat = "endommagé"
                else:
                    update_stat = "opérationnel"

            except:
                update_stat = "inconnu"
                file_error.append("Update_test.pyw")
                file_error.append("Update.pyw")

            if update_stat == "endommagé":
                file_error.append("Update_test.pyw")
                file_error.append("Update.pyw")

            check = 0

            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            fichier=open("log.txt","a")
            if os.stat("log.txt").st_size == 0:
                fichier.write("________  __     __  __      ___     ________      _____      __  __" + "\n")
                fichier.write("| |     \ | |\   | | | |    /___/    | |     \    / ___ \     \ \/ /." + "\n")
                fichier.write("| |     | | | \  | | | |             | |     |   / /   \ \     \ \/.  " + "\n")
                fichier.write("| |_____/ | |\ \ | | | |             | |_____/  / /     \ \     \ \. " + "\n")
                fichier.write("| |     \ | | \ \| | | |             | |     \  \ \     / /    / \ \." + "\n")
                fichier.write("| |     | | |  \   | | |____         | |     |   \ \___/ /    / / \ \." + "\n")
                fichier.write("|_|_____/ |_|   \__| |______|        |_|_____/    \_____/    /_/   \_\." + "\n")
                fichier.write("\n")  
            fichier.write(str(dt_string) +"\n")
            fichier.write("Compte-rendu de l'outil de verification integre, BNL's Box Security mode : "+"\n")
            fichier.write("\n")
            if file_error == []:
                fichier.write("Aucun fichier endommage trouve..."+"\n")
            else:
                fichier.write("Fichiers endommages :"+"\n")
                fichier.write("\n")
                for i in file_error:
                    fichier.write(i+"\n")
            fichier.write("\n")
            fichier.close()

        pygame.draw.rect(fenetre, (0,0,150), pygame.Rect(0,0,1280,720))
        texte = font.render("Outil de vérification", 5, (255,0,0))
        fenetre.blit(texte, (500, 10))
        texte = font.render("- Scan des fichiers actuels", 5, (255,255,255))
        fenetre.blit(texte, (10, 150))
        texte = font.render("- Comparaison des fichiers", 5, (255,255,255))
        fenetre.blit(texte, (10, 200))

        texte = font.render("occurence(s) : " + str(error_count_f), 5, (255,255,255))
        fenetre.blit(texte, (530, 200))

        texte = font.render("- Test des modules", 5, (255,255,255))
        fenetre.blit(texte, (10, 250))

        texte = font.render("occurence(s) : " + str(error_count_m), 5, (255,255,255))
        fenetre.blit(texte, (530, 250))

        texte = font.render("- Analyse du programme 'Menu'", 5, (255,255,255))
        fenetre.blit(texte, (10, 300))

        texte = font.render("état : " + menu_stat, 5, (255,255,255))
        fenetre.blit(texte, (530, 300))

        texte = font.render("- Analyse du programme 'Level'", 5, (255,255,255))
        fenetre.blit(texte, (10, 350))

        texte = font.render("état : " + level_stat, 5, (255,255,255))
        fenetre.blit(texte, (530, 350))

        texte = font.render("- Analyse du programme 'Update'", 5, (255,255,255))
        fenetre.blit(texte, (10, 400))

        texte = font.render("état : " + update_stat, 5, (255,255,255))
        fenetre.blit(texte, (530, 400))

        if error_count_f == 0 and error_count_m == 0 and menu_stat == "opérationnel" and level_stat == "opérationnel" and update_stat == "opérationnel":
            texte = font.render("Aucun problème détecté...", 5, (255,255,255))
            fenetre.blit(texte, (10, 450))
        else :
            texte = font.render("Erreur(s) détectée(s) : press U for launch Repair Tool", 5, (255,255,255))
            fenetre.blit(texte, (10, 500))

        texte = font.render("", 5, (255,255,255))
        fenetre.blit(texte, (10, 500))
        texte = font.render("Press ENTER to continue", 5, (255,255,255))
        fenetre.blit(texte, (10, 570))
        texte = font.render("Mini Picture : BNL's Box error and recovery mode", 5, (255,255,255))
        fenetre.blit(texte, (300, 685))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_KP_ENTER or  event.key == pygame.K_RETURN:
                    error_menu = True
                    error_check = False

                if event.key == pygame.K_u:
                    char_to_replace = {'\\': '/'}
                    for i in range(len(file_error)):
                        file_error[i] = file_error[i].translate(str.maketrans(char_to_replace))

                    fichier=open("Update_check.py","w")
                    file_error.append("Update_check.py")
                    fichier.write(f'update_unzip = {str(file_error)}'+"\n")
                    fichier.write('update_process = ["Update.unzip(update_unzip)"]'+"\n")
                    fichier.write('update_stat = ("","")'+"\n")
                    fichier.write('after_update = "Menu"'+"\n")

                    fichier.close()

                    erreur_report = False
                    error_menu = False
                    error_check = False
                    STOP("Update.bat")

            if event.type == QUIT:
                erreur_report = False
                error_menu = False
                error_check = False
                STOP()