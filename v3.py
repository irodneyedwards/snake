# # ------------------------------------------------------------------------------------------------------- #
# Computer Science for Designers and Artists
# HSCI-234-01
# Week 14
# Final Project
# Rodney Edwards
# --------------------------------------------------------------------------------------------------------- #
# ---------------------------------- Final Project Overview ----------------------------------------------- #
# For your final project you will create a game inspired by the 80’s arcade. You’ll put together all the programming 
# techniques we’ve learned: branching, looping, data structures and functions along with a couple of new concepts: 
# events and graphics. This project will extend the simulation concept from the midterm to include real-time interaction 
# with a user and an ending condition based on user input.
# --------------------------------------------------------------------------------------------------------- #
# -------------------------------------- Snake Game ------------------------------------------------------- #
# The purpose of the game is to collect the highest-score by eating food, 
# while avoid colliding with yourself and the gameboard.
# --------------------------------------------------------------------------------------------------------- #

# -------------------------------------- Pre-Flight ------------------------------------------------------- #
# Initializing Pygame, Imports, Defining Global Constants, Functions

# 1. Imports
import pygame, sys
from pygame import font
clock = pygame.time.Clock()
import random

# 2. Initialize Pygame
pygame.init()

# Set the GAME_DISPLAY window sizes
SCREEN_SIZE_BEGINNER = 600
SCREEN_SIZE_ADVANCED = 400

# 3. Write boilerplate Pygame Syntax to Draw basic window
# Pass through screen size variables into the Tuple with an extra set of ()
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE_BEGINNER, SCREEN_SIZE_BEGINNER))

# Styles  ------------------------------------------------------- #

# 4. Game Window Title
pygame.display.set_caption('Snakeyy - a python game.')

# 3. Declare constants

# GAME COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Fonts ------------------------------------------------------- #
FONT_SIZE_XXS = 20
FONT_SIZE_XS  = 30
FONT_SIZE_SM  = 40
FONT_SIZE_MD  = 60
FONT_SIZE_LG  = 80
FONT_SIZE_XL  = 120

# Making a font variable, to reference for game text 
## Second parameter, equals font size



# Styles ------------------------------------------------------- #
BUTTON_PLATE = (100, 50)

# Defining messages function to draw text to screen ------------------------------------------------------- #
## Which takes a msg parameter and a color parameter
# def text_object(text, font, color):

#     # 1. First Render Font
#     ## The first parmeter is msg, which stands for what text string you will pass through
#     ### The second patameter is set to True, which means Anti-Aliasing
#     ### The third parameter is color which equals the text color
#     font = pygame.font.SysFont("Arial", FONT_SIZE_XS)
#     text_surface = font.render(text, True, color)

#     return text_surface, text_surface.get_rect()
#     # # 2. Putting the font onto GAME_DISPLAY, i.e., "to blit"
#     # # First parameter (the message to pass through)
#     # ## Second parameter (X, Y) = where to be placed on screen
#     # ### Make this dynamic later 
#     # GAME_DISPLAY.blit(screen_text, (TEXT_X, TEXT_Y))

# def message_display(text, color, font_size):

#     font = pygame.font.SysFont("Arial", 20)
#     text_surface, text_rect = text_object (text, font, color)
#     text_rect.center = (int(SCREEN_SIZE_BEGINNER/2), int(SCREEN_SIZE_BEGINNER/4))
#     GAME_DISPLAY.blit(text_surface, text_rect)

#     pygame.display.update()


# Flight: Main Game Window -------------------------------------------------------------------------------- #

def start_screen():

    click = False

    # button_plate = (100, 50)

    # Scene 1 - Game Starting Menu Screen
    
    # - Player is greeted with a welcome, Title
    # - Under Title, there is a sub-title that says, "Choose a Mode...
    # - Player can choose between difficulty level
    # - Easy Mode = Slower starting speed for snake body, and large screen display
    # - Hard Mode = Faster starting speed for snake body, and smaller screen display

    running = True
    while running:

        # 1. Draw the game window
        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)

        # 2. Draw a Title, in the center of the window
        # message_display("Welcome", GREEN, FONT_SIZE_LG)

        # 3. Draw a Sub-Title under Title. 
          

        # 4. Easy and Hard Buttons
        # 4a. - This Button needs to run the game in easy mode
        ## - This Button needs to run the game in easy mode
        easy = pygame.Rect((200, 250), BUTTON_PLATE)
        pygame.draw.rect(GAME_DISPLAY, GREEN, easy)

        # 4b. Draw a button that has text inside that reads, "Hard."
        ## - This Button needs to run the game in hard mode
        hard = pygame.Rect((400, 250), BUTTON_PLATE)
        pygame.draw.rect(GAME_DISPLAY, RED, hard)
        
    
        # 5. There needs to be a click state for the buttons
        mx, my = pygame.mouse.get_pos()

        if easy.collidepoint((mx, my)):
            if click:
                game()
        if hard.collidepoint((mx, my)):
            if click:
                game_over()
        
        # 6. Event List
        #resets every frame before handling the input
        click = False 

        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True   

        # updates the entire the surface
        ## pygame.display.flip()
        ### updates the area around what's suppose to update
        pygame.display.update()

scale = 5

def update(snake, x_speed, y_speed):
    head = snake[-1].copy()
    snake.pop(0)
    head.x += x_speed * scale
    head.y += y_speed * scale
    snake.append(head)
    
def grow(snake, x_speed, y_speed):
    head = snake[-1].copy()
    head.x += x_speed * scale
    head.y += y_speed * scale
    snake.append(head)

def random_location(screen_size):
    x = random.randint(10, screen_size - 10)
    y = random.randint(10, screen_size - 10)

    return(x, y)

# returns if snake collides with something that should end the game
def end_game_collision(snake, screen_size):
    head = snake[-1]
    x, y = head.x, head.y
    # collides with wall
    if x > screen_size or x < 0 or y > screen_size or y < 0:
        return True
    # collides with self not including head
    for i in range(len(snake) - 1):
        part = snake[i]
        if part.x == x and part.y == y:
            return True

def game():

    # Game Evironment ------------------------------------------------- #

    # Generic block, to pass in as snake, food, poison 
    CUBE = (20, 20)

    # Top Score ------------------------------------------------------- #
    # Scene 2 - Main Game Window
    # A. There is a score at the top of the screen
    # -- Draw text to the top right of the game window

    # Snake ---------------------------------------------------------- #
    # There needs to be an object which will represent our snake
    # 1. Define variable named snake

    head_of_snake_top = 20
    head_of_snake_left = 30
    snake = [pygame.Rect((head_of_snake_top, head_of_snake_left), CUBE)]

    # Intial speed of snake
    speed_x = 0
    speed_y = 0

    screen_size = SCREEN_SIZE_BEGINNER

   # Food  ---------------------------------------------------------- #

    # To Do: 
    # Food is generated on the screen
    # -- 1. Define variable named food
    food = pygame.Rect(random_location(screen_size), CUBE)
    # -- 2. Draw the object to the screen to represent food
    # -- 3. Food object appears on game board in random x / y position
    # -- 4. When the snake object collides with food object
    # --- 4a. The food is redrawn in a different location within the game board
    # --- 4b. Snake object grows by one
    # ----4b.1. Append to back of the snake object
    # -- 5. Arbitrary Score is added to the Score at the top of the screen

    

    # Poison ------------------------------------------------------- #

    # To Do:
    # Poison is randomly generated on the screen at a time interval
    # -- 1. Define variable named poison
    poison = pygame.Rect(random_location(screen_size), CUBE)
    # -- 2. Poison object to screen to represent poison
    # -- 3. Poison object appears on game board in random x / y position
    # -- 4. When the snake object collides with poison object
    # --- 4a. The snake object shrinks
    # ----4b. Delete from the back of the snake object
    # -- 5. Arbitrary Score is reduced to the Score at the top of the screen


    # Main Game Loop ------------------------------------------------------- #
    
    # Snake object begins to move on the screen, player interacts with snake by pressing left, right, up, down keys
   # To Do:
    # -- 1. Snake starts moving in x-axis on the start of the game
    # -- 2. There needs to be an event to recognize user input, so the snake object can be controlled, and the direction can change to the orientation of the keyboard event-triggered
    # -- 4. Snake may not collide with itself
    
    # Write loop, to listen for events
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
                    
        # snake[0].x += speed_x
        # snake[0].y += speed_y
        update(snake, speed_x, speed_y)


        # -- 3. Snake may not exit through the walls of the game display
        # --- 3/4a. The game will be over if the snake object hits the walls or itself
        # if snake[0].right > screen_size or snake[0].left < 0:
        #     running = False

        # if snake[0].bottom > screen_size or snake[0].top < 0:
        #     running = False

        running = not end_game_collision(snake, screen_size)

        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)

        # Tuple = (Where you want to draw, what color you want to fill, (X,Y,WIDTH, HEIGHT)
        for body in snake:
            pygame.draw.rect(GAME_DISPLAY, BLUE, body)
        
        # Generate food on window
        # # Food needs a location on window
        pygame.draw.rect(GAME_DISPLAY, RED, food)

        pygame.draw.rect(GAME_DISPLAY, GREEN, poison)

                    

        # When snake collides 
        if snake[-1].colliderect(food):
            # snake.append(snake[-1].copy())
            grow(snake, speed_x, speed_y)
            food.x, food.y = random_location(screen_size)
            print(snake)

        if snake[-1].colliderect(poison):
            # snake.append(snake[-1].copy())
           running = False


        # message_display("This your score:", WHITE, FONT_SIZE_MD)

        # updates the entire the surface
        ## pygame.display.flip()
        ### updates the area around what's suppose to update
        pygame.display.update()
        # clock.tick(1000)

    game_over()

def game_over():

    click = False

    # button_plate = (100, 50)

    # Scene 3 - Game Over Screen
    
    # - Player dies
    # - Game over screen pops up
    # - Under Title, there is a sub-title that says, "Start Over"
    # - Player can select button to start over

    running = True
    while running:

        # 1. Draw the game window
        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)

        # 2. Draw a Title, in the center of the window
        # message_display("Game Over", WHITE, FONT_SIZE_MD)

        # 3. Draw a Sub-Title under Title. 
          

        # 4. Start Over
        # 4a. - This Button needs to return player to the start screen
        start_again = pygame.Rect((200, 250), BUTTON_PLATE)
        pygame.draw.rect(GAME_DISPLAY, WHITE, start_again)
        
    
        # 5. There needs to be a click state for the buttons
        mx, my = pygame.mouse.get_pos()

        if start_again.collidepoint((mx, my)):
            if click:
                start()
        
        # 6. Event List
        #resets every frame before handling the input
        click = False 

        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True   

        # updates the entire the surface
        ## pygame.display.flip()
        ### updates the area around what's suppose to update
        pygame.display.update()

start_screen()
game()


#Archive Notes

# Another option to draw rectangle
        # GAME_DISPLAY.fill(RED, rect=(10, 20, 50, 50))