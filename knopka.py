import pygame

class Knopka:
    def __init__(self,rect,kartinka):
        self.rect = rect
        self.kartinka = kartinka
        kartinka = pygame.image.load(self.kartinka)
        self.kartinka_re = pygame.transform.scale(kartinka, [self.rect[2], self.rect[3]])

    def draw (self,surface:pygame.Surface):
        surface.blit(self.kartinka_re,self.rect)
