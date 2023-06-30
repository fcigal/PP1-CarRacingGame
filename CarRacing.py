# importing library
import sys
import pygame
import time
import random

# Initialize pygame and set the colors with captions
pygame.init()

# Define color codes
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 70, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
white = (255, 255, 255)

# Define display dimensions
display_width = 800
display_height = 600

# Setup game display
game_displays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("CAR RACING GAME")
clock = pygame.time.Clock()

# Load car image and background image
car_img = pygame.image.load('images/car.png')
background_pic = pygame.image.load('images/gross.jpg')
yellow_strip = pygame.image.load('images/yellow_strip.png')
intro_background = pygame.image.load('images/background4.png')
instruction_background = pygame.image.load('images/background3.png')
strip = pygame.image.load("images/strip.jpg")
gameoverSound = pygame.mixer.Sound('sounds/crash2.wav')
car_sound = pygame.mixer.Sound('sounds/driving.wav')
flag = pygame.image.load('images/flag.png')
start_strip = pygame.image.load('images/start_strip.png')

# Set car width and initalize pause state
car_width = 36
pause = False


# Intro screen
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        # Display background image
        game_displays.blit(intro_background, (0, 0))

        # Render and display "CAR GAME" text
        largetext = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects('CAR RACING GAME', largetext, black)
        TextRect.center = (400, 100)
        game_displays.blit(TextSurf, TextRect)

        # Render and display "START" button
        button("START", 150, 520, 100, 50, green, bright_green, "play")

        # Render and display "QUIT" button
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")

        # Render and display "INSTRUCTION" button
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")

        pygame.display.update()

        clock.tick(50)


# Function to create a button  with specified parameters
# msg: The text to be displayed on the button
# x, y: The coordinates of the top-left corner of the button
# w, h: The width and height of the button
# ic: The color of the button when inactive
# ac: The color of the button when active(hovered over)
# action: The action to be performed when the button is clicked

def button(msg, x, y, w, h, ic, ac, action=None):
    # Get the current mouse position
    mouse = pygame.mouse.get_pos()
    # Get the current state of the mouse buttons
    click = pygame.mouse.get_pressed()

    # Check if mouse is within the button's boundaries
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # Draw button with active color
        pygame.draw.rect(game_displays, ac, (x, y, w, h))
        # Check if left mouse button is clicked and action is specified
        if click[0] == 1 and action != None:
            # If action is "play", call the coutdown()
            if action == "play":
                countdown()
            # If action is "quit", quit the game
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            # If action is "menu", call the intro_loop() function
            elif action == "menu":
                intro_loop()
            # If action is "pause", call the paused() function
            elif action == "pause":
                paused()
            # If action is "unpause", call the unpaused() function
            elif action == "unpause":
                unpaused()

    else:
        # Draw button with inactive color
        pygame.draw.rect(game_displays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    game_displays.blit(textsurf, textrect)


# Function to display the introduction screen
def introduction():
    introduction = True
    while introduction:
        # Get events from the event queue
        for event in pygame.event.get():
            # If the "QUIT" event is triggered (e.g., window closed)
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame
                quit()  # Quit the game
                sys.exit()  # Exit the system
        # Draw the instruction background
        game_displays.blit(instruction_background, (0, 0))
        # Set font for large text
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        # Set font for small text
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        # Set font for medium text
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)

        # Render and draw the instruction text
        textSurf, textRect = text_objects("This car an car game " + "in which you need dodge the coming cars",
                                          smalltext)
        textRect.center = ((400), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400), (100))
        game_displays.blit(TextSurf, TextRect)
        game_displays.blit(textSurf, textRect)

        # Render and draw the control instructions
        stextSurf, stextRect = text_objects("ARROW LEFT: LEFT TURN", smalltext)
        stextRect.center = ((150), (550))
        hTextSurf, hTextRect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        hTextRect.center = ((150), (500))
        atextSurf, atextRect = text_objects("A : ACCELERATOR", smalltext)
        atextRect.center = ((150), (450))
        rtextSurf, rtextRect = text_objects("B : BRAKE", smalltext)
        rtextRect.center = ((150), (400))
        ptextSurf, ptextRect = text_objects("P : PAUSE", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((170), (300))
        game_displays.blit(sTextSurf, sTextRect)
        game_displays.blit(stextSurf, stextRect)
        game_displays.blit(hTextSurf, hTextRect)
        game_displays.blit(atextSurf, atextRect)
        game_displays.blit(rtextSurf, rtextRect)
        game_displays.blit(ptextSurf, ptextRect)

        # Render and draw the "BACK" button
        button("BACK", 600, 400, 100, 50, red, bright_red, "menu")

        pygame.display.update()  # Update the display
        clock.tick(30)  # Limit frame rate to 30 FPS


def paused():
    global pause

    # Loop for handling events during pause state
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_displays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("PAUSED", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_displays.blit(TextSurf, TextRect)
        # Create buttons for continue, restart, and main menu
        button("CONTINUE", 150, 450, 150, 50, green, bright_green, "unpause")
        button("RESTART", 350, 450, 150, 50, blue, bright_blue, "play")
        button("MAIN MENU", 550, 450, 200, 50, red, bright_red, "menu")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def countdown_background():
    # Import the necessary modules and set up the game display
    # Initialize the font for displaying text
    font = pygame.font.SysFont(None, 25)
    # Set the initial positions for the game objects (background, strips, car, and text)
    x = (display_width * 0.55)
    y = (display_height * 0.8)
    # Draw the background image on the game display

    game_displays.blit(background_pic, (0, 0))
    game_displays.blit(background_pic, (0, 200))
    game_displays.blit(background_pic, (0, 400))
    game_displays.blit(background_pic, (700, 0))
    game_displays.blit(background_pic, (700, 200))
    game_displays.blit(background_pic, (700, 400))
    # Draw the yellow strips on the game display
    game_displays.blit(yellow_strip, (400, 100))
    game_displays.blit(yellow_strip, (400, 200))
    game_displays.blit(yellow_strip, (400, 300))
    game_displays.blit(yellow_strip, (400, 400))
    game_displays.blit(yellow_strip, (400, 100))
    game_displays.blit(yellow_strip, (400, 500))
    game_displays.blit(yellow_strip, (400, 0))
    game_displays.blit(yellow_strip, (400, 600))
    # Draw the side strips on the game display
    game_displays.blit(strip, (120, 200))
    game_displays.blit(strip, (120, 0))
    game_displays.blit(strip, (120, 100))
    game_displays.blit(strip, (680, 100))
    game_displays.blit(strip, (680, 0))
    game_displays.blit(strip, (680, 200))
    # Draw the car on the game display
    game_displays.blit(car_img, (x, y))
    # Draw the text for the score and number of dogged cars
    text = font.render("DOGGED: 0", True, black)
    score = font.render("SCORE: 0", True, red)
    game_displays.blit(text, (0, 50))
    game_displays.blit(score, (0, 30))
    # Draw the "PAUSE" button on the game display
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")
    game_displays.blit(flag, (640, 440))


def countdown():
    # Initialize a boolean variable to indicate if countdown is in progress
    countdown = True
    # Continue looping until countdown is complete
    while countdown:
        # Check for events in the pygame event queue
        for event in pygame.event.get():
            # If user closes the game window
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame
                quit()  # Quit the game
                sys.exit()  # Exit the program
        # Fill the game display with a gray color
        game_displays.fill(gray)
        # Call a function to display the countdown background
        countdown_background()

        # Display "3" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_displays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        game_displays.fill(gray)
        countdown_background()

        # Display "2" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("2", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_displays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        game_displays.fill(gray)
        countdown_background()

        # Display "1" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("1", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_displays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        game_displays.fill(gray)
        countdown_background()

        # Display "GO!!!" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("GO!!!", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        game_displays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second
        # Call the game loop function after the countdown is complete
        game_loop()


# Loading the obstacles
def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("images/car1.png")
    elif obs == 1:
        obs_pic = pygame.image.load("images/car2.png")
    elif obs == 2:
        obs_pic = pygame.image.load("images/car3.png")
    elif obs == 3:
        obs_pic = pygame.image.load("images/car4.png")
    elif obs == 4:
        obs_pic = pygame.image.load("images/car5.png")
    elif obs == 5:
        obs_pic = pygame.image.load("images/car6.png")
    elif obs == 6:
        obs_pic = pygame.image.load("images/car7.png")
    elif obs == 7:
        obs_pic = pygame.image.load("images/car2.png")
    game_displays.blit(obs_pic, (obs_startx, obs_starty))


# Impementing score system
def score_system(passed, score):
    # Create a font object with size 25
    font = pygame.font.SysFont(None, 25)
    # Render the "Passed" text with passed parameter and color black
    text = font.render("Passed" + str(passed), True, black)
    # Render the "Score" text with score parameter and color red
    score = font.render("Score" + str(score), True, red)
    # Draw the "Passed" text on the game display at (0 ,50) coordiantes
    game_displays.blit(text, (0, 50))
    # Draw the "Score" text on the game display at (0 ,30) coordinates
    game_displays.blit(score, (0, 30))


def text_objects(text, font, color=black):
    # Render the given text with the given font and color black
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def message_display(text):
    # Create a font object with size 80
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    # Render the given text with the created font
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    # Draw the rendered text on the game display at the center of the screen
    game_displays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


# Fallback logic
def crash():
    car_sound.stop()
    gameoverSound.play()
    message_display("YOU CRASHED")


# Onscreen Game UI
# On screen UI
def background():
    game_displays.blit(background_pic, (0, 0))
    game_displays.blit(background_pic, (0, 200))
    game_displays.blit(background_pic, (0, 400))
    game_displays.blit(background_pic, (700, 0))
    game_displays.blit(background_pic, (700, 200))
    game_displays.blit(background_pic, (700, 400))
    game_displays.blit(yellow_strip, (400, 0))
    game_displays.blit(yellow_strip, (400, 100))
    game_displays.blit(yellow_strip, (400, 200))
    game_displays.blit(yellow_strip, (400, 300))
    game_displays.blit(yellow_strip, (400, 400))
    game_displays.blit(yellow_strip, (400, 500))
    game_displays.blit(strip, (120, 0))
    game_displays.blit(strip, (120, 100))
    game_displays.blit(strip, (120, 200))
    game_displays.blit(strip, (680, 0))
    game_displays.blit(strip, (680, 100))
    game_displays.blit(strip, (680, 200))


def car(x, y):
    game_displays.blit(car_img, (x, y))


# Working on game
def game_loop():
    car_sound.play()
    global pause
    x = (display_width * 0.55)
    y = (display_height * 0.8)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    # Flag to indicate that the player has been crashed
    bumped = False

    while not bumped:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        # Update player's car position
        x += x_change
        # Set pause flag to True
        pause = True

        # Fill the game display with gray color
        game_displays.fill(gray)

        # Upgrade background position
        rel_y = y2 % background_pic.get_rect().width
        game_displays.blit(background_pic, (0, rel_y - background_pic.get_rect().width))
        game_displays.blit(background_pic, (700, rel_y - background_pic.get_rect().width))

        # Draw background strips
        if rel_y < 800:
            # Draw background strips
            game_displays.blit(background_pic, (0, rel_y))
            game_displays.blit(background_pic, (700, rel_y))
            game_displays.blit(yellow_strip, (400, rel_y))
            game_displays.blit(yellow_strip, (400, rel_y + 100))
            game_displays.blit(yellow_strip, (400, rel_y + 200))
            game_displays.blit(yellow_strip, (400, rel_y + 300))
            game_displays.blit(yellow_strip, (400, rel_y + 400))
            game_displays.blit(yellow_strip, (400, rel_y + 500))
            game_displays.blit(yellow_strip, (400, rel_y - 100))
            game_displays.blit(strip, (120, rel_y - 200))
            game_displays.blit(strip, (120, rel_y + 20))
            game_displays.blit(strip, (120, rel_y + 30))
            game_displays.blit(strip, (680, rel_y - 100))
            game_displays.blit(strip, (680, rel_y + 20))
            game_displays.blit(strip, (680, rel_y + 30))

        # Update obstacle positions and display them
        y2 += obstacle_speed
        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed

        # Ubdate player's car position and display it
        car(x, y)

        # Ubdate core system and display score
        score_system(passed, score)

        # Check for collision with screen edges and call crash() function if collison occurs
        if x > 690 - car_width or x < 110:
            crash()
        if x > display_width - (car_width + 110):
            crash()
        if x < 110:
            crash()

        # Ubdate obstacle positions and display them
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 7)
            passed = passed + 1
            score = passed * 10

            # Check for level up and update obstacle speed, display level text, and pause for 3 seconds
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed += 2
                largetext = pygame.font.Font('freesansbold.ttf', 80)
                textsurf, textrect = text_objects('LEVEL' + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                game_displays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        # Check for collision with obstacles and call crash() function if collision occurs
        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or \
                    x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()

        # Draw pause button
        button('Pause', 650, 0, 150, 50, blue, bright_blue, 'pause')

        # Ubdate game display and set frames per second to 60
        pygame.display.update()
        gameoverSound.stop()

        clock.tick(60)


# Calling functions
intro_loop()
game_loop()
pygame.quit()
quit()
