# importib Pygame
import pygame

#
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (0, 255, 255)
# lisab pacmani logo
Trollicon = pygame.image.load('images/pacman.png')
pygame.display.set_icon(Trollicon)

TIMER, tt = pygame.USEREVENT+2, 1000

pygame.time.set_timer(TIMER, tt)

# Seina klass
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


def setupRoomOne(all_sprites_list):  # teeb leveli
    wall_list = pygame.sprite.RenderPlain()

    # Seinad
    walls = [[0, 0, 6, 600],
             [0, 0, 600, 6],
             [0, 600, 606, 6],
             [600, 0, 6, 606],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    # Teeb seinad
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)
    return wall_list


# lisab otsijate alguse kasti värava
def setupGate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, white))
    all_sprites_list.add(gate)
    return gate


# punktid, söök
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


# mängija klass
class Player(pygame.sprite.Sprite):
    # määrab kiiruse
    change_x = 0
    change_y = 0

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.prev_x = x
        self.prev_y = y

    # pacmani pööramine
    def updateimg(self, degrees):
        img = pygame.image.load("images/pacman.png")
        self.image = pygame.transform.rotate(img, degrees)

    # kustutab mängija kiiruse
    def prevdirection(self):
        self.prev_x = self.change_x
        self.prev_y = self.change_y

    # muudab mäbgija positsiooni
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    # uuendab asukohta
    def update(self, walls, gate):
        old_x = self.rect.left
        new_x = old_x + self.change_x

        self.rect.left = new_x
        old_y = self.rect.top
        new_y = old_y + self.change_y

        x_collide = pygame.sprite.spritecollide(self, walls, False)
        if x_collide:
            self.rect.left = old_x
        else:
            self.rect.top = new_y
            y_collide = pygame.sprite.spritecollide(self, walls, False)
            if y_collide:
                self.rect.top = old_y

        if gate:  # kui värav on tõene
            gate_hit = pygame.sprite.spritecollide(self, gate, False)
            if gate_hit:
                self.rect.left = old_x
                self.rect.top = old_y


# Inheritime Player klassist
class Ghost(Player):
    def changespeed(self, listt, ghost, turn, steps, le):
        try:
            z = listt[turn][2]
            if steps < z:
                self.change_x = listt[turn][0]
                self.change_y = listt[turn][1]
                steps += 1
            else:
                if turn < le:
                    turn += 1
                elif ghost == "clyde":
                    turn = 2
                else:
                    turn = 0
                self.change_x = listt[turn][0]
                self.change_y = listt[turn][1]
                steps = 0
            return [turn, steps]
        except IndexError:
            return [0, 0]


# kuhu otsija liigub
Pinky_directions = [
    [0, -30, 4],
    [15, 0, 9],
    [0, 15, 11],
    [-15, 0, 23],
    [0, 15, 7],
    [15, 0, 3],
    [0, -15, 3],
    [15, 0, 19],
    [0, 15, 3],
    [15, 0, 3],
    [0, 15, 3],
    [15, 0, 3],
    [0, -15, 15],
    [-15, 0, 7],
    [0, 15, 3],
    [-15, 0, 19],
    [0, -15, 11],
    [15, 0, 9]
]
# kuhu otsija liigub
Blinky_directions = [
    [0, -15, 4],
    [15, 0, 9],
    [0, 15, 11],
    [15, 0, 3],
    [0, 15, 7],
    [-15, 0, 11],
    [0, 15, 3],
    [15, 0, 15],
    [0, -15, 15],
    [15, 0, 3],
    [0, -15, 11],
    [-15, 0, 3],
    [0, -15, 11],
    [-15, 0, 3],
    [0, -15, 3],
    [-15, 0, 7],
    [0, -15, 3],
    [15, 0, 15],
    [0, 15, 15],
    [-15, 0, 3],
    [0, 15, 3],
    [-15, 0, 3],
    [0, -15, 7],
    [-15, 0, 3],
    [0, 15, 7],
    [-15, 0, 11],
    [0, -15, 7],
    [15, 0, 5]
]
# kuhu otsija liigub
Inky_directions = [
    [30, 0, 2],
    [0, -15, 4],
    [15, 0, 10],
    [0, 15, 7],
    [15, 0, 3],
    [0, -15, 3],
    [15, 0, 3],
    [0, -15, 15],
    [-15, 0, 15],
    [0, 15, 3],
    [15, 0, 15],
    [0, 15, 11],
    [-15, 0, 3],
    [0, -15, 7],
    [-15, 0, 11],
    [0, 15, 3],
    [-15, 0, 11],
    [0, 15, 7],
    [-15, 0, 3],
    [0, -15, 3],
    [-15, 0, 3],
    [0, -15, 15],
    [15, 0, 15],
    [0, 15, 3],
    [-15, 0, 15],
    [0, 15, 11],
    [15, 0, 3],
    [0, -15, 11],
    [15, 0, 11],
    [0, 15, 3],
    [15, 0, 1],
]
# kuhu otsija liigub
Clyde_directions = [
    [-30, 0, 2],
    [0, -15, 4],
    [15, 0, 5],
    [0, 15, 7],
    [-15, 0, 11],
    [0, -15, 7],
    [-15, 0, 3],
    [0, 15, 7],
    [-15, 0, 7],
    [0, 15, 15],
    [15, 0, 15],
    [0, -15, 3],
    [-15, 0, 11],
    [0, -15, 7],
    [15, 0, 3],
    [0, -15, 11],
    [15, 0, 9],
]
# otsijate liikumise suund
pl = len(Pinky_directions) - 1
bl = len(Blinky_directions) - 1
il = len(Inky_directions) - 1
cl = len(Clyde_directions) - 1

# initsialiseerimine
pygame.init()

# Teeb 606x606 suuruse ekraani
screen = pygame.display.set_mode([606, 606])

# Lisab  mängu kasti üles vasakusse äärde "Pacman"
pygame.display.set_caption('Pacman')

# Teeb ekraani
background = pygame.Surface(screen.get_size())
background = background.convert()
# Värvib tausta mustaks
background.fill(black)
# fpsi jaoks
clock = pygame.time.Clock()

# Font
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 24)

# Alguse asukohad pacmanile ja otsijatele
w = 303 - 16  # Laius
p_h = (7 * 60) + 19  # Pacmani Suurus
m_h = (4 * 60) + 19  # otsija Suurus
b_h = (3 * 60) + 19  # otsija Suurus
i_w = 303 - 16 - 32  # otsija Suurus
c_w = 303 + (32 - 16)  # otsija Suurus


def startGame():  # mängu põhi funktsioon
    # seab vajalikud muutujad
    all_sprites_list = pygame.sprite.RenderPlain()

    block_list = pygame.sprite.RenderPlain()

    monsta_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setupRoomOne(all_sprites_list)

    gate = setupGate(all_sprites_list)

    p_turn = 0
    p_steps = 0

    b_turn = 0
    b_steps = 0

    i_turn = 0
    i_steps = 0

    c_turn = 0
    c_steps = 0

    pygame.mixer.music.set_volume(0.2)

    pygame.mixer.music.load('images/kann.mp3')
    pygame.mixer.music.play(-1)

    # Mängija pacmani kujutis
    Pacman = Player(w, p_h, "images/pacman.png")
    all_sprites_list.add(Pacman)
    pacman_collide.add(Pacman)
    # üks otsijatest
    Blinky = Ghost(w, b_h, "images/ual.png")
    monsta_list.add(Blinky)
    all_sprites_list.add(Blinky)
    # üks otsijatest
    Pinky = Ghost(w, m_h, "images/cartman.png")
    monsta_list.add(Pinky)
    all_sprites_list.add(Pinky)
    # üks otsijatest
    Inky = Ghost(i_w, m_h, "images/marke.png")
    monsta_list.add(Inky)
    all_sprites_list.add(Inky)
    # üks otsijatest
    Clyde = Ghost(c_w, m_h, "images/bjorn.png")
    monsta_list.add(Clyde)
    all_sprites_list.add(Clyde)

    # joonistab kõik söögi
    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(yellow, 4, 4)
                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    # Lisab söögi kõikide asjade listi
                    block_list.add(block)
                    all_sprites_list.add(block)

    bll = len(block_list)

    score = 0
    Timer = 0

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == TIMER:
                Timer += 1
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:  # Mängija liikumine
                if event.key == pygame.K_LEFT:  # liigub vasakule
                    Pacman.changespeed(-30, 0)  # seab positsiooni x-30 pixlit
                    Pacman.updateimg(180)
                if event.key == pygame.K_RIGHT:  # liigub vasakule
                    Pacman.changespeed(30, 0)  # seab positsiooni y30 pixlit
                    Pacman.updateimg(0)
                if event.key == pygame.K_UP:  # liigub üles
                    Pacman.changespeed(0, -30)
                    Pacman.updateimg(90)
                if event.key == pygame.K_DOWN:  # liigub alla
                    Pacman.changespeed(0, 30)
                    Pacman.updateimg(-90)

                if event.key == pygame.K_a:  # cheat
                    Pacman.changespeed(-60, 0)
                    Pacman.updateimg(180)  # cheat
                if event.key == pygame.K_d:
                    Pacman.changespeed(60, 0)
                    Pacman.updateimg(0)
                if event.key == pygame.K_w:
                    Pacman.changespeed(0, -60)
                    Pacman.updateimg(90)
                if event.key == pygame.K_s:
                    Pacman.changespeed(0, 60)
                    Pacman.updateimg(-90)

            # et pacman lõpmatuseni ei liiguks
            if event.type == pygame.KEYUP:  #
                if event.key == pygame.K_LEFT:
                    Pacman.changespeed(30, 0)
                if event.key == pygame.K_RIGHT:
                    Pacman.changespeed(-30, 0)
                if event.key == pygame.K_UP:
                    Pacman.changespeed(0, 30)
                if event.key == pygame.K_DOWN:
                    Pacman.changespeed(0, -30)

                if event.key == pygame.K_a:
                    Pacman.changespeed(60, 0)
                if event.key == pygame.K_d:
                    Pacman.changespeed(-60, 0)
                if event.key == pygame.K_w:
                    Pacman.changespeed(0, 60)
                if event.key == pygame.K_s:
                    Pacman.changespeed(0, -60)
                #

        # KÕIK EVENDID LÄHEVAD SELLE REA ÜLES

        # KÕIK MÄNGU LOOGIKA LÄHEB SELLE REA ALLA
        Pacman.update(wall_list, gate)

        returned = Pinky.changespeed(Pinky_directions, False, p_turn, p_steps, pl)
        p_turn = returned[0]
        p_steps = returned[1]
        Pinky.changespeed(Pinky_directions, False, p_turn, p_steps, pl)
        Pinky.update(wall_list, False)

        returned = Blinky.changespeed(Blinky_directions, False, b_turn, b_steps, bl)
        b_turn = returned[0]
        b_steps = returned[1]
        Blinky.changespeed(Blinky_directions, False, b_turn, b_steps, bl)
        Blinky.update(wall_list, False)

        returned = Inky.changespeed(Inky_directions, False, i_turn, i_steps, il)
        i_turn = returned[0]
        i_steps = returned[1]
        Inky.changespeed(Inky_directions, False, i_turn, i_steps, il)
        Inky.update(wall_list, False)

        returned = Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        c_turn = returned[0]
        c_steps = returned[1]
        Clyde.changespeed(Clyde_directions, "clyde", c_turn, c_steps, cl)
        Clyde.update(wall_list, False)

        # Kui pacman on millegiga kokku puutunud
        blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)

        # kui pacman sööb täpi ära skoor läheb üles
        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        # KÕIK MÄNGU LOOGIKA LÄHEB SELLE REA ÜLES

        # KÕIK JOONISTAMINE LÄHEB SELLE REA ALLA
        screen.fill(black)
        # Joonistab tausta
        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monsta_list.draw(screen)
        # skoor
        text = font.render("Score: " + str(score) + "/" + str(bll), True, red)
        timer = font.render("Time: " + str(Timer), True, green)
        screen.blit(text, [10, 10])
        screen.blit(timer, [200, 10])
        # Kui koik pallid on korjatud tuleb kiri "You WOn"
        if score == bll:
            doNext("Congratulations, you won!", 145, all_sprites_list, block_list, monsta_list, pacman_collide,
                   wall_list, gate)
        # kui pacman läheb tagaotsjatele pihta
        monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)
        # kui pacman läheb tagaotsjatele pihta
        if monsta_hit_list:
            doNext("Game Over", 235, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate)

        # KÕIK JOONISTAMINE LÄHEB SELLE REA ÜLES
        # uuendab ekraani
        pygame.display.flip()
        # fps
        clock.tick(10)


#
def doNext(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    while True:
        # KÕIK EVENDID LÄHEVAD SELLE REA ALLA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    startGame()

        # Hall taust
        pygame.mixer.music.stop()
        win = pygame.Surface((400, 200))  # Ekraani suurus
        win.set_alpha(10)  # Läbipaistvus
        win.fill((128, 128, 128))  # Täidab ekraani halliga
        screen.blit(win, (100, 200))  # Ekraani asukoht kus joonistab

        # Võitis või kaotas
        text1 = font.render(message, True, white)
        screen.blit(text1, [left, 233])
        # kui saad surma tuleb text kas "Vajutada enter ja mangida uuesti" või "vajutada ESC ja panna mäng kinni"
        text2 = font.render("To play again, press ENTER.", True, white)
        screen.blit(text2, [135, 303])
        text3 = font.render("To quit, press ESCAPE.", True, white)
        screen.blit(text3, [165, 333])
        # uuendab ekraani
        pygame.display.flip()
        # fps
        clock.tick(10)


startGame()

pygame.quit()
