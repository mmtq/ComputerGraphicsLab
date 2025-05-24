import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
WHITE, PURPLE = (255, 255, 255), (128, 0, 128)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle - Midpoint Algorithm")
screen.fill(WHITE)

def draw_circle_midpoint(cx, cy, r, color):
    x = r
    y = 0
    p = 1 - r

    def plot_circle_points(cx, cy, x, y):
        for dx, dy in [
            (x, y), (-x, y), (x, -y), (-x, -y),
            (y, x), (-y, x), (y, -x), (-y, -x)
        ]:
            screen.set_at((cx + dx, cy + dy), color)

    while x >= y:
        plot_circle_points(cx, cy, x, y)
        y += 1
        if p < 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * (y - x) + 1

# Draw circle at center
draw_circle_midpoint(200, 200, 100, PURPLE)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
