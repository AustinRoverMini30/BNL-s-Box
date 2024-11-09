# Créé par Nicolas, le 21/04/2023 en Python 3.7

# Menu soundtrack ou lecteur multimédia (présent depuis le cycle 2.0)
while soundtrack:

    étape_programme = "Soundtrack"
    if AdaptoRAM_check:
        if psutil.virtual_memory()[1] < RAM_free:
            animations = False
            transition_check = False

    a,b= pygame.mouse.get_pos ( )
    pygame.mixer.music.set_volume(volume/10)
    sound_viewer_pos = pygame.mixer.music.get_volume()*200

    if a > 1000 :
        if volume_control_transition_stat == 1 :
            volume_control_transition_stat = 0
            volume_control_transition("entry",0)
        volume_control = "enable"
    else :
        if volume_control_transition_stat == 0 :
            volume_control_transition_stat = 1
            volume_control_transition("out",0)
        volume_control = "disable"

    a_string=pygame.mixer.music.get_pos()/1000
    float_str = float(a_string)
    test= int(float_str)

    fenetre.blit(wallpapers_use.wallpaper, (0,0))
    g = 15
    fenetre.blit(fond_visibilité, (0,0))
    fenetre.blit(Selection_soundtrack, (0,13+18*(p)))
    """
    for i in range(38):
        texte = font_soundtrack.render(liste[i], 1, (255,255,255))
        globals() ["pos_sound_"+str(i)] = texte.get_rect(topleft=(10,g))
        fenetre.blit(texte, (10, g))
        g += 18
    """

    fenetre.blit(Soundtrack,(315,35))
    pygame.draw.rect(fenetre, (255,0,0), pygame.Rect(350,650,580, 2))
    fenetre.blit(Curseur, (325+avance, 636))

    if volume_control == "enable":
        fenetre.blit(sound_up,(1036,150))
        fenetre.blit(sound_down,(1036,450))
        fenetre.blit(sound_viewer,(1036,431-sound_viewer_pos))
    fenetre.blit(Lecture,(1136,576))
    fenetre.blit(Avancer,(1136,432))
    fenetre.blit(Reculer,(1136,288))
    fenetre.blit(Menu1,(1136,0))
    temps = 580/audio_reader_proc.time

    if not(pygame.mixer.music.get_busy()):
        fenetre.blit(Pause1,(1136,144))
        if update_at_quit:
            fenetre.blit(download_stat_downloading,(400,5))
        pygame.display.flip()
    if pygame.mixer.music.get_busy():
        avance=temps*test
        fenetre.blit(Pause,(1136,144))
    fenetre.blit(Lecture,(1136,576))
    fenetre.blit(Avancer,(1136,432))
    fenetre.blit(Reculer,(1136,288))
    fenetre.blit(Menu1,(1136,0))

    if audio_reader_proc.is_finish():
        if p < 37:
            audio_reader_proc.avancer()
            p += 1
        else:
            audio_reader_proc.__init__(0,True)
            p = 0
        fenetre.blit(Selection_soundtrack, (0,13+18*(p)))

    if update_at_quit:
        fenetre.blit(download_stat_downloading,(400,5))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_stat = pygame.mouse.get_pressed()
            if mouse_stat[0]:
                soundtrack_is_click()
                if pos_Pause.collidepoint(event.pos):
                    audio_reader_proc.pause()
                    fenetre.blit(Pause1,(1136,144))

                if pos_Lecture.collidepoint(event.pos):
                    fenetre.blit(Lecture1,(1136,576))
                    pygame.display.flip()
                    time.sleep(0.5)
                    audio_reader_proc.lecture()

                if pos_Avancer.collidepoint(event.pos) and p<37:
                    fenetre.blit(Avancer1,(1136,432))
                    pygame.display.flip()
                    time.sleep(0.1)
                    audio_reader_proc.avancer()
                    p += 1

                if pos_Reculer.collidepoint(event.pos) and p>=1:
                    fenetre.blit(Reculer1,(1136,288))
                    pygame.display.flip()
                    time.sleep(0.1)
                    audio_reader_proc.reculer()
                    p -= 1

                if pos_sound_up.collidepoint(event.pos) and volume < 10:
                    fenetre.blit(sound_up1,(1036,150))
                    pygame.display.flip()
                    volume += 1
                    data_base.update("volume", str(volume))
                    time.sleep(0.1)

                if pos_sound_down.collidepoint(event.pos) and volume >= 0 :
                    fenetre.blit(sound_down1,(1036,450))
                    pygame.display.flip()
                    volume -= 1
                    data_base.update("volume", str(volume))
                    time.sleep(0.1)
                if pos_Menu1.collidepoint(event.pos):

                    soundtrack=False
                    if Skin_selected == "Titanium":
                        menu_continuer=True
                        fenetre.blit(Menu11,(1136,0))
                        ouverture_titre(200,2,1)
                    elif Skin_selected == "Carroussel":
                        fenetre.blit(Menu11,(1136,0))
                        Menu_skin2 = True
                        menu_carroussel.open()
                    elif Skin_selected == "Legacy":
                        fenetre.blit(Menu11,(1136,0))
                        Menu_skin1 = True
                        menu_continuer = False
                        transition_ouverture(320)

                    pygame.display.flip()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT and p<37:
                fenetre.blit(Avancer1,(1136,432))
                pygame.display.flip()
                time.sleep(0.1)
                audio_reader_proc.avancer()
                p += 1

            if event.key == pygame.K_LEFT and p>=1:
                fenetre.blit(Reculer1,(1136,288))
                pygame.display.flip()
                time.sleep(0.1)
                audio_reader_proc.reculer()
                p -= 1

            if event.key == K_ESCAPE:
                soundtrack=False
                if Skin_selected == "Titanium":
                    menu_continuer=True
                    fenetre.blit(Menu11,(1136,0))
                    ouverture_titre(200,2,1)
                elif Skin_selected == "Carroussel":
                    fenetre.blit(Menu11,(1136,0))
                    Menu_skin2 = True
                    menu_carroussel.open()
                elif Skin_selected == "Legacy":
                    fenetre.blit(Menu11,(1136,0))
                    Menu_skin1 = True
                    menu_continuer = False
                    transition_ouverture(320)
                pygame.display.flip()
        if event.type == QUIT:
            if quit_enable and not(update_web):
                STOP()
            elif quit_enable and update_web:
                STOP("Update.bat")

