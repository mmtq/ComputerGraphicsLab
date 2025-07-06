import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scale Triangle About Another Point with Axes")

WHITE, BLACK, BLUE, RED, GRAY = (255, 255, 255), (0, 0, 0), (0, 128, 255), (255, 0, 0), (150, 150, 150)
FONT = pygame.font.SysFont(None, 24)

def draw_text(text, x, y):
    WIN.blit(FONT.render(text, True, WHITE), (x, y))

def draw_axes():
    pygame.draw.line(WIN, GRAY, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 1)
    pygame.draw.line(WIN, GRAY, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)
    f = pygame.font.SysFont(None, 20)
    WIN.blit(f.render("I", True, WHITE), (WIDTH // 2 + 5, HEIGHT // 2 - 20))
    WIN.blit(f.render("II", True, WHITE), (WIDTH // 2 - 25, HEIGHT // 2 - 20))
    WIN.blit(f.render("III", True, WHITE), (WIDTH // 2 - 30, HEIGHT // 2 + 5))
    WIN.blit(f.render("IV", True, WHITE), (WIDTH // 2 + 5, HEIGHT // 2 + 5))

def scale_about_point(x, y, cx, cy, sx, sy):
    dx, dy = x - cx, y - cy
    dx *= sx
    dy *= sy
    return cx + dx, cy + dy

def main():
    clock = pygame.time.Clock()
    triangle = [(200, 100), (250, 180), (150, 180)]
    center = (300, 200)
    sx, sy = 1.0, 1.0

    running = True
    while running:
        clock.tick(60)
        WIN.fill(BLACK)

        draw_axes()
        draw_text("Use WASD keys to scale", 10, 10)
        draw_text(f"Sx: {sx:.2f}  Sy: {sy:.2f}", 10, 40)

        scaled = [scale_about_point(x, y, *center, sx, sy) for x, y in triangle]

        pygame.draw.circle(WIN, RED, center, 6)
        pygame.draw.polygon(WIN, BLUE, [(int(x), int(y)) for x, y in scaled], 3)

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
