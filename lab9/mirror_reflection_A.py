import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mirror Reflection of 'A'")

WHITE, BLACK, RED, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 128, 255)
FONT = pygame.font.SysFont("Arial", 120, bold=True)

def draw_axes():
    # Draw vertical y-axis at center
    pygame.draw.line(WIN, (150, 150, 150), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    # Draw horizontal x-axis at center
    pygame.draw.line(WIN, (150, 150, 150), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)

def mirror_reflect_point(px, py, axis='vertical', axis_pos=WIDTH//2):
    # Reflect point px,py about a vertical or horizontal axis at axis_pos
    if axis == 'vertical':
        # Mirror about vertical line x = axis_pos
        dx = px - axis_pos
        rx = axis_pos - dx
        return rx, py
    elif axis == 'horizontal':
        # Mirror about horizontal line y = axis_pos
        dy = py - axis_pos
        ry = axis_pos - dy
        return px, ry
    else:
        return px, py  # no change if axis unknown

def main():
    clock = pygame.time.Clock()
    axis = 'vertical'  # Change to 'horizontal' to reflect about horizontal axis

    running = True
    while running:
        clock.tick(60)
        WIN.fill(BLACK)
        draw_axes()

        # Render character 'A'
        char_surf = FONT.render("A", True, RED)
        char_rect = char_surf.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2))

        # Draw original 'A'
        WIN.blit(char_surf, char_rect)

        # Calculate mirrored position of the rect center
        mx, my = mirror_reflect_point(char_rect.centerx, char_rect.centery, axis=axis, axis_pos=WIDTH // 2)

        # Draw mirrored 'A'
        mirrored_rect = char_surf.get_rect(center=(mx, my))
        WIN.blit(char_surf, mirrored_rect)

        # Labels
        font_small = pygame.font.SysFont(None, 24)
        WIN.blit(font_small.render(f"Mirroring about {axis} axis", True, WHITE), (10, 10))
        WIN.blit(font_small.render("Press H for horizontal axis, V for vertical axis", True, WHITE), (10, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    axis = 'vertical'
                elif event.key == pygame.K_h:
                    axis = 'horizontal'

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
