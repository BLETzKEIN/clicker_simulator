import pygame


def click():
    global moneys
    moneys += za_click

def upgrade():
    global moneys,za_click
    if moneys >= upgrade_cena:
        moneys -= upgrade_cena
        za_click += za_click




za_click = 2
moneys = 0
upgrade_cena = 10
rect = pygame.Rect([1400-750,0,50,50])
show_rects = False