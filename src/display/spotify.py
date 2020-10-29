from PIL import Image
from src.util.fonts import ds32, ds16, find_string_width

eink_width = 400


def format_text(width, text):
    if (find_string_width(text, 1) <= width):
        return [text]
    split_text = text.split()
    return_list = ['', '']
    split_index = 0
    for word in split_text:
        if (find_string_width(return_list[0] + word + ' ', 1) <= width):
            return_list[0] += (word + ' ')
            split_index += 1
    return_list[0] = return_list[0][0:-1]
    for word in split_text[split_index:]:
        if (len(split_text) == split_index + 1):
            if (find_string_width(return_list[1] + word, 1) <= width):
                return_list[1] += word + ' '
                split_index += 1
        elif (find_string_width(return_list[1] + word + '...', 1) <= width):
            return_list[1] += word + ' '
            split_index += 1
        else:
            break
    return_list[1] = return_list[1][0:-1]
    if len(split_text) > split_index:
        return_list[1] += '...'
    return return_list


def add_spotify_graphics(image, draw, xoffset, yoffset, spotify_info):
    formatted_track = format_text(eink_width - xoffset - 8,
                                  spotify_info['track'])
    add_track_name(draw, xoffset, yoffset, formatted_track)
    yaddition = 36
    if len(formatted_track) > 1:
        yaddition = 72
    add_artist_name(draw, xoffset, yoffset + yaddition, spotify_info['artist'])


def add_track_name(draw, xoffset, yoffset, formatted_track):
    for line in formatted_track:
        draw.text((xoffset, yoffset), line, font=ds32)


def add_artist_name(draw, xoffset, yoffset, artist):
    draw.text((xoffset, yoffset), artist, font=ds32)
