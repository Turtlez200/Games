from tabnanny import check
import pygame
import sys
from pygame.locals import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
running = True
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Tic Tac Toe')
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((0, 0, 0))
basic_font = pygame.font.SysFont(None, 60)
small = pygame.font.SysFont(None, 35)
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
isx = True
pygame.display.update()


def checkwin(grid):
    for x in range(3):
        n = grid[0][x]
        count = 0
        if n != 0:
            for y in grid:
                if y[x] == n:
                    count += 1
            if count >= 3:
                return grid[0][x]
    for x in grid:
        if x[0] == x[1] and x[1] == x[2] and x[0] != 0:
            return x[0]
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != 0:
        return grid[0][2]
    return 0


while running:
    pygame.draw.line(window, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(window, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(window, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(window, (255, 255, 255), (0, 400), (600, 400), 10)
    pos = pygame.mouse.get_pressed()
    if (pos[0] == True):
        xcords = pygame.mouse.get_pos()[0]
        ycords = pygame.mouse.get_pos()[1]
        if xcords < 200:
            xcords = 200
        elif xcords > 200 and xcords < 400:
            xcords = 400
        elif xcords > 400:
            xcords = 600
        if ycords < 200:
            ycords = 200
        elif ycords > 200 and ycords < 400:
            ycords = 400
        elif ycords > 400:
            ycords = 600
        if (grid[int(xcords/200) - 1][int(ycords/200) - 1] == 0):
            if isx:
                pygame.draw.line(window, (255, 255, 255), (xcords-180,
                                                           ycords-180), (xcords-20, ycords-20), 8)
                pygame.draw.line(window, (255, 255, 255), (xcords-20,
                                                           ycords-180), (xcords-180, ycords-20), 8)
                grid[int(xcords/200) - 1][int(ycords/200) - 1] = 2
                isx = False
            elif isx == False:
                pygame.draw.circle(window, (255, 255, 255),
                                   (xcords-100, ycords-100), 80, 6)
                isx = True
                grid[int(xcords/200) - 1][int(ycords/200) - 1] = 1
    l = checkwin(grid)
    if l != 0:
        if l == 2:
            text = basic_font.render("X Winner", True, (255, 0, 0))
        else:
            text = basic_font.render("O Winner", True, (255, 0, 0))
        window.blit(text, (210, 50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
pygame.quit()
