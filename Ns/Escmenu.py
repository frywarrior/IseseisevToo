import pygame
import pygame_gui


def escmenu(screen):
    s = pygame.Surface((640, 480))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    clock = pygame.time.Clock()
    paused = True

    while paused:
        clock.tick(30)
        # mängu sulgemine ristist
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                quit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    paused = False

        pygame.display.flip()


