import sys
from grid import Grid
from blocks import *

import pygame
pygame.init()
dark_blue = (44,44,127)

screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Teris")

clock = pygame.time.Clock()

game_grid = Grid()

block = OBlock()
block.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Drawing
        screen.fill(dark_blue)
        game_grid.draw(screen)
        block.draw(screen)

        pygame.display.update()
        clock.tick(60 )