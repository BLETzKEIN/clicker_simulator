import pygame
from pygame import event
# from pygame import *
import button
import model


def events():
    b = event.get()
    for t in model.a:
        t.events(b)
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.MOUSEBUTTONDOWN:
            if model.rect.collidepoint(s.pos):
                model.upgrade()
            elif s.button in [pygame.BUTTON_LEFT, pygame.BUTTON_RIGHT]:
                model.click()
                # print(model.moneys)
            else:
                print("НЕ ДЕЛАЙ ТАК")
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])