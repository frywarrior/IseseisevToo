import pygame
import pygame_gui
import math

def button(name, location, size, manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(location, size),
                                        text=f'{name}',
                                        manager=manager)


def main():
    sums = "0"
    disp = "0"
    marks = ["+", "-", "/", "*"]

    pygame.init()

    pygame.display.set_caption('Kalk')
    window_surface = pygame.display.set_mode((200, 300))

    background = pygame.Surface((200, 300))
    background.fill((0, 0, 0))

    manager = pygame_gui.UIManager((200, 300))

    # Märgid

    plus = button("+", (150, 100), (50, 50), manager)

    miinus = button("-", (150, 150), (50, 50), manager)

    jaga = button("÷", (150, 200), (50, 50), manager)

    korruta = button("x", (150, 250), (50, 50), manager)

    astenda = button("^", (0, 50), (50, 50), manager)

    ruutjuur = button("√", (50, 50), (50, 50), manager)

    kustuta = button("C", (100, 50), (50, 50), manager)

    clear = button("Ce", (150, 50), (50, 50), manager)

    equal = button("=", (100, 250), (50, 50), manager)

    point = button(".", (50, 250), (50, 50), manager)

    # Numbrid

    seitse = button("7", (0, 100), (50, 50), manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # Märgid
                if event.ui_element == plus:
                    if sums[-1] not in marks:
                        sums = sums + "+"
                        disp = disp + "+"
                        print(sums)

                if event.ui_element == miinus:
                    if sums[-1] not in marks:
                        sums = sums + "-"
                        disp = disp + "-"
                        print(sums)

                if event.ui_element == jaga:
                    if sums[-1] not in marks:
                        sums = sums + "/"
                        disp = disp + "÷"
                        print(sums)

                if event.ui_element == korruta:
                    if sums[-1] not in marks:
                        sums = sums + "*"
                        disp = disp + "x"
                        print(sums)

                if event.ui_element == astenda:
                    if sums[-1] not in marks:
                        sums = 2 ** eval(sums)
                        disp = sums
                        print(sums)

                if event.ui_element == ruutjuur:
                    if sums[-1] not in marks:
                        sums = math.sqrt(eval(sums))
                        disp = math.sqrt(eval(sums))
                        print(sums)

                if event.ui_element == kustuta:
                    sums = sums[:-1]
                    disp = disp[:-1]
                    print(sums)

                if event.ui_element == clear:
                    sums = "0"
                    disp = "0"
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
