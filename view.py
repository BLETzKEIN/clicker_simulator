import model
import pygame
from pygame import image,display as display_mod

display=display_mod.set_mode([1400,700])
plac=image.load("sprites/place/place1.jpg")
place = pygame.transform.scale(plac,[1400,700])
display.blit(place,[0,0])
display_mod.flip()