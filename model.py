import random
import knopka
import vecherinki
import nadpisi
import pygame

pygame.mixer.init()

def money_plus():
    moneys.chislo += moneys_per_second.chislo

def click():
    moneys.chislo += za_click_ysilenniy


def upgrade():
    global za_click_upgrade, upgrade_cena, level_bomj, za_click_ysilenniy
    if moneys.chislo >= upgrade_cena:
        moneys.chislo -= upgrade_cena
        upgrade_cena *= 1.05
        za_click.chislo += za_click_upgrade
        if level_musicant >= 20:
            za_click_ysilenniy = za_click.chislo * 1.3
        else:
            za_click_ysilenniy = za_click.chislo
        za_click_upgrade += 2
        level_bomj += 1
        nadpis3.chislo = level_bomj
        nadpis6.chislo = upgrade_cena
        nadpis7.chislo = za_click_upgrade
        nadpis9.chislo = za_click_ysilenniy
    else:
        zvyk.play()


def musicant_buy():
    global upgrade_musicant_cena, level_musicant, moneys_per_second,upgrade_musicant_cena_rost,za_click_ysilenniy
    if moneys.chislo < upgrade_musicant_cena:
        zvyk.play()
    else:
        moneys.chislo -= upgrade_musicant_cena
        upgrade_musicant_cena *= upgrade_musicant_cena_rost
        upgrade_musicant_cena_rost += 0.02283
        level_musicant += 1
        moneys_per_second.chislo += 5
        if level_musicant == 20:
            za_click_ysilenniy *= 1.3
        nadpis5.chislo = level_musicant
        nadpis8.chislo = upgrade_musicant_cena
        nadpis9.chislo = za_click_ysilenniy



def always():
    for h in bykashki:
        h.model()


def knopka_create(rect, kartinka, deistvie):
    dss = knopka.Knopka(rect, kartinka, deistvie)
    dss.obvodka = "green"
    buttons.append(dss)


def vechirinka_create(rect, kryg_or_kvadrat):
    d = vecherinki.Vecherinka(rect, kryg_or_kvadrat)
    bykashki.append(d)


def napeshi_uppand(x, y, strochka1 = "", strochka2 ="", chislo = 0):
    pon = nadpisi.Nadpis(x, y, strochka1, strochka2, chislo)
    napeshi.append(pon)
    return pon


level_bomj = 0
za_click_ysilenniy = 2
upgrade_musicant_cena = 10000
upgrade_musicant_cena_rost = 1.02
upgrade_cena = 10
za_click_upgrade = 2
# rect = pygame.Rect([1400 - 750, 0, 50, 50])
zvyk = pygame.mixer.Sound("zvyki/puk.mp3")
level_musicant = 0
rect_button_yellow2 = pygame.Rect([1400 - 750, 0, 50, 50])
rect_bomj = pygame.Rect([0, 450, 250, 250])
show_rects = False
rect_musicant = pygame.Rect([250, 300, 300, 400])
rect_button_green = pygame.Rect([rect_musicant.right, rect_musicant.top + 100, 50, 50])
rect_vecherinki1 = pygame.Rect([200, 200, 400, 400])
rect_vecherinki2 = pygame.Rect([700, 500, 400, 200])
napeshi = []
moneys_per_second = napeshi_uppand(rect_musicant.right, rect_musicant.bottom - 30, strochka2=" монет в секунду",
                        chislo= 0)
za_click = napeshi_uppand(0, 30, strochka2=" монет за клик", chislo=2)
nadpis3 = napeshi_uppand(rect_bomj.left + 30, rect_bomj.top - 30, "уровень ", )
moneys = napeshi_uppand(0, 0, strochka2=" монет")
nadpis5 = napeshi_uppand(rect_musicant.left + 30, rect_musicant.top - 30, "уровень ")
nadpis6 = napeshi_uppand(rect_button_yellow2.left, rect_button_yellow2.bottom, "апгреид стоит ", " монет", upgrade_cena)
buttons = []
bykashki = []
nadpis7 = napeshi_uppand(rect_button_yellow2.left, rect_button_yellow2.bottom + 30, "за апгреид будет +", " за клик",
               za_click_upgrade)
nadpis8 = napeshi_uppand(rect_musicant.right,rect_musicant.top + 150,"апгреид стоит "," монет",upgrade_musicant_cena)
nadpis9 = napeshi_uppand(0,60,"реально "," монет за клик",za_click_ysilenniy)
knopka_create(rect_button_yellow2, "sprites/controls/up_yellow.png", upgrade)
knopka_create(rect_button_green, "sprites/controls/up_green.png", musicant_buy)

vechirinka_create(rect_vecherinki1, "kvadrat")
