import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw A and B with Lines")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)

# Draw letter A
pygame.draw.line(screen, BLACK, (50, 200), (75, 100), 3)   # left diagonal
pygame.draw.line(screen, BLACK, (75, 100), (100, 200), 3)  # right diagonal
pygame.draw.line(screen, BLACK, (60, 150), (90, 150), 3)   # cross bar

# Draw letter B
pygame.draw.line(screen, BLACK, (150, 100), (150, 200), 3)  # vertical spine
pygame.draw.arc(screen, BLACK, (150, 100, 50, 50), 3.14 * 1.5, 3.14 * 2.5, 3)  # upper curve
pygame.draw.arc(screen, BLACK, (150, 150, 50, 50), 3.14 * 1.5, 3.14 * 2.5, 3)  # lower curve

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
