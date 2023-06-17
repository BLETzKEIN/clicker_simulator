import model
import pygame
from pygame import image, display as display_mod
import knopka

pygame.init()
f = pygame.font.SysFont("arial", 30, True, False)

display = display_mod.set_mode([1400, 700])
plac = image.load("sprites/place/place1.jpg")
place = pygame.transform.scale(plac, [1400, 700])
u = image.load("sprites/controls/up_yellow.png")
up = pygame.transform.scale(u, model.rect.size)
bom = image.load("sprites/worker/worker1.png")
bomj = pygame.transform.scale(bom, model.rect_bomj.size)
musican = image.load("sprites/worker/worker2_inv.png")
musicant = pygame.transform.scale(musican, model.rect_musicant.size)

c = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
d = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)


def cursor_fon():
    pygame.mouse.set_cursor(d)
    for y in model.buttons:
        if y.fon:
            pygame.mouse.set_cursor(c)
    # for y in model.a:
    #     if y.fon:
    #         pygame.mouse.set_cursor(c)


def vyalia():
    moneyts = f.render(str(int(model.moneys)) + " монет", True, [197, 36, 23], [52, 12, 10])
    money_za_click = f.render("за клик " + str(model.za_click) + " монет", True, [197, 36, 23], [52, 12, 10])
    ypgreid = f.render("апгреид стоит " + str(int(model.upgrade_cena)) + " монет", True, [197, 36, 23], [52, 12, 10])
    ypgreid_prirost = f.render("за апгреид будет +" + str(model.za_click_upgrade) + " за клик", True, [197, 36, 23],
                               [52, 12, 10])
    display.blit(place, [0, 0])
    cursor_fon()

    model.dss.draw(display, model.show_rects)
    model.dss2.draw(display, model.show_rects)
    model.pv.view(display)
    # model.dse.draw(display)
    # model.dsf.draw(display)
    # model.dsg.draw(display)
    level_text = f.render("уровень " + str(model.level_bomj), True, [197, 36, 23], [52, 12, 10])
    display.blit(up, [model.rect.left, model.rect.top])
    display.blit(bomj, model.rect_bomj.topleft)
    display.blit(money_za_click, [0, 30])
    display.blit(moneyts, [0, 0])
    display.blit(ypgreid, [model.rect.left, model.rect.bottom])
    display.blit(ypgreid_prirost, [model.rect.left, model.rect.bottom + 30])
    display.blit(level_text, [model.rect_bomj.left + 30, model.rect_bomj.top - 30])
    display.blit(musicant, model.rect_musicant)
    tab()
    display_mod.flip()


def tab():
    if model.show_rects == True:
        pygame.draw.rect(display, [3, 30, 127], model.rect, 5)
        pygame.draw.rect(display, [3, 30, 127], model.rect_bomj, 5)
        pygame.draw.rect(display, [3, 30, 127], model.rect_musicant, 5)
