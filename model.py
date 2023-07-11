import random
import knopka
import vecherinki
import nadpisi
import pygame
pygame.mixer.init()


def click():
    global moneys
    moneys += za_click
    nadpis4.chislo = moneys

def upgrade():
    global moneys, za_click, za_click_upgrade, upgrade_cena, level_bomj
    if moneys >= upgrade_cena:
        moneys -= upgrade_cena
        upgrade_cena *= 1.05
        za_click += za_click_upgrade
        za_click_upgrade += 2
        level_bomj += 1
        nadpis2.chislo = za_click
        nadpis3.chislo = level_bomj
        nadpis4.chislo = moneys
    else:
        zvyk.play()

def musicant_buy():
    global moneys,upgrade_musicant_cena,level_musicant,moneys_per_second
    if moneys < upgrade_musicant_cena:
        zvyk.play()
    else:
        moneys -= upgrade_musicant_cena
        upgrade_musicant_cena *=1.02
        level_musicant += 1
        moneys_per_second +=5
        nadpis1.chislo = moneys_per_second


def always ():
    for h in bykashki:
        h.model()
def knopka_create (rect,kartinka,deistvie):
    dss = knopka.Knopka(rect, kartinka, deistvie)
    dss.obvodka = "green"
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
moneys_per_second = 0
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
nadpis1 = nadpisi.Nadpis(rect_musicant.right,rect_musicant.bottom-30,strochka2=" монет в секунду",chislo=moneys_per_second)
nadpis2 = nadpisi.Nadpis(0,30,strochka2=" монет за клик",chislo=za_click)
nadpis3 = nadpisi.Nadpis(rect_bomj.left + 30, rect_bomj.top - 30,"уровень ",)
nadpis4 = nadpisi.Nadpis(0,0,strochka2=" монет")
nadpis5 = nadpisi.Nadpis(rect_musicant.left +30,rect_musicant.top-30,"уровень ")
buttons = []
bykashki = []





knopka_create(rect_button_yellow2,"sprites/controls/up_yellow.png",upgrade)
knopka_create(rect_button_green,"sprites/controls/up_green.png",musicant_buy)

vechirinka_create(rect_vecherinki1,"kvadrat")
