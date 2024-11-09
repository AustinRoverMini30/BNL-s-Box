# Créé par Nicolas, le 08/12/2021 en Python 3.7
import os
import time
import pygame
from zipfile import ZipFile
import sys
import shutil
import datetime

update_reset_stat = False

time.sleep(2)

try :
    from Update_check import*
    from Version_Update import*
    try:
        if update_stat[0] == "update" and Update_Update != Version_Update:
            update = "update"
            update_reset_stat = True
        elif Cible_f == [] and Cible_d == [] and Cible_f_only_suppr == [] and Cible_d_only_suppr == [] and Cible_f_only_extract == [] and Cible_d_only_extract == []:
            update = "full"
        else :
            update = "part"
    except:
        if Cible_f == [] and Cible_d == [] and Cible_f_only_suppr == [] and Cible_d_only_suppr == [] and Cible_f_only_extract == [] and Cible_d_only_extract == []:
            update = "full"
        else :
            update = "part"
except :
        update = "full"

try:
    # Initialisation de la bibliothèque Pygame
    pygame.init()
    # Création de la fenêtre
    fenetre = pygame.display.set_mode((500,200))

    cadre = pygame.image.load("progress.png").convert_alpha()

    fenetre.blit(cadre,(75,50))
    pygame.display.flip()

    if update == "update":

        with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
            progress = 333
            try :
                os.remove("Update.pyw")
                os.remove("Update_test.pyw")
                os.remove("Version_Update.py")
            except:
                None

            pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
            fenetre.blit(cadre,(75,50))

            pygame.draw.rect(fenetre, (255,255,255), pygame.Rect(84,60, progress, 80))

            font = pygame.font.Font(None, 40)
            texte = font.render("Mise à jour d'Update", 1, (0,0,0))
            fenetre.blit(texte, (100, 75))

            for event in pygame.event.get():
                None

            pygame.display.flip()

            zipObject.extract("Update.pyw")
            zipObject.extract("Update_test.pyw")
            zipObject.extract("Version_Update.py")
            for event in pygame.event.get():
                None
            font = pygame.font.Font(None, 40)
            texte = font.render("OK", 1, (255,255,255))
            fenetre.blit(texte, (450, 10))
            pygame.display.flip()

        time.sleep(1)

    if update == "part":
        try:
            progress = 0

            for indice in Cible_d_only_suppr:

                shutil.rmtree(indice)

                font = pygame.font.Font(None, 40)
                texte = font.render("Suppression en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))

                progress += (333/(len(Cible_d_only_suppr)))
                for event in pygame.event.get():
                    None
                color = (0,0,255)
                pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                pygame.display.flip()

                font = pygame.font.Font(None, 40)
                texte = font.render("OK", 1, (255,255,255))
                fenetre.blit(texte, (450, 10))
                progress = 0
                i = 0

            for indice in Cible_f_only_suppr:

                os.remove(indice)

                font = pygame.font.Font(None, 40)
                texte = font.render("Suppression en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))

                progress += (333/(len(Cible_f_only_suppr)))
                for event in pygame.event.get():
                    None
                color = (0,0,255)
                pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                pygame.display.flip()

                font = pygame.font.Font(None, 40)
                texte = font.render("OK", 1, (255,255,255))
                fenetre.blit(texte, (450, 10))
                progress = 0
                i = 0

            for indice in Cible_d:

                shutil.rmtree(indice)

                font = pygame.font.Font(None, 40)
                texte = font.render("Suppression en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))

                progress += (333/(len(Cible_d)))
                for event in pygame.event.get():
                    None
                color = (0,0,255)
                pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                pygame.display.flip()

                font = pygame.font.Font(None, 40)
                texte = font.render("OK", 1, (255,255,255))
                fenetre.blit(texte, (450, 10))
            progress = 0
            i = 0

            for indice in Cible_d :

                pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
                fenetre.blit(cadre,(75,50))
                font = pygame.font.Font(None, 40)
                texte = font.render("Extraction en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))
                pygame.display.flip()

                zip_f = ZipFile("Level mise à niveau.zip")
                liste = []

                for f in zip_f.namelist():
                    zinfo = zip_f.getinfo(f)
                    if(zinfo.is_dir()):
                        liste.append(zinfo)

                with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
                    listOfFileNames = zipObject.namelist()
                    for fileName in listOfFileNames:
                        if fileName[0:(len(indice))] == indice :
                            zipObject.extract(fileName)

                        progress += (333/(len(listOfFileNames)-3))
                        for event in pygame.event.get():
                            None
                        color = (0,0,255)
                        pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                        pygame.display.flip()

                progress = 0
                i = 0

            for indice in Cible_f_only_extract :

                pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
                fenetre.blit(cadre,(75,50))
                font = pygame.font.Font(None, 40)
                texte = font.render("Extraction en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))
                with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
                    zipObject.extract(indice)
                    progress += (333/(len(Cible_f_only_extract)))
                    for event in pygame.event.get():
                        None
                    color = (0,0,255)
                    pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                    pygame.display.flip()

            progress = 0
            i = 0

            for indice in Cible_d_only_extract :
                pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
                fenetre.blit(cadre,(75,50))
                font = pygame.font.Font(None, 40)
                texte = font.render("Extraction en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))
                pygame.display.flip()

                zip_f = ZipFile("Level mise à niveau.zip")
                liste = []

                for f in zip_f.namelist():
                    zinfo = zip_f.getinfo(f)
                    if(zinfo.is_dir()):
                        liste.append(zinfo)

                with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
                    listOfFileNames = zipObject.namelist()
                    for fileName in listOfFileNames:
                        if fileName[0:(len(indice))] == indice :
                            zipObject.extract(fileName)

                        progress += (333/(len(listOfFileNames)-3))
                        for event in pygame.event.get():
                            None
                        color = (0,0,255)
                        pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                        pygame.display.flip()

                progress = 0
                i = 0

            for indice in Cible_f:

                test = os.listdir()
                with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
                    listOfFileNames = zipObject.namelist()
                progress = 0

                try:
                    os.remove(indice)
                except:
                    None

                pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
                fenetre.blit(cadre,(75,50))

                font = pygame.font.Font(None, 40)
                texte = font.render("Suppression en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))

                progress += (333/(len(test)-3))
                for event in pygame.event.get():
                    None
                color = (0,0,255)
                pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                pygame.display.flip()

                font = pygame.font.Font(None, 40)
                texte = font.render("OK", 1, (255,255,255))
                fenetre.blit(texte, (450, 10))
                progress = 0
                i = 0

                pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
                fenetre.blit(cadre,(75,50))
                font = pygame.font.Font(None, 40)
                texte = font.render("Extraction en cours...", 1, (255,255,255))
                fenetre.blit(texte, (95, 10))
                pygame.display.flip()
                with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
                    listOfFileNames = zipObject.namelist()
                    for fileName in listOfFileNames:
                        if fileName == indice :
                            zipObject.extract(fileName)
                        progress += (333/(len(listOfFileNames)-3))
                        for event in pygame.event.get():
                            None
                        color = (0,0,255)
                        pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                        pygame.display.flip()
        except Exception as e:
            print(e)

    if update == "full":

        test = os.listdir()
        with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
            listOfFileNames = zipObject.namelist()
        i = 0
        progress = 0

        while i < len(test):

            font = pygame.font.Font(None, 40)
            texte = font.render("Suppression en cours...", 1, (255,255,255))
            fenetre.blit(texte, (95, 10))

            if test[i] != "Update.pyw" and test[i] != "Level mise à niveau.zip" and test[i] != "progress.png" and test[i] != "Level Update Utility":
                try:
                    shutil.rmtree(test[i])
                except NotADirectoryError :
                    os.remove(test[i])
                progress += (333/(len(test)-3))
                for event in pygame.event.get():
                    None
                color = (0,0,255)
                pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                pygame.display.flip()

            i += 1

        font = pygame.font.Font(None, 40)
        texte = font.render("OK", 1, (255,255,255))
        fenetre.blit(texte, (450, 10))

        time.sleep(1)
        progress = 0
        i = 0

        pygame.draw.rect(fenetre, (0,0,0), pygame.Rect(0,0,500,200))
        fenetre.blit(cadre,(75,50))
        font = pygame.font.Font(None, 40)
        texte = font.render("Extraction en cours...", 1, (255,255,255))
        fenetre.blit(texte, (95, 10))
        pygame.display.flip()
        with ZipFile('Level mise à niveau.zip', 'r') as zipObject:
            listOfFileNames = zipObject.namelist()
            for fileName in listOfFileNames:
                zipObject.extract(fileName)
                progress += (333/(len(listOfFileNames)-3))
                for event in pygame.event.get():
                    None
                color = (0,0,255)
                pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
                pygame.display.flip()

    color = (0,255,0)
    pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
    font = pygame.font.Font(None, 40)
    texte = font.render("OK", 1, (255,255,255))
    fenetre.blit(texte, (450, 75))

    font = pygame.font.Font(None, 40)
    texte = font.render("Update success !", 1, (255,255,255))
    fenetre.blit(texte, (95, 160))

    pygame.display.flip()

    time.sleep(1)
    try :
        if update_stat[1] == "restart" and update_reset_stat:
            os.startfile("Update.bat")
            pygame.quit()
        elif after_update == "Menu":
            os.startfile("Menu.bat")
            pygame.quit()
    except :
        pygame.quit()

except Exception as e:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    fichier=open("log.txt","a")
    fichier.write(str(dt_string) +"\n")
    fichier.write(str(e)+"\n")
    fichier.write("Localisation : BNL's Update Utility" +"\n")
    fichier.write("\n")
    fichier.close()
    color = (255,0,0)
    pygame.draw.rect(fenetre, color, pygame.Rect(84,60, progress, 80))
    font = pygame.font.Font(None, 40)
    texte = font.render("X", font,(255,0,0))
    fenetre.blit(texte, (450, 10))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()