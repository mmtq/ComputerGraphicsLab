import pygame
import math

# --- Setup ---
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("1. Dynamically Rotate a Point About the Origin")
clock = pygame.time.Clock()

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# --- Point and Rotation ---
point_pos = (150, 50)
angle_degrees = 0  # Start with no rotation
rotation_speed = 3 # Degrees per frame

# --- Center the coordinate system ---
center_x, center_y = screen_width // 2, screen_height // 2

def rotate_point_about_origin(x, y, angle_rad):
    """Rotates a point (x, y) about the origin (0, 0)."""
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return new_x, new_y

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
    rotated_x, rotated_y = rotate_point_about_origin(point_pos[0], point_pos[1], angle_radians)

    # --- Drawing ---
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (center_x, 0), (center_x, screen_height), 1)
    pygame.draw.line(screen, BLACK, (0, center_y), (screen_width, center_y), 1)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), 7)
    pygame.draw.circle(screen, BLUE, (center_x + point_pos[0], center_y - point_pos[1]), 7)
    pygame.draw.circle(screen, RED, (center_x + int(rotated_x), center_y - int(rotated_y)), 7)

    pygame.display.flip()
    clock.tick(60) # Limit frame rate to 60 FPS

pygame.quit()