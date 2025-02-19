from PIL import Image
from src.util.fonts import ds32, find_string_width
from src.util.util import eink_width

playlist_icon = Image.open('icons/Playlist.png')
artist_icon = Image.open('icons/Artist.png')
album_icon = Image.open('icons/Album.png')


def format_text(width, text):
    text = text.split('(')[0]
    text = text.split(',')[0]
    if (find_string_width(text, 1) <= width):
        return text
    shortened_text = ''
    for char in text:
        if (find_string_width(shortened_text + char, 1) <= width):
            shortened_text += char
    shortened_text = shortened_text[0:-3] + '...'
    return shortened_text


def add_spotify_graphics(image, draw, xoffset, yoffset, spotify_info):
    if not spotify_info:
        return
    formatted_track = format_text(eink_width - xoffset - 8,
                                  spotify_info['track'])
    formatted_artist = format_text(eink_width - xoffset - 8,
                                   spotify_info['artist'])
    image_offset = xoffset
    type = spotify_info['type']
    if type:
        image_offset += 32
        icon = album_icon
        if type == 'playlist':
            icon = playlist_icon
        if type == 'artist':
            icon = artist_icon
        image.paste(icon, (xoffset, yoffset))
    formatted_name = format_text(eink_width - image_offset - 8,
                                 spotify_info['name'])
    draw.text((image_offset, yoffset), formatted_name, font=ds32)
    draw.text((xoffset, yoffset + 36), formatted_track, font=ds32)
    draw.text((xoffset, yoffset + 72), formatted_artist, font=ds32)
    draw.text((xoffset, yoffset + 108), spotify_info['time_passed'], font=ds32)
