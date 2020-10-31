from datetime import datetime
import json
from PIL import Image, ImageDraw
import sys
from time import time, sleep
from waveshare_epd import epd4in2

from src.requests.bitcoin import get_bitcoin_price
from src.requests.weather import get_weather
from src.requests.spotify import get_spotify
from src.display.weather import add_weather_graphics
from src.display.bitcoin import add_bitcoin_graphics
from src.display.general import draw_box
from src.display.time import add_time_graphics
from src.display.spotify import add_spotify_graphics


if __name__ == '__main__':
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print('Failed to open config file')
        sys.exit(1)
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    time_elapsed = 15.0
    while True:
        hour = int(datetime.today().strftime("%H"))
        if (int(hour) >= 4):
            start = time()
            sec_left = 60 - int(datetime.today().strftime("%S"))
            bitcoin_price = get_bitcoin_price()
            weather = get_weather(config['weather'])
            spotify = get_spotify(config['spotify'])
            image = Image.new('1', (epd.width, epd.height), 128)
            draw = ImageDraw.Draw(image)
            add_bitcoin_graphics(image, draw, 8, 6, bitcoin_price)
            draw_box(draw, 0, 400, 60, 63)
            date = datetime.today().strftime('%b %d')
            day = datetime.today().strftime('%a')
            time = datetime.today().strftime('%H:%M')
            add_time_graphics(draw, 8, 66, time, date, day)
            draw_box(draw, 0, 400, 223, 226)
            draw_box(draw, 140, 143, 63, 226)
            add_spotify_graphics(image, draw, 151, 75, spotify)
            add_weather_graphics(image, draw, 8, 232, weather)
            time_elapsed = time() - start
            remaining_time = sec_left - time_elapsed
            image_buffer = epd.getbuffer(image)
            epd.display(image_buffer)
            sleep(remaining_time + 120)
        else:
            epd.Clear()
            sleep(1860)
