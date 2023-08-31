import pygame
import random

# Initialize pygame
pygame.init()

# CreatingWindow(width,height)
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption('Space Wars')
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('bg-img.png')

# Player
playerImg = pygame.image.load('ufo1.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enimy
enimyImg = pygame.image.load('alien.png')
enimyX = random.randint(0, 800)
enimyY = random.randint(50, 150)
enimyX_change = 2
enimyY_change = 40


def enimy(x, y):
    screen.blit(enimyImg, (x, y))


# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'


def bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


# Game Specific Variable
running = True

#  Creating a game loop
while running:
    # (R,G,B)
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If any key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
                print('Left arrow is pressed')
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                print('Right arrow is pressed')
            if event.key == pygame.K_SPACE:
                bullet(playerX,playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print('Left or Right arrow is Released')

    # Checking for boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enimyX += enimyX_change

    if enimyX <= 0:
        enimyX_change = 2
        enimyY += enimyY_change
    elif enimyX >= 736:
        enimyX_change = -2
        enimyY += enimyY_change

    #Bullet Movement


    player(playerX, playerY)
    enimy(enimyX, enimyY)
    pygame.display.update()
 
    