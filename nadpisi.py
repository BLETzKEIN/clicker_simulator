import pygame

pygame.init()

def podmenatel(view_def):
    def hcxghc(self,display):
        print(self.strochka + str(int(self._chislo)) + self.strochka2)
        view_def(self,display)
    return hcxghc


class Nadpis:
    def __init__(self, x, y, strochka="", strochka2="", chislo=0, shrift = 30,):
        self.f = pygame.font.SysFont("arial", shrift, True, False)
        self.strochka = strochka
        self.strochka2 = strochka2
        self.x = x
        self.y = y
        self._chislo = chislo
        self.g = self.f.render(self.strochka + str(int(self._chislo)) + self.strochka2, True, [197, 36, 23], [52, 12, 10])

    @podmenatel
    def view(self, display: pygame.Surface):
        display.blit(self.g, [self.x, self.y])

    @property
    def chislo(self):
        return self._chislo

    @chislo.setter
    def chislo(self, novoe_chislo):
        if novoe_chislo != self._chislo:
            self._chislo = novoe_chislo
            self.g = self.f.render(self.strochka + str(int(self._chislo)) + self.strochka2, True, [197, 36, 23], [52, 12, 10])






