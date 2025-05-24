import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw A and B")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Draw letter A using lines
def drawA(x, y):
    pygame.draw.line(screen, WHITE, (x, y), (x - 20, y + 50), 2)  # Left leg
    pygame.draw.line(screen, WHITE, (x, y), (x + 20, y + 50), 2)  # Right leg
    pygame.draw.line(screen, WHITE, (x - 10, y + 25), (x + 10, y + 25), 2)  # Crossbar

# Draw letter B using lines and arcs
def drawB(x, y):
    pygame.draw.line(screen, WHITE, (x, y), (x, y + 50), 2)  # Vertical line
    pygame.draw.arc(screen, WHITE, (x, y, 20, 30), 3.14 * 1.5, 3.14 * 0.5, 2)  # Upper curve
    pygame.draw.arc(screen, WHITE, (x, y + 20, 20, 30), 3.14 * 1.5, 3.14 * 0.5, 2)  # Lower curve
    pygame.draw.line(screen, WHITE, (x, y + 25), (x + 10, y + 25), 2)  # Connector

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    drawA(100, 100)
    drawB(150, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
