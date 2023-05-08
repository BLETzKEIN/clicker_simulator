import model
import pygame
from pygame import image, display as display_mod

pygame.init()
f = pygame.font.SysFont("arial", 30, True, False)

display = display_mod.set_mode([1400, 700])
plac = image.load("sprites/place/place1.jpg")
place = pygame.transform.scale(plac, [1400, 700])
u = image.load("sprites/controls/up_yellow.png")
up = pygame.transform.scale(u,model.rect.size)


def vyalia():
    moneyts = f.render(str(model.moneys) + " монет", True, [197, 36, 23], [52, 12, 10])
    money_za_click = f.render("за клик " + str(model.za_click) + " монет", True, [197, 36, 23], [52, 12, 10])
    ypgreid = f.render("апгреид стоит "+ str(model.upgrade_cena)+" монет",True, [197, 36, 23], [52, 12, 10])
    display.blit(place, [0, 0])
    display.blit(up,[model.rect.left,model.rect.top])
    display.blit(money_za_click, [0, 30])
    display.blit(moneyts, [0, 0])
    display.blit(ypgreid,[model.rect.left,model.rect.bottom])
    tab()
    display_mod.flip()

def tab():
    if model.show_rects == True:
        pygame.draw.rect(display,[3,30,127],model.rect,5)

