import pygame
import random
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
dblue = (9, 56, 90)
blue = (25, 76, 106)
lblue = (0, 193, 237)

dis_width = 640
dis_height = 480

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 20

fimg = pygame.image.load("food.png")

foodimg = fimg

mi = -1

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 50)

PULSEEVENT, pt = pygame.USEREVENT+1, 250

pygame.time.set_timer(PULSEEVENT, pt)

TIMER, tt = pygame.USEREVENT+2, 1000

pygame.time.set_timer(TIMER, tt)


def your_score(score):
    value = score_font.render(str(score), True, dblue)
    dis.blit(value, [dis_width / 2, dis_height / 2])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():

    global foodimg
    paused = False
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    ind = 0

    Timer = 0

    x1_change = 0
    y1_change = 0

    snake_List = []

    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_over:

        while paused:
            dis.fill(blue)
            message("Paused", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == PULSEEVENT:
                if ind == 0:
                    foodimg = pygame.image.load("food.png")
                    ind = 1
                else:
                    foodimg = pygame.transform.scale(pygame.image.load("food.png"), [15, 15])
                    ind = 0
            if event.type == TIMER:
                Timer += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True

                global mi

                if event.key == pygame.K_LEFT and mi != 1:
                    x1_change = -snake_block
                    y1_change = 0
                    mi = 0
                elif event.key == pygame.K_RIGHT and mi != 0:
                    x1_change = snake_block
                    y1_change = 0
                    mi = 1
                elif event.key == pygame.K_UP and mi != 3:
                    y1_change = -snake_block
                    x1_change = 0
                    mi = 2
                elif event.key == pygame.K_DOWN and mi != 2:
                    y1_change = snake_block
                    x1_change = 0
                    mi = 3

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        # pygame.draw.rect(dis, lblue, [foodx, foody, snake_block, snake_block])

        dis.blit(foodimg, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        your_score(length_of_snake - 1)
        our_snake(snake_block, snake_List)

        dis.blit(pygame.font.Font(None, 30).render(f"Time: {Timer}", True, [255, 255, 255]), [10, 10])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Esc-Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            mi = -1

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
