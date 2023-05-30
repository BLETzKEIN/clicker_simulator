import random

import pygame


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


level_bomj = 0
za_click = 2
moneys = 0
upgrade_cena = 10
za_click_upgrade = 2
rect = pygame.Rect([1400 - 750, 0, 50, 50])
rect_bomj = pygame.Rect([0, 450, 250, 250])
show_rects = False
rect_musicant = pygame.Rect([250, 300, 300, 400])


import button

def create():
    defes = button.Button(random.randint(5,45),
                          [random.randint(5,255),random.randint(5,255),random.randint(5,255)],
                          [random.randint(0,1400),random.randint(0,700)],dsf)
    return defes

dsf = button.Button(20, [55, 97, 148],[700,350],None)
dsf.glavnyi = dsf
dsf.a -= 10
dsf.plus_piat()
dsf.minus(7)
print(dsf)
dse = button.Button(55, [197, 36, 23],[100,100],dsf)

dse.plus_piat()
dse.plus_piat()
dse.minus(25)

dsg = button.Button(10,[32,195,225],[400,200],dsf)

a = []
a.append(dsf)
a.append(dsg)
a.append(dse)

print("Hello from platok")
for o in range(200):
    a.append(create())

def always ():
    for y in a :
        y.rost()
#     dsf.rost()
#     dse.rost()
#     dsg.rost()
#     # a[].rost()


