import pygame
from pygame import image
class Workyr:
    def __init__(self,worker,rect:pygame.Rect):
        self.rect = rect
        self.worker = worker
        wor = image.load(worker)
        self.workir = pygame.transform.scale(wor, self.rect.size)

    def blit(self,display: pygame.Surface):
        display.blit(self.workir,[self.rect.x,self.rect.y])

