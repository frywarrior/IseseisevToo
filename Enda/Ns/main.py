# Franco Kikkas IS21, Lis ns kuna igav
import pygame
from world import Hero
from pub import Pub as Pubd
from Escmenu import escmenu


def main():
    def draw():
        frame = pygame.transform.scale(screen, (screen_x, screen_y))
        window.blit(frame, frame.get_rect())
        pygame.display.flip()

    def loop():
        # fps
        clock.tick(30)
        # mängu sulgemine ristist
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                quit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                pos = list(pygame.mouse.get_pos())
                # take the mouse position and scale it, too
                ratio_x = (window_rect.width / screen_rect.width)
                ratio_y = (window_rect.height / screen_rect.height)
                scaled_pos = ((pos[0] / ratio_x) - hero.sc_x, (pos[1] / ratio_y) - hero.sc_y)

                print(scaled_pos)
                print(pygame.mouse.get_pos())
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    escmenu(window)

    pygame.init()

    # ekraani seaded
    screen_x = 640
    screen_y = 480
    screen_pos_x, screen_pos_y = -200, -450

    window = pygame.display.set_mode([screen_x, screen_y])
    window_rect = window.get_rect()

    screen = pygame.Surface([160, 144])
    screen_rect = screen.get_rect()

    pygame.display.set_caption("Game_Test")
    clock = pygame.time.Clock()
    #

    # graafika laadimine

    hero = Hero(screen, (72, 66), (screen_pos_x, screen_pos_y))
    Pub = Pubd(screen, (72, 66), (-21, -60))

    #
    gameover = False

    world = True
    pub = False
    while not gameover:
        while world:
            loop()

            hero.moving()
            if hero.pub_collide():
                world = False
                pub = True
                screen.fill([0, 0, 0])
            draw()

        while pub:
            loop()
            Pub.moving()
            if Pub.pub_collide():
                world = True
                pub = False

            draw()


if __name__ == "__main__":
    main()
