import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shahid Minar (Simplified)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (204, 0, 0)

# Function to draw the central pillar (rectangle)
def draw_central_pillar(x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x - width // 2, y - height, width, height))

# Function to draw smaller pillars
def draw_small_pillars(x, y, width, height):
    # Left small pillar
    pygame.draw.rect(screen, WHITE, (x - 150 - width // 2, y - height, width, height))
    # Right small pillar
    pygame.draw.rect(screen, WHITE, (x + 150 - width // 2, y - height, width, height))
    # Front-left small pillar
    pygame.draw.rect(screen, WHITE, (x - 50 - width // 2, y - height, width, height))
    # Front-right small pillar
    pygame.draw.rect(screen, WHITE, (x + 50 - width // 2, y - height, width, height))

# Function to draw the steps
def draw_steps(x, y, width, height):
    pygame.draw.rect(screen, WHITE, (x - 100, y, 200, height))  # bottom step
    pygame.draw.rect(screen, WHITE, (x - 80, y - height, 160, height))  # middle step
    pygame.draw.rect(screen, WHITE, (x - 60, y - 2 * height, 120, height))  # top step

# Function to draw the top circle (symbolizing the upper part)
def draw_top_circle(x, y, radius):
    pygame.draw.circle(screen, WHITE, (x, y), radius)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)  # Fill the background with black

    # Draw the simplified Shahid Minar structure
    draw_steps(300, 250, 40, 10)
    draw_central_pillar(300, 150, 20, 100)
    draw_small_pillars(300, 150, 10, 40)
    draw_top_circle(300, 100, 15)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
