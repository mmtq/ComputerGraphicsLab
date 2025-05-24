import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ka Kha")

screen.fill((255, 255, 255))

font = pygame.font.SysFont('Nirmala UI', 60) 

letter_ka = font.render('ক', True, (0, 0, 0)) 
letter_kha = font.render('খ', True, (0, 0, 0)) 

screen.blit(letter_ka, (100, 100))
screen.blit(letter_kha, (200, 100))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
