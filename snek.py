import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and Apple properties
block_size = 20
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont(None, 30)

# Function to display message on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Function to display snake
def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], block_size, block_size])

# Function to display game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial positions
    x1 = width / 2
    y1 = height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Random apple position
    foodx = round(random.randrange(0, width - block_size) / 20) * 20
    foody = round(random.randrange(0, height - block_size) / 20) * 20

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Boundary conditions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update position
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(display, red, [foodx, foody, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_list)
        pygame.display.update()

        # Collision detection
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20) * 20
            foody = round(random.randrange(0, height - block_size) / 20) * 20
            length_of_snake += 1

        pygame.display.update()

        # Speed control
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()