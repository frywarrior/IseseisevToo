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
        #

        if direction == 'W' and self.sc_y < -1 and self.player.y == 66:
            self.rect.move_ip(0, self.speed)
            self.display.blit(self.img, self.rect, self.imgpos)
        #

        if direction == 'A' and self.sc_x < -2 and self.player.x == 72:
            self.rect.move_ip(self.speed, 0)
            self.display.blit(self.img, self.rect, self.imgpos)

        #

        if direction == 'D' and self.sc_x > -560 and self.player.x == 72:
            self.rect.move_ip(-self.speed, 0)
            self.display.blit(self.img, self.rect, self.imgpos)

        #

        #
        self.display.blit(self.img, self.rect, self.imgpos)
