from datetime import datetime
import json
import sys
from PIL import Image, ImageDraw
from waveshare_epd import epd4in2

from src.requests.bitcoin import get_bitcoin_price
# from src.requests.weather import get_weather
from src.requests.spotify import get_spotify
# from src.display.weather import draw_weather_icon
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
    bitcoin_price = get_bitcoin_price()
    # print(json.dumps(get_weather(config['weather'])))
    spotify = get_spotify(config['spotify'])
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    image = Image.new('1', (epd.width, epd.height), 128)
    draw = ImageDraw.Draw(image)
    add_bitcoin_graphics(image, draw, 8, 6, bitcoin_price)
    draw_box(draw, 0, 400, 60, 63)
    time = datetime.today().strftime('%H:%M')
    date = datetime.today().strftime('%b %d')
    add_time_graphics(draw, 8, 63, time, date)
    draw_box(draw, 0, 400, 183, 186)
    draw_box(draw, 140, 143, 63, 186)
    add_spotify_graphics(draw, image, 151, 69, spotify)
    image_buffer = epd.getbuffer(image)
    epd.display(image_buffer)
