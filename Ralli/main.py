import pygame, sys, random, time

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
clock = pygame.time.Clock()
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

    # hit dectection
    if RposY <= BposY + 90 and BposY <= RposY + 90 and RposX == BposX:
        print("ai")
        screen.blit(f1_red, (RposX, RposY))
        screen.blit(f1_blue, (BposX, BposY))
        pygame.display.flip()
        time.sleep(3)
        gameover = True
    else:
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
            RspeedY = -random.randint(3, 15)
            Score += 1
        #
    #
    while gameover:
        clock.tick(60)
        screen.fill([135, 206, 235])
        screen.blit(pygame.font.Font(None, 100).render(f"Gameover", True, [255, 255, 255]), [150, 100])
        screen.blit(pygame.font.Font(None, 50).render(f"Your total score: {Score}", True, [255, 255, 255]), [180, 200])
        pygame.display.flip()

        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                quit()
                sys.exit()
    # graafika kuvamine ekraanil
    pygame.display.flip()
