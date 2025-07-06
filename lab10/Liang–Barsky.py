import pygame
def liang_barsky_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            u = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, u)
            else:
                u2 = min(u2, u)

    if u1 > u2:
        return None

    x1_clip = x1 + u1 * dx
    y1_clip = y1 + u1 * dy
    x2_clip = x1 + u2 * dx
    y2_clip = y1 + u2 * dy
    return (round(x1_clip), round(y1_clip), round(x2_clip), round(y2_clip))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Line Clipping Algorithms")

    clock = pygame.time.Clock()

    xmin, ymin = 200, 150
    xmax, ymax = 600, 450
    line_start = (100, 100)
    line_end = (700, 500)

    running = True
    while running:
        screen.fill((30, 30, 30))

        # Clipping rectangle
        pygame.draw.rect(screen, (255, 255, 255), (xmin, ymin, xmax - xmin, ymax - ymin), 2)

        # Original line
        pygame.draw.line(screen, (100, 100, 255), line_start, line_end, 1)

        # # Cohen–Sutherland Clipped
        # cs_clip = cohen_sutherland_clip(*line_start, *line_end, xmin, xmax, ymin, ymax)
        # if cs_clip:
        #     pygame.draw.line(screen, (0, 255, 0), (cs_clip[0], cs_clip[1]), (cs_clip[2], cs_clip[3]), 3)

        # Liang–Barsky Clipped
        lb_clip = liang_barsky_clip(*line_start, *line_end, xmin, xmax, ymin, ymax)
        if lb_clip:
            pygame.draw.line(screen, (255, 0, 0), (lb_clip[0], lb_clip[1]), (lb_clip[2], lb_clip[3]), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
