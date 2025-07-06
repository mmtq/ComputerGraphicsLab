import pygame

# Region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
    code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        return (round(x1), round(y1), round(x2), round(y2))
    else:
        return None

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

        # Cohen–Sutherland Clipped
        cs_clip = cohen_sutherland_clip(*line_start, *line_end, xmin, xmax, ymin, ymax)
        if cs_clip:
            pygame.draw.line(screen, (0, 255, 0), (cs_clip[0], cs_clip[1]), (cs_clip[2], cs_clip[3]), 3)

        # # Liang–Barsky Clipped
        # lb_clip = liang_barsky_clip(*line_start, *line_end, xmin, xmax, ymin, ymax)
        # if lb_clip:
        #     pygame.draw.line(screen, (255, 0, 0), (lb_clip[0], lb_clip[1]), (lb_clip[2], lb_clip[3]), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
