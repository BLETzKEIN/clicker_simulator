import pygame


def click():
    global moneys
    moneys += za_click

def upgrade():
    global moneys,za_click,za_click_upgrade,upgrade_cena
    if moneys >= upgrade_cena:
        moneys -= upgrade_cena
        upgrade_cena *= 1.05
        za_click += za_click_upgrade
        za_click_upgrade += 2




za_click = 2
moneys = 0
upgrade_cena = 10
za_click_upgrade = 2
rect = pygame.Rect([1400-750,0,50,50])
rect_bomj = pygame.Rect([0,450,250,250])
show_rects = False









