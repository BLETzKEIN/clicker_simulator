import random
import knopka
import vecherinki

import pygame
pygame.mixer.init()


def click():
    global moneys
    moneys += za_click


def upgrade():
    global moneys, za_click, za_click_upgrade, upgrade_cena, level_bomj
    if moneys >= upgrade_cena:
        moneys -= upgrade_cena
        upgrade_cena *= 1.05
        za_click += za_click_upgrade
        za_click_upgrade += 2
        level_bomj += 1

def musicant_buy():
    global moneys,upgrade_musicant_cena,level_musicant
    if moneys < upgrade_musicant_cena:
        zvyk.play()
    else:
        moneys -= upgrade_musicant_cena
        upgrade_musicant_cena *=1.02
        level_musicant += 1


def always ():
    for h in bykashki:
        h.model()
def knopka_create (rect,kartinka,deistvie):
    dss = knopka.Knopka(rect, kartinka, deistvie)
    buttons.append(dss)
def vechirinka_create (rect,kryg_or_kvadrat):
    d = vecherinki.Vecherinka(rect,kryg_or_kvadrat)
    bykashki.append(d)

level_bomj = 0
za_click = 2
moneys = 0
upgrade_musicant_cena = 10000
upgrade_cena = 10
za_click_upgrade = 2
# rect = pygame.Rect([1400 - 750, 0, 50, 50])
zvyk = pygame.mixer.Sound("zvyki/puk.mp3")
level_musicant = 0
rect_button_yellow2 = pygame.Rect([1400 - 750, 0, 50, 50])
rect_bomj = pygame.Rect([0, 450, 250, 250])
show_rects = False
rect_musicant = pygame.Rect([250, 300, 300, 400])
rect_button_green = pygame.Rect ([rect_musicant.right,rect_musicant.top+100,50,50])
rect_vecherinki1 = pygame.Rect([200,200,400,400])
rect_vecherinki2 = pygame.Rect([700,500,400,200])
buttons = []
bykashki = []






knopka_create(rect_button_yellow2,"sprites/controls/up_yellow.png",upgrade)
knopka_create(rect_button_green,"sprites/controls/up_green.png",musicant_buy)

vechirinka_create(rect_vecherinki1,"kvadrat")
