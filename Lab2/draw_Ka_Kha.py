import pygame
import sys
import math

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw ক (Ka) and খ (Kha) manually")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_ka(x, y):
    # Simulated ক (Ka)
    pygame.draw.line(screen, WHITE, (x, y), (x, y + 40), 2)  # vertical
    pygame.draw.line(screen, WHITE, (x, y + 20), (x + 20, y + 10), 2)  # diagonal
    pygame.draw.arc(screen, WHITE, (x, y - 10, 30, 20), math.pi, 2 * math.pi, 2)  # upper curve (matra)
    pygame.draw.line(screen, WHITE, (x + 15, y + 15), (x + 15, y + 40), 2)  # short vertical leg

def draw_kha(x, y):
    # Simulated খ (Kha)
    pygame.draw.arc(screen, WHITE, (x, y - 10, 30, 20), math.pi, 2 * math.pi, 2)  # upper curve (matra)
    pygame.draw.line(screen, WHITE, (x + 5, y), (x + 5, y + 40), 2)  # main vertical
    pygame.draw.line(screen, WHITE, (x + 5, y + 20), (x + 25, y + 15), 2)  # diagonal arm
    pygame.draw.line(screen, WHITE, (x + 25, y + 15), (x + 25, y + 40), 2)  # tail down

clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    draw_ka(100, 100)
    draw_kha(180, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
