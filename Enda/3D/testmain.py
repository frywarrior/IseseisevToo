import pygame as py

py.init()

SCREEN_W, SCREEN_H = 640, 480
SCREEN = py.display.set_mode((SCREEN_W, SCREEN_H), vsync=1)

clock = py.time.Clock()

while True:
    clock.tick(60)
    [quit() for event in py.event.get() if event.type == py.QUIT]
    py.display.update()
