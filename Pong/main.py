import pygame, sys


# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
Score = 0


ball = pygame.image.load("Pong/Img/ball.png")

pad = pygame.image.load("Pong/Img/pad.png")

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


