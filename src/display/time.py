from src.util.fonts import ds64


def add_time_graphics(draw, xoffset, yoffset, time, date, day):
    draw.text((xoffset, yoffset), time, font=ds64)
    draw.text((xoffset, yoffset + 53), day, font=ds64)
    draw.text((xoffset, yoffset + 106), date, font=ds64)
