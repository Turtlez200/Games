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
basic_font = pygame.font.SysFont(None, 48)
small = pygame.font.SysFont(None, 35)

pygame.display.update()

while running:
    pygame.draw.rect(window, )
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            sys.exit()
