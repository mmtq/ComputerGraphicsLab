import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smiling Face")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Clock
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen, YELLOW, (200, 200), 100)  # face
    pygame.draw.circle(screen, BLACK, (160, 170), 10)    # left eye
    pygame.draw.circle(screen, BLACK, (240, 170), 10)    # right eye

    # smile (arc)
    mouth_rect = pygame.Rect(150, 200, 100, 50)
    pygame.draw.arc(screen, BLACK, mouth_rect, math.pi, 2 * math.pi, 3) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
