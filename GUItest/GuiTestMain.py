import pygame
import pygame_gui
import math


def button(name, location, size, manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect(location, size),
                                        text=f'{name}',
                                        manager=manager)


def main():
    sums = ""
    disp = ""
    marks = ["+", "-", "/", "*", "."]

    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('Kalk')
    window_surface = pygame.display.set_mode((200, 300))

    background = pygame.Surface((200, 300))
    background.fill((25, 55, 84))

    manager = pygame_gui.UIManager((200, 300), 'theme.json')

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

    kaheksa = button("8", (50, 100), (50, 50), manager)

    uheksa = button("9", (100, 100), (50, 50), manager)

    neli = button("4", (0, 150), (50, 50), manager)

    viis = button("5", (50, 150), (50, 50), manager)

    kuus = button("6", (100, 150), (50, 50), manager)

    uks = button("1", (0, 200), (50, 50), manager)

    kaks = button("2", (50, 200), (50, 50), manager)

    kolm = button("3", (100, 200), (50, 50), manager)

    null = button("0", (0, 250), (50, 50), manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                # Märgid
                try:
                    if event.ui_element == plus:
                        if sums[-1] not in marks:
                            sums = sums + "+"
                            disp = disp + "+"
                            print(sums)
                except:
                    pass

                if event.ui_element == miinus:
                    try:
                        if sums[-1] not in marks:
                            sums = sums + "-"
                            disp = disp + "-"
                            print(sums)
                    except:
                        pass

                if event.ui_element == jaga:
                    try:
                        if sums[-1] not in marks:
                            sums = sums + "/"
                            disp = disp + "÷"
                            print(sums)
                    except:
                        pass

                if event.ui_element == korruta:
                    try:
                        if sums[-1] not in marks:
                            sums = sums + "*"
                            disp = disp + "x"
                            print(sums)
                    except:
                        pass

                if event.ui_element == astenda:
                    try:
                        if sums[-1] not in marks:
                            sums = str(eval(sums) ** 2)
                            disp = sums
                            print(sums)
                    except:
                        pass

                if event.ui_element == ruutjuur:
                    try:
                        if sums[-1] not in marks:
                            sums = str(math.sqrt(eval(sums)))
                            disp = sums
                            print(sums)
                    except:
                        pass

                if event.ui_element == kustuta:
                    sums = sums[:-1]
                    disp = disp[:-1]
                    print(sums)

                if event.ui_element == clear:
                    sums = ""
                    disp = ""
                    print(sums)

                if event.ui_element == equal:
                    try:
                        if sums[-1] not in marks:
                            try:
                                sums = str(eval(sums))
                                disp = sums
                                print(sums)
                            except:
                                sums = "0"
                                disp = "ERROR"
                    except:
                        pass

                if event.ui_element == point:
                    try:
                        if sums[-1] not in marks:
                            sums = sums + "."
                            disp = disp + "."
                            print(sums)
                    except:
                        pass
                # Numbrid
                if event.ui_element == seitse:
                    sums = sums + "7"
                    disp = disp + "7"
                    print(sums)
                if event.ui_element == kaheksa:
                    sums = sums + "8"
                    disp = disp + "8"
                    print(sums)
                if event.ui_element == uheksa:
                    sums = sums + "9"
                    disp = disp + "9"
                    print(sums)

                if event.ui_element == neli:
                    sums = sums + "4"
                    disp = disp + "4"
                    print(sums)
                if event.ui_element == viis:
                    sums = sums + "5"
                    disp = disp + "5"
                    print(sums)
                if event.ui_element == kuus:
                    sums = sums + "6"
                    disp = disp + "6"
                    print(sums)

                if event.ui_element == uks:
                    sums = sums + "1"
                    disp = disp + "1"
                    print(sums)
                if event.ui_element == kaks:
                    sums = sums + "2"
                    disp = disp + "2"
                    print(sums)
                if event.ui_element == kolm:
                    sums = sums + "3"
                    disp = disp + "3"
                    print(sums)

                if event.ui_element == null:
                    sums = sums + "0"
                    disp = disp + "0"
                    print(sums)

            manager.process_events(event)

        manager.update(time_delta)

        pygame.draw.rect(background, (69, 73, 78), (2, 2, 196, 46), 0, 5)
        pygame.draw.rect(background, (221, 221, 221), (2, 2, 196, 46), 1, 5)

        background.blit(
            pygame.font.SysFont("arial", 16, bold=False, italic=False).render(f"{disp}", True, [197, 203, 216]),
            [10, 16])

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == '__main__':
    main()
