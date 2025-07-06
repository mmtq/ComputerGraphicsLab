import pygame

def inside(p, edge, clip_rect):
    x, y = p
    xmin, ymin, xmax, ymax = clip_rect
    if edge == "LEFT":
        return x >= xmin
    elif edge == "RIGHT":
        return x <= xmax
    elif edge == "BOTTOM":
        return y >= ymin
    elif edge == "TOP":
        return y <= ymax

def intersection(p1, p2, edge, clip_rect):
    x1, y1 = p1
    x2, y2 = p2
    xmin, ymin, xmax, ymax = clip_rect
    if x1 == x2:
        m = float('inf')
    else:
        m = (y2 - y1) / (x2 - x1)

    if edge == "LEFT":
        x = xmin
        y = y1 + m * (xmin - x1)
    elif edge == "RIGHT":
        x = xmax
        y = y1 + m * (xmax - x1)
    elif edge == "BOTTOM":
        y = ymin
        if m == float('inf'):
            x = x1
        else:
            x = x1 + (ymin - y1) / m
    elif edge == "TOP":
        y = ymax
        if m == float('inf'):
            x = x1
        else:
            x = x1 + (ymax - y1) / m
    return (round(x), round(y))

def clip_polygon(subject_polygon, clip_rect):
    edges = ["LEFT", "RIGHT", "BOTTOM", "TOP"]
    output = subject_polygon
    for edge in edges:
        input_list = output
        output = []
        if not input_list:
            break
        s = input_list[-1]
        for e in input_list:
            if inside(e, edge, clip_rect):
                if not inside(s, edge, clip_rect):
                    output.append(intersection(s, e, edge, clip_rect))
                output.append(e)
            elif inside(s, edge, clip_rect):
                output.append(intersection(s, e, edge, clip_rect))
            s = e
    return output

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sutherland–Hodgman Polygon Clipping")
    clock = pygame.time.Clock()

    # Define the clipping rectangle
    clip_rect = (200, 150, 600, 450)
    xmin, ymin, xmax, ymax = clip_rect

    # Define a subject polygon (clockwise or counter-clockwise)
    polygon = [(100, 100), (700, 100), (700, 500), (400, 300), (100, 500)]

    running = True
    while running:
        screen.fill((30, 30, 30))

        # Draw clipping window
        pygame.draw.rect(screen, (255, 255, 255), (xmin, ymin, xmax - xmin, ymax - ymin), 2)

        # Draw original polygon
        pygame.draw.polygon(screen, (100, 100, 255), polygon, 2)

        # Clip polygon
        clipped = clip_polygon(polygon, clip_rect)
        if clipped:
            pygame.draw.polygon(screen, (0, 255, 0), clipped, 0)  # filled

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
