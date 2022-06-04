import pygame
import pygame_gui


def button(name, location, size, manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(location, size),
                                        text=f'{name}',
                                        manager=manager)


def main():
    sums = ""

    pygame.init()

    pygame.display.set_caption('Kalk')
    window_surface = pygame.display.set_mode((200, 300))

    background = pygame.Surface((200, 300))
    background.fill((0, 0, 0))

    manager = pygame_gui.UIManager((200, 300))

    plus = button("+", (150, 100), (50, 50), manager)

    miinus = button("-", (150, 150), (50, 50), manager)

    jagamine = button("÷", (150, 200), (50, 50), manager)

    korrutamine =  button("x", (150, 250), (50, 50), manager)

    seitse = button("7", (0, 100), (50, 50), manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == plus:
                    if sums[-1] != "+":
                        sums = sums + "+"
                        print(sums)
                    else:
                        print(sums)
                if event.ui_element == seitse:
                    sums = sums + "7"
                    print(sums)

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == '__main__':
    main()
