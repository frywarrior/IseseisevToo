# Franco Kikkas IS21, Lis ns kuna igav
import pygame
import sys
from hero import Hero

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screenPosX, screenPosY = -200, -450


window = pygame.display.set_mode([screenX, screenY])
window_rect = window.get_rect()

screen = pygame.Surface([160, 144])
screen_rect = screen.get_rect()


def draw():
    frame = pygame.transform.scale(screen, (screenX, screenY))
    window.blit(frame, frame.get_rect())
    pygame.display.flip()


pygame.display.set_caption("Game_Test")
clock = pygame.time.Clock()
#

# graafika laadimine

hero = Hero(screen, (72, 66), (screenPosX, screenPosY))

#

world = False
while not world:
    # fps
    clock.tick(30)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = list(pygame.mouse.get_pos())
            # take the mouse position and scale it, too
            ratio_x = (window_rect.width / screen_rect.width)
            ratio_y = (window_rect.height / screen_rect.height)
            scaled_pos = ((pos[0] / ratio_x) - hero.sc_x, (pos[1] / ratio_y) - hero.sc_y)

            print(scaled_pos)

    hero.moving()
    hero.pub_collide()
    draw()
