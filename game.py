# # --------------------------------------------------------------------------------------------------------
# Computer Science for Designers and Artists
# HSCI-234-01
# Week 14
# Final Project
# Rodney Edwards
# ----------------------------------------------------------------------------------------------------------
# ---------------------------------- Final Project Overview ------------------------------------------------
# For your final project you will create a game inspired by the 80’s arcade. You’ll put together all the programming 
# techniques we’ve learned: branching, looping, data structures and functions along with a couple of new concepts: 
# events and graphics. This project will extend the simulation concept from the midterm to include real-time interaction 
# with a user and an ending condition based on user input.
# ----------------------------------------------------------------------------------------------------------
# -------------------------------------- Snake Game --------------------------------------------------------
# The purpose purpose of the game is to get to be the first player to get four in a row, on the game board.
# ----------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------
# Step One: Initializing Pygame, and scafold game window skeleton

import pygame
# import random

# Intialize PyGame
pygame.init()

# Game Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setting up the screen size(s)
SCREEN_SIZE_BEGINNER = 600, 600
SCREEN_SIZE_ADVANCED = 400, 400

# Pass through screen size variables into the Tuple with an extra set of ()
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE_ADVANCED))

# Game Window Title
pygame.display.set_caption('Snakeyy - a python game.')

game_running = True

head_of_snake_x = 20
head_of_snake_y = 30

while game_running:

    event_list = pygame.event.get()
    # Handle closing the game with the x button

    for event in event_list:
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head_of_snake_x -= 10
            if event.key == pygame.K_RIGHT:
                head_of_snake_x += 10

    # Draw to surface (with fill color) or background color
    GAME_DISPLAY.fill(BLACK)
    # Tuple = (Where you want to draw, what color you want to fill, (X,Y,WIDTH, HEIGHT))
    pygame.draw.rect(GAME_DISPLAY, BLUE,(head_of_snake_x, head_of_snake_y, 30, 20))
    # Another option to draw rectangle
    # GAME_DISPLAY.fill(RED, rect=(10, 20, 50, 50))


    # updates the entire the surface
    # pygame.display.flip()
    # updates the area around what's suppose to update
    pygame.display.update()

pygame.quit()