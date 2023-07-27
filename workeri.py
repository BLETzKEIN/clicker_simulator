import pygame
from pygame import image
class Workyr:
    def __init__(self,worker,rect:pygame.Rect,visible = False):
        self.visible = visible
        self.rect = rect
        self.worker = worker
        wor = image.load(worker)
        self.workir = pygame.transform.scale(wor, self.rect.size)

    def show(self):
        self.visible = True

    def blit(self,display: pygame.Surface):
        if self.visible :
            display.blit(self.workir,[self.rect.x,self.rect.y])


