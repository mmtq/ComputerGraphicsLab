import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 400, 400
WHITE, ORANGE = (255, 255, 255), (255, 140, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sector (Pie Slice)")
screen.fill(WHITE)

def draw_sector(cx, cy, r, start_angle, end_angle, color):
    # Fill the sector by drawing lines from center to arc points
    for angle in range(start_angle, end_angle + 1):
        theta = math.radians(angle)
        x = int(cx + r * math.cos(theta))
        y = int(cy + r * math.sin(theta))
        pygame.draw.line(screen, color, (cx, cy), (x, y))

# Draw sector from 30° to 120° with radius 100 centered at (200, 200)
draw_sector(200, 200, 100, 30, 120, ORANGE)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
