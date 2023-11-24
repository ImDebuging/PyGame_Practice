import sys,pygame
from game import Game

import pygame
pygame.init()
dark_blue = (44,44,127)

screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Python Teris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and game.game_over == False:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()

        if event.type == pygame.KEYDOWN and game.game_over ==True:
            if event.key == pygame.K_r:
                game.game_over = False
                game.reset()

        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

        # Drawing
        screen.fill(dark_blue)
        game.draw(screen)


        pygame.display.update()
        clock.tick(60)