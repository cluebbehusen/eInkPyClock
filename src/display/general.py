def draw_line(draw, x1, x2, y1, y2):
    for i in range(abs(y2 - y1)):
        draw.line([(x1, y1 + i), (x2, y1 + i)], fill=0)
