from PIL import Image
from src.util.fonts import ds32, ds16, find_string_width


def add_spotify_graphics(image, draw, xoffset, yoffset, spotify_info):
    add_track_name(draw, xoffset, yoffset, spotify_info['track'])
    add_artist_name(draw, xoffset, yoffset + 40, spotify_info['artist'])


def add_track_name(draw, xoffset, yoffset, track_name):
    draw.text((xoffset, yoffset), track_name, font=ds32)


def add_artist_name(draw, xoffset, yoffset, artist):
    draw.text((xoffset, yoffset), artist, font=ds32)