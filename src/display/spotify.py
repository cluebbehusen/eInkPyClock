from PIL import Image
from src.util.fonts import ds32, ds16, find_string_width


def add_spotify_graphics(image, draw, xoffset, yoffset, spotify_info):
    print(spotify_info)
    add_track_name(xoffset, yoffset, spotify_info('track'))


def add_track_name(draw, xoffset, yoffset, track_name):
    draw.text((xoffset, yoffset), track_name, font=ds32)
