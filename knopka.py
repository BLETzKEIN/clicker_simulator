import pygame


class Knopka:
    def __init__(self, rect, kartinka):
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
            pygame.draw.rect(surface, [3, 30, 127], self.rect, 5)

    def events(self, b):
        for i in b:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.fon = True
            else:
                self.fon = False
            if i.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(i.pos):
                    print(self.rect)
