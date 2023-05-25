import random

import pygame


class Button():
    def __init__(self, a, color, mesto):
        self.a = a
        self.color = color
        self.mesto = mesto
        self.skorost_rosta = random.randint(1,3)
        print("dxgfdgdgfghxdg")

    def plus_piat(self):
        self.a += 5

    def minus(self, min):
        self.a -= min

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.mesto, self.a)

    def rost(self):
        if self.a < 50:
            self.a += self.skorost_rosta/3
        else:
            self.a -= 50
