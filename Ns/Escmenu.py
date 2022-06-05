import pygame
import pygame_gui


def button(name, location, size, manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(location, size),
                                        text=f'{name}',
                                        manager=manager)


def escmenu(screen):
    s = pygame.Surface((640, 480))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    clock = pygame.time.Clock()

    manager = pygame_gui.UIManager((640, 480), "theme.json")

    ret = button("Return", (270, 240), (100, 50), manager)

    qui = button("Quit", (270, 300), (100, 50), manager)

    paused = True

    while paused:
        time_delta = clock.tick(30) / 1000.0

        # mängu sulgemine ristist

        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                quit()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    paused = False

            if i.type == pygame_gui.UI_BUTTON_PRESSED:

                if i.ui_element == ret:
                    paused = False

                if i.ui_element == qui:
                    quit()
            manager.process_events(i)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
