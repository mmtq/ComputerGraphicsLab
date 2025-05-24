import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Display")

# Set background color
screen.fill((255, 255, 0))  # yellow

# Load font and render text
font = pygame.font.SysFont("Arial", 96)
text = font.render("Hello World", True, (0, 0, 255))  # Blue text

# Draw text to the screen
screen.blit(text, (100, 200))

pygame.display.flip()

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
