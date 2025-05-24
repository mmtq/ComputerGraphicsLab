import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Drawing Example")

screen.fill((255, 255, 255))

font = pygame.font.SysFont(None, 120) 

letterA = font.render('A', True, (0, 0, 0))
letterB = font.render('B', True, (0, 0, 0))

screen.blit(letterA, (100, 100))
screen.blit(letterB, (250, 100)) 

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
sys.exit()
