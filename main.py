import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('grassy.png')

pygame.display.set_caption("Tank Game")

player = pygame.image.load('player1.png')
opponent = pygame.image.load('player2.png')

icon = pygame.image.load('tank.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player1.png')
playerX = 250
playerY = 480

# Opponent
opponentImg = pygame.image.load('player2.png')
opponentX = 500
opponentY = 480

# Define stuff

display_orig_player = True


def player(x, y):
    while display_orig_player:
        screen.blit(playerImg, (x, y))
        break


def opponent(x, y):
    screen.blit(opponentImg, (x, y))

# Player Movement Stuff


rotate_left = False
rotate_right = False
move_down = False
move_up = False
Img = playerImg
playerUP_change = 0
playerDOWN_change = 0

# Game running


running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    display_new_player = screen.blit(Img, (playerX - 5, playerY - 5))
    angle = 0

    while rotate_left:
        scale = 1
        display_orig_player = False
        for angle in (0, 360, -10):
            Img = pygame.transform.rotozoom(playerImg, angle, scale)
            screen.blit(Img, (playerX - 5, playerY - 5))

        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotate_left = True
            if event.key == pygame.K_RIGHT:
                rotate_right = True
            if event.key == pygame.K_UP:
                playerUP_change = -1
            if event.key == pygame.K_DOWN:
                playerDOWN_change = 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rotate_left = False
                # display_new_player
            if event.key == pygame.K_RIGHT:
                rotate_right = False
            if event.key == pygame.K_UP:
                playerUP_change = 0
            if event.key == pygame.K_DOWN:
                playerDOWN_change = 0

    playerY += playerUP_change
    playerY += playerDOWN_change
    player(playerX, playerY)
    opponent(opponentX, opponentY)
    pygame.display.update()

# MOVEMENT STUFF HERE

#    elif rotate_right:
#    angle = 0
#    while rotate_right:
#        rotated_image = pygame.transform.rotate(playerImg, angle)
#        angle += 10
#        screen.blit(rotated_image, (playerX - 5, playerY - 5))
#        pygame.display.flip()
#        break

# elif move_down:
# playerY += 1
# elif move_up:
# playerY -= 1
