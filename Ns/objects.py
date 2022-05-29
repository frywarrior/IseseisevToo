import pygame


class Obj:
    def __init__(self, display, speed, screenpos, player, img, imgpos, rect):
        self.display = display
        self.speed = speed
        self.sc_x = screenpos[0]
        self.sc_y = screenpos[1]
        #
        #
        self.player = player
        self.img = img
        self.imgpos = imgpos
        self.rect = pygame.Rect(rect)

    def main(self, direction):
        if direction == 'S' and self.sc_y > -576 and self.player.y == 66:
            self.rect.move_ip(0, -self.speed)
            self.display.blit(self.img, self.rect, self.imgpos)
        elif direction == 'S' and self.sc_y > -576 and self.player.y == 63:
            self.rect.move_ip(0, self.speed)
        #

        if direction == 'W' and self.sc_y < -1 and self.player.y == 66:
            self.rect.move_ip(0, self.speed)
            self.display.blit(self.img, self.rect, self.imgpos)
        elif direction == 'W' and self.sc_y < -1 and self.player.y == 69:
            self.rect.move_ip(0, -self.speed)
        #

        if direction == 'A' and self.sc_x < -2 and self.player.x == 72:
            self.rect.move_ip(self.speed, 0)
            self.display.blit(self.img, self.rect, self.imgpos)
        elif direction == 'A' and self.sc_x < -2 and self.player.x == 75:
            self.rect.move_ip(-self.speed, 0)
        #

        if direction == 'D' and self.sc_x > -560 and self.player.x == 72:
            self.rect.move_ip(-self.speed, 0)
            self.display.blit(self.img, self.rect, self.imgpos)
        elif direction == 'D' and self.sc_x > -560 and self.player.x == 69:
            self.rect.move_ip(self.speed, 0)
        #

        #
        self.display.blit(self.img, self.rect, self.imgpos)

    def enter_pub(self, direction):
        if direction == 'S':
            self.rect.move_ip(0, 3 * self.speed)
        if direction == 'W':
            self.rect.move_ip(0, 3 * -self.speed)
        if direction == 'A':
            self.rect.move_ip(3 * -self.speed, 0)
        if direction == 'D':
            self.rect.move_ip(3 * self.speed, 0)
