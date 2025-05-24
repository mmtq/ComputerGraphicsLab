import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bangladeshi Flag")

GREEN = (0, 106, 78)
RED = (204, 0, 0) 

circle_radius = 100
circle_center = (280, 200)

clock = pygame.time.Clock()
while True:
    screen.fill(GREEN) 

    pygame.draw.circle(screen, RED, circle_center, circle_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
