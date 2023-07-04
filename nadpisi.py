import pygame
pygame.init()
f = pygame.font.SysFont("arial", 30, True, False)
class Nadpis:
    def __init__(self,x,y):
        self.g = f.render("0 монет в секунду",True,[197, 36, 23], [52, 12, 10])
        self.x = x
        self.y = y
        self.chislo = 0

    def view(self,display:pygame.Surface):
        display.blit(self.g, [self.x, self.y])

    def set_chislo(self,novoe_chislo):
        if novoe_chislo != self.chislo:
            self.chislo = novoe_chislo
            self.g = f.render(str(self.chislo) + " монет в секунду",True,[197, 36, 23], [52, 12, 10])
