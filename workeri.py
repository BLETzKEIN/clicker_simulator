import pygame
from pygame import image

import knopka


class Workyr:
    def __init__(self, worker, rect: pygame.Rect, visible=False, money):
        self.money = money
        self.visible = visible
        self.rect = rect
        self.worker = worker
        wor = image.load(worker)
        self.workir = pygame.transform.scale(wor, self.rect.size)

        self.rect_button_green2 = pygame.Rect([self.rect.right - 50, self.rect.top, 50, 50])
        self.button = knopka.Knopka(self.rect_button_green2, "sprites/controls/up_green.png", self.prent)

    def prent(self):
        cena = 100000
        if self.money > cena:
            self.money - cena


    def show(self):
        self.visible = True

    def blit(self, display: pygame.Surface):
        if self.visible:
            display.blit(self.workir, [self.rect.x, self.rect.y])
            self.button.draw(display, True)

    def events(self, b):
        self.button.events(b)
        for t in b:
            pass
