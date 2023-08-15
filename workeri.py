import pygame
from pygame import image

import knopka
import nadpisi


class Workyr:
    def __init__(self, worker, rect: pygame.Rect, money:nadpisi.Nadpis, visible=False ):
        self.money = money
        self.visible = visible
        self.rect = rect
        self.worker = worker
        wor = image.load(worker)
        self.workir = pygame.transform.scale(wor, self.rect.size)

        self.rect_button_green2 = pygame.Rect([self.rect.right - 50, self.rect.top, 50, 50])
        self.button = knopka.Knopka(self.rect_button_green2, "sprites/controls/up_green.png", self.prent)

        self.level = nadpisi.Nadpis(self.rect.left,self.rect.top - 30,"уровень ")

    def prent(self):
        cena = 1000000
        if self.money.chislo >= cena:
            self.money.chislo -= cena
            self.level.chislo += 1


    def show(self):
        self.visible = True

    def blit(self, display: pygame.Surface):
        if self.visible:
            display.blit(self.workir, [self.rect.x, self.rect.y])
            self.button.draw(display, True)
            self.level.view(display)

    def events(self, b):
        self.button.events(b)
        for t in b:
            pass
