import json
import sys
from PIL import Image
from waveshare_epd import epd4in2

# from src.requests.bitcoin import get_bitcoin_price
# from src.requests.weather import get_weather
# from src.requests.spotify import get_spotify
# from src.display.weather import draw_weather_icon
from src.display.bitcoin import add_bitcoin_graphics


if __name__ == '__main__':
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print('Failed to open config file')
        sys.exit(1)
    # print(get_bitcoin_price())
    # print(json.dumps(get_weather(config['weather'])))
    # print(get_spotify(config['spotify']))
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    image = Image.new('1', (epd.width, epd.height), 128)
    add_bitcoin_graphics(image, 2, 2)
