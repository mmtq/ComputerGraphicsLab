import pygame
import math
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
WHITE, RED = (255, 255, 255), (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle - Polynomial Method")
screen.fill(WHITE)

def draw_circle_polynomial(cx, cy, r, color):
    for x in range(-r, r + 1):
        y = int(math.sqrt(r * r - x * x))
        screen.set_at((cx + x, cy + y), color)
        screen.set_at((cx + x, cy - y), color)

# Draw circle at center
draw_circle_polynomial(200, 200, 100, RED)
pygame.display.flip()

# Main loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
