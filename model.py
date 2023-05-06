import pygame


def click():
    global moneys
    moneys += za_click

def upgrade():
    global moneys,za_click
    if moneys >= 10:
        moneys -= 10
        za_click += za_click




za_click = 2
moneys = 0
rect = pygame.Rect([1400-50,0,50,50])
show_rects = False