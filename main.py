import pygame, sys
import random

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
clock = pygame.time.Clock()

Score = 0

# graafika laadimine
bg = pygame.image.load("img/bg_rally.jpg")


f1_blue = pygame.image.load("img/f1_blue.png")
f1_blue = pygame.transform.rotate(f1_blue, 180)

f1_red = pygame.image.load("img/f1_red.png")
f1_red = pygame.transform.rotate(f1_red, 180)

# kiirus ja asukoht
BposX, BposY = 420, 0
BspeedY = 30

RposX, RposY = 300, 390
RspeedY = 0
gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(bg, (0, 0))

    screen.blit(f1_blue, (BposX, BposY))
    BposY += BspeedY

    screen.blit(f1_red, (RposX, RposY))
    RposY += RspeedY

    screen.blit(pygame.font.Font(None, 30).render(f"Score: {Score}", True, [255, 255, 255]), [10, 460])

    if BposY >= screenY:
        BposY = -120
        BposX = random.choice([420, 300, 180])
        Score += 1

    if RposY >= screenY:
        RposY = -120

    if RposY <= BposY+90 <= RposY + 90 and RposX == BposX:
        print("ai")
        gameover = True
        screen.blit(f1_blue, (BposX, RposY + 90))

    while gameover:
        clock.tick(60)
        screen.fill([135, 206, 235])
    # graafika kuvamine ekraanil
    pygame.display.flip()
