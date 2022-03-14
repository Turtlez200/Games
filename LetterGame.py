import pygame
import sys
from pygame.locals import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
running = True
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Letter Game')
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((0, 0, 0))
basic_font = pygame.font.SysFont(None, 48)
small = pygame.font.SysFont(None, 35)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
buttons = [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v,
           K_w, K_x, K_y, K_z, ]
score = 0
lives = 0
paused = True
scores = []
pygame.display.update()


class Letter():
    x = random.randint(1, 581)
    y = 0
    move = 0
    speed = 90
    image = basic_font.render('a', True, (255, 255, 255), (0, 0, 0))


class Bomb():
    x = 3000
    y = 3500
    move = 0
    speed = 350


letter = Letter()
letter1 = Letter()
bomb = Bomb()
bomb1 = Bomb()
index_letter1 = letters.index('a')
index_letter = letters.index('a')

while running:
    if len(scores) > 0:
        high = small.render(f"High: {max(scores)}",
                            True, (255, 255, 255), (0, 0, 0))
        window.blit(high, (0, 40))
    window.blit(letter.image, (letter.x, letter.y))
    pygame.draw.circle(window, (255, 0, 0), (bomb.x, bomb.y), 15)
    pygame.draw.circle(window, (255, 0, 0), (bomb1.x, bomb1.y), 15)

    score_blit = basic_font.render(
        str(score), True, (255, 255, 255), (0, 0, 0))
    window.blit(score_blit, (0, 0))
    timePassed = clock.tick(30)
    timeSeconds = timePassed / 1000.0
    # move letters and bomb
    if score >= 10:
        window.blit(letter1.image, (letter1.x, letter1.y))
        letter1.move = letter1.speed
        letter1.y = letter1.y + (letter1.move * timeSeconds)
        if letter1.y >= HEIGHT - 20:
            letter1.y = HEIGHT - 20
        if letter1.y == 380:
            letter1_choice = str(random.choice(letters))
            index_letter1 = letters.index(letter1_choice)
            letter1.image = basic_font.render(
                letter1_choice, True, (255, 255, 255), (0, 0, 0))
            letter1.y = 0
            letter1.x = random.randint(1, 581)
            lives += 1
        if bomb1.y <= letter1.y + 20:
            letter1_choice = str(random.choice(letters))
            index_letter1 = letters.index(letter1_choice)
            score += 1
            letter1.image = basic_font.render(
                letter1_choice, True, (255, 255, 255), (0, 0, 0))
            bomb1.x = 3000
            bomb1.y = 3050
            bomb1.move = 0
            letter1.y = 0
            letter1.x = random.randint(1, 581)
            letter1.speed += 2
        bomb1.y = bomb1.y + (bomb1.move * timeSeconds)
    letter.move = letter.speed
    letter.y = letter.y + (letter.move * timeSeconds)
    bomb.y = bomb.y + (bomb.move * timeSeconds)
    # check letter boundries
    if letter.y >= HEIGHT - 20:
        letter.y = HEIGHT - 20
    if letter.y == 380:
        letter_choice = str(random.choice(letters))
        index_letter = letters.index(letter_choice)
        letter.image = basic_font.render(
            letter_choice, True, (255, 255, 255), (0, 0, 0))
        letter.y = 0
        letter.x = random.randint(1, 581)
        lives += 1
    if bomb.y <= letter.y + 20:
        letter_choice = str(random.choice(letters))
        index_letter = letters.index(letter_choice)
        score += 1
        letter.image = basic_font.render(
            letter_choice, True, (255, 255, 255), (0, 0, 0))
        bomb.x = 3000
        bomb.y = 3050
        bomb.move = 0
        letter.y = 0
        letter.x = random.randint(1, 581)
        letter.speed += 4
    if lives == 3 or scores == []:
        paused = True
        letter.speed = 0
        letter1.speed = 0
        letter.x = 3000
        letter1.x = 3000

    if paused:
        bomb.move = 0
        bomb1.move = 0
        window.blit(basic_font.render('press space to play',
                    True, (255, 255, 255), (0, 0, 0)), (0, 0))
        bomb.y = 3000
        bomb.x = 4000
        bomb1.y = 3001
        bomb1.x = 4001
        scores.append(score)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == buttons[index_letter]:
                bomb.x = letter.x + 10
                bomb.y = HEIGHT
                bomb.move = -bomb.speed
            elif paused:
                if event.key == K_SPACE:
                    paused = False
                    lives = 0
                    letter.speed = 90
                    letter1.speed = 90
                    letter.x = random.randint(1, 581)
                    letter1.x = random.randint(1, 581)
                    score = 0
            elif score >= 10:
                if event.key == buttons[index_letter1]:
                    bomb1.x = letter1.x + 10
                    bomb1.y = HEIGHT
                    bomb1.move = -bomb1.speed

pygame.quit()
