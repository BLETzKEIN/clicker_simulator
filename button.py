import random

import pygame


# otbivka_y = 0
# otbivka_x = 0
class Button:
    def __init__(self, a, color, mesto):
        self.a = a
        self.color = color
        self.mesto = mesto
        self.skorost_rosta = random.randint(1, 3)
        self.otbivka_y = 0
        self.otbivka_x = 0
        print("dxgfdgdgfghxdg")

    def plus_piat(self):
        self.a += 5

    def minus(self, min):
        self.a -= min

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.mesto, self.a)

    def rost(self):
        # global otbivka_y,otbivka_x
        if self.a < 50:
            self.a += self.skorost_rosta / 3
        else:
            self.a -= 50

        if self.a + self.mesto[1] >= 700:
            self.otbivka_y = 1
        if self.mesto[1] - self.a <= 0:
            self.otbivka_y = 0

        if self.otbivka_y == 0:
            self.mesto[1] += 1

        if self.otbivka_y == 1:
            self.mesto[1] -= 1

        if self.a + self.mesto[0] >= 1400:
            self.otbivka_x = 1
        if self.mesto[0] - self.a <=0:
            self.otbivka_x = 0

        if self.otbivka_x == 0:
            self.mesto[0] += 1

        if self.otbivka_x == 1:
            self.mesto[0] -= 1

            # self.mesto[0] += 1
