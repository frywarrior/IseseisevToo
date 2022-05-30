import pygame
import random


class Dot:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.color = random_color()
        self.size = size

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, 1)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


dots = []

screen, im = pygame.display.set_mode([640, 480]), 8  # loob ekraani suurusega 640 x 480 ja ringi suuruse
while True:  # kui on tõen
    screen.fill([0, 0, 0])
    for i in pygame.event.get():  # võtab evendid
        if i.type == pygame.QUIT:  # kui kasutaja vajutab "X" nupule
            quit()  # väljub mängust
        if i.type == pygame.MOUSEBUTTONDOWN:  # kui hiirenupp on all
            dots.append(Dot(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], im))
            if im >= 48:  # if dot in range ball
                del dots[0]
            im += 4  # Uuendab järgmise ringi suurust
    for dot in dots:
        dot.draw()
    pygame.display.flip()  # uuendab ekraani
