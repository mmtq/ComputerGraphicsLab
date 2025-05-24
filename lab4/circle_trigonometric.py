import pygame
import math
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
WHITE, GREEN = (255, 255, 255), (0, 200, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle - Trigonometric Method")
screen.fill(WHITE)

def draw_circle_trig(cx, cy, r, color):
    for angle in range(0, 360):
        theta = math.radians(angle)
        x = int(cx + r * math.cos(theta))
        y = int(cy + r * math.sin(theta))
        screen.set_at((x, y), color)

# Draw circle at center
draw_circle_trig(200, 200, 100, GREEN)
pygame.display.flip()

# Main loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
