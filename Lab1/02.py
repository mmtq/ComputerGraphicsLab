import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Text Display")

# Set background color
screen.fill((255, 255, 255))

# Load font and render text
font = pygame.font.SysFont("Arial", 48)
text = font.render("Hello World", True, (0, 0, 255))  # Blue text

# Draw text to the screen
screen.blit(text, (100, 120))

pygame.display.flip()

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()