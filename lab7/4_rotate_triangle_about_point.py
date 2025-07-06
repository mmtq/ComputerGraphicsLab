import pygame
import math

# --- Setup ---
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("4. Dynamically Rotate a Triangle About a Point")
clock = pygame.time.Clock()

# --- Colors ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# --- Triangle, Pivot, and Rotation ---
triangle_vertices = [(300, 200), (500, 200), (400, 100)]
pivot_point = (250, 350)
angle_degrees = 0
rotation_speed = 2

def rotate_point_about_pivot(px, py, pivot_x, pivot_y, angle_rad):
    """Rotates a point (px, py) about a pivot point."""
    translated_x = px - pivot_x
    translated_y = py - pivot_y
    rotated_x = translated_x * math.cos(angle_rad) - translated_y * math.sin(angle_rad)
    rotated_y = translated_x * math.sin(angle_rad) + translated_y * math.cos(angle_rad)
    return rotated_x + pivot_x, rotated_y + pivot_y

# --- Main Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Handle Keyboard Input for Rotation ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle_degrees -= rotation_speed
    if keys[pygame.K_RIGHT]:
        angle_degrees += rotation_speed

    # --- Rotation Calculation (every frame) ---
    angle_radians = math.radians(angle_degrees)
    rotated_triangle_vertices = []
    for vertex in triangle_vertices:
        rotated_vertex = rotate_point_about_pivot(
            vertex[0], vertex[1],
            pivot_point[0], pivot_point[1],
            angle_radians
        )
        rotated_triangle_vertices.append(rotated_vertex)

    # --- Drawing ---
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, pivot_point, 7)
    pygame.draw.polygon(screen, BLUE, triangle_vertices)
    pygame.draw.polygon(screen, RED, rotated_triangle_vertices)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()