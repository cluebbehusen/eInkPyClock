from datetime import datetime, timedelta
import json
from PIL import Image, ImageDraw
import sys
import time
from waveshare_epd import epd4in2

from src.requests.bitcoin import get_bitcoin_price
from src.requests.weather import get_weather
from src.requests.spotify import get_spotify
from src.display.weather import add_weather_graphics
from src.display.bitcoin import add_bitcoin_graphics
from src.display.general import draw_box
from src.display.time import add_time_graphics
from src.display.spotify import add_spotify_graphics
from src.util.util import general_log


def draw_borders():
    draw_box(draw, 0, 400, 223, 226)
    draw_box(draw, 145, 148, 63, 226)
    draw_box(draw, 0, 400, 60, 63)


if __name__ == '__main__':
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print('Failed to open config file')
        sys.exit(1)
    if 'spotify' not in config:
        print('Spotify details missing from config file')
        sys.exit(1)
    if 'weather' not in config:
        print('Weather details missing from config file')
        sys.exit(1)
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    while True:
        hour = int(datetime.today().strftime("%H"))
        if (int(hour) >= 4):
            sec = int(datetime.today().strftime("%S"))
            while (sec < 50 or sec > 55):
                time.sleep(1)
                sec = int(datetime.today().strftime("%S"))
            future_time = datetime.today() + timedelta(minutes=1)
            bitcoin_price = 0
            weather = None
            spotify = None
            try:
                bitcoin_price = get_bitcoin_price()
            except Exception as e:
                general_log(' Failed to get bitcoin price: ' + str(e))
            try:
                weather = get_weather(config['weather'])
            except Exception as e:
                general_log(' Failed to get weather: ' + str(e))
            try:
                spotify = get_spotify(config['spotify'])
            except Exception as e:
                general_log(' Failed to get spotify: ' + str(e))
            image = Image.new('1', (epd.width, epd.height), 128)
            draw = ImageDraw.Draw(image)
            try:
                draw_borders()
                date_string = future_time.strftime('%b %d')
                day_string = future_time.strftime('%a')
                time_string = future_time.strftime('%H:%M')
                add_time_graphics(draw, 8, 66, time_string, date_string,
                                  day_string)
                add_bitcoin_graphics(image, draw, 8, 6, bitcoin_price)
                add_spotify_graphics(image, draw, 156, 75, spotify)
                add_weather_graphics(image, draw, 8, 232, weather)
                image_buffer = epd.getbuffer(image)
                epd.display(image_buffer)
            except Exception as e:
                general_log(' Failed when drawing graphics: ' + str(e))
            time.sleep(120)
        else:
            epd.Clear()
            time.sleep(1860)
