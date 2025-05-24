import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Bitmap Font Example")

# Fill background white
screen.fill((255, 255, 255))

# Use default font, size 24
font = pygame.font.SysFont(None, 24)
text_surface = font.render("This is Bitmap Font", True, (0, 0, 0))

# Blit text at (100, 100)
screen.blit(text_surface, (100, 100))

# Update display
pygame.display.flip()

# Wait for window to be closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
