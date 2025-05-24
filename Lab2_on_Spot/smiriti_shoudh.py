import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Structure")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fill background
screen.fill(BLACK)

# Draw base platform
pygame.draw.rect(screen, WHITE, (100, 400, 440, 20))  # rectangle(100, 400, 540, 420)
pygame.draw.line(screen, WHITE, (80, 420), (560, 420), 1)

# Main triangle
pygame.draw.line(screen, WHITE, (320, 100), (380, 400))
pygame.draw.line(screen, WHITE, (320, 100), (260, 400))
pygame.draw.line(screen, WHITE, (260, 400), (380, 400))

# Inner triangle
pygame.draw.line(screen, WHITE, (320, 160), (290, 300))
pygame.draw.line(screen, WHITE, (320, 160), (350, 300))
pygame.draw.line(screen, WHITE, (290, 300), (350, 300))

# Left side symmetrical triangles
pygame.draw.line(screen, WHITE, (260, 400), (230, 320))
pygame.draw.line(screen, WHITE, (230, 320), (200, 400))
pygame.draw.line(screen, WHITE, (200, 400), (180, 350))
pygame.draw.line(screen, WHITE, (180, 350), (160, 400))
pygame.draw.line(screen, WHITE, (160, 400), (140, 370))
pygame.draw.line(screen, WHITE, (140, 370), (120, 400))

# Right side symmetrical triangles
pygame.draw.line(screen, WHITE, (380, 400), (410, 320))
pygame.draw.line(screen, WHITE, (410, 320), (440, 400))
pygame.draw.line(screen, WHITE, (440, 400), (460, 350))
pygame.draw.line(screen, WHITE, (460, 350), (480, 400))
pygame.draw.line(screen, WHITE, (480, 400), (500, 370))
pygame.draw.line(screen, WHITE, (500, 370), (520, 400))

# Update display
pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
