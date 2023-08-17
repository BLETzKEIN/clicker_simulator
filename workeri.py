import pygame
from pygame import image

import knopka
import nadpisi


class Workyr:
    def __init__(self, worker,worker2, rect: pygame.Rect, money:nadpisi.Nadpis,moneys_per_second:nadpisi.Nadpis, visible=False ):
        self.money = money
        self.moneys_per_second = moneys_per_second
        self.visible = visible
        self.rect = rect
        self.worker2 = worker2
        self.worker = worker
        wor = image.load(worker)
        wor2 = image.load(worker2)
        self.workir = pygame.transform.scale(wor, self.rect.size)
        self.workir2 = pygame.transform.scale(wor2, self.rect.size)

        self.rect_button_green2 = pygame.Rect([self.rect.right - 50, self.rect.top, 50, 50])
        self.button = knopka.Knopka(self.rect_button_green2, "sprites/controls/up_green.png", self.prent)

        self.level = nadpisi.Nadpis(self.rect.left,self.rect.top - 30,"уровень ")

        self.cena = nadpisi.Nadpis(self.rect.right-60,self.rect.y + 60,"апгреид стоит "," монет",1000000,20)

        self.moneys_per_second_plus = nadpisi.Nadpis(self.rect.x,self.rect.bottom-30,strochka="+",strochka2=" монет в секунду",chislo=10)

    def prent(self):
        if self.money.chislo >= self.cena.chislo:
            self.money.chislo -= self.cena.chislo
            self.level.chislo += 1
            self.moneys_per_second.chislo += self.moneys_per_second_plus.chislo
            self.moneys_per_second_plus.chislo += 10


    def show(self):
        self.visible = True

    def blit(self, display: pygame.Surface):
        if self.visible == False:
            return
        a = self.workir if self.level.chislo <= 0 else self.workir2
        display.blit(a,[self.rect.x, self.rect.y])
        self.button.draw(display, True)
        self.level.view(display)
        self.cena.view(display)
        self.moneys_per_second_plus.view(display)

    def events(self, b):
        self.button.events(b)
        for t in b:
            pass
