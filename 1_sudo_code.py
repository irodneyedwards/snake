#Initialize Game
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
# __ 2. Draw the object to the screen to represent a snake

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