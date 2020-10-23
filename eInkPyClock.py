from src.requests.bitcoin import get_bitcoin_price
from src.requests.weather import get_weather

import json

if __name__ == '__main__':
    print(get_bitcoin_price())
    print(json.dumps(get_weather()))
