import random
import knopka
import vecherinki
import nadpisi
import pygame
import workeri

pygame.mixer.init()

def money_plus():
    moneys.chislo += moneys_per_second.chislo

def prent():
    print("kakashka")

def click():
    moneys.chislo += za_click_ysilenniy.chislo


def upgrade():
    if moneys.chislo >= upgrade_cena.chislo:
        moneys.chislo -= upgrade_cena.chislo
        upgrade_cena.chislo *= 1.05
        za_click.chislo += za_click_upgrade.chislo
        if level_musicant.chislo >= 20:
            za_click_ysilenniy.chislo = za_click.chislo * 1.3
        else:
            za_click_ysilenniy.chislo = za_click.chislo
        za_click_upgrade.chislo += 2
        level_bomj.chislo += 1
    else:
        zvyk.play()


def musicant_buy():
    global upgrade_musicant_cena_rost
    if moneys.chislo < upgrade_musicant_cena.chislo:
        zvyk.play()
    else:
        moneys.chislo -= upgrade_musicant_cena.chislo
        upgrade_musicant_cena.chislo *= upgrade_musicant_cena_rost
        upgrade_musicant_cena_rost += 0.02283
        level_musicant.chislo += 1
        moneys_per_second.chislo += 5
        if level_musicant.chislo == 10:
            workyr3.show()
        if level_musicant.chislo == 20:
            za_click_ysilenniy.chislo *= 1.3



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


def napeshi_uppand(x, y, strochka1 = "", strochka2 ="", chislo = 0, shrift = 30):
    pon = nadpisi.Nadpis(x, y, strochka1, strochka2, chislo, shrift)
    napeshi.append(pon)
    return pon


upgrade_musicant_cena_rost = 1.02
# rect = pygame.Rect([1400 - 750, 0, 50, 50])
zvyk = pygame.mixer.Sound("zvyki/puk.mp3")
rect_button_yellow2 = pygame.Rect([1400 - 750, 0, 50, 50])
rect_bomj = pygame.Rect([0, 450, 250, 250])
show_rects = False
rect_musicant = pygame.Rect([250, 300, 300, 400])
rect_musicant_copy = pygame.Rect([600,300,300,400])
workyr3_rect = pygame.Rect([650,300,200,400])
rect_button_green = pygame.Rect([rect_musicant.right-40, rect_musicant.top + 160, 40, 40])
rect_button_green2 = pygame.Rect([workyr3_rect.right-50,workyr3_rect.top,50,50])
rect_vecherinki1 = pygame.Rect([200, 200, 400, 400])
rect_vecherinki2 = pygame.Rect([700, 500, 400, 200])
napeshi = []
moneys_per_second = napeshi_uppand(0, 90, strochka2=" монет в секунду",
                        chislo= 0)
za_click = napeshi_uppand(0, 30, strochka2=" монет за клик", chislo=2)
level_bomj = napeshi_uppand(rect_bomj.left + 30, rect_bomj.top - 30, "уровень ", )
moneys = napeshi_uppand(0, 0, strochka2=" монет",chislo=10000000)
level_musicant = napeshi_uppand(rect_musicant.left + 30, rect_musicant.top - 30, "уровень ")
upgrade_cena = napeshi_uppand(rect_button_yellow2.left, rect_button_yellow2.bottom, "апгреид стоит ", " монет", 10)
buttons = []
bykashki = []
workers = []
za_click_upgrade = napeshi_uppand(rect_button_yellow2.left, rect_button_yellow2.bottom + 30, "за апгреид будет +", " за клик",
               2)
upgrade_musicant_cena = napeshi_uppand(rect_musicant.right-160,rect_musicant.top + 200,"апгреид стоит "," монет",10000,20)
za_click_ysilenniy = napeshi_uppand(0,60,"реально "," монет за клик",2)
knopka_create(rect_button_yellow2, "sprites/controls/up_yellow.png", upgrade)
knopka_create(rect_button_green, "sprites/controls/up_green.png", musicant_buy)

vechirinka_create(rect_vecherinki1, "kvadrat")



workyr3 = workeri.Workyr(100000,10,10,"sprites/worker/worker3_inv.png","sprites/worker/worker3.png",workyr3_rect,moneys,moneys_per_second)
workyr2 = workeri.Workyr(10000,2,2,"sprites/worker/worker2_inv.png","sprites/worker/worker2.png",rect_musicant_copy,moneys,moneys_per_second,True)
workers.append(workyr3)
workers.append(workyr2)