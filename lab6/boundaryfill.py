import pygame
import sys
import collections

# Iterative boundary fill function (using a stack)
def boundary_fill_iterative(surface, x, y, fill_color, boundary_color):
    width = surface.get_width()
    height = surface.get_height()

    # Create a stack (or queue) and add the starting point
    stack = collections.deque([(x, y)])

    # Process the stack
    while stack:
        px, py = stack.pop()

        # 1. Check bounds
        if not (0 <= px < width and 0 <= py < height):
            continue

        # 2. Get current color
        current_color = surface.get_at((px, py))

        # 3. Check if it's NOT boundary and NOT already filled
        if current_color != boundary_color and current_color != fill_color:
            # 4. Fill the pixel
            surface.set_at((px, py), fill_color)

            # 5. Add neighbors to the stack
            stack.append((px + 1, py))
            stack.append((px - 1, py))
            stack.append((px, py + 1))
            stack.append((px, py - 1))

# --- Your Original Pygame Code (with the new boundary_fill) ---

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Boundary Fill Example (Iterative)")

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fill background white
screen.fill(WHITE)

# Draw black rectangle (boundary color = black)
pygame.draw.rect(screen, BLACK, (100, 100, 100, 100), 1)

# Call boundary fill inside the rectangle
boundary_fill_iterative(
    screen,
    150,
    150,
    RED,    # fill color = red
    BLACK   # boundary color = black
)

# Update display
pygame.display.flip()

# Wait until window is closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()