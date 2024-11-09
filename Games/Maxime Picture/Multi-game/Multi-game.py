#Importation des bibliothèques
import pygame
import math
import random
from pygame.locals import *
#Préparation du chargement
def chargement(nom_chargement):
    '''Initialisation de la fenêtre'''
    pygame.init()
    '''Taille de la police'''
    font = pygame.font.Font("police.ttf", 10)
    '''Taille de la fenêtre'''
    fenêtre = pygame.display.set_mode((300,100))
    '''Couleurs'''
    couleur_fond_chargement=(0,0,0)
    couleur_chargement=(255,255,255)
    couleur_barre=(0,150,255)
    '''Barre vide + fond'''
    pygame.draw.rect(fenêtre,couleur_fond_chargement,pygame.Rect(0,0,300,100))
    pygame.draw.rect(fenêtre,couleur_chargement,pygame.Rect(49,29,202,42))
    pygame.draw.rect(fenêtre,couleur_fond_chargement,pygame.Rect(52,32,196,36))
    '''Texte du chargement pour tous'''
    texte_chargement= font.render("Chargement", 1, (255,255,255))
    '''Précision du chargement'''
    texte_chargement2= font.render(nom_chargement, 1, (255,255,255))
    '''Affichage du fond et du texte'''
    fenêtre.blit(texte_chargement,(55,5))
    fenêtre.blit(texte_chargement2,(135,5))
    '''Rafraîchisement de l'écran'''
    pygame.display.flip()
    '''Coordonées X du début de la barre'''
    charge_barre=52
    '''Boucle du remplissage de la barre'''
    for i in range(196):
        '''Chargement'''
        pygame.draw.rect(fenêtre,couleur_barre,pygame.Rect(charge_barre,32,1,36))
        '''Rafraîchisement de l'écran'''
        pygame.display.flip()
        '''Avancement de la barre'''
        charge_barre+=1
        '''Délai du chargement'''
        pygame.time.delay(random.randint(0,5))
    '''Arrêt du chargement'''
    pygame.quit()
#Gestion du Menu principal
def Menu_principal():
    '''Variables'''
    Menu_principal_actif=True
    selection=1
    Validation=False
    changement=True
    '''Couleur contours'''
    couleur_contours=(0,150,255)
    '''Hitboxes boutons'''
    Bouton_puissance=Rect(((25,45),(260,50)))
    Bouton_quitter=Rect(((25,135),(260,50)))
    chargement(" du menu principal...")
    pygame.init()
    fenêtre= pygame.display.set_mode((900,600))
    pygame.display.flip()
    Fond_puissance=pygame.image.load("Fond_puissance.png").convert_alpha()
    Fond_quitter=pygame.image.load("Fond_quitter.png").convert_alpha()
    font = pygame.font.Font("police.ttf", 30)
    #actions
    while Menu_principal_actif==True:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    Menu_principal_actif = False
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
                if event.key == K_RETURN or event.key == K_SPACE:
                    Validation=True
            elif event.type == pygame.MOUSEMOTION:
                if Bouton_quitter.collidepoint(event.pos):
                    selection=2
                    changement=True
                if Bouton_puissance.collidepoint(event.pos):
                    selection=1
                    changement=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Bouton_quitter.collidepoint(event.pos):
                    Validation=True
                if Bouton_puissance.collidepoint(event.pos):
                    Validation=True
        if Validation==True and selection==1:
            pygame.quit()
            Menu_principal_actif = False
            puissance4(couleur_contours)
        elif Validation==True and selection==2:
            pygame.quit()
            Menu_principal_actif = False
        if changement==True:
            changement=False
            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,300,600))
            pygame.draw.rect(fenêtre,(255,255,255),pygame.Rect(300,0,600,600))
            pygame.draw.rect(fenêtre,couleur_contours,pygame.Rect(20,-30+70*selection,260,60))
            pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(25,-25+70*selection,250,50))
            texte_menu1=font.render("Puissance 4", 1, (255,255,255))
            texte_menu2=font.render("Quitter", 1, (255,255,255))
            fenêtre.blit(texte_menu1,(45,55))
            fenêtre.blit(texte_menu2,(45,125))
            if selection==1:
                fenêtre.blit(Fond_puissance,(350,45))
            if selection==2:
                fenêtre.blit(Fond_quitter,(325,0))
            pygame.display.flip()
def puissance4(c1):
    chargement("du puissance 4")
    Menu_puissance=True
    selection=1
    selection2=1
    Jeu=False
    fin=False
    Validation=False
    changement=True
    couleur1=(255,0,0)
    couleur2=(255,255,0)
    couleur_ligne_de_4=(0,0,0)
    Bouton_puissance_commencer=Rect(((300,400),(370,80)))
    Bouton_puissance_quitter=Rect(((360,550),(260,80)))
    Boutonj1=Rect(((280,230),(140,140)))
    Boutonj2=Rect(((530,230),(140,140)))
    pygame.init()
    font = pygame.font.Font("police.ttf", 10)
    font_titre = pygame.font.Font("police.ttf", 50)
    font2 = pygame.font.Font("police.ttf", 30)
    fenêtre = pygame.display.set_mode((960,740))
    pygame.draw.rect(fenêtre,(255,255,255),pygame.Rect(0,0,960,740))
    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(200,20,560,700))
    pygame.draw.rect(fenêtre,c1,pygame.Rect(205,25,550,690))
    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(210,30,540,680))
    titre=font_titre.render("Puissance 4", 1, (255,255,255))
    t1=font2.render("Qui commence ?", 1, (255,255,255))
    t2=font_titre.render("Commencer", 1, (255,255,255))
    t3=font_titre.render("Quitter", 1, (255,255,255))
    t4=font_titre.render("Victoire", 1, (255,255,255))
    t5=font_titre.render("du Joueur", 1, (255,255,255))
    v1=font_titre.render("1", 1, (255,255,255))
    v2=font_titre.render("2", 1, (255,255,255))
    v3=font_titre.render("Egalité", 1, (255,255,255))
    fenêtre.blit(titre,(300,50))
    fenêtre.blit(t1,(350,150))
    fenêtre.blit(t2,(320,400))
    fenêtre.blit(t3,(380,550))
    pygame.display.flip()
    while Menu_puissance==True:
        for event in pygame.event.get():
            #quitter
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
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
            if Validation==True and selection==1:
                Menu_puissance = False
                Jeu=True
            if Validation==True and selection==2:
                pygame.quit()
                Menu_puissance = False
                Menu_principal()
            if changement==True:
                changement=False
                pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(280,230,450,400))
                if selection2==1:
                    pygame.draw.rect(fenêtre,c1,pygame.Rect(280,230,140,140))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(285,235,130,130))
                    joueur=1
                elif selection2==2:
                    pygame.draw.rect(fenêtre,c1,pygame.Rect(530,230,140,140))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(535,235,130,130))
                    joueur=2
                if selection==1:
                    pygame.draw.rect(fenêtre,c1,pygame.Rect(300,400,370,80))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(305,405,360,70))
                elif selection==2:
                    pygame.draw.rect(fenêtre,c1,pygame.Rect(360,550,260,80))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(365,555,250,70))
                pygame.draw.circle(fenêtre,couleur1, (350,300),50,0)
                pygame.draw.circle(fenêtre,couleur2, (600,300),50,0)
                fenêtre.blit(t2,(320,400))
                fenêtre.blit(t3,(380,550))
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
        Colone1=Rect(((60,0),(120,740)))
        Colone2=Rect(((180,0),(120,740)))
        Colone3=Rect(((300,0),(120,740)))
        Colone4=Rect(((420,0),(120,740)))
        Colone5=Rect(((540,0),(120,740)))
        Colone6=Rect(((660,0),(120,740)))
        Colone7=Rect(((780,0),(120,740)))
        while Jeu==True:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
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
            if changement_puissance==True:
                changement_puissance=False
                pygame.draw.rect(fenêtre,(0,0,255),pygame.Rect(0,0,960,740))
                for i in range(7):
                    for i in range(6):
                     for j in range(7):
                            if grille[i][j]==0:
                                pygame.draw.circle(fenêtre,(255,255,255), (120+j*120,70+i*120),50,0)
                            elif grille[i][j]==1:
                                pygame.draw.circle(fenêtre,couleur1, (120+j*120,70+i*120),50,0)
                            elif grille[i][j]==5:
                                pygame.draw.circle(fenêtre,couleur2, (120+j*120,70+i*120),50,0)
                b=emplacements[case]
                if b!=-1:
                    pygame.draw.circle(fenêtre,c1, (120+case*120,70+b*120),25,0)
                    if joueur==1:
                        pygame.draw.circle(fenêtre,couleur1, (120+case*120,70+b*120),15,0)
                    else:
                        pygame.draw.circle(fenêtre,couleur2, (120+case*120,70+b*120),15,0)
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
                    pygame.draw.circle(fenêtre,c1, (120+case*120,70+b*120),25,0)
                    if joueur==1:
                        pygame.draw.circle(fenêtre,couleur1, (120+case*120,70+b*120),15,0)
                    else:
                        pygame.draw.circle(fenêtre,couleur2, (120+case*120,70+b*120),15,0)
                if bouge==True:
                    pygame.mouse.set_pos((120+120*case,70+120*b))
                bouge=False
                pygame.display.flip()
                for i in range(6):
                    for j in range(4):
                        if grille[i][j]+grille[i][j+1]+grille[i][j+2]+grille[i][j+3]==4:
                            victoire=1
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*(j+3),70+120*i),épaisseur_trait)
                            fin=True
                        elif grille[i][j]+grille[i][j+1]+grille[i][j+2]+grille[i][j+3]==20:
                            victoire=2
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*(j+3),70+120*i),épaisseur_trait)
                            fin=True
                for i in range(3):
                    for j in range(7):
                        if grille[i][j]+grille[i+1][j]+grille[i+2][j]+grille[i+3][j]==4:
                            victoire=1
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*j,70+120*(i+3)),épaisseur_trait)
                            fin=True
                        elif grille[i][j]+grille[i+1][j]+grille[i+2][j]+grille[i+3][j]==20:
                            victoire=2
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*j,70+120*(i+3)),épaisseur_trait)
                            fin=True
                for i in range(3):
                    for j in range(4):
                        if grille[i][j]+grille[i+1][j+1]+grille[i+2][j+2]+grille[i+3][j+3]==4:
                            victoire=1
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*(j+3),70+120*(i+3)),épaisseur_trait)
                            fin=True
                        elif grille[i][j]+grille[i+1][j+1]+grille[i+2][j+2]+grille[i+3][j+3]==20:
                            victoire=2
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*(j+3),70+120*(i+3)),épaisseur_trait)
                            fin=True
                for i in range(3):
                    for j in range(3,7):
                        if grille[i][j]+grille[i+1][j-1]+grille[i+2][j-2]+grille[i+3][j-3]==4:
                            victoire=1
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*(j-3),70+120*(i+3)),épaisseur_trait)
                            fin=True
                        elif grille[i][j]+grille[i+1][j-1]+grille[i+2][j-2]+grille[i+3][j-3]==20:
                            victoire=2
                            pygame.draw.line(fenêtre,couleur_ligne_de_4,(120+120*j,70+120*i),(120+120*(j-3),70+120*(i+3)),épaisseur_trait)
                            fin=True
                if emplacements==[-1,-1,-1,-1,-1,-1,-1]:
                    victoire=3
                    fin=True
                if fin==True:
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    pygame.draw.rect(fenêtre,(255,255,255),pygame.Rect(0,0,960,740))
                    pygame.draw.rect(fenêtre,(0,150,255),pygame.Rect(205,25,550,690))
                    pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(210,30,540,680))
                    if victoire==1:
                        fenêtre.blit(t4,(350,150))
                        fenêtre.blit(t5,(320,200))
                        fenêtre.blit(v1,(600,200))
                        pygame.draw.circle(fenêtre,couleur1, (480,370),50,0)
                    elif victoire==2:
                        fenêtre.blit(t4,(350,150))
                        fenêtre.blit(t5,(320,200))
                        fenêtre.blit(v2,(600,200))
                        pygame.draw.circle(fenêtre,couleur2, (480,370),50,0)
                    elif victoire==3:
                        fenêtre.blit(v3,(320,200))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    pygame.quit()
                    Jeu=False
                    puissance4(c1)





Menu_principal()

