import pygame
from pygame import event
# from pygame import *
import button
import model
import knopka
import vecherinki
dfs = pygame.event.custom_type()
pygame.time.set_timer(dfs,1000)

def events():
    b = event.get()
    for t in model.bykashki:
        t.evenets(b)
    for i in model.buttons:
        i.events(b)
    for h in model.workers:
        h.events(b)

    for s in b:
        if s.type == dfs:
            model.money_plus()
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.MOUSEBUTTONDOWN:
            if s.button in [pygame.BUTTON_LEFT, pygame.BUTTON_RIGHT]:
                if model.workyr2.rect_button_green2.collidepoint(s.pos):
                    model.musicant_buy()
                model.click()
                # print(model.moneys)
            else:
                print("НЕ ДЕЛАЙ ТАК")
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])