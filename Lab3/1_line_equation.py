import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Line Equation")

screen.fill((255, 255, 255))

# Line equation: y = x + 50
# We will draw the line from x = 0 to x = 600
m = 1  # Slope
b = 50  # y-intercept

start_x = 0
end_x = 600

start_y = m * start_x + b
end_y = m * end_x + b

pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
