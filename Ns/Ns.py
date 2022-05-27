# Franco Kikkas IS21, Lis ns kuna igav
import pygame
import sys
from hero import Hero

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480

window = pygame.display.set_mode([screenX, screenY])
w = pygame.Surface([160, 144])


def draw():
    frame = pygame.transform.scale(w, (screenX, screenY))
    window.blit(frame, frame.get_rect())
    pygame.display.flip()


pygame.display.set_caption("Game_Test")
clock = pygame.time.Clock()
#

# graafika laadimine
bg = pygame.image.load("img/Veiled_Village.png")
hero = pygame.image.load("img/Hero_all.png")

#

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
            sys.exit()

    w.blit(bg, (0, 0))
    Hero.lookS()

    draw()
