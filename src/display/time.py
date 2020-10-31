from src.util.fonts import ds64


def add_time_graphics(draw, xoffset, yoffset, time, date, day):
    draw.text((xoffset, yoffset), time, font=ds64)
    draw.text((xoffset, yoffset + 51), day, font=ds64)
    draw.text((xoffset, yoffset + 102), date, font=ds64)
