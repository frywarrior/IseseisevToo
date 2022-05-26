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
BallspeedY = 10
BallspeedX = 10

PadposX, PadposY = 340, 320
PadspeedX = 10
#

# muud muutujad
Score = 0
ind = 0
#

# laadib muusika

pygame.mixer.music.set_volume(0.2)

pygame.mixer.music.load('Sound/taust.mp3')
pygame.mixer.music.play(-1)

boing = pygame.mixer.Sound('Sound/boing.mp3')

death = pygame.mixer.Sound('Sound/death.mp3')
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
                pygame.mixer.Sound.play(boing)
                BallspeedY = -BallspeedY
                Score += 1
    #

    # kui pall puudutab ekraani alust
    if BallposY + 20 == screenY:
        gameover = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(death)
    #

    # uuendab ekraani
    pygame.display.flip()
    #

    # Kui mäng on läbi
    while gameover:
        clock.tick(120)
        screen.fill([135, 206, 235])
        screen.blit(pygame.font.Font(None, 100).render(f"Gameover", True, [255, 255, 255]), [150, 100])
        screen.blit(pygame.font.Font(None, 50).render(f"Your total score: {Score}", True, [255, 255, 255]), [180, 200])
        pygame.display.flip()

        # mängu sulgemine ristist
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                quit()
                sys.exit()
