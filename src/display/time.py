from src.util.fonts import ds64


def add_time_graphics(draw, xoffset, yoffset, time, date):
    draw.text((xoffset, yoffset), time, font=ds64)
    draw.text((xoffset, yoffset + 56), date, font=ds64)
