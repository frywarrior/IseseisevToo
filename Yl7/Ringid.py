import pygame, random  # impordib pygame ja random'i
screen, im = pygame.display.set_mode([640, 480]), 8  # loob ekraani suurusega 640 x 480 ja ringi suuruse
while True:  # kui on tõene
    for i in pygame.event.get():  # võtab evendid
        if i.type == pygame.QUIT:  # kui kasutaja vajutab "X" nupule
            quit()  # väljub mängust
        if i.type == pygame.MOUSEBUTTONDOWN:  # kui hiirenupp on all
            pygame.draw.circle(screen, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],pygame.mouse.get_pos(), im, 1)  # joonistab ringi
            im += 4  # Uuendab järgmise ringi suurust
    pygame.display.flip()  # uuendab ekraani
    # 10 rida yee
