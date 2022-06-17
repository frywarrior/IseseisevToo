import pygame as py

py.init()

# colors

white = (255, 255, 255)
gray = (230, 230, 230)
dgray = (200, 200, 200)
ddgray = (150, 150, 150)

scind = 0
ofset = py.math.Vector2(28, -26)
Scythe = py.transform.scale(py.image.load("Img/Scythe.png"), (60, 56))


def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = py.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = py.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot + rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


boxX, boxY = 40, 120
boxspeedY = 0
boxspeedX = 3

GRAVITY = 9.6

FPS = 60

screen = py.display.set_mode([640, 480])

clock = py.time.Clock()

gameover = False
while not gameover:

    clock.tick(FPS)

    screen.fill(white)

    #
    screen.blit(py.font.Font(None, 30).render(f"FPS: {round(clock.get_fps(), 1)}", True, [0, 0, 0]), [10, 10])

    #

    # platform
    platformRect = py.rect.Rect(15, 360, 610, 10)
    py.draw.rect(screen, gray, platformRect, 0, 5, )
    py.draw.rect(screen, dgray, platformRect, 1, 5)

    #

    # blitRotateCenter(screen, Scythe, (100, 100), scind)

    screen.blit(rotate(Scythe, scind, (100, 156), ofset)[0], rotate(Scythe, scind, (100, 156), ofset)[1])

    py.draw.rect(screen, (255, 0, 0), rotate(Scythe, scind, (100, 156), ofset)[1], 1)

    scind += 1
    if scind >= 360:
        scind -= 360

    """
    screen.blit(scytherot(-next(degs)), (100, 100))
    """
    # box XD
    boxRect = py.rect.Rect(boxX, boxY, 40, 40)
    boxInnerRect = py.rect.Rect(boxRect[0] + 2, boxRect[1] + 2, boxRect[2] - 4, boxRect[3] - 4)
    boxNFRect = py.Rect(boxRect[0], boxRect[1] + boxspeedY, boxRect[2], boxRect[3])  # box rect next frame

    box = py.draw.rect(screen, ddgray, boxRect, 0, 6)
    boxinner = py.draw.rect(screen, dgray, boxInnerRect, 0, 6)

    grnddec = boxNFRect.colliderect(platformRect)

    if grnddec:
        boxY = platformRect[1] - 39
        boxspeedY = 0
    else:
        boxspeedY += GRAVITY / FPS
        boxY += boxspeedY

    if boxRect[1] > 640:
        boxX, boxY = 300, -80

    #

    #
    events = py.event.get()
    keys = py.key.get_pressed()

    # [quit() for i in pygame.event.get() if i.type == pygame.QUIT]
    for i in events:
        if i.type == py.QUIT:
            quit()
        if i.type == py.KEYDOWN:
            if i.key == py.K_UP and boxspeedY == 0:
                boxY -= 1
                boxspeedY = -6

    if keys[py.K_RIGHT]:
        boxX += boxspeedX
        if grnddec:
            boxX -= 1
    if keys[py.K_LEFT]:
        boxX -= boxspeedX
        if grnddec:
            boxX += 1
    #

    py.display.flip()
