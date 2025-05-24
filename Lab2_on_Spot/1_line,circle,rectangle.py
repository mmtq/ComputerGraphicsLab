import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line, Circle, and Rectangle")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, (50, 50), (200, 50), 2)

    pygame.draw.circle(screen, WHITE, (150, 150), 40, 2)

    pygame.draw.rect(screen, WHITE, (250, 100, 100, 60), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
