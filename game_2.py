# REV A - Let's just get a window open

import pygame

# some global definitions
SCREEN_SIZE = 600
BOARD_SIZE = 5


# initialize pygame
pygame.init()

# create display window
screen_surface = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))



user_quit = False

while not user_quit:

    # check if a mole was whacked
    for my_event in pygame.event.get():
        if my_event.type == pygame.QUIT:
            user_quit = True
