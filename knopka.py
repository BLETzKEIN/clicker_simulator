import pygame


class Knopka:
    def __init__(self, rect, kartinka,deistvie):
        self.clr = [255,0,0]
        self.deistvie = deistvie
        self.fon = False
        self.rect = pygame.Rect(rect)
        self.kartinka = kartinka
        kartinka = pygame.image.load(self.kartinka)
        self.kartinka_re = pygame.transform.scale(kartinka, [self.rect[2], self.rect[3]])

    def draw(self, surface: pygame.Surface, show):
        if self.fon:

            pygame.draw.rect(surface, [33, 78, 197], self.rect)
            pygame.draw.rect(surface, [43, 88, 207], self.rect,3)

        surface.blit(self.kartinka_re, self.rect)
        if show:
            pygame.draw.rect(surface, self.clr, self.rect, 5)

    @property
    def obvodka(self):
        if self.clr == [255,0,0]:
            return "red"
        if self.clr == [0,255,0]:
            return "green"
        if self.clr == [255,255,255]:
            return "white"
    @obvodka.setter
    def obvodka(self,noviy_cvet):
        if noviy_cvet == "green":
            self.clr = [0,255,0]
        if noviy_cvet == "red":
            self.clr = [255,0,0]
        if noviy_cvet == "white":
            self.clr = [255,255,255]



    def events(self, b):
        for i in b:
            # if self.rect.collidepoint(pygame.mouse.get_pos()):
            #     self.fon = True


                # self.fon = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(i.pos):
                    self.deistvie()
