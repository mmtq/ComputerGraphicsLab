import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shahid Minar")

# Colors
WHITE = (255, 255, 255)
DARKGRAY = (64, 64, 64)
RED = (255, 0, 0)

screen.fill(DARKGRAY)

midX = WIDTH // 2
baseY = HEIGHT - 100

# Draw stairs (6 steps)
stepY = baseY
step_width = 700
shahid_minar_width = 60
for i in range(6):
    x = midX - step_width // 2
    pygame.draw.rect(screen, WHITE, (x, stepY, step_width, 10), 1)
    stepY -= 10
    step_width -= (step_width - shahid_minar_width) // 6

# Draw red sun
pygame.draw.circle(screen, RED, (midX, stepY - 70), 50)

# Draw central structure
pygame.draw.rect(screen, WHITE, (midX - 30, stepY - 200, 60, 200), 1)
pygame.draw.line(screen, WHITE, (midX - 15, stepY - 200), (midX - 15, stepY))
pygame.draw.line(screen, WHITE, (midX + 15, stepY - 200), (midX + 15, stepY))

# Draw side pillars
pygame.draw.rect(screen, WHITE, (midX - 80, stepY - 150, 30, 150), 1)
pygame.draw.rect(screen, WHITE, (midX + 50, stepY - 150, 30, 150), 1)
pygame.draw.rect(screen, WHITE, (midX - 120, stepY - 100, 20, 100), 1)
pygame.draw.rect(screen, WHITE, (midX + 100, stepY - 100, 20, 100), 1)

# Draw text
font = pygame.font.SysFont(None, 36)
text = font.render("Shahid Minar", True, WHITE)
screen.blit(text, (midX - 80, baseY + 20))

pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
