import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line, Circle, and Rectangle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    # Draw a line: from (50, 50) to (200, 50)
    pygame.draw.line(screen, WHITE, (50, 50), (200, 50), 2)

    # Draw a circle: center at (150, 150), radius 40
    pygame.draw.circle(screen, WHITE, (150, 150), 40, 2)

    # Draw a rectangle: top-left at (250, 100), width=100, height=60
    pygame.draw.rect(screen, WHITE, (250, 100, 100, 60), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
