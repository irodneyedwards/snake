# ------------------------------------------------------------------------------------------------------- #
# Rodney Edwards
# --------------------------------------------------------------------------------------------------------- #
# ---------------------------------- Final Project Overview ----------------------------------------------- #
# For your final project you will create a game inspired by the 80’s arcade. You’ll put together all the programming 
# techniques we’ve learned: branching, looping, data structures and functions along with a couple of new concepts: 
# events and graphics. This project will extend the simulation concept from the midterm to include real-time interaction 
# with a user and an ending condition based on user input.
# --------------------------------------------------------------------------------------------------------- #
# -------------------------------------- Snake Game ------------------------------------------------------- #
# The purpose of the game is to collect the highest score by eating food, 
# while avoiding poison objects as well as colliding with yourself and the gameboard.
# --------------------------------------------------------------------------------------------------------- #

# -------------------------------------- Pre-Flight ------------------------------------------------------- #
# Initializing Pygame, Imports, Defining Global Constants, Functions

# 1. Imports
import pygame, sys
import random
import time
clock = pygame.time.Clock()

# 2. Initialize Pygame
pygame.init()
pygame.font.init()

# 3. Declare constants
## I wanted to make utility variables, to abstract any hard code values at the function call level.

# Utilities ------------------------------------------------------- #
CUBE = 20 # Generic block, to pass in as snake, food, poison 

# Set the GAME_DISPLAY window sizes
SCREEN_SIZE_BEGINNER = 600
#Descoped feature
## I wanted to have an advanced mode that would load the initial snake speed faster with the GAME_DISPLAY being smaller. 
### if I had more time...
# SCREEN_SIZE_ADVANCED = 400

# 4. Game Window Title
pygame.display.set_caption('Snakeyy - a python game.')

# 5. Write boilerplate Pygame Syntax to Draw basic window
# Pass through screen size variables into the Tuple with an extra set of ()
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE_BEGINNER, SCREEN_SIZE_BEGINNER))

# Bounding Frame Size
BUTTON_PLATE = (100, 50)

# Colors ---------------------------------------------------------- #
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

NEON_PURPLE = (193,131,255)
NEON_BLUE = (73,222,255)
NEON_GREEN =(67,255,175)

# Fonts ---------------------------------------------------------- #
FONT_SIZE_SM  = 20
FONT_SIZE_MD  = 30
FONT_SIZE_LG  = 60
FONT_SIZE_XL  = 80

small_font = pygame.font.SysFont(None, FONT_SIZE_SM)
medium_font = pygame.font.SysFont(None, FONT_SIZE_MD)
large_font =   pygame.font.SysFont(None, FONT_SIZE_LG) 
xlarge_font =   pygame.font.SysFont(None, FONT_SIZE_XL)          

text_x = 20
texy_y = 30

# Image Loads ------------------------------------------------------- #
snake_header_img = pygame.image.load('imgs/snake_xl.png')
food_img = pygame.image.load('imgs/donut.png')

# ---------------------------------- Pre-Flight: Functions -------------------------------------------------- #

# Defining message function(s) to draw text to screen ------------------------------------------------------- #
def text_object(text, color, size):
    # 1. First Render Font
    ## The first parmeter is text, which stands for what text string you will pass through
    ### The second patameter is set to True, which means Anti-Aliasing
    ### The third parameter is color which equals the text color
    #### The fourth parameter is for the font size
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

def message_on_screen(msg, color, x_displace=0, y_displace=0, size = "medium" ):
    # 2. Putting the text onto GAME_DISPLAY, i.e., "to blit"
    # Display the text_object
    # Text Object is a rectangle, with an invisible plate, and then you can center plate around text
    ## Text Surface is like a pygame.surface object - where we put the text
    ## Tuple Text rect is the rectangle around text data

    text_surface, text_rect = text_object (msg, color, size)

    # What is the center of this text rectangle object? 
    ## - it's width and height of the main display divided by two.
    ### I added the ability to displace the x or y coordinate to make this message function more flexible,
    #### as I knew I would need to draw text in a few locations
    text_rect.center = (int(SCREEN_SIZE_BEGINNER/2) + x_displace, int(SCREEN_SIZE_BEGINNER/2) + y_displace)

    # We blit to text surface, which blits the text rectangle
    GAME_DISPLAY.blit(text_surface, text_rect)


# Flight: Main Game Window Function(s) ---------------------------------------------------------------------- #

def start_screen():
    # Scene 1 - Game Starting Menu Screen

    # - Player is greeted with a welcome, Title
    # - Under Title, there is a sub-title that says, "Click Start to Begin!"
    # - Player can choose between difficulty level
    # - Easy Mode = Slower starting speed for snake body and large screen display
    # - Feature Omitted
    # ## Hard Mode = Faster starting speed for snake body and smaller screen display

    # This click variable is my switcher for the mouseclick event later referenced
    click = False
    
    # Function Game Loop
    ## to solve for needing screens in my game, i.e., the ability to present a user with a 
    ## starting screen and a game_over screen, I solved by running an independent game loop
    ## per function
    running = True
    while running:

        # 1. Draw the game window
        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)

        # 2. Draw a Title, in the center of the window
        # 3. Draw a Sub-Title under Title. 
        message_on_screen("Neon Dragon", NEON_GREEN, x_displace = 0, y_displace= -50, size= "xlarge")
        message_on_screen("Click Start to Begin!", WHITE, x_displace = 0, y_displace= 0, size="medium")

    
        GAME_DISPLAY.blit(snake_header_img, (200, 0))
        # GAME_DISPLAY.blit(snake_header_img, (600-snake_header_img.get_width()/2, 600-snake_header_img.get_height()/2))
        

        # 4. Easy and Hard Buttons
        # 4a. - This Button needs to run the game in easy mode
        ## - This Button needs to run the game in easy mode
        easy = pygame.Rect((250, 400), BUTTON_PLATE)
        pygame.draw.rect(GAME_DISPLAY, NEON_PURPLE, easy)

        # # 4b. Draw a button that has text inside that reads, "Hard."
        # ## - This Button needs to run the game in hard mode
        # hard = pygame.Rect((400, 250), BUTTON_PLATE)
        # pygame.draw.rect(GAME_DISPLAY, NEON_PURPLE, hard)


        # 5. There needs to be a click state for the buttons
        mx, my = pygame.mouse.get_pos()

        if easy.collidepoint((mx, my)):
            if click:
                game()
        # if hard.collidepoint((mx, my)):
        #     if click:
        #         game_over()
        

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
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True   

        # updates the entire the surface
        ## pygame.display.flip()
        ### updates the area around what's suppose to update
        pygame.display.update()


scale = 5

def update(snake, speed_x, speed_y):
    head = snake[-1].copy()
    snake.pop(0)
    head.x += speed_x * scale
    head.y += speed_y * scale
    snake.append(head)
    
def grow(snake, speed_x, speed_y):
    head = snake[-1].copy()
    head.x += speed_x * scale
    head.y += speed_y * scale
    snake.append(head)

def random_location(screen_size):
    x = random.randrange(10, screen_size-CUBE, CUBE)
    y = random.randrange(10, screen_size-CUBE, CUBE)
    print(x,y)
    return(x, y)

# returns if snake collides with something that should end the game
def end_game_collision(snake, screen_size):
    head = snake[-1]
    x, y = head.x, head.y
    # collides with wall
    if x > screen_size - 10  or x < 0 or y > screen_size - 10 or y < 0:
        return True
    # collides with self not including head
    for i in range(len(snake) - 1):
        part = snake[i]
        if part.x == x and part.y == y:
            return True

# loads a random location for x, y equal to the screen_size
def random_location(screen_size):
    x = random.randrange(10, screen_size-CUBE, CUBE)
    y = random.randrange(10, screen_size-CUBE, CUBE)
    print(x,y)
    return(x, y)

def score(score):
    # Top Score ------------------------------------------------------- #
    # Scene 2 - Main Game Window
    # A. There is a score at the top of the screen
    # -- Draw text to the top right of the game window
    message_on_screen("Score:" +str(score), WHITE, x_displace = -200, y_displace = -280, size="small")
    # text = small_font.render("Score" +str(score), True, WHITE)
    # GAME_DISPLAY.blit(text, (0, 0))

    # Game Environment ------------------------------------------------- #
def game():

    # Function Variables ---------------------------------------------- #
    FPS = 60 # Frames Per Second
    screen_size = SCREEN_SIZE_BEGINNER

    # Snake ---------------------------------------------------------- #
    # There needs to be an object which will represent our snake
    # 1. Define variable named snake, and generate poisition on screen 

    # I CAN'T FIGURE OUT HOW TO GET THE SNAKE TO BE ON THE SAME X OR Y DURING COLLISON
    # head_of_snake_top = random.randrange(10, screen_size-CUBE, CUBE)
    # head_of_snake_left = random.randrange(10, screen_size-CUBE, CUBE)

    head_of_snake_top = 20
    head_of_snake_left = 30

    snake = [pygame.Rect((head_of_snake_top, head_of_snake_left), (CUBE, CUBE))]

    # Intial speed of snake
    speed_x = 0 # Container for storing updated location change: x-axis
    speed_y = 0 # Container for storing updated location change: y-axis

    # Food  ---------------------------------------------------------- #

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

    poison = pygame.Rect(random_location(screen_size), (CUBE, CUBE))

    
    # distance_traveled = 10 #distance traveled when location is updated

    running = True # Default Loop Running State
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
       
        # head_of_snake_top += speed_x
        # head_of_snake_left += speed_y
        update(snake, speed_x, speed_y)

        # -- 3. Snake may not exit through the walls of the game display
        # --- 3/4a. The game will be over if the snake object hits the walls or itself
                # if snake[0].right > screen_size or snake[0].left < 0:
                #     running = False
                # if snake[0].bottom > screen_size or snake[0].top < 0:
                #     running = False
        running = not end_game_collision(snake, screen_size)
        if end_game_collision(snake, screen_size):
            game_over()
       

        # Draw to surface (with fill color) or background color
        GAME_DISPLAY.fill(BLACK)
        # Message_on_screen
        # message_on_screen("Top Score:", BLACK, x_displace=-200, y_displace=-400)

        # # Snake needs to be drawn to screen
        # snake(head_of_snake_top, head_of_snake_left)
        for body in snake:
            pygame.draw.rect(GAME_DISPLAY, NEON_GREEN, body)

        # Generate food on window
        # # Food needs a location on window
        # pygame.draw.rect(GAME_DISPLAY, GREEN, food)
        GAME_DISPLAY.blit(food_img, food)

        # Generate poison on window
        # # at random
        pygame.draw.rect(GAME_DISPLAY, NEON_BLUE, poison)

        # When snake collides 
        if snake[-1].colliderect(food):
            # snake.append(snake[-1].copy())
            grow(snake, speed_x, speed_y)
            food.x, food.y = random_location(screen_size)
        if snake[-1].colliderect(poison):
            game_over()
    
        #Call Score

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

def game_over():

    click = False
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
        message_on_screen("Game Over!", NEON_GREEN, x_displace=0, y_displace=-50, size="large")
        # 3. Draw a Sub-Title = to score() under Title. 

          
        # 4. Start Over
        # 4a. - This Button needs to return player to the start screen
        start_again = pygame.Rect((250, 400), BUTTON_PLATE)
        pygame.draw.rect(GAME_DISPLAY, NEON_PURPLE, start_again)
        
    
        # 5. There needs to be a click state for the buttons
        mx, my = pygame.mouse.get_pos()

        if start_again.collidepoint((mx, my)):
            if click:
                start_screen()
        
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
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True   

        # updates the entire the surface
        ## pygame.display.flip()
        ### updates the area around what's suppose to update
        pygame.display.update()

start_screen()
game()


# event handling
# logic
# graphics rendering
        # if head_of_snake_top == food.x and head_of_snake_left == food.y:
        #     food = pygame.Rect(random_location(screen_size), (CUBE, CUBE))
