import numpy
import pygame


class Ring:
    def __init__(self):
        self.xy = pygame.mouse.get_pos()
        self.color = list(numpy.random.choice(range(256), size=3))
        self.size = im

    def draw(self):
        pygame.draw.circle(screen, self.color, self.xy, self.size, 1)


ringid = []

screen, im = pygame.display.set_mode([640, 480]), 8  # loob ekraani suurusega 640 x 480 ja ringi suuruse
while True:  # kui on tõen
    screen.fill([0, 0, 0])
    for i in pygame.event.get():  # võtab evendid
        if i.type == pygame.QUIT:  # kui kasutaja vajutab "X" nupule
            quit()  # väljub mängust
        if i.type == pygame.MOUSEBUTTONDOWN:  # kui hiirenupp on all
            ringid.append(Ring())
            if im >= 48:  # if dot in range ball
                del ringid[0]
            im += 4  # Uuendab järgmise ringi suurust
    for ring in ringid:
        ring.draw()
    pygame.display.flip()  # uuendab ekraani
