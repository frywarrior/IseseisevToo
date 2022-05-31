import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()


class Snekhead:
    def __init__(self, loc):
        self.rect = (loc[0], loc[1], 10, 10)

    def draw(self):
        pygame.draw.rect(screen, [100, 100, 100], self.rect)


snake_speed = 5

ind = 0

snake = []

snake.append(Snekhead([320, 240]))

gameover = False
while not gameover:
    clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

    screen.fill([0, 0, 0])

    for i in snake:
        i.draw()
        ind += 1



    pygame.display.flip()

