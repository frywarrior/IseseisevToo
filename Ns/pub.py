import pygame

from objects import Obj


class Pub:

    def __init__(self, display, location, screenpos):
        self.heroPNG = pygame.image.load("img/Hero_all.png")
        self.bg = pygame.image.load("img/NPub.png")
        self.display = display
        self.x = location[0]
        self.y = location[1]
        self.sc_x = screenpos[0]
        self.sc_y = screenpos[1]
        self.rect = pygame.rect.Rect(self.x, self.y, 16, 16)
        self.speed = 3
        # Objectid
        self.pub_door = Obj(self.display, self.speed, (self.sc_x, self.sc_y), self.rect,
                            self.bg,
                            (96, 143, 16, 16), (71, 83, 16, 16))

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

    heroLoc = 1

    def stand(self):
        if Pub.heroLoc == 0:
            self.display.blit(self.heroPNG, self.rect, Pub.heroD[0])
        elif Pub.heroLoc == 1:
            self.display.blit(self.heroPNG, self.rect, Pub.heroU[0])
        elif Pub.heroLoc == 2:
            self.display.blit(self.heroPNG, self.rect, Pub.heroL[0])
        elif Pub.heroLoc == 3:
            self.display.blit(self.heroPNG, self.rect, Pub.heroR[0])

    def look(self, direction):
        if direction == 'S':
            Pub.heroLoc = 0
            if Pub.heroDC == 0:
                self.display.blit(self.heroPNG, self.rect, Pub.heroD[3])
            elif Pub.heroDC == 1:
                self.display.blit(self.heroPNG, self.rect, Pub.heroD[1])

            Pub.CDC += 1

            if Pub.CDC == Pub.CDC_Time and Pub.heroDC == 0:
                Pub.heroDC = 1
                Pub.CDC = 0
            elif Pub.CDC == Pub.CDC_Time and Pub.heroDC == 1:
                Pub.heroDC = 0
                Pub.CDC = 0

        elif direction == 'W':
            Pub.heroLoc = 1
            if Pub.heroUC == 0:
                self.display.blit(self.heroPNG, self.rect, Pub.heroU[3])
            elif Pub.heroUC == 1:
                self.display.blit(self.heroPNG, self.rect, Pub.heroU[1])

            Pub.CDC += 1

            if Pub.CDC == Pub.CDC_Time and Pub.heroUC == 0:
                Pub.heroUC = 1
                Pub.CDC = 0
            elif Pub.CDC == Pub.CDC_Time and Pub.heroUC == 1:
                Pub.heroUC = 0
                Pub.CDC = 0

        elif direction == 'A':
            Pub.heroLoc = 2
            if Pub.heroLC == 0:
                self.display.blit(self.heroPNG, self.rect, Pub.heroL[3])
            elif Pub.heroLC == 1:
                self.display.blit(self.heroPNG, self.rect, Pub.heroL[1])

            Pub.CDC += 1

            if Pub.CDC == Pub.CDC_Time and Pub.heroLC == 0:
                Pub.heroLC = 1
                Pub.CDC = 0
            elif Pub.CDC == Pub.CDC_Time and Pub.heroLC == 1:
                Pub.heroLC = 0
                Pub.CDC = 0

        elif direction == 'D':
            Pub.heroLoc = 3
            if Pub.heroRC == 0:
                self.display.blit(self.heroPNG, self.rect, Pub.heroR[3])
            elif Pub.heroRC == 1:
                self.display.blit(self.heroPNG, self.rect, Pub.heroR[1])

            Pub.CDC += 1

            if Pub.CDC == Pub.CDC_Time and Pub.heroRC == 0:
                Pub.heroRC = 1
                Pub.CDC = 0
            elif Pub.CDC == Pub.CDC_Time and Pub.heroRC == 1:
                Pub.heroRC = 0
                Pub.CDC = 0

    def move(self, direction):
        if direction == 'S' and self.sc_y > -72 and self.rect.y == 66:
            self.sc_y -= self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'S' and self.sc_y <= -72 or direction == 'S' and self.rect.y < 66:
            self.rect.move_ip(0, self.speed)
        #

        if direction == 'W' and self.sc_y < -1 and self.rect.y == 66:
            self.sc_y += self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'W' and self.sc_y >= -1 or direction == 'W' and self.rect.y > 66:
            self.rect.move_ip(0, -self.speed)
        #

        if direction == 'A' and self.sc_x < -2 and self.rect.x == 72:
            self.sc_x += self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'A' and self.sc_x >= -2 or direction == 'A' and self.rect.x > 72:
            self.rect.move_ip(-self.speed, 0)
        #

        if direction == 'D' and self.sc_x > -42 and self.rect.x == 72:
            self.sc_x -= self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'D' and self.sc_x <= -42 or direction == 'D' and self.rect.x < 72:
            self.rect.move_ip(self.speed, 0)
        #
        self.pub_door.main(direction)
        #
        self.display.blit(self.bg, (self.sc_x, self.sc_y))

    def update(self):
        self.display.blit(self.bg, (self.sc_x, self.sc_y))
        self.display.blit(self.bg, self.pub_door.rect, self.pub_door.imgpos)
        Pub.CDC = 0

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
        if self.pub_door.rect.colliderect(self.rect):
            self.sc_y += 3 * self.speed
            self.pub_door.enter_pub('S')
            print('yep')
            return True
