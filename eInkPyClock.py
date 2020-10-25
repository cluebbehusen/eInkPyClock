import json
import sys

from src.requests.bitcoin import get_bitcoin_price
from src.requests.weather import get_weather
from src.requests.spotify import get_spotify


if __name__ == '__main__':
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print('Failed to open config file')
        sys.exit(1)
    print(get_bitcoin_price())
    print(json.dumps(get_weather(config['weather'])))
    print(get_spotify(config['spotify']))
