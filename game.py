#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from config import *
import pygame
pygame.init()

color = (0, 128, 128)
# Pos is used to record how far a player was able to reach
pos = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
time = 0
# scr_wid and X serve the same purpose and scr_hei and Y serve the same purpose
scr_wid = 1000
scr_hei = 820
X = 1000
Y = 820
lives = [3, 3]
score = [0, 0]
level = [1, 1]
player = 0
# initializes the pygame window
win = pygame.display.set_mode((scr_wid, scr_hei))
pygame.display.set_caption('2019101065')
font = pygame.font.Font('freesansbold.ttf', 32)
# Renders the Welcome message
textaa = font.render('Welcome!', True, (255, 255, 255), (0, 0, 0))
textaaRect = textaa.get_rect()
textaaRect.center = (X // 2, Y // 2 - 50)
text = font.render('To Begin Press <ENTER>', True, (255, 255, 255), (0,
                                                                     0, 0))
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
textab = font.render('Controls: Player 1 - WASD   Player 2 - IJKL',
                     True, (255, 255, 255), (0, 0, 0))
textabRect = textab.get_rect()
textabRect.center = (X // 2, Y // 2 + 50)
run = True
# Loop to detect if RETURN was pressed
while run:
    win.fill((0, 0, 0))
    win.blit(textaa, textaaRect)
    win.blit(text, textRect)
    win.blit(textab, textabRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        run = False
    pygame.display.update()
# Renders Player 1
win.fill((0, 0, 0))
win.blit(text_config_3, text_config_3_Rect)
pygame.display.update()
pygame.time.delay(3000)

run = True
velo = 5
hei = 30
wid = 30
x = (scr_wid - wid) / 2
y = scr_hei - hei
ymax = 100
ymin = scr_hei - hei
temp_score = 0

# The class of objects which cause the player to lose a life
class death:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.side = 60
        self.vel = 0

# The function to check for collision
def coll(o):
    global x, y, wid, hei
    if o.x - x < wid and o.y - y < hei and o.x - x >= 0 and o.y - y \
            >= 0:
        return True
    elif x - o.x < o.side and y - o.y < o.side and x - o.x >= 0 and y \
            - o.y >= 0:
        return True
    elif o.x - x < wid and y - o.y < o.side and o.x - x >= 0 and y \
            - o.y >= 0:
        return True
    elif x - o.x < o.side and o.y - y < hei and x - o.x >= 0 and o.y \
            - y >= 0:
        return True
    else:
        return False

# The function which is executed when both players die
def the_end():
    win.fill((0, 0, 0))
    text2 = font.render('GAME OVER', True, (255, 255, 255), (0, 0, 0))
    text2Rect = text2.get_rect()
    text2Rect.center = (X // 2, Y // 2)

    text3 = font.render('Player 1 : Player 2', True, (255, 255, 255),
                        (0, 0, 0))
    text3Rect = text3.get_rect()
    text3Rect.center = (X // 2, Y // 2 + 50)

    text4 = font.render(str(score[0]) + ' : ' + str(score[1]), True,
                        (255, 255, 255), (0, 0, 0))
    text4Rect = text4.get_rect()
    text4Rect.center = (X // 2, Y // 2 + 100)

    run2 = True

    while run2:
        win.fill((0, 0, 0))
        win.blit(text2, text2Rect)
        win.blit(text3, text3Rect)
        win.blit(text4, text4Rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            run2 = False
        pygame.display.update()

# Resets the speed of an object passed as an argument
def speed_reset(d):
    d.vel = random.randrange(1, 8)
    d.x = 0

# Function which is executed when a player crashes into an obstacle
def ded():
    global player, scr_wid, wid, scr_hei, hei, x, y, temp_score, ymax, \
        ymin, die1, die2, die3, die4, die5, die6, die7, time
    lives[player] -= 1
    # Used to show the collision messages
    if player == 0:
        win.fill((0, 0, 0))
        win.blit(text_config_1, text_config_1_Rect)
        pygame.display.update()
        pygame.time.delay(3000)
    else:
        win.fill((0, 0, 0))
        win.blit(text_config_2, text_config_2_Rect)
        pygame.display.update()
        pygame.time.delay(3000)
    time = 0
    # Used to update the position of the player
    if player == 0:
        x = (scr_wid - wid) / 2
        y = scr_hei - hei
    else:
        x = (scr_wid - wid) / 2
        y = 100
    # Executed if a Player loses all of their lives
    if lives[player] == 0:
        player = player + 1
        win.fill((0, 0, 0))
        if player == 1:
            win.blit(text_config_4, text_config_4_Rect)
            pygame.display.update()
            pygame.time.delay(3000)
        # Resets the speeds of the obstacles for the next player
        speed_reset(die1)
        speed_reset(die2)
        speed_reset(die3)
        speed_reset(die4)
        speed_reset(die5)
        speed_reset(die6)

        pygame.display.update()
        if player >= 2:
            the_end()
    ymax = 100
    ymin = scr_hei - hei
    # Resets the position list for the next life
    pos_reset()

# Function to update the position of an object
def upd(b):
    b.x += b.vel
    b.x = b.x % scr_wid
    pygame.draw.rect(win, (200, 20, 20), (b.x, b.y, b.side, b.side))

# Scoring for Player 1
def score_upd():
    global ymin, player
    if ymin <= 100 and pos[10] == 0:
        score[player] += 10
        pos[10] = 1
    elif ymin <= 160 and pos[9] == 0:
        score[player] += 5
        pos[9] = 1
    elif ymin <= 220 and pos[8] == 0:
        score[player] += 10
        pos[8] = 1
    elif ymin <= 280 and pos[7] == 0:
        score[player] += 5
        pos[7] = 1
    elif ymin <= 340 and pos[6] == 0:
        score[player] += 10
        pos[6] = 1
    elif ymin <= 400 and pos[5] == 0:
        score[player] += 5
        pos[5] = 1
    elif ymin <= 460 and pos[4] == 0:
        score[player] += 10
        pos[4] = 1
    elif ymin <= 520 and pos[3] == 0:
        score[player] += 5
        pos[3] = 1
    elif ymin <= 580 and pos[2] == 0:
        score[player] += 10
        pos[2] = 1
    elif ymin <= 640 and pos[1] == 0:
        score[player] += 5
        pos[1] = 1
    elif ymin <= 700 and pos[0] == 0:
        score[player] += 10
        pos[0] = 1

# Scoring for Player 2
def score_upd2():
    global ymax, player
    if ymax >= 760 + 30 and pos[10] == 0:
        score[player] += 10
        pos[10] = 1
    elif ymax >= 700 + 30 and pos[9] == 0:
        score[player] += 5
        pos[9] = 1
    elif ymax >= 640 + 30 and pos[8] == 0:
        score[player] += 10
        pos[8] = 1
    elif ymax >= 580 + 30 and pos[7] == 0:
        score[player] += 5
        pos[7] = 1
    elif ymax >= 520 + 30 and pos[6] == 0:
        score[player] += 10
        pos[6] = 1
    elif ymax >= 460 + 30 and pos[5] == 0:
        score[player] += 5
        pos[5] = 1
    elif ymax >= 400 + 30 and pos[4] == 0:
        score[player] += 10
        pos[4] = 1
    elif ymax >= 340 + 30 and pos[3] == 0:
        score[player] += 5
        pos[3] = 1
    elif ymax >= 280 + 30 and pos[2] == 0:
        score[player] += 10
        pos[2] = 1
    elif ymax >= 220 + 30 and pos[1] == 0:
        score[player] += 5
        pos[1] = 1
    elif ymax >= 160 + 30 and pos[0] == 0:
        score[player] += 10
        pos[0] = 1

# Updates the maximum and minimum values of y
# Used to score the player
def y_upd():
    global y, ymax, ymin
    if y > ymax:
        ymax = y

    if y < ymin:
        ymin = y

# Resets the values in the pos list
def pos_reset():
    global ymax, ymin, scr_hei, hei
    pos[0] = 0
    pos[1] = 0
    pos[2] = 0
    pos[3] = 0
    pos[4] = 0
    pos[5] = 0
    pos[6] = 0
    pos[7] = 0
    pos[8] = 0
    pos[9] = 0
    pos[10] = 0
    ymax = 100
    ymin = scr_hei - hei

# Increases the velocity of an object passed as argument
def new_vel(c):
    c.vel = c.vel + random.randrange(1, 4)

# Creating obstacle objects
die1 = death()
die1.y = 100
die1.vel = random.randrange(1, 8)

die2 = death()
die2.y = 220
die2.vel = random.randrange(1, 8)

die3 = death()
die3.y = 340
die3.vel = random.randrange(1, 8)

die4 = death()
die4.y = 460
die4.vel = random.randrange(1, 8)

die5 = death()
die5.y = 580
die5.vel = random.randrange(1, 8)

die6 = death()
die6.y = 700
die6.vel = random.randrange(1, 8)

die7 = death()
die7.y = 160
die7.x = random.randrange(100, 900)

die8 = death()
die8.y = 280
die8.x = random.randrange(100, 900)

die9 = death()
die9.y = 400
die9.x = random.randrange(100, 900)

die10 = death()
die10.y = 520
die10.x = random.randrange(100, 900)

die11 = death()
die11.y = 640
die11.x = random.randrange(100, 900)

# PLAYER 1 LOOP

time = 0

while run:
    # Checking if quit was pressed
    pygame.time.delay(30)
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if lives[0] == 0:
        run = False
    
    # Reading player input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y >= velo + 100:
        y -= velo
    elif keys[pygame.K_w] and y < velo + 100:
        y = 100

    if keys[pygame.K_a] and x >= velo:
        x -= velo
    elif keys[pygame.K_a] and x < velo:
        x = 0

    if keys[pygame.K_s] and y <= scr_hei - velo - hei:
        y += velo
    elif keys[pygame.K_s] and y > scr_hei - velo - hei:
        y = scr_hei - hei

    if keys[pygame.K_d] and x <= scr_wid - velo - wid:
        x += velo
    elif keys[pygame.K_d] and x > scr_wid - velo - wid:
        x = scr_wid - wid

    win.fill((0, 0, 0))

    # Checking for collision
    if coll(die1):
        ded()
    elif coll(die2):
        ded()
    elif coll(die3):
        ded()
    elif coll(die4):
        ded()
    elif coll(die5):
        ded()
    elif coll(die6):
        ded()
    elif coll(die7):
        ded()
    elif coll(die8):
        ded()
    elif coll(die9):
        ded()
    elif coll(die10):
        ded()
    elif coll(die11):
        ded()
    # Updates score
    y_upd()
    score_upd()
    
    # Executes if player finishes the level
    if y == 100:
        y = scr_hei - hei
        ymax = 100
        ymin = y
        # increases velocity of obstacles
        new_vel(die1)
        new_vel(die2)
        new_vel(die3)
        new_vel(die4)
        new_vel(die5)
        new_vel(die6)
        # Resets pos list
        pos[0] = 0
        pos[1] = 0
        pos[2] = 0
        pos[3] = 0
        pos[4] = 0
        pos[5] = 0
        pos[6] = 0
        pos[7] = 0
        pos[8] = 0
        pos[9] = 0
        pos[10] = 0
        ymax = 100
        ymin = scr_hei - hei
        time += 1
        score[0] += 3000 // time
        time = 0
        level[0] += 1
        win.fill((0, 0, 0))
        win.blit(text_config_5, text_config_5_Rect)
        pygame.display.update()
        pygame.time.delay(3000)
    # Draws river
    pygame.draw.rect(win, (100, 100, 100), (0, 100, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 220, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 340, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 460, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 580, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 700, 1000, 60))
    # Updates locations of obstacles
    upd(die1)
    upd(die2)
    upd(die3)
    upd(die4)
    upd(die5)
    upd(die6)
    upd(die7)
    upd(die8)
    upd(die9)
    upd(die10)
    upd(die11)
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 1000, 100))
    # Updates Score, lives and level values in header
    texta = font.render('Lives: ' + str(lives[0])
                        + '    Player 1 Score: ' + str(score[0])
                        + '    Level: ' + str(level[0]), True, (0, 0,
                                                                0), (255, 255, 255))
    textaRect = texta.get_rect()
    textaRect.center = (X // 2, 50)
    win.blit(texta, textaRect)
    # Updates location of player
    pygame.draw.rect(win, color, (x, y, wid, hei))
    pygame.display.update()

# Adjusts locations of obstacles
die1.y = 100 + 60
die1.vel = random.randrange(1, 8)

die2.y = 220 + 60
die2.vel = random.randrange(1, 8)

die3.y = 340 + 60
die3.vel = random.randrange(1, 8)

die4.y = 460 + 60
die4.vel = random.randrange(1, 8)

die5.y = 580 + 60
die5.vel = random.randrange(1, 8)

die6.y = 700 + 60
die6.vel = random.randrange(1, 8)

die7.y = 160 + 60
die7.x = random.randrange(100, 900)

die8.y = 280 + 60
die8.x = random.randrange(100, 900)

die9.y = 400 + 60
die9.x = random.randrange(100, 900)

die10.y = 520 + 60
die10.x = random.randrange(100, 900)

die11.y = 640 + 60
die11.x = random.randrange(100, 900)

y = 100

run = True
pos_reset()
time = 0

# SECOND PLAYER LOOP
while run:
    pygame.time.delay(30)
    time += 1
    # Checks if quit was pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if lives[1] == 0:
        run = False
    # Reading player input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_i] and y >= velo + 100:
        y -= velo
    elif keys[pygame.K_i] and y < velo + 100:

        y = 100
    if keys[pygame.K_j] and x >= velo:
        x -= velo
    elif keys[pygame.K_j] and x < velo:

        x = 0
    if keys[pygame.K_k] and y <= scr_hei - velo - hei:
        y += velo
    elif keys[pygame.K_k] and y > scr_hei - velo - hei:

        y = scr_hei - hei

    if keys[pygame.K_l] and x <= scr_wid - velo - wid:
        x += velo
    elif keys[pygame.K_l] and x > scr_wid - velo - wid:
        x = scr_wid - wid

    win.fill((0, 0, 0))
    
    # Checks for collisions
    if coll(die1):
        ded()
    elif coll(die2):
        ded()
    elif coll(die3):
        ded()
    elif coll(die4):
        ded()
    elif coll(die5):
        ded()
    elif coll(die6):
        ded()
    elif coll(die7):
        ded()
    elif coll(die8):
        ded()
    elif coll(die9):
        ded()
    elif coll(die10):
        ded()
    elif coll(die11):
        ded()

    # Updates score
    y_upd()
    score_upd2()
    
    # Executes if player finishes the level
    if y == scr_hei - hei:
        y = 100
        # Increases velocity of obstacles
        new_vel(die1)
        new_vel(die2)
        new_vel(die3)
        new_vel(die4)
        new_vel(die5)
        new_vel(die6)
        # Resets pos list
        pos[0] = 0
        pos[1] = 0
        pos[2] = 0
        pos[3] = 0
        pos[4] = 0
        pos[5] = 0
        pos[6] = 0
        pos[7] = 0
        pos[8] = 0
        pos[9] = 0
        pos[10] = 0
        ymax = 100
        ymin = scr_hei - hei
        score[1] += 3000 // time
        time = 0
        level[1] += 1
        win.blit(text_config_6, text_config_6_Rect)
        pygame.display.update()
        pygame.time.delay(3000)
    # Draws rivers
    pygame.draw.rect(win, (100, 100, 100), (0, 160, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 280, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 400, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 520, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 640, 1000, 60))
    pygame.draw.rect(win, (100, 100, 100), (0, 760, 1000, 60))
    # Updates locations of obstacles
    upd(die1)
    upd(die2)
    upd(die3)
    upd(die4)
    upd(die5)
    upd(die6)
    upd(die7)
    upd(die8)
    upd(die9)
    upd(die10)
    upd(die11)
    # Updates location of player
    pygame.draw.rect(win, (200, 200, 70), (x, y, wid, hei))
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 1000, 100))
    textb = font.render('Lives: ' + str(lives[1])
                        + '    Player 2 Score: ' + str(score[1])
                        + '    Level: ' + str(level[1]), True, (0, 0,
                                                                0), (255, 255, 255))
    textbRect = textb.get_rect()
    textbRect.center = (X // 2, 50)
    win.blit(textb, textbRect)
    pygame.display.update()

# Quits Game
pygame.quit()