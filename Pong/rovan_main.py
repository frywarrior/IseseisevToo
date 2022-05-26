import pygame

pygame.init()

lBlue = [51, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping pong - Rovan")
screen.fill(lBlue)

# Surface kasutamine
surf = pygame.Surface((200, 200))
pygame.draw.circle(surf, lBlue, (140, 100), 100)

clock = pygame.time.Clock()
posX, posY = 0, 0
posX2, posY2 = 245, 300
speedX, speedY = 3, 4
speedX2 = 2
# player
player = pygame.Rect(posX, posY, 20, 20)
playerImage = pygame.image.load("Img/ball.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

# alus
alus = pygame.Rect(posX2, posY2, 120, 20)
aluspilt = pygame.image.load("Img/pad.png")
aluspilt = pygame.transform.scale(aluspilt, [alus.width, alus.height])

gameover = False
while not gameover:
    clock.tick(60)
    # mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # player liikumine
    player = pygame.Rect(posX, posY, 20, 20)
    screen.blit(playerImage, player)

    posX += speedX
    posY += speedY

    if posX > screenX - playerImage.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - playerImage.get_rect().height or posY < 0:
        speedY = -speedY

    #   print(playerImage.get_rect().,)

    if player.colliderect(alus) and speedY > 0:
        speedY = -speedY
        print("hit")

    # alus
    alus = pygame.Rect(posX2, posY2, 120, 20)
    screen.blit(aluspilt, alus)

    posX2 += speedX2

    if posX2 > screenX - aluspilt.get_rect().width or posX2 < 0:
        speedX2 = -speedX2

    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()
