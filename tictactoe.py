import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

# Define variables
line_width = 6
MARKERS = []
clicked = False
pos = []
player = 1
WINNER = 0
GAME_OVER = False

# Define colors
green = (0, 255, 0)
red = (255, 0, 0)


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
    MARKERS.append(row)


def draw_markers():
    x_pos = 0
    for x in MARKERS:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(
                    screen,
                    green,
                    (x_pos * 100 + 15, y_pos * 100 + 15),
                    (
                        x_pos * 100 + 85,
                        y_pos * 100 + 85,
                    ),
                    line_width,
                )
                pygame.draw.line(
                    screen,
                    green,
                    (x_pos * 100 + 15, y_pos * 100 + 85),
                    (
                        x_pos * 100 + 85,
                        y_pos * 100 + 15,
                    ),
                    line_width,
                )
            if y == -1:
                pygame.draw.circle(
                    screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width
                )
            y_pos += 1
        x_pos += 1


def check_winner():
    y_pos = 0
    for x in MARKERS:
        # Check columns
        if sum(x) == 3:
            WINNER = 1
            GAME_OVER = True
        if sum(x) == -3:
            WINNER = 1
            GAME_OVER = True
        # Check rows
        if MARKERS[0][y_pos] + MARKERS[1][y_pos] + MARKERS[2][y_pos] == 3:
            WINNER = 1
            GAME_OVER = True
        if MARKERS[0][y_pos] + MARKERS[1][y_pos] + MARKERS[2][y_pos] == -3:
            WINNER = 2
            GAME_OVER = True
        y_pos += 1

        # Check cross
        if (
            MARKERS[0][0] + MARKERS[1][1] + MARKERS[2][2] == 3
            or MARKERS[2][0] + MARKERS[1][1] + MARKERS[0][2] == 3
        ):
            WINNER = 1
            GAME_OVER = True


run = True
while run:
    draw_grid()
    draw_markers()
    # Add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if MARKERS[cell_x // 100][cell_y // 100] == 0:
                MARKERS[cell_x // 100][cell_y // 100] = player
                player *= -1
                check_winner()

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
