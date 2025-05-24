import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 400, 400
WHITE, BLUE = (255, 255, 255), (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Arc")
screen.fill(WHITE)

def draw_arc(cx, cy, r, start_angle, end_angle, color):
    # angles in degrees
    for angle in range(start_angle, end_angle + 1):
        theta = math.radians(angle)
        x = int(cx + r * math.cos(theta))
        y = int(cy + r * math.sin(theta))
        screen.set_at((x, y), color)

# Draw arc from 45° to 135° with radius 100 centered at (200, 200)
draw_arc(200, 200, 100, 45, 135, BLUE)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
