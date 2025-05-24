import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bangladeshi Flag")

# Colors
GREEN = (0, 106, 78)  # Flag green
RED = (204, 0, 0)    # Flag red

# Dimensions for the red circle
circle_radius = 75
circle_center = (250, 200)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(GREEN)  # Fill the screen with green

    # Draw the red circle (slightly off-center)
    pygame.draw.circle(screen, RED, circle_center, circle_radius)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
