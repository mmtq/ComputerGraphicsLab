import pygame
import sys
import collections # Using collections.deque can be slightly more efficient for stack/queue

# Iterative flood fill function (using a stack)
def flood_fill_iterative(surface, x, y, new_color):
    width = surface.get_width()
    height = surface.get_height()

    # Get the color of the starting pixel
    try:
        old_color = surface.get_at((x, y))
    except IndexError:
        print(f"Start coordinates ({x}, {y}) out of bounds.")
        return # Start point is outside the screen

    # If the start color is the same as the new color, or if the start
    # point is outside, do nothing.
    if old_color == new_color:
        return

    # Create a stack (or queue) and add the starting point
    stack = collections.deque([(x, y)])

    # Process the stack
    while stack:
        px, py = stack.pop()

        # Check if the current pixel is within bounds
        if 0 <= px < width and 0 <= py < height:
            # If the current pixel has the old color, change it and add neighbors
            if surface.get_at((px, py)) == old_color:
                surface.set_at((px, py), new_color)

                # Add neighbors to the stack
                stack.append((px + 1, py))
                stack.append((px - 1, py))
                stack.append((px, py + 1))
                stack.append((px, py - 1))


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Flood Fill Example (Iterative)")

# Fill background white
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen.fill(WHITE)

# Draw rectangle (same coordinates as in C++)
pygame.draw.rect(screen, BLACK, (100, 100, 100, 100), 1)  # outline only

# Perform flood fill from inside the rectangle
# Get the color we want to replace (should be WHITE)
start_x, start_y = 150, 150
flood_fill_iterative(screen, start_x, start_y, RED)  # fill with red

# Update the display
pygame.display.flip()

# Wait until window is closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()