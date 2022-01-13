import pygame
import random
import math
from pygame import mixer
# This game is based on the game "Space Invaders"
# Based on tutorial: https://www.youtube.com/watch?v=FfWpgLFMI7w
# freeCodeCamp.org
# Images by https://www.flaticon.com/icons

# Initialize the pygame module
pygame.init()

# Create game screen | Parameters of screen width / height
screen = pygame.display.set_mode((800, 600))

# Add background image
background = pygame.image.load("background.jpg")

# Add Background sound
mixer.music.load('background.wav')
mixer.music.play(-1) # -1 to loop .wav file

# Change Title and icon of window | Image by https://www.flaticon.com/icons
pygame.display.set_caption("Task 15 - A Simple Game (by: Yolandie Wilsch)")
icon = pygame.image.load("artificial-intelligence.png")
pygame.display.set_icon(icon) # Change the icon image in the title bar of the game window

# Create player, position player at the bottom of the screen in the middle
playerImg = pygame.image.load("turtles.png")
playerX = 370 # horizontal position
playerY = 480 # vertical position
playerX_change = 0
playerY_change = 0

# Creating the enemies
# Create empty lists, and iterate through each enemy constructor to include
# the number of enemies you want ie. 6
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Introduce 6 enemy objects for the game
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("seagull.png"))
    enemyX.append(random.randint(0, 735)) # each object appears randomly within 735pixels from side
    enemyY.append(random.randint(50, 150)) # each object appears randomly within 150 pixels from top
    enemyX_change.append(0.3) # Speed at which objects move horizontally
    enemyY_change.append(40) # pixels the objects drop at when they hit the size of the window

# Bullet
# Ready state - you can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480 # Starting point of player object
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready" # When bullet is NOT seen, it is "ready" to be fired

# Keeping track of the score
score_value = 0
font = pygame.font.Font("CHERI___.ttf", 32) # downloaded font from dafont.com
textX = 10 # horizontal position of text
textY = 10 # vertical position of text

# Game Over Text
over_font = pygame.font.Font("CHERI___.ttf", 70)

# The score function renders the text on the screen, drawing it onto the background image
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

# The "GAME OVER" text is displayed at x=200 y= 250 once enemy objects reach a certain Y position
def game_over_text():
    over_text = over_font.render("GAME OVER: " + str(score_value), True, (0, 0, 0))
    screen.blit(over_text, (200, 250))

# Drawing the Player object onto the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# Drawing the enemy objects onto the screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Function to fire the bullet from the center of the player object
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Distance between two coordinates:
# https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint
# If the bullet hits the enemy object, the enemy is eliminated and a score of 1 is added
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27: # reasonable distance within enemy object to be classified a "collision"
        return True
    else:
        return False

# Game Loop
running = True
while running:
    # RGB - Red | Green | Blue
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    # Closes the Window when the red cross button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if keystroke [ LEFT or RIGHT or UP or DOWN] is pressed
        if event.type == pygame.KEYDOWN: # Checking for keys that are pressed
            if event.key == pygame.K_LEFT: # if LEFT is pressed, change PlayerX position by -0.3px
                playerX_change = -0.3
            if event.key == pygame.K_UP: # if UP is pressed, change PlayerY position by -0.3px
                playerY_change = -0.3
            if event.key == pygame.K_RIGHT: # if RIGHT is pressed, change PlayerX position by 0.3px
                playerX_change = 0.3
            if event.key == pygame.K_DOWN: # if DOWN is pressed, change PlayerX position by 0.3px
                playerY_change = 0.3
            if event.key == pygame.K_SPACE: # if SPACE is pressed, fire a bullet (function)
                if bullet_state == "ready": # the bullet_state MUST be == "ready" to be fired
                    bullet_sound = mixer.Sound("laser.wav") # play sound when "fire"
                    bullet_sound.play()
                    # Get the current  co-ordinate of the turtle & stores it in bulletX
                    bulletX = playerX # Find position of PlayerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP: # Once any of the pressed keys are released, update PlayerX and PlayerY position
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    # Checking Player boundaries - checking turtle does not go off screen / out of bounds
    playerX += playerX_change # New position for playerX
    playerY += playerY_change # New position for playerY

    # Ensure the player is not able to exit the game window - placing boundaries
    if playerX <= 0: # placing boundaries on the left of the window
        playerX = 0
    elif playerY <= 0: # placing boundaries on the top of the window
        playerY = 0
    elif playerX >= 736: # placing boundaries on the right of the window
        playerX = 736
    elif playerY >= 736: # placing boundaries on the bottom of the window
        playerY = 736

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480 # Starting vertical position for the bullet
        bullet_state = "ready" # as soon as bullet_state returns to "ready"

    if bullet_state == "fire": # Bullet is released, and travels upward independantly of player object
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Checking Enemy boundaries - checking seagull does not go off screen / out of bounds
    for i in range(num_of_enemies):
    # When enemy objects reach lower than 440px:
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000 # move enemy objects to vertical position 2000 (taking them off the screen)
            game_over_text() # call the game_over_text() function
            break

        # Enemy movement - iterate through enemy object for loop
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3 # speed of enemy objects
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736: # enemy boundary wall
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # When the bullet collides with the enemy
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bulletY = 480 # starting point for bullet
            bullet_state = "ready"
            score_value += 1 # add 1 to score
            enemyX[i] = random.randint(0, 735) # initiate another enemy object randomly
            enemyY[i] = random.randint(50, 150) # initiate anotehr enemy object randomly (top)

        enemy(enemyX[i], enemyY[i], i)

    # Display the player object as a constant throughout the game
    player(playerX, playerY)
    # Display the score on the screen as a constant throughout the game
    show_score(textX, textY)
    # Update the loop
    pygame.display.update()
