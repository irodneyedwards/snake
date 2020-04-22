# 1. Imports
import pygame, sys
# import random

# 2. Initialize Pygame
pygame.init()

# Set the GAME_DISPLAY window sizes
SCREEN_SIZE_BEGINNER = 600
SCREEN_SIZE_ADVANCED = 400

# 3. Write boilerplate Pygame Syntax to Draw basic window
# Pass through screen size variables into the Tuple with an extra set of ()
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE_BEGINNER, SCREEN_SIZE_BEGINNER))

def game():
    running = True
    while running:
        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    pygame.display.update()

    pygame.quit()

game()
