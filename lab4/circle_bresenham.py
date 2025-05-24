import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
WHITE, BLUE = (255, 255, 255), (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle - Bresenham's Algorithm")
screen.fill(WHITE)

def draw_circle_bresenham(cx, cy, r, color):
    x = 0
    y = r
    d = 3 - 2 * r

    def plot_circle_points(cx, cy, x, y):
        for dx, dy in [
            (x, y), (-x, y), (x, -y), (-x, -y),
            (y, x), (-y, x), (y, -x), (-y, -x)
        ]:
            screen.set_at((cx + dx, cy + dy), color)

    while x <= y:
        plot_circle_points(cx, cy, x, y)
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

# Draw circle at center
draw_circle_bresenham(200, 200, 100, BLUE)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
