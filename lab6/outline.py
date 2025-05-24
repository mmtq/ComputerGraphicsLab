import pygame
import sys

def render_outline_text(text, font, text_color, outline_color, outline_width=1):
    # Render the main text
    text_surface = font.render(text, True, text_color)

    # Create a slightly larger surface for the outline + text
    width = text_surface.get_width() + 2 * outline_width
    height = text_surface.get_height() + 2 * outline_width
    outline_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Render the outline by blitting the text multiple times, offset
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0: # Don't draw center yet
                outline_text = font.render(text, True, outline_color)
                outline_surface.blit(outline_text, (dx + outline_width, dy + outline_width))

    # Blit the main text on top
    outline_surface.blit(text_surface, (outline_width, outline_width))

    return outline_surface

def main():
    # --- Pygame Initialization ---
    pygame.init()

    # --- Screen Setup ---
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Text Example")

    # --- Colors ---
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255) 
    YELLOW = (255, 255, 0) 

    try:
        font = pygame.font.SysFont('Arial', 50)
    except:
        font = pygame.font.Font(None, 60)

    # --- Text Rendering ---
    text_to_display = "Outline Font"
    # Use the outline function
    text_surface = render_outline_text(text_to_display, font, BLUE, YELLOW, outline_width=2)

    # --- Text Position ---
    text_x = 100
    text_y = 100

    # --- Main Loop ---
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                running = False

        # --- Drawing ---
        screen.fill(BLACK) # Fill background (graphics.h usually starts black)
        screen.blit(text_surface, (text_x, text_y)) # Draw the text

        # --- Update Display ---
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()