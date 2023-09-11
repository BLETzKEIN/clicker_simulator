import pygame
from pygame import image

import knopka
import nadpisi

pygame.mixer.init()
zvek = pygame.mixer.Sound("zvyki/puk.mp3")

class Workyr:
    def __init__(self,rect_button,cena_upgreid,rost_pribavki, worker,worker2, rect: pygame.Rect, money:nadpisi.Nadpis,moneys_per_second:nadpisi.Nadpis,x = None,y = None, visible=False ):
        self.x = x
        self.y = y
        self.rost_pribavki = rost_pribavki
        self.cena_upgreid = cena_upgreid
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

        self.rect_button_green2 = rect_button
        self.button = knopka.Knopka(self.rect_button_green2, "sprites/controls/up_green.png", self.prent)
        if self.x is None:
            self.x = self.rect_button_green2.x - 40
        if self.y is None:
            self.y = self.rect_button_green2.y + 40

        self.level = nadpisi.Nadpis(self.rect.left,self.rect.top - 30,"уровень ")

        self.cena = nadpisi.Nadpis(self.x,self.y ,"апгреид стоит "," монет",self.cena_upgreid,20)

        self.moneys_per_second_plus = nadpisi.Nadpis(self.rect.x,self.rect.bottom-30,strochka="+",strochka2=" монет в секунду",chislo= self.rost_pribavki)

    def prent(self):
        if self.money.chislo >= self.cena.chislo:
            self.money.chislo -= self.cena.chislo
            self.cena.chislo *= 1.02
            self.level.chislo += 1
            self.moneys_per_second.chislo += self.moneys_per_second_plus.chislo
            self.moneys_per_second_plus.chislo += self.rost_pribavki
        else:
            zvek.play()



    def show(self):
        self.visible = True

    def blit(self, display: pygame.Surface):
        if self.visible == False:
            return
        a = self.workir if self.level.chislo <= 0 else self.workir2
        display.blit(a,[self.rect.x, self.rect.y])
        print(self.button.rect)
        self.button.draw(display, True)
        self.level.view(display)
        self.cena.view(display)
        self.moneys_per_second_plus.view(display)

    def events(self, b):
        self.button.events(b)
        for t in b:
            pass
