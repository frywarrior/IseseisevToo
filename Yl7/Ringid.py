import pygame, random
screen, im = pygame.display.set_mode([640, 480]), 8
screen.fill([0, 0, 0])
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], pygame.mouse.get_pos(), im, 1)
            im += 4
    pygame.display.flip()
