from PIL import Image
from src.util.fonts import ds64, ds32, find_string_width

cloudy_icon = Image.open('icons/Cloudy.png')
mist_icon = Image.open('icons/Mist.png')
partly_cloudy_icon = Image.open('icons/Partly_Cloudy.png')
rain_icon = Image.open('icons/Rain.png')
snow_icon = Image.open('icons/Snow.png')
sun_icon = Image.open('icons/Sun.png')
thunderstorm_icon = Image.open('icons/Thunderstorm.png')


def add_weather_graphics(image, draw, xoffset, yoffset, weather_info):
    current_temp = str(weather_info['c']['temp'])
    current_temp_width = find_string_width(current_temp, 2)
    current_id = str(weather_info['c']['id'])
    current_high = str(weather_info['f'][0]['temp']['max'])
    current_high_width = find_string_width(current_high, 1)
    current_low = str(weather_info['f'][0]['temp']['min'])
    draw.text((xoffset, yoffset + 4), current_temp, font=ds64)
    xincrement = xoffset + current_temp_width + 6
    draw.text((xincrement, yoffset), current_high, font=ds32)
    draw.text((xincrement, yoffset + 32), current_low, font=ds32)
    xincrement += current_high_width + 6
    draw_weather_icon(image, xincrement, yoffset + 24, current_id)
    future = weather_info['f'][1:]


def draw_weather_icon(image, xoffset, yoffset, code):
    if code >= 200 and code < 300:
        image.paste(thunderstorm_icon, (xoffset, yoffset))
    elif code >= 300 and code < 600:
        image.paste(rain_icon, (xoffset, yoffset))
    elif code >= 600 and code < 700:
        image.paste(snow_icon, (xoffset, yoffset))
    elif code >= 700 and code < 800:
        image.paste(mist_icon, (xoffset, yoffset))
    elif code == 801 or code == 802:
        image.paste(partly_cloudy_icon, (xoffset, yoffset))
    elif code == 803 or code == 804:
        image.paste(cloudy_icon, (xoffset, yoffset))
    else:
        image.paste(sun_icon, (xoffset, yoffset))
