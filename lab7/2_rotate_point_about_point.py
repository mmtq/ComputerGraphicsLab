import pygame
import math

# --- Setup ---
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2. Dynamically Rotate a Point About Another Point")
clock = pygame.time.Clock()

# --- Colors ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# --- Point, Pivot, and Rotation ---
point_to_rotate = (350, 200)
pivot_point = (250, 300)
angle_degrees = 0
rotation_speed = 3

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
    rotated_point_pos = rotate_point_about_pivot(
        point_to_rotate[0], point_to_rotate[1],
        pivot_point[0], pivot_point[1],
        angle_radians
    )

    # --- Drawing ---
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, pivot_point, 7)
    pygame.draw.circle(screen, BLUE, point_to_rotate, 7)
    pygame.draw.circle(screen, RED, (int(rotated_point_pos[0]), int(rotated_point_pos[1])), 7)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()