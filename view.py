import model
import pygame
from pygame import image, display as display_mod
import knopka
import nadpisi

pygame.init()


display = display_mod.set_mode([1400, 700])
plac = image.load("sprites/place/place1.jpg")
place = pygame.transform.scale(plac, [1400, 700])
# u = image.load("sprites/controls/up_yellow.png")
# up = pygame.transform.scale(u, model.rect.size)
bom = image.load("sprites/worker/worker1.png")
bomj = pygame.transform.scale(bom, model.rect_bomj.size)
musican = image.load("sprites/worker/worker2_inv.png")
musicant = pygame.transform.scale(musican, model.rect_musicant.size)
orig_musican = image.load("sprites/worker/worker2.png")
orig_musicant = pygame.transform.scale(orig_musican, model.rect_musicant.size)
# worke3 = image.load("sprites/worker/worker3_inv.png")
# worker3

c = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
d = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)

f = pygame.font.SysFont("arial", 30, True, False)

def cursor_fon():
    pygame.mouse.set_cursor(d)
    for y in model.buttons:
        if y.fon:
            pygame.mouse.set_cursor(c)
    # for y in model.a:
    #     if y.fon:
    #         pygame.mouse.set_cursor(c)


def vyalia():
    display.blit(place, [0, 0])
    cursor_fon()

    for g in model.buttons:
        g.draw(display,model.show_rects)

    for t in model.bykashki:
        t.view(display)

    for v in model.napeshi:
        v.view(display)

    display.blit(bomj, model.rect_bomj.topleft)
    model.workyr3.blit(display)
    model.workyr2.blit(display)
    if model.level_musicant.chislo < 1:
        display.blit(musicant, model.rect_musicant)
    else:
        display.blit(orig_musicant, model.rect_musicant)

    tab()
    display_mod.flip()


def tab():
    if model.show_rects == True:
        # pygame.draw.rect(display, [3, 30, 127], model.rect_, 5)
        pygame.draw.rect(display, [3, 30, 127], model.rect_bomj, 5)
        pygame.draw.rect(display, [3, 30, 127], model.rect_musicant, 5)
        pygame.draw.rect(display, [3, 30, 127], model.rect_vecherinki1, 5)
        pygame.draw.rect(display, [3, 30, 127], model.rect_vecherinki2, 5)
