# ------------------------------------------------------------------------------------- #
# Computer Science for Designers and Artists
# HSCI-234-01
# Week 14
# Final Project
# Rodney Edwards
# ------------------------------------------------------------------------------------- #
# -------------------------- Final Project Overview ----------------------------------- #
# For your final project you will create a game inspired by the 80’s arcade. You’ll put
# together all the programming techniques we’ve learned: branching, looping, data structures
# and functions along with a couple of new concepts: events and graphics. This project will
# extend the simulation concept from the midterm to include real-time interaction with
# a user and an ending condition based on user input.
# ------------------------------------------------------------------------------------- #
# ---------------------------- Snake Game Purpose ------------------------------------- #
# The purpose of the game is to collect the highest-score by eating food,
# while avoid colliding with yourself and the gameboard.
# ------------------------------------------------------------------------------------- #
# -------------------------------- Pre-Flight ----------------------------------------- #
# Initializing Pygame, Imports, Defining Global Constants, Functions

# 1. Imports
import pygame
import sys
import random
import time
clock = pygame.time.Clock()

# 2. Initialize Pygame
pygame.init()
pygame.font.init()

# 3. Declare constants
# I wanted to make utility variables, to abstract any hard code values at the function call level.
# Utilities ----------------------------------------------------- #
CUBE = 20  # Generic block, to pass in as snake, food, poison

# Set the GAME_DISPLAY window sizes
SCREEN_SIZE_BEGINNER = 600
# Descoped feature
# I wanted to have an advanced mode that would load the initial snake speed faster with the GAME_DISPLAY being smaller.
# if I had more time...
# SCREEN_SIZE_ADVANCED = 400

# 4. Game Window Title
pygame.display.set_caption('Neon Dragon - a python snake game.')

# 5. Write boilerplate Pygame Syntax to Draw basic window
# Pass through screen size variables into the Tuple with an extra set of ()
GAME_DISPLAY = pygame.display.set_mode(
    (SCREEN_SIZE_BEGINNER, SCREEN_SIZE_BEGINNER))

# Bounding Frame Size
BUTTON_PLATE = (100, 50)

# Colors -------------------------------------------------------- #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

NEON_PURPLE = (193, 131, 255)
NEON_BLUE = (73, 222, 255)
NEON_GREEN = (67, 255, 175)

# Fonts --------------------------------------------------------- #
FONT_SIZE_SM = 20
FONT_SIZE_MD = 30
FONT_SIZE_LG = 60
FONT_SIZE_XL = 80

small_font = pygame.font.SysFont(None, FONT_SIZE_SM)
medium_font = pygame.font.SysFont(None, FONT_SIZE_MD)
large_font = pygame.font.SysFont(None, FONT_SIZE_LG)
xlarge_font = pygame.font.SysFont(None, FONT_SIZE_XL)

text_x = 20
text_y = 30

# Game Environment ---------------------------------------------- #

snake_header_img = pygame.image.load('imgs/snake_xl.png')
food_img = pygame.image.load('imgs/donut.png')
poison_img = pygame.image.load('imgs/poison.png')

# Defining message function(s) to draw text to screen ----------- #
def text_object(text, color, size):
    # 1. First Render Font
    # The first parmeter is text, which stands for what text string you will pass through
    # The second parameter is set to True, which means Anti-Aliasing
    # The third parameter is color which equals the text color
    # The fourth parameter is for the font size
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = medium_font.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)
    elif size == "xlarge":
        text_surface = xlarge_font.render(text, True, color)

    # returns the text_surface and gets the empty text rectangle
    return text_surface, text_surface.get_rect()


def message_on_screen(msg, color, x_displace=0, y_displace=0, size="medium"):
    # 2. Putting the text onto GAME_DISPLAY, i.e., "to blit"
    # Display the text_object
    # Text Object is a rectangle, with an invisible plate, and then you can center plate around text
    # Text Surface is like a pygame.surface object - where we put the text
    # Tuple Text rect is the rectangle around text data

    text_surface, text_rect = text_object(msg, color, size)

    # What is the center of this text rectangle object?
    # - it's width and height of the main display divided by two.
    # I added the ability to displace the x or y coordinate to make this message function more flexible,
    # as I knew I would need to draw text in a few locations
    text_rect.center = (int(SCREEN_SIZE_BEGINNER/2) +
                        x_displace, int(SCREEN_SIZE_BEGINNER/2) + y_displace)

    # We blit to text surface, which will blit the text rectangle
    GAME_DISPLAY.blit(text_surface, text_rect)


def button(text, position, color, on_click):
    # I had initially been implementing the button logic within the start_screen()function
    # during refactoring, I built out a button function to be more dynamic, and reusable

    # I needed to get mouseX, and mouseY for my event
    mx, my = pygame.mouse.get_pos()
    left_click, _, _ = pygame.mouse.get_pressed()

    # Defining, and drawing the button
    # passing in the Position, BUTTON_PLATE
    button_rect = pygame.Rect(position, BUTTON_PLATE)

    pygame.draw.rect(GAME_DISPLAY, color, button_rect)
    if button_rect.collidepoint((mx, my)) and left_click:
        on_click()

    # I couldn't figure out how to load text into the buttons easily,
    # or utilize my message_on_screen function here after reading the
    # pygame documentation, I'm using methods from pygame, and
    # basically using the same logic from my message_on_screen function

    text_surface, text_rect = text_object(text, WHITE, "medium")
    text_rect.center = ((button_rect.x+int((button_rect.w/2))),
                        (button_rect.y+int((button_rect.h/2))))

    # blit to display
    GAME_DISPLAY.blit(text_surface, text_rect)

    # Archive Logic - pulled from start_screen() function
    # this worked there fine, but it was breaking when I trying
    # to draw text into the button rect.
    # --
    # 4. Easy and Hard Buttons
    # 4a. - This Button needs to run the game in easy mode
    # - This Button needs to run the game in easy mode
    # easy = pygame.Rect((250, 400), BUTTON_PLATE)
    # pygame.draw.rect(GAME_DISPLAY, NEON_PURPLE, easy)

    # # 4b. Draw a button that has text inside that reads, "Hard."
    # ## - This Button needs to run the game in hard mode
    # hard = pygame.Rect((400, 250), BUTTON_PLATE)
    # pygame.draw.rect(GAME_DISPLAY, NEON_PURPLE, hard)

    # 5. There needs to be a click state for the buttons
    # mx, my = pygame.mouse.get_pos()

    # if easy.collidepoint((mx, my)):
    #     if click:
    #         game()
    # if hard.collidepoint((mx, my)):
    #     if click:
    #         game_over()
    # I need to get the

# Flight: Main Game Window Functions ---------------------------- #
def start_screen():
    # Scene 1 - Game Starting Menu Screen

    # - Player is greeted with a welcome, Title
    # - Under Title, there is a sub-title that says, "Click Start to Begin!"
    # - Feature Omitted
    # - Player can choose between difficulty level
    # - Easy Mode = Slower starting speed for snake body, and large screen display
    # ## Hard Mode = Faster starting speed for snake body, and smaller screen display

    # This click variable is my switcher for the mouseclick event later referenced
    click = False

    # function game loop
    running = True
    while running:
        # 1. Draw the game window ----------------------------------- #
        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)
        # 2. Draw a Title, in the center of the window -------------- #
        # 3. Draw a Sub-Title under Title.
        # 4. Authorship
        message_on_screen("Neon Dragon", NEON_GREEN,
                          x_displace=0, y_displace=-50, size="xlarge")
        message_on_screen("Click Start to Begin!", WHITE,
                          x_displace=0, y_displace=0, size="medium")
        message_on_screen("Design & Dev by: Rodney Edwards", WHITE,
                          x_displace=+180, y_displace=+280, size="small")

        # 5. Load the game logo ------------------------------------- #
        GAME_DISPLAY.blit(
            snake_header_img, (SCREEN_SIZE_BEGINNER//2-100, SCREEN_SIZE_BEGINNER//2-300))
        # GAME_DISPLAY.blit(snake_header_img, (600-snake_header_img.get_width()/2, 600-snake_header_img.get_height()/2))

        # 5. Calling my button function ----------------------------- #
        # and passing in (size, color, gamescreen to load)
        button("START", (SCREEN_SIZE_BEGINNER//2-50,
                         SCREEN_SIZE_BEGINNER//2+50), NEON_PURPLE, game)
        # 6. Event List --------------------------------------------- #
        # resets every frame before handling the input

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # updates the entire the surface
        # pygame.display.flip()
        # updates the area around what's suppose to update
        pygame.display.update()


# distance snake will travel
distance_to_travel = 5

# function to update the snake location relative to the head ---- #
def update(snake, speed_x, speed_y):
    # The idea is that, I'm making a copy of the head
    # popping off the tail
    # then updating the head position
    # and adding to the back of the list later because it makes it
    # easier for the body to follow the head list backward
    head = snake[-1].copy()
    # removes the first element in the snake_list
    snake.pop(0)
    head.x += speed_x * distance_to_travel
    head.y += speed_y * distance_to_travel
    snake.append(head)

# function to grow the snake body by predicting where the snake will soon be -- #
def grow(snake, speed_x, speed_y):
    head = snake[-1].copy()
    # when the snake grows, it's growing a new head and the last head becomes a part of the body
    # therefore to understand and to have head in the right place, I'm using speed_x
    # and then predicting where the head will soon be using distance_to_travel to get next x and y,
    # speed_x is a constant speed when the key event is pressed, i.e, if the K_LEFT is pressed
    # speed_x = -1, speed_y = 0
    head.x += speed_x * distance_to_travel
    head.y += speed_y * distance_to_travel
    snake.append(head)

# returns if snake collides with something that should end the game - #
def end_game_collision(snake, screen_size):
    head = snake[-1]
    x, y = head.x, head.y
    # collides with wall
    if x > screen_size - CUBE or x < 0 or y > screen_size - CUBE or y < 0:
        return True
    # collides with self not including head
    for i in range(len(snake) - 1):
        part = snake[i]
        if part.x == x and part.y == y:
            return True

# loads a random location for x, y equal to the screen_size, with a step size of CUBE - #

def random_location(screen_size):
    x = random.randrange(10, screen_size-CUBE, CUBE)
    y = random.randrange(10, screen_size-CUBE, CUBE)
    # I wanted to log my x, y during testing
    # print(x, y)
    return(x, y)

# Top Score Tracker --------------------------------------------- #
def score(snake_len):
    # Scene 2 - Main Game Window
    # score is equal to the length of the snake (correlated by the amount of food collided with),
    # and then multiplied by an arbitrary number value for vanity.
    score = snake_len * 20

    # A. There is a score at the top of the screen
    # -- Draw text to the top right of the game window
    message_on_screen("Score:" + str(score), WHITE,
                      x_displace=-240, y_displace=-280, size="medium")

# ------------------------------------------------------------------------------------- #
# ------------------------------ MAIN GAME LOOP --------------------------------------- #

# Game Environment ---------------------------------------------- #
def game():

    # Function Variables --------------------------------------------- #
    FPS = 60  # Frames Per Second
    screen_size = SCREEN_SIZE_BEGINNER

    # Snake ---------------------------------------------------------- #
    # There needs to be an object which will represent our snake
    # 1. Define variable named snake, and generate position on the screen

    #initial_x and _y
    initial_x = 20
    initial_y = 30

    # snake represented through a list
    snake = [pygame.Rect(
        (initial_x, initial_y), (CUBE, CUBE))]

    # Initial value - speed of the snake
    # constant direction - if you want to go left, you decrease position over time
    # gives directions +add 1 to give right direction, subtract -1 to give you left direction
    # same logic applied for speed_y
    speed_x = 0  # Container for storing updated location change: x-axis
    speed_y = 0  # Container for storing updated location change: y-axis

    # Food  --------------------------------------------------------- #
    # Food is generated on the screen
    # -- 1. Define variable named food
    # -- 2. Draw the object to the screen to represent food
    # -- 3. Food object appears on game board in random x / y position
    # -- 4. When the snake object collides with food object
    # --- 4a. The food is redrawn in a different location within the game board
    # --- 4b. Snake object grows by one
    # ----4b.1. Append to back of the snake object
    # -- 5. Arbitrary Score is added to the Score at the top of the screen

    food = pygame.Rect(random_location(screen_size), (30, 30))

    # Poison ------------------------------------------------------- #
    # Poison is randomly generated on the screen at a time interval
    # -- 1. Define variable named poison
    # -- 2. Poison object to screen to represent poison
    # -- 3. Poison object appears on game board in random x / y position
    # -- 4. When the snake object collides with poison object
    # --- 4a. The snake object shrinks
    # ----4b. Delete from the back of the snake object
    # -- 5. Arbitrary Score is reduced to the Score at the top of the screen

    poison = pygame.Rect(random_location(screen_size), (30, 30))

    # Loop ---------------------------------------------------------- #
    running = True  # Default Loop Running State
    while running:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game_exit = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    speed_x = -1
                    speed_y = 0
                elif event.key == pygame.K_RIGHT:
                    speed_x = 1
                    speed_y = 0
                elif event.key == pygame.K_UP:
                    speed_x = 0
                    speed_y = -1
                elif event.key == pygame.K_DOWN:
                    speed_x = 0
                    speed_y = 1
        # Call Update
        update(snake, speed_x, speed_y)
    # Handling Snake Collision w/ self or boundaries  ---------------- #
        # -- 3. Snake may not exit through the walls of the game display
        # --- 3/4a. The game will be over if the snake object hits the walls or itself
        # if snake[0].right > screen_size or snake[0].left < 0:
        #     running = False
        # if snake[0].bottom > screen_size or snake[0].top < 0:
        #     running = False
        # I refactored into a function
        running = not end_game_collision(snake, screen_size)
        if end_game_collision(snake, screen_size):
            game_over()

    # Graphic / IMG Loads ------------------------------------------- #
        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)

        # Snake needs to be drawn to screen
        # snake(initial_x, initial_y)
        # I couldn't figure out how to replace the rect object with an image
        # I figured it out for the food and poison objects, but for the snake it would break
        for body in snake:
            pygame.draw.rect(GAME_DISPLAY, NEON_GREEN, body)

        # Generate food on window
        # # Food needs a location on window
        # When the object was just a cube
        # pygame.draw.rect(GAME_DISPLAY, GREEN, food)
        # after refactoring into img
        GAME_DISPLAY.blit(food_img, food)

        # Generate poison on window at random
        # move posion everytime the snake collides with food
        GAME_DISPLAY.blit(poison_img, poison)
        # pygame.draw.rect(GAME_DISPLAY, NEON_BLUE, poison)

    # Handling Snake Collision w/ food and posion -------------------- #
        # When snake collides the head of the snake is the last element in the snakelist
        # Collides with food, grow is called, food is redrawn, and poison is moved at random
        if snake[-1].colliderect(food):
            # before refactor
            # snake.append(snake[-1].copy())
            # after refactor
            grow(snake, speed_x, speed_y)
            # .x, .y, is built into rect object from pygame
            food.x, food.y = random_location(screen_size)
            poison.x, poison.y = random_location(screen_size)
        # handling game_over
        # I was going to build posion at more dynamic
        # and have it decrease score, with multiples
        # descoped into just game_over for time
        if snake[-1].colliderect(poison):
            game_over()

    # Loads Score --------------------------------------------------- #
        # Call Score
        # always minus the head
        snake_body_len = len(snake) - 1
        score(snake_body_len)

    # Update, and FPS ----------------------------------------------- #
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

# Handling the game_over scene loading -------------------------- #
def game_over():
    # Scene 1 - Game Starting Menu Screen

    # - Player is greeted with a welcome, Title
    # - Under Title, there is a sub-title that says, "Click Start to Begin!"
    # - Feature Omitted
    # - Player can choose between difficulty level
    # - Easy Mode = Slower starting speed for snake body, and large screen display
    # ## Hard Mode = Faster starting speed for snake body, and smaller screen display

    # This click variable is my switcher for the mouseclick event later referenced
    click = False
    # Loop -------------------------------------------------------------- #
    running = True
    while running:

        # 1. Draw the game window
        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)

        # 2. Draw a Title, in the center of the window -------------- #
        message_on_screen("Game Over!", NEON_GREEN,
                          x_displace=0, y_displace=-50, size="xlarge")
        # 3. Draw a Sub-Title under Title --------------------------- #
        message_on_screen("Click to play again!", WHITE,
                          x_displace=0, y_displace=0, size="medium")
        # 4. Authorship
        message_on_screen("Design & Dev by: Rodney Edwards", WHITE,
                          x_displace=+180, y_displace=+280, size="small")
        # 5. Calling my button function ----------------------------- #
        # and passing in (size, color, gamescreen to load)
        button("AGAIN?", (SCREEN_SIZE_BEGINNER//2-50,
                          SCREEN_SIZE_BEGINNER//2+50), NEON_PURPLE, game)
        # 6. Event List --------------------------------------------- #
        # resets every frame before handling the input

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # updates the entire the surface
        # pygame.display.flip()
        # updates the area around what's suppose to update
        pygame.display.update()


# ------------------------------------------------------------------------------------- #
# -----------------------------------  CALLS  ----------------------------------------- #
start_screen()
game()

