import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scale Point About Origin")

WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
FONT = pygame.font.SysFont(None, 24)

def draw_text(text, x, y):
    WIN.blit(FONT.render(text, True, WHITE), (x, y))

def scale_point(x, y, sx, sy):
    return x * sx, y * sy

def main():
    clock = pygame.time.Clock()
    point = (100, 60)  # Relative to origin
    sx, sy = 1, 1

    running = True
    while running:
        clock.tick(60)
        WIN.fill(BLACK)

        draw_text("Use WASD keys to scale", 10, 10)
        draw_text(f"Sx: {sx:.2f}  Sy: {sy:.2f}", 10, 40)

        origin = (WIDTH // 2, HEIGHT // 2)
        scaled_x, scaled_y = scale_point(*point, sx, sy)

        # Convert to screen coordinates
        screen_x = origin[0] + int(scaled_x)
        screen_y = origin[1] - int(scaled_y)

        pygame.draw.circle(WIN, RED, (screen_x, screen_y), 7)
        pygame.draw.circle(WIN, WHITE, origin, 4)
        pygame.draw.line(WIN, RED, origin, (screen_x, screen_y), 2)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: sy += 0.01
        if keys[pygame.K_s]: sy -= 0.01
        if keys[pygame.K_d]: sx += 0.01
        if keys[pygame.K_a]: sx -= 0.01

    pygame.quit()

if __name__ == "__main__":
    main()
