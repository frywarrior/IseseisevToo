import pygame, sys

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
clock = pygame.time.Clock()

# graafika laadimine
bg = pygame.image.load("img/bg_rally.jpg")


f1_blue = pygame.image.load("img/f1_blue.png")
f1_blue = pygame.transform.rotate(f1_blue, 180)

f1_red = pygame.image.load("img/f1_red.png")
f1_red = pygame.transform.rotate(f1_red, 180)

# kiirus ja asukoht
BposX, BposY = 420, 0
BspeedY = 3

RposX, RposY = 298, 0
RspeedY = 1
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

    if BposY >= screenY:
        BposY = -120

    if RposY >= screenY:
        RposY = -120

    # graafika kuvamine ekraanil
    pygame.display.flip()
