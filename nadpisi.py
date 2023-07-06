import pygame

pygame.init()
f = pygame.font.SysFont("arial", 30, True, False)


class Nadpis:
    def __init__(self, x, y, strochka="", strochka2="", chislo=0):
        self.strochka = strochka
        self.strochka2 = strochka2
        self.x = x
        self.y = y
        self.chislo = chislo
        self.g = f.render( self.strochka + str(self.chislo) + self.strochka2, True, [197, 36, 23], [52, 12, 10])

    def view(self, display: pygame.Surface):
        display.blit(self.g, [self.x, self.y])

    def set_chislo(self, novoe_chislo):
        if novoe_chislo != self.chislo:
            self.chislo = novoe_chislo
            self.g = f.render( self.strochka + str(self.chislo) + self.strochka2, True, [197, 36, 23], [52, 12, 10])

