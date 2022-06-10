import pygame
from itertools import cycle

pygame.init()

# colors

white = (255, 255, 255)
gray = (230, 230, 230)
dgray = (200, 200, 200)
ddgray = (150, 150, 150)

degs = cycle(list(range(361)))
Scythe = pygame.transform.scale(pygame.image.load("Img/Scythe.png"), (60, 56))


def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


boxX, boxY = 40, 120
boxspeedY = 0
boxspeedX = 3

GRAVITY = 9.6

FPS = 60

screen = pygame.display.set_mode([640, 480])

clock = pygame.time.Clock()

lastkey = None

gameover = False
while not gameover:

    clock.tick(FPS)

    screen.fill(white)

    # platform
    platformRect = pygame.rect.Rect(15, 360, 610, 10)
    pygame.draw.rect(screen, gray, platformRect, 0, 5, )
    pygame.draw.rect(screen, dgray, platformRect, 1, 5)

    #

    blitRotateCenter(screen, Scythe, (100, 100), -next(degs))
    """
    screen.blit(scytherot(-next(degs)), (100, 100))
    """
    # box XD
    boxRect = pygame.rect.Rect(boxX, boxY, 40, 40)
    boxNFRect = pygame.Rect(boxRect[0], boxRect[1] + boxspeedY, boxRect[2], boxRect[3])  # box rect next frame
    box = pygame.draw.rect(screen, ddgray, boxRect, 0, 6)

    if boxNFRect.colliderect(platformRect):
        boxY = platformRect[1] - 39
        boxspeedY = 0
    else:
        boxspeedY += GRAVITY / FPS
        boxY += boxspeedY

    if boxRect[1] > 640:
        boxX, boxY = 300, -80

    #

    #
    events = pygame.event.get()

    # [quit() for i in pygame.event.get() if i.type == pygame.QUIT]
    for i in events:
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                boxY -= 1
                boxspeedY = -6
            if i.key != pygame.K_UP:
                lastkey = i.key

        if i.type == pygame.KEYUP:
            if i.key != pygame.K_UP:
                lastkey = None

    if lastkey == pygame.K_RIGHT:
        boxX += boxspeedX
    if lastkey == pygame.K_LEFT:
        boxX -= boxspeedX
    #

    pygame.display.flip()
