import random
import math
import pygame


# otbivka_y = 0
# otbivka_x = 0
class Button:
    def __init__(self, a, color, mesto, glavnyi, friend):
        self.glavnyi = glavnyi
        self.a = a
        self.color = color
        self.mesto = mesto
        self.skorost_rosta = random.randint(1, 3)
        self.otbivka_y = 0
        self.otbivka_x = 0
        self.friend = friend
        # self.symma_radiysov = self.a + self.friend.a
        print("dxgfdgdgfghxdg")

    def plus_piat(self):
        self.a += 5

    def minus(self, min):
        self.a -= min

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.mesto, self.a)
        pygame.draw.circle(surface, [1, 1, 1], self.mesto, 3)
        pygame.draw.line(surface, [1, 1, 1], self.mesto, self.glavnyi.mesto)

    def kasanie(self):
        for i in self.friend:
            if math.dist(i.mesto, self.mesto) > i.a + self.a:
                return False
            else:
                return True


    def rost(self):
        if  self.kasanie()==False and self.a < 300:
            self.a += self.skorost_rosta / 3
        else:
            while self.kasanie()==True and self.a > 0:
                self.a -= self.skorost_rosta / 3
        self.otbivka()

    def otbivka(self):
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
        if self.mesto[0] - self.a <= 0:
            self.otbivka_x = 0

        if self.otbivka_x == 0:
            self.mesto[0] += 1

        if self.otbivka_x == 1:
            self.mesto[0] -= 1

            # self.mesto[0] += 1
