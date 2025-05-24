import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fill background
screen.fill(BLACK)

# DDA Line Drawing Function
def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        screen.set_at((int(round(x)), int(round(y))), WHITE)
        x += x_inc
        y += y_inc

# Call the DDA line function with start and end points
draw_line_dda(100, 100, 500, 300)

# Update the display
pygame.display.flip()

# Wait for exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
