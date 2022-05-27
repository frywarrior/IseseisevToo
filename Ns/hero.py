import pygame


class Hero:
    def __init__(self, display, location, screenpos):
        self.heroPNG = pygame.image.load("img/Hero_all.png")
        self.bg = pygame.image.load("img/Veiled_Village.png")
        self.display = display
        self.x = location[0]
        self.y = location[1]
        self.sc_x = screenpos[0]
        self.sc_y = screenpos[1]
        self.speed = 3

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
            self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroD[0])
        elif Hero.heroLoc == 1:
            self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroU[0])
        elif Hero.heroLoc == 2:
            self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroL[0])
        elif Hero.heroLoc == 3:
            self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroR[0])

    def look(self, direction):
        if direction == 'S':
            Hero.heroLoc = 0
            if Hero.heroDC == 0:
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroD[3])
            elif Hero.heroDC == 1:
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroD[1])

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
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroU[3])
            elif Hero.heroUC == 1:
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroU[1])

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
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroL[3])
            elif Hero.heroLC == 1:
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroL[1])

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
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroR[3])
            elif Hero.heroRC == 1:
                self.display.blit(self.heroPNG, (self.x, self.y), Hero.heroR[1])

            Hero.CDC += 1

            if Hero.CDC == Hero.CDC_Time and Hero.heroRC == 0:
                Hero.heroRC = 1
                Hero.CDC = 0
            elif Hero.CDC == Hero.CDC_Time and Hero.heroRC == 1:
                Hero.heroRC = 0
                Hero.CDC = 0

    def move(self, direction):
        if direction == 'S':
            self.sc_y -= self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'W':
            self.sc_y += self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'A':
            self.sc_x += self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))
        elif direction == 'D':
            self.sc_x -= self.speed
            self.display.blit(self.bg, (self.sc_x, self.sc_y))

    def update(self):
        self.display.blit(self.bg, (self.sc_x, self.sc_y))
        Hero.CDC = 0
