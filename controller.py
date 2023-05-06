import pygame
from pygame import event
# from pygame import *
import model


def events():
    b = event.get()
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.MOUSEBUTTONDOWN:
            if s.button in [pygame.BUTTON_LEFT, pygame.BUTTON_RIGHT]:
                model.click()
                print(model.moneys)
            else:
                print("НЕ ДЕЛАЙ ТАК")
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])