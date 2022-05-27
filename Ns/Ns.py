# Franco Kikkas IS21, Lis ns kuna igav
import pygame
import sys
from hero import Hero

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screenPosX, screenPosY = 0, 0


window = pygame.display.set_mode([screenX, screenY])
screen = pygame.Surface([160, 144])



def draw():
    frame = pygame.transform.scale(screen, (screenX, screenY))
    window.blit(frame, frame.get_rect())
    pygame.display.flip()


pygame.display.set_caption("Game_Test")
clock = pygame.time.Clock()
#

# graafika laadimine
bg = pygame.image.load("img/Veiled_Village.png")
hero = Hero(screen, (80, 72), (screenPosX,screenPosY))

#

gameover = False
while not gameover:
    # fps
    clock.tick(30)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        hero.move('S')
        hero.look('S')
    elif keys[pygame.K_UP]:
        hero.move('W')
        hero.look('W')
    elif keys[pygame.K_LEFT]:
        hero.move('A')
        hero.look('A')
    elif keys[pygame.K_RIGHT]:
        hero.move('D')
        hero.look('D')
    else:
        hero.update()
        hero.stand()

    draw()
