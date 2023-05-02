import pygame
from pygame import event
# from pygame import *
import model
def events():
    b = event.get()
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)