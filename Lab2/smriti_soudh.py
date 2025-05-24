import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Converted to Pygame")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Coordinates for the base rectangle
base_x1, base_y1 = 100, 100
base_x2, base_y2 = 300, 200

# Coordinates for the top angled part (triangle)
top_x1, top_y1 = 150, 200
top_x2, top_y2 = 250, 300
top_x3, top_y3 = 100, 200

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)  # Fill the background with black

    # Draw the base rectangle
    pygame.draw.rect(screen, WHITE, (base_x1, base_y1, base_x2 - base_x1, base_y2 - base_y1), 2)

    # Draw the top angled part (triangle)
    pygame.draw.line(screen, WHITE, (top_x1, top_y1), (top_x2, top_y2), 2)
    pygame.draw.line(screen, WHITE, (top_x2, top_y2), (top_x3, top_y3), 2)
    pygame.draw.line(screen, WHITE, (top_x3, top_y3), (top_x1, top_y1), 2)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
