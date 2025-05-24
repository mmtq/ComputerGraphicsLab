import pygame
import math
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 400
WHITE, GREEN = (255, 255, 255), (0, 180, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ellipse - Trigonometric Method")
screen.fill(WHITE)

def draw_ellipse_trig(cx, cy, a, b, color):
    for angle in range(0, 360):
        theta = math.radians(angle)
        x = int(cx + a * math.cos(theta))
        y = int(cy + b * math.sin(theta))
        screen.set_at((x, y), color)

# Draw ellipse at center (250, 200), horizontal radius=150, vertical radius=100
draw_ellipse_trig(250, 200, 150, 100, GREEN)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
