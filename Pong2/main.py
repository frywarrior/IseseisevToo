import pygame
import sys

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()
#

# Lisab graafika
ball = pygame.image.load("Img/ball.png")

pad = pygame.image.load("Img/pad.png")
pad = pygame.transform.scale(pad, [120, 20])
#

# kiirus ja positsioon
BallposX, BallposY = 300, 150
BallspeedY = 5
BallspeedX = 5

PadposX, PadposY = 340, 320
PadspeedX = 5
#

# muud muutujad
Score = 0
ind = 0
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

    # taust
    screen.fill([149, 203, 255])
    #

    # aluse liikumine ja skoor
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and PadposX < screenX - 120:
        PadposX += PadspeedX
    if keys[pygame.K_LEFT] and 0 < PadposX:
        PadposX -= PadspeedX

    screen.blit(pad, (PadposX, PadposY))

    screen.blit(pygame.font.Font(None, 30).render(f"Score: {Score}", True, [255, 255, 255]), [10, 10])
    #

    # palli liikumine
    BallposY += BallspeedY
    BallposX += BallspeedX

    screen.blit(ball, (BallposX, BallposY))
    if 0 > BallposY or BallposY > screenY - 20:
        BallspeedY = -BallspeedY

    if 0 > BallposX or BallposX > screenX - 20:
        BallspeedX = -BallspeedX
        #

    # kui pall puudutab alust
    if PadposY <= BallposY + 20 and BallposY <= PadposY + 20:
        if PadposX <= BallposX + 20 and BallposX <= PadposX + 120:
            if BallspeedY > 0:
                BallspeedY = -BallspeedY
                Score += 1
    #

    # kui pall puudutab ekraani alust
    if BallposY + 20 == screenY:
        if ind == 1:
            Score -= 1
            ind = 0
        else:
            ind = 1
    #

    # uuendab ekraani
    pygame.display.flip()
    #
