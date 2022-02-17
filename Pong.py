import pygame
from pygame.locals import *
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont('calibri', 40)
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong')
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((0, 0, 0))
paused = True


class Player():
    x = 0
    y = 0
    speed = 450
    move = 0
    score = 0
    height = 100
    width = 10
    image = pygame.Surface((width, height)).convert()
    image.fill((255, 255, 255))


class Ball():
    size = 16
    x = WIDTH/2 - size/2
    y = HEIGHT/2 - size/2
    xmove = 250
    ymove = 250
    speed = 1
    image = pygame.Surface((size, size)).convert()
    pygame.draw.circle(image, (255, 255, 255), (size/2, size/2), size/2)
    image = image.convert()


player1 = Player()
player2 = Player()
ball = Ball()
ball1 = Ball()
player1.x = 10
player1.y = HEIGHT/2 - player1.height/2
player2.x = WIDTH - 10 - player2.width
player2.y = HEIGHT/2 - player2.height/2
while running:
    window.blit(background, (0, 0))
    pygame.draw.rect(window, (255, 255, 255), Rect(
        (5, 5), (WIDTH-10, HEIGHT-10)), 2)
    pygame.draw.aaline(window, (255, 255, 255),
                       (int(WIDTH/2), 5), (int(WIDTH/2), HEIGHT-10))
    window.blit(player1.image, (player1.x, player1.y))
    window.blit(player2.image, (player2.x, player2.y))
    score1 = font.render(str(player1.score), True, (255, 255, 255))
    score2 = font.render(str(player2.score), True, (255, 255, 255))
    window.blit(score1, (WIDTH/2-45, 15))
    window.blit(score2, (WIDTH/2+15, 15))
    window.blit(ball.image, (ball.x, ball.y))
    if player1.score >= 3 or player2.score >= 3:
        window.blit(ball1.image, (ball1.x, ball1.y))
    timePassed = clock.tick(30)
    timeSeconds = timePassed/1000.0
    if not paused:
        player1.y = player1.y + (player1.move * timeSeconds)
        player2.y = player2.y + (player2.move * timeSeconds)
        ball.x = ball.x + (ball.xmove * timeSeconds * ball.speed)
        ball.y = ball.y + (ball.ymove * timeSeconds * ball.speed)
        ball.speed += 0.0002
        if player1.score >= 3 or player2.score >= 3:
            ball1.x = ball1.x + (ball1.xmove * timeSeconds * ball1.speed)
            ball1.y = ball1.y + (ball1.ymove * timeSeconds * ball1.speed)
            ball1.speed += 0.0002

    if player1.y >= HEIGHT-player1.height - 10:
        player1.y = HEIGHT-player1.height - 10
    elif player1.y <= 10:
        player1.y = 10
    elif player2.y >= HEIGHT-player2.height - 10:
        player2.y = HEIGHT-player2.height - 10
    elif player2.y <= 10:
        player2.y = 10
    elif ball.y <= 10:
        ball.ymove = -ball.ymove
        ball.y = 10
    elif ball.y >= HEIGHT - 10 - ball.size:
        ball.ymove = -ball.ymove
        ball.y = HEIGHT-10 - ball.size
    if player1.score >= 3 or player2.score >= 3:
        if ball1.y <= 10:
            ball1.ymove = -ball1.ymove
            ball1.y = 10
        elif ball1.y >= HEIGHT - 10 - ball1.size:
            ball1.ymove = -ball1.ymove
            ball1.y = HEIGHT-10 - ball1.size

    if ball.x <= player1.x + player1.width:
        if ball.y + ball.size >= player1.y and ball.y <= player1.y + player1.height:
            ball.x = player1.x + player1.width + 5
            ball.xmove = - ball.xmove
    if ball.x + ball.size >= player2.x:
        if ball.y + ball.size >= player2.y and ball.y <= player2.y + player2.height:
            ball.x = player2.x - player2.width - 5
            ball.xmove = -ball.xmove
    if ball.x < 5:
        player2.score += 1
    elif ball.x > WIDTH - 5 - ball.size:
        player1.score += 1

    if ball.x < 5 or ball.x > WIDTH - ball.size:
        ball.x = WIDTH/2 - ball.size/2
        ball.y = HEIGHT/2 - ball.size/2
        ball1.x = WIDTH/2 - ball1.size/2
        ball1.y = HEIGHT/2 - ball1.size/2
        player1.y = HEIGHT/2 - player1.height/2
        player2.y = HEIGHT/2 - player2.height/2
        ball.speed = 1
        ball1.speed = 1
        paused = True
    if player1.score >= 3 or player2.score >= 3:
        if ball1.x <= player1.x + player1.width:
            if ball1.y + ball1.size >= player1.y and ball1.y <= player1.y + player1.height:
                ball1.x = player1.x + player1.width + 5
                ball.xmove = - ball1.xmove
        if ball1.x + ball1.size >= player2.x:
            if ball1.y + ball1.size >= player2.y and ball1.y <= player2.y + player2.height:
                ball1.x = player2.x - player2.width - 5
                ball1.xmove = -ball1.xmove
        if ball1.x < 5:
            player2.score += 1
        elif ball1.x > WIDTH - 5 - ball.size:
            player1.score += 100000

        if ball1.x < 5 or ball1.x > WIDTH - ball1.size:
            ball1.x = WIDTH/2 - ball1.size/2
            ball1.y = HEIGHT/2 - ball1.size/2
            ball.x = WIDTH/2 - ball.size/2
            ball.y = HEIGHT/2 - ball.size/2
            player1.y = HEIGHT/2 - player1.height/2
            player2.y = HEIGHT/2 - player2.height/2
            ball.speed = 1
            ball1.speed = 1
            paused = True
    if paused:
        window.blit(font.render('press SPACE to play', True,
                    (255, 255, 255)), (WIDTH/2 - 210, HEIGHT/2-70))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                player1.move = -player1.speed
            elif event.key == K_s:
                player1.move = player1.speed
            elif event.key == K_UP:
                player2.move = -player2.speed
            elif event.key == K_DOWN:
                player2.move = player2.speed
            elif event.key == K_SPACE:
                paused = False
                ball.xmove = random.randint(100, 250)
                ball.ymove = random.randint(100, 250)
                ball1.xmove = random.randint(100, 250)
                ball1.ymove = random.randint(100, 250)
                if random.randint(0, 1) == 0:
                    ball.xmove = -ball.xmove
                if random.randint(0, 1) == 0:
                    ball.ymove = -ball.ymove
                if player1.score >= 3 or player2.score >= 3:
                    ball1.xmove = -ball.xmove
                    if random.randint(0, 1) == 0:
                        ball1.ymove = -ball1.ymove
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                player1.move = 0
            elif event.key == K_UP or event.key == K_DOWN:
                player2.move = 0


pygame.quit()
