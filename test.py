import pygame, sys, random

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
clock = pygame.time.Clock()
pressed = False
Score = 0
Dpos = 480
Upos = 0
#

# graafika laadimine
bg = pygame.image.load("img/bg_rally.jpg")

f1_blue = pygame.image.load("img/f1_blue.png")
f1_blue = pygame.transform.rotate(f1_blue, 180)

f1_red = pygame.image.load("img/f1_red.png")
f1_red = pygame.transform.rotate(f1_red, 180)
#

# kiirus ja asukoht
BposX, BposY = 300, 150
BspeedY = 5

RposX, RposY = 300, 390
RspeedY = -2
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

    # pildi lisamine ekraanile

    # Tausta liikumine ja skoor
    Upos -= BspeedY
    Dpos -= BspeedY
    screen.blit(bg, (0, Upos))
    screen.blit(bg, (0, Dpos))

    if Upos <= -screenY:
        Upos = screenY

    if Dpos <= -screenY:
        Dpos = screenY
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {Score}", True, [255, 255, 255]), [10, 460])
    #

    # Sinise auto liikumine
    screen.blit(f1_blue, (BposX, BposY))

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and BposX != 180:
                BposX -= 120
            if event.key == pygame.K_RIGHT and BposX != 420:
                BposX += 120


    ##

    # Punase auto liikumine
    screen.blit(f1_red, (RposX, RposY))
    RposY += RspeedY

    if RposY + 90 <= 0:
        RposY = 600
        RposX = random.choice([420, 300, 180])
        Score += 1
    #

    # graafika kuvamine ekraanil
    pygame.display.flip()
