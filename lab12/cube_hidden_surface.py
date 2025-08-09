import pygame
import math

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube with Painter's Algorithm")
clock = pygame.time.Clock()

# --- Colors ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Using different colors for each face to make them distinguishable
FACE_COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255)
]

# --- 3D Cube Definition ---
# Each point is a vertex in 3D space (x, y, z)
points = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
]

# --- Projection Settings ---
projection_matrix = [
    [1, 0, 0],
    [0, 1, 0]
]
scale = 100
angle_x, angle_y, angle_z = 0, 0, 0

# --- Main Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Handle Keyboard Input for Rotation ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle_y -= 0.03
    if keys[pygame.K_RIGHT]:
        angle_y += 0.03
    if keys[pygame.K_UP]:
        angle_x -= 0.03
    if keys[pygame.K_DOWN]:
        angle_x += 0.03
        
    # Automatic rotation
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01


    # --- 3D to 2D Projection and Rotation ---
    rotated_points = []
    for point in points:
        # Rotate around X-axis
        rotated_x = point[0]
        rotated_y = point[1] * math.cos(angle_x) - point[2] * math.sin(angle_x)
        rotated_z = point[1] * math.sin(angle_x) + point[2] * math.cos(angle_x)
        
        # Rotate around Y-axis
        temp_x = rotated_x * math.cos(angle_y) + rotated_z * math.sin(angle_y)
        temp_y = rotated_y
        temp_z = -rotated_x * math.sin(angle_y) + rotated_z * math.cos(angle_y)

        # Rotate around Z-axis
        final_x = temp_x * math.cos(angle_z) - temp_y * math.sin(angle_z)
        final_y = temp_x * math.sin(angle_z) + temp_y * math.cos(angle_z)
        final_z = temp_z
        
        rotated_points.append([final_x, final_y, final_z])

    # Project 3D points to 2D screen coordinates
    projected_points = []
    for point in rotated_points:
        projected_x = point[0] * scale + WIDTH / 2
        projected_y = point[1] * scale + HEIGHT / 2
        projected_points.append((projected_x, projected_y))

    # --- Painter's Algorithm Implementation ---
    faces = [
        (0, 1, 2, 3), # Back
        (4, 5, 6, 7), # Front
        (0, 4, 7, 3), # Left
        (1, 5, 6, 2), # Right
        (3, 2, 6, 7), # Top
        (0, 1, 5, 4)  # Bottom
    ]

    # Calculate the average Z-depth for each face
    face_depths = []
    for i, face in enumerate(faces):
        # Sum the z-coordinates of all vertices of the face
        avg_z = sum(rotated_points[j][2] for j in face) / len(face)
        face_depths.append((i, avg_z))

    # Sort the faces from farthest to nearest (min z to max z)
    face_depths.sort(key=lambda x: x[1])

    # --- Drawing ---
    screen.fill(BLACK)

    # Draw the faces in the sorted order
    for face_index, _ in face_depths:
        face_vertices_indices = faces[face_index]
        face_screen_coords = [projected_points[i] for i in face_vertices_indices]
        
        pygame.draw.polygon(screen, FACE_COLORS[face_index], face_screen_coords)
        # Draw outlines for better visibility
        pygame.draw.polygon(screen, WHITE, face_screen_coords, 2)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()