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

# Initialize Game
# ----- Things to do: -----
# 1. Initialize Pygame
# 2. Declare constants
# 3. Write boilerplate Pygame Syntax to Draw basic window

# Main Game Loop
# 1. Write loop, to listen for events

# Scene 1 - Game Starting Screen Context
# - Player is greeted with a welcome, Title
# - Under Title, there is a sub-title that says, "Choose a Mode...
# - Player can choose between difficulty level
# - Easy Mode = Slower starting speed for snake body, and large screen display
# - Hard Mode = Faster starting speed for snake body, and smaller screen display

# ----- Things to do: -----
# 1. Draw the game window
# 2. Draw a Title, in the center of the window
# 3. Draw a Sub-Title under Title.
# 4. Draw a button that has text inside that reads, "Easy."
# 4a. - This Button needs to run the game in easy mode
# 5. Draw a button that has text inside that reads, "Hard."
# 5a. - This Button needs to run the game in hard mode


# Scene 2 - Main Game Window
# A. There is a score at the top of the screen
# -- Draw text to the top right of the game window

# B. There needs to be an object which will represent our snake
# -- 1. Define variable named snake
# -- 2. Draw the object to the screen to represent a snake

# C. Snake object begins to move on the screen, player interacts with snake by pressing left, right, up, down keys
# -- 1. Snake starts moving in x-axis on the start of the game
# -- 2. There needs to be an event to recognize user input, so the snake object can be controlled, and the direction can change to the orientation of the keyboard event-triggered
# -- 3. Snake may not exit through the walls of the game display
# -- 4. Snake may not collide with itself
# --- 3/4a. The game will be over if the snake object hits the walls or itself

# D. Food is generated on the screen
# -- 1. Define variable named food
# -- 2. Draw the object to the screen to represent food
# -- 3. Food object appears on game board in random x / y position
# -- 4. When the snake object collides with food object
# --- 4a. The food is redrawn in a different location within the game board
# --- 4b. Snake object grows by one
# ----4b.1. Append to back of the snake object
# -- 5. Arbitrary Score is added to the Score at the top of the screen

# E. Poison is randomly generated on the screen at a time interval
# -- 1. Define variable named poison
# -- 2. Poison object to screen to represent poison
# -- 3. Poison object appears on game board in random x / y position
# -- 4. When the snake object collides with poison object
# --- 4a. The snake object shrinks
# ----4b. Delete from the back of the snake object
# -- 5. Arbitrary Score is reduced to the Score at the top of the screen

# G. Handling game over 
# -- If snake object collides with itself, the walls of the game display, or if there score falls to zero 
# --- Game is over
# -- 1. Return the user to start screen


# ---------------------------------------------------------------------------------------------------------
# Step Zero: Initializing Pygame, and Draw Board

# - Declare the game module
# - Declare constant variables

# imports 
import pygame

# Intialize PyGame
pygame.init()

# GAME COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setting up the screen size(s)
SCREEN_SIZE_BEGINNER = 600, 600
SCREEN_SIZE_ADVANCED = 400, 400

# Pass through screen size variables into the Tuple with an extra set of ()
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE_BEGINNER))

# Game Window Title
pygame.display.set_caption('Snakeyy - a python game.')

game_running = True

head_of_snake_top = 20
head_of_snake_left = 30

cube = (20, 20)

snake = pygame.Rect((head_of_snake_top, head_of_snake_left), cube)

speed_x = 0
speed_y = 0

#Creating Variable for food -- done
food = pygame.Rect((150, 250), cube)


# ---------------------------------------------------------------------------------------------------------
# Step: Main Game Loop

game_running = True

while game_running:

    event_list = pygame.event.get()
    # Handle closing the game with the x button

    for event in event_list:
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -1
                speed_y = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 1
                speed_y = 0
            if event.key == pygame.K_UP:
                speed_x = 0
                speed_y = -1
            if event.key == pygame.K_DOWN:
                speed_x = 0
                speed_y = 1

    snake.x += speed_x
    snake.y += speed_y


    # Draw to surface (with fill color) or background color
    GAME_DISPLAY.fill(BLACK)
    # Tuple = (Where you want to draw, what color you want to fill, (X,Y,WIDTH, HEIGHT)
    # pygame.draw.rect(GAME_DISPLAY, BLUE,(head_of_snake_x, head_of_snake_y, 30, 20))
    pygame.draw.rect(GAME_DISPLAY, BLUE, snake)
    # Another option to draw rectangle
    # GAME_DISPLAY.fill(RED, rect=(10, 20, 50, 50))

    # Generate food on window
    # # Food needs a location on window
    pygame.draw.rect(GAME_DISPLAY, RED, food)

    # When snake collides 
    if snake.colliderect(food):
        food.x = 100
        food.y = 200 

    ##  with food add to snake
    ### Generate new food in random place after eaten

    # when snake x or y, meets food x or y

    # updates the entire the surface
    ## pygame.display.flip()
    ### updates the area around what's suppose to update
    pygame.display.update()

pygame.quit()


