import random

import pygame

import button


class Vecherinka:
    def __init__(self,rect,forma,kolvo=10):
        self.forma = forma
        self.a = []
        self.dsf = button.Button(20, [55, 97, 148], [700, 350], None, self.a,rect,"kryg")
        self.dsf.glavnyi = self.dsf
        self.vecherinka_bydet = False
        self.vidimost = False
        self.rect = rect
        for o in range(kolvo):
            self.a.append(self.create())
        self.a.append(self.dsf)

    def view(self, display):
        # if model.vecherinka == True:
        # self.a.append(self.dsf)
        if self.vidimost == False:
            return
        for u in self.a:
            u.draw(display)
        print(len(self.a))

    def create(self):
        defes = button.Button(random.randint(5, 45),
                              [random.randint(5, 255), random.randint(5, 255), random.randint(5, 255)],
                              [random.randint(0, 1400), random.randint(0, 700)], self.dsf, self.a,self.rect,self.forma)
        return defes

    def model(self):
        if self.vecherinka_bydet and self.vidimost:
            for y in self.a:
                y.rost()

    def evenets(self, b):
        if self.vidimost:
            for t in self.a:
                t.events(b)
        for i in b:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_1:
                    self.vecherinka_bydet = not self.vecherinka_bydet
                if i.key == pygame.K_2:
                    self.vidimost = not self.vidimost
