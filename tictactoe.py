import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")


run = True
while run:
    # Add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()


# Part 1
# Import modules
# Create grid and setup the grid list

# Part 2
# Create event handler for clicking on a cell
# Check if cell is empty and place a marker
# Setup function for drawing markers onto the grid


# Part 3
# Create check winner function including checks for winning combinations
# Create event handle for post game
# Reset game
