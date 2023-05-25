import time, view, model, controller

import pygame

while True:
    time.sleep(1 / 100)
    controller.events()
    view.vyalia()
    model.always()
