import pygame

class Hero:
    def __init__(self):
        self.heroPNG = pygame.image.load("img/Hero_all.png")

    def lookS(self):
        w.blit(self.heroPNG, (0, 0), (16, 48, 16, 16))