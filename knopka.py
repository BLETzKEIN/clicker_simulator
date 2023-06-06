import pygame

class Knopka:
    def __init__(self,rect,kartinka):
        self.rect = rect
        self.kartinka = kartinka

    def draw (self,surface:pygame.Surface):
        kartinka = pygame.image.load(self.kartinka)
        kartinka_re = pygame.transform.scale(kartinka, [self.rect[2],self.rect[3]])
        surface.blit(kartinka_re,self.rect)
