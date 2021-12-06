# https://www.youtube.com/watch?v=FfWpgLFMI7w
# Guiden för detta spel

import pygame
import time

# Initialize the pygame
pygame.init()
game_over = False

# Create the screen
screen = pygame.display.set_mode((1024, 800))
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')
game_over_screen = pygame.image.load('go.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 512
playerY = 700
player_change = 0

# Enemy
enemyImg = pygame.image.load('invader2.png')
enemyX = 512
enemyY = 30
enemy_change = 0.12

# Projectile
proj = pygame.image.load('proj.png')
projX = 0
projY = playerY
projY_change = 0.80
projectilesX = []
projectilesY = []
n_enemies = 3


def fire(x):
    projectilesX.append(x)
    projectilesY.append(playerY)


def draw_proj(x, y):
    screen.blit(proj, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def enemy_array(number):
    e_array = []
    for enee in range(number):
        e_array.append(512 + enee * 48 - 6 * 48)
    return e_array


enemies = enemy_array(n_enemies)
destroyed = enemy_array(n_enemies)

enemy_charge = 0

# Game loop
running = True
while running:
    # RGB - Red, Green, Blue

    screen.fill((192, 192, 192))
    screen.blit(background, (0, 0))

    # if pygame.key.get_pressed()[pygame.K_RIGHT] and playerX <= 1000 :
    #       playerX += 0.1
    # if pygame.key.get_pressed()[pygame.K_LEFT] and playerX >= -10 :
    #       playerX -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(projectilesY) < 2:
                    fire(playerX)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and playerX >= 0:
                player_change = -0.2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and playerX <= 1000:
                player_change = 0.2
        if event.type == pygame.KEYUP:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                player_change = 0.2
            elif keys_pressed[pygame.K_LEFT]:
                player_change = -0.2
            elif keys_pressed[pygame.K_RIGHT] == False and keys_pressed[pygame.K_LEFT] == False:
                player_change = 0
            # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #   player_change = 0.
    # Draw enemy

    for e in range(n_enemies):
        if destroyed[e] > 0:
            if (enemies[e] >= 976) or (enemies[e] <= 24):
                enemy_change = enemy_change * -1
                enemy_charge += 1
            enemies[e] += enemy_change
            enemy(int(enemies[e]), enemyY)

    if enemy_charge >= 1:
        enemy_charge = 0
        enemy_change *= 1.05
        enemyY = enemyY + 30

    # Check for collision
    if len(projectilesY) > 1:
        if projectilesY[1] <= (enemyY + 23) and projectilesY[1] <= (enemyY):
            counter = 0
            for h in enemies:
                if destroyed[counter] > 0:
                    if projectilesX[1] >= (h-8) and projectilesX[1] <= (h + 8):
                        projectilesY.pop(1)
                        projectilesX.pop(1)
                        destroyed[counter] = -10
                        enemies[counter] = -100
                        break
                counter += 1

    if len(projectilesY) > 0:
        if projectilesY[0] <= (enemyY + 23) and projectilesY[0] <= (enemyY):
            counter = 0
            for h in enemies:
                if destroyed[counter] > 0:
                    if projectilesX[0] >= (h-8) and projectilesX[0] <= (h + 8):
                        projectilesY.pop(0)
                        projectilesX.pop(0)
                        destroyed[counter] = -10
                        break
                counter += 1

    # Draw Projectiles
    if len(projectilesY) != 0:
        for projectile in range(len(projectilesY), 0, -1):
            if projectilesY[projectile - 1] > 1:
                projectilesY[projectile - 1] -= projY_change
                draw_proj(projectilesX[projectile - 1], projectilesY[projectile - 1])
            else:
                projectilesY.pop(0)
                projectilesX.pop(0)

    # Draw player
    playerX += player_change
    player(playerX, playerY)


    for e in range(len(destroyed)):
        round_over = True
        if destroyed[e] > 0:
            round_over = False
            break
    if round_over:
        if n_enemies >= 1:
            n_enemies -= 1
            player_change *= 1.1
            enemies = enemy_array(n_enemies)
            destroyed = enemy_array(n_enemies)
            game_over = False
        else: game_over = True
    if game_over:
        screen.blit(game_over_screen, (0, 0))
        pygame.display.update()# print("game over")
        time.sleep(3)
        # print("Bye")
        running = False

    # Updating the display
    pygame.display.update()

    if (enemyY + 24) >= playerY:
        break
