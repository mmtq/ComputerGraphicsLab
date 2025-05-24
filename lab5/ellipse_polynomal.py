import pygame
import math
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 400
WHITE, RED = (255, 255, 255), (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ellipse - Polynomial Method")
screen.fill(WHITE)

def draw_ellipse_polynomial(cx, cy, a, b, color):
    for x in range(-a, a + 1):
        y = int(b * math.sqrt(1 - (x**2) / (a**2)))
        screen.set_at((cx + x, cy + y), color)
        screen.set_at((cx + x, cy - y), color)

# Draw ellipse at center (cx=250, cy=200), horizontal radius=150, vertical radius=100
draw_ellipse_polynomial(250, 200, 150, 100, RED)
pygame.display.flip()

# Main loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
