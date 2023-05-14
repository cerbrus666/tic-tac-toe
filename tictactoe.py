import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

# Define variables
line_width = 6
markers = []


def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(
            screen, grid, (0, x * 100), (screen_width, x * 100), line_width
        )
        pygame.draw.line(
            screen, grid, (x * 100, 0), (x * 100, screen_height), line_width
        )


for x in range(3):
    row = [0] * 3
    markers.append(row)

print(markers)

run = True
while run:
    draw_grid()
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
