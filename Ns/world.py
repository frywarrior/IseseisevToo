import pygame
from objects import Obj


class Hero:
    def __init__(self, display, location, screenpos):
        self.heroPNG = pygame.image.load("img/Hero_all.png")
        self.bg = pygame.image.load("img/map.png")
        self.display = display
        self.x = location[0]
        self.y = location[1]
        self.sc_x = screenpos[0]
        self.sc_y = screenpos[1]
        self.rect = pygame.rect.Rect(self.x, self.y, 16, 16)
        self.hitrect = pygame.rect.Rect(self.x, self.y + 11, 16, 5)
        self.speed = 3
        # Objectid
        self.pub_door = Obj(self.display, self.speed, (self.sc_x, self.sc_y), self.rect,
                            pygame.image.load("img/map.png"),
                            (288, 434, 24, 20), (88, -16, 24, 20))

    CDC_Time = 4
    CDC = 0
    heroR = ((16, 0, 16, 16), (0, 0, 16, 16), (16, 0, 16, 16), (32, 0, 16, 16))
    heroRC = 0
    heroL = ((16, 16, 16, 16), (0, 16, 16, 16), (16, 16, 16, 16), (32, 16, 16, 16))
    heroLC = 0
    heroU = ((16, 32, 16, 16), (0, 32, 16, 16), (16, 32, 16, 16), (32, 32, 16, 16))
    heroUC = 0
    heroD = ((16, 48, 16, 16), (0, 48, 16, 16), (16, 48, 16, 16), (32, 48, 16, 16))
    heroDC = 0
    heroMisc = ((0, 64, 16, 16), (16, 64, 16, 16), (32, 64, 16, 16))

    heroLoc = 0

    def stand(self):
        if Hero.heroLoc == 0:
            self.display.blit(self.heroPNG, self.rect, Hero.heroD[0])
        elif Hero.heroLoc == 1:
            self.display.blit(self.heroPNG, self.rect, Hero.heroU[0])
        elif Hero.heroLoc == 2:
            self.display.blit(self.heroPNG, self.rect, Hero.heroL[0])
        elif Hero.heroLoc == 3:
            self.display.blit(self.heroPNG, self.rect, Hero.heroR[0])

    def look(self, direction):
        if direction == 'S':
            Hero.heroLoc = 0
            if Hero.heroDC == 0:
                self.display.blit(self.heroPNG, self.rect, Hero.heroD[3])
            elif Hero.heroDC == 1:
                self.display.blit(self.heroPNG, self.rect, Hero.heroD[1])

            Hero.CDC += 1

            if Hero.CDC == Hero.CDC_Time and Hero.heroDC == 0:
                Hero.heroDC = 1
                Hero.CDC = 0
            elif Hero.CDC == Hero.CDC_Time and Hero.heroDC == 1:
                Hero.heroDC = 0
                Hero.CDC = 0

        elif direction == 'W':
            Hero.heroLoc = 1
            if Hero.heroUC == 0:
                self.display.blit(self.heroPNG, self.rect, Hero.heroU[3])
            elif Hero.heroUC == 1:
                self.display.blit(self.heroPNG, self.rect, Hero.heroU[1])

            Hero.CDC += 1

            if Hero.CDC == Hero.CDC_Time and Hero.heroUC == 0:
                Hero.heroUC = 1
                Hero.CDC = 0
            elif Hero.CDC == Hero.CDC_Time and Hero.heroUC == 1:
                Hero.heroUC = 0
                Hero.CDC = 0

        elif direction == 'A':
            Hero.heroLoc = 2
            if Hero.heroLC == 0:
                self.display.blit(self.heroPNG, self.rect, Hero.heroL[3])
            elif Hero.heroLC == 1:
                self.display.blit(self.heroPNG, self.rect, Hero.heroL[1])

            Hero.CDC += 1

            if Hero.CDC == Hero.CDC_Time and Hero.heroLC == 0:
                Hero.heroLC = 1
                Hero.CDC = 0
            elif Hero.CDC == Hero.CDC_Time and Hero.heroLC == 1:
                Hero.heroLC = 0
                Hero.CDC = 0

        elif direction == 'D':
            Hero.heroLoc = 3
            if Hero.heroRC == 0:
                self.display.blit(self.heroPNG, self.rect, Hero.heroR[3])
            elif Hero.heroRC == 1:
                self.display.blit(self.heroPNG, self.rect, Hero.heroR[1])

            Hero.CDC += 1

            if Hero.CDC == Hero.CDC_Time and Hero.heroRC == 0:
                Hero.heroRC = 1
                Hero.CDC = 0
            elif Hero.CDC == Hero.CDC_Time and Hero.heroRC == 1:
                Hero.heroRC = 0
                Hero.CDC = 0

    def move(self, direction):
        if direction == 'S' and self.sc_y > -576 and self.rect.y == 66:  # map height -144 ehk dummy surfaci korgus
            self.sc_y -= self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'S' and self.sc_y <= -576 or direction == 'S' and self.rect.y < 66:
            self.rect.move_ip(0, self.speed)

        #

        if direction == 'W' and self.sc_y < -1 and self.rect.y == 66:  # koigil sama
            self.sc_y += self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'W' and self.sc_y >= -1 or direction == 'W' and self.rect.y > 66:
            self.rect.move_ip(0, -self.speed)
        #

        if direction == 'A' and self.sc_x < -2 and self.rect.x == 72:  # koigil sama
            self.sc_x += self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'A' and self.sc_x >= -2 or direction == 'A' and self.rect.x > 72:
            self.rect.move_ip(-self.speed, 0)
        #

        if direction == 'D' and self.sc_x > -560 and self.rect.x == 72:  # map width - 160 ehk dummy surfaci laius
            self.sc_x -= self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'D' and self.sc_x <= -560 or direction == 'D' and self.rect.x < 72:
            self.rect.move_ip(self.speed, 0)
        #
        self.pub_door.main(direction)
        #
        self.display.blit(self.bg, (self.sc_x, self.sc_y))

    def update(self):
        self.display.blit(self.bg, (self.sc_x, self.sc_y))
        self.display.blit(self.bg, self.pub_door.rect, self.pub_door.imgpos)
        Hero.CDC = 0

    def dispos(self):
        return self.sc_x, self.sc_y

    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.move('S')
            self.look('S')
        elif keys[pygame.K_UP]:
            self.move('W')
            self.look('W')
        elif keys[pygame.K_LEFT]:
            self.move('A')
            self.look('A')
        elif keys[pygame.K_RIGHT]:
            self.move('D')
            self.look('D')
        else:
            self.update()
            self.stand()

    def pub_collide(self):
        if self.pub_door.rect.colliderect(self.hitrect):
            self.sc_y -= 3 * self.speed
            self.pub_door.enter_pub('W')
            print('asukoht: pub')
            return True
