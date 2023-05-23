import pygame

class Button():
    def __init__(self,a,color):
        self.a = a
        self.color = color
        print("dxgfdgdgfghxdg")

    def plus_piat(self):
        self.a += 5

    def minus(self,min):
        self.a -= min

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,[700,350],self.a)