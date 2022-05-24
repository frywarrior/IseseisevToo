import pygame, sys


# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
Score = 0


ball = pygame.image.load("Img/ball.png")

pad = pygame.image.load("Img/pad.png")
pad = pygame.transform.scale(pad, [120, 20])

BallposX, BallposY = 300, 150
BallspeedY = 5
BallspeedX = 5

PadposX, PadposY = 340, 320
PadspeedX = 3


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

    screen.fill([149, 203, 255])

    #
    BallposY += BallspeedY
    BallposX += BallspeedX

    screen.blit(ball, (BallposX, BallposY))
    if 0 > BallposY or BallposY > screenY - 20:
        BallspeedY = -BallspeedY

    if 0 > BallposX or BallposX > screenX - 20:
        BallspeedX = -BallspeedX
    #
    if PadposY <= BallposY + 20 and BallposY <= PadposY + 20:
        if PadposX <= BallposX + 20 and BallposX <= PadposX + 120:
            if BallspeedY > 0:
                BallspeedY = -BallspeedY


    #
    PadposX += PadspeedX

    screen.blit(pad, (PadposX, PadposY))

    if 0 > PadposX or PadposX > screenX - 120:
        PadspeedX = -PadspeedX
    #

    pygame.display.flip()

