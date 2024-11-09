#Project T.A.N.K.S.
##########################################################################
#bibliothèques
import pygame
from math import *
import random as rn
from pygame.locals import *
from PIL import Image
import time
import sys
import socket
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
            balle=Bullet(pygame.image.load("bullet_r.png").convert_alpha(),self.rec[0]+self.rec[2]/2-4,self.rec[1]+self.rec[3]/2-4,self.dir,1,self.vit_bul,self.fe)
            self.ammo-=1
            bullets.append(balle)
        elif self.id==2 and self.ammo!=0:
            balle=Bullet(pygame.image.load("bullet_b.png").convert_alpha(),self.rec[0]+self.rec[2]/2-4,self.rec[1]+self.rec[3]/2-4,self.dir,2,self.vit_bul,self.fe)
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
                s=particles("par_2.png",self.x,self.y,self.fe)
                particules.append(s)
            bullets.pop(l)
        if self.id==2 and pygame.Rect.colliderect(self.rec,t1.rec):
            for _ in range(50):
                s=particles("par_1.png",self.x,self.y,self.fe)
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
                s=particles("par_0.png",self.x,self.y,self.fe)
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
    list_up=["Santé.png","deg.png","Vroum.png"]
    l_up=[]
    touches=[K_s,K_DOWN,K_q,K_d,K_LEFT,K_a,K_RIGHT]
    selec=1
    for _ in range(3):
        up=rn.randint(0,2)
        l_up.append(up)
    fenêtre.blit(pygame.image.load("Fond_Menu.png").convert_alpha(),(5,5))
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
        fenêtre.blit(pygame.image.load("Fond_Menu.png").convert_alpha(),(5,5))
        fenêtre.blit(pygame.image.load(list_up[l_up[0]]).convert_alpha(),(95,100))
        fenêtre.blit(pygame.image.load(list_up[l_up[1]]).convert_alpha(),(490,100))
        fenêtre.blit(pygame.image.load(list_up[l_up[2]]).convert_alpha(),(885,100))
        fenêtre.blit(pygame.image.load("curseur.png").convert_alpha(),(selec*395+225,25))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==touches[tank.id-1]:
                    upgrade_en_cours=False
                    if list_up[l_up[selec]]=="Santé.png":
                        tank.vie = tank.vie*2
                    elif list_up[l_up[selec]]=="deg.png":
                        tank.deg = tank.deg*1.7
                    elif list_up[l_up[selec]]=="Vroum.png":
                        tank.vit = tank.vit*1.3
                        tank.vit_rot = tank.vit_rot*0.8
                if event.key==touches[tank.id*2] or (tank.id==1 and touches[5]==event.key):
                    if selec!=0:
                        selec-=1
                if event.key==touches[tank.id*3]:
                    if selec!=2:
                        selec+=1
################################################################################################
#Menu

def menu():
    #initialisation fenêtre
    Stats_base=lecture("Valeurs")
    fullscreen=False
    nb_manche=5
    selection_menu=0
    menu_en_cours=True
    pygame.init()
    font = pygame.font.Font("police.ttf", 50)
    couleur_menu=(0,150,250)
    fenêtre=pygame.display.set_mode((1280,720))
    pygame.display.set_caption("T.A.N.K.S.1.0")
    fond=pygame.image.load("Fond_menu.png").convert_alpha()
    pygame.mouse.set_visible(False)
    #boucle menu
    while menu_en_cours:
        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
        fenêtre.blit(fond,(5,5))
        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(380,240+selection_menu*100,485,5))
        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(380,328+selection_menu*100,485,5))
        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(380,240+selection_menu*100,5,93))
        pygame.draw.rect(fenêtre,couleur_menu,pygame.Rect(865,240+selection_menu*100,5,93))
        fenêtre.blit(font.render("Jouer en Local",1,(0,0,0)),(410,250))
        fenêtre.blit(font.render("Jouer en Réseau",1,(0,0,0)),(390,350))
        fenêtre.blit(font.render("Paramètres",1,(0,0,0)),(450,450))
        fenêtre.blit(font.render("Quitter",1,(0,0,0)),(500,550))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                    pygame.quit()
                    menu_en_cours=False
                    ecriture("Valeurs",Stats_base)
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    menu_en_cours=False
                    ecriture("Valeurs",Stats_base)
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
                        pygame.quit()
                        menu_en_cours=False
                        ecriture("Valeurs",Stats_base)
                if event.key==K_F11:
                    if not fullscreen:
                        fenêtre=pygame.display.set_mode((1280,720),FULLSCREEN)
                        fullscreen=True
                    else:
                        fenêtre=pygame.display.set_mode((1280,720))
                        fullscreen=False
##########################################################################################################
#Paramètres
def options(full,fenêtre):
    stats=lecture("Valeurs")
    option_en_cours=True
    fond=pygame.image.load("Fond_menu.png").convert_alpha()
    font = pygame.font.Font("police.ttf", 50)
    pygame.mouse.set_visible(True)
    while option_en_cours:
        pygame.draw.rect(fenêtre,(0,0,0),pygame.Rect(0,0,1280,720))
        fenêtre.blit(fond,(5,5))
        fenêtre.blit(font.render("Manches :  "+str(stats[0]),1,(0,0,0)),(10,10))
        fenêtre.blit(font.render("Vit déplacements :  "+str(stats[1]),1,(0,0,0)),(10,70))
        fenêtre.blit(font.render("Vit rotation :  "+str(stats[2]),1,(0,0,0)),(10,130))
        fenêtre.blit(font.render("Vie :  "+str(stats[3]),1,(0,0,0)),(10,190))
        fenêtre.blit(font.render("Munitions :  "+str(stats[4]),1,(0,0,0)),(10,250))
        fenêtre.blit(font.render("Dégats :  "+str(stats[5]),1,(0,0,0)),(10,320))
        fenêtre.blit(font.render("Vit balles :  "+str(stats[6]),1,(0,0,0)),(10,390))
        fenêtre.blit(font.render("Vit rechargement :  "+str(stats[7]),1,(0,0,0)),(10,460))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                    option_en_cours=False
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    option_en_cours=False
    pygame.mouse.set_visible(False)
    ecriture("Valeurs",stats)

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
    score=[0,0]
    partie=True
    fond=pygame.image.load("Fond_3.png").convert_alpha()
    cd1=time.time()
    cd2=time.time()
    properties=lecture("Valeurs")
    font = pygame.font.Font("police.ttf", 20)
    buisson=pygame.image.load("buisson.png").convert_alpha()
    sapin=pygame.image.load("sapin.png").convert_alpha()
    clock = pygame.time.Clock()
    #variables
    full=not(full)
    end=0
    if not full:
        fenêtre=pygame.display.set_mode((1280,720),FULLSCREEN)
        full=True
    else:
        fenêtre=pygame.display.set_mode((1280,720))
        full=False
    #création tank
    tank1=Tank(100,100,-90,pygame.image.load("char_r.png").convert_alpha(),1,properties[1],properties[2],properties[3],properties[4],properties[5],properties[6],properties[7],fenêtre)
    tank2=Tank(1180,620,90,pygame.image.load("char_b.png").convert_alpha(),2,properties[1],properties[2],properties[3],properties[4],properties[5],properties[6],properties[7],fenêtre)
    while partie:
        print(score)
        en_cours=True
        while en_cours:
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
            fenêtre.blit(pygame.transform.scale(pygame.image.load("bullet_r.png").convert_alpha(),(10,24)),(30,660))
            fenêtre.blit(font.render("X",1,(0,0,0)),(42,655))
            fenêtre.blit(font.render(str(int(tank1.ammo)),1,(0,0,0)),(60,655))
            fenêtre.blit(pygame.transform.scale(pygame.image.load("bullet_b.png").convert_alpha(),(10,24)),(1185,660))
            fenêtre.blit(font.render("X",1,(0,0,0)),(1197,655))
            fenêtre.blit(font.render(str(int(tank2.ammo)),1,(0,0,0)),(1215,655))
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
                    ecriture("Valeurs",lecture("Valeurs"))
                    en_cours=False
                    partie=False
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        ecriture("Valeurs",lecture("Valeurs"))
                        en_cours=False
                        partie=False
                    if event.key==K_F11:
                        if not full:
                            fenêtre=pygame.display.set_mode((1280,720),FULLSCREEN)
                            full=True
                        else:
                            fenêtre=pygame.display.set_mode((1280,720))
                            full=False
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
                    fenêtre.blit(pygame.transform.scale(pygame.image.load("bullet_r.png").convert_alpha(),(10,24)),(30,660))
                    fenêtre.blit(font.render("X",1,(0,0,0)),(42,655))
                    fenêtre.blit(font.render(str(int(tank1.ammo)),1,(0,0,0)),(60,655))
                    fenêtre.blit(pygame.transform.scale(pygame.image.load("bullet_b.png").convert_alpha(),(10,24)),(1185,660))
                    fenêtre.blit(font.render("X",1,(0,0,0)),(1197,655))
                    fenêtre.blit(font.render(str(int(tank2.ammo)),1,(0,0,0)),(1215,655))
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
                    particules.append(particles("par_3.png",tank1.x,tank1.y,fenêtre))
                for _ in range(100):
                    particules.append(particles("par_4.png",tank1.x,tank1.y,fenêtre))
                for _ in range(100):
                    particules.append(particles("par_5.png",tank1.x,tank1.y,fenêtre))
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
                    fenêtre.blit(pygame.transform.scale(pygame.image.load("bullet_r.png").convert_alpha(),(10,24)),(30,660))
                    fenêtre.blit(font.render("X",1,(0,0,0)),(42,655))
                    fenêtre.blit(font.render(str(int(tank1.ammo)),1,(0,0,0)),(60,655))
                    fenêtre.blit(pygame.transform.scale(pygame.image.load("bullet_b.png").convert_alpha(),(10,24)),(1185,660))
                    fenêtre.blit(font.render("X",1,(0,0,0)),(1197,655))
                    fenêtre.blit(font.render(str(int(tank2.ammo)),1,(0,0,0)),(1215,655))
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
                    particules.append(particles("par_3.png",tank2.x,tank2.y,fenêtre))
                for _ in range(100):
                    particules.append(particles("par_4.png",tank2.x,tank2.y,fenêtre))
                for _ in range(100):
                    particules.append(particles("par_5.png",tank2.x,tank2.y,fenêtre))
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
                ecriture("Valeurs",lecture("Valeurs"))
                partie=False
                en_cours=False
        clock.tick(60)
########################################################################################################
menu()