from PIL import Image
from src.util.fonts import ds64, ds32, ds16, find_string_width

cloudy_icon = Image.open('icons/Cloudy.png')
mist_icon = Image.open('icons/Mist.png')
partly_cloudy_icon = Image.open('icons/Partly_Cloudy.png')
rain_icon = Image.open('icons/Rain.png')
snow_icon = Image.open('icons/Snow.png')
sun_icon = Image.open('icons/Sun.png')
thunderstorm_icon = Image.open('icons/Thunderstorm.png')
eink_width = 400


def add_weather_graphics(image, draw, xoffset, yoffset, weather_info):
    f_32_width = find_string_width('F', 1)
    f_16_width = find_string_width('F', 0)
    current_temp = str(weather_info['c']['temp'])
    current_temp_width = find_string_width(current_temp, 2)
    current_id = weather_info['c']['id']
    current_high = str(weather_info['f'][0]['temp']['max'])
    current_high_width = find_string_width(current_high, 1)
    current_low = str(weather_info['f'][0]['temp']['min'])
    current_low_width = find_string_width(current_low, 1)
    draw.text((xoffset, yoffset + 5), current_temp, font=ds64)
    xincrement = xoffset + current_temp_width + 2
    draw.text((xincrement, yoffset + 10), 'F', font=ds32)
    xincrement += f_32_width + 6
    draw.text((xincrement, yoffset), current_high, font=ds32)
    draw.text((xincrement, yoffset + 34), current_low, font=ds32)
    draw.text((xincrement + current_high_width + 2, yoffset + 3),
              'F', font=ds16)
    draw.text((xincrement + current_low_width + 2, yoffset + 37),
              'F', font=ds16)
    xincrement += current_high_width + f_16_width + 6
    draw_weather_icon(image, xincrement, yoffset + 6, current_id)
    xincrement += 50
    remaining_space = eink_width - xincrement
    future = weather_info['f']
    for i in range(1, 3):
        future_high = str(future[i]['temp']['max'])
        future_low = str(future[i]['temp']['min'])
        future_high_width = find_string_width(future_high, 1)
        future_low_width = find_string_width(future_low, 1)
        future_id = future[i]['id']
        draw.text((xoffset, yoffset), future_high, font=ds32)
        draw.text((xoffset, yoffset + 34), future_low, font=ds32)
        draw.text((xoffset + future_high_width + 2, yoffset + 3),
                  'F', font=ds16)
        draw.text((xoffset + future_low_width + 2, yoffset + 37),
                  'F', font=ds16)
        xoffset += future_high_width + f_16_width + 6
        draw_weather_icon(image, xoffset, yoffset + 6, future_id)
        xincrement += remaining_space / 2


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
