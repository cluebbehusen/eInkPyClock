import datetime
import requests as req

from src.util.util import request_log


def get_weather(config):
    api_key = config['api_key']
    lat = float(config['latitude'])
    long = float(config['longitude'])
    response = req.get('https://api.openweathermap.org/data/2.5/onecall?lat=' +
                       str(lat) + '&lon=' + str(long) + '&appid=' + api_key +
                       '&exclude=minutely,hourly,alerts&units=imperial')
    if response.status_code > 400 and response.status_code < 499:
        request_log(str(datetime.datetime.now()) +
                    ' Open weather get request failed with status code: ' +
                    str(response.status_code))
        return None
    data = response.json()
    return_data = {}
    return_data['c'] = {'temp': float(data['current'].get('temp', 0)),
                        'id': int(data['current']['weather'][0].get('id', 0))}
    return_data['f'] = []
    for i in range(6):
        obj = data['daily'][i]
        return_data['f'].append({
            'temp': {'min': float(obj['temp'].get('min', 0)),
                     'max': float(obj['temp'].get('max', 0))},
            'id': int(obj['weather'][0].get('id', 0))
        })
    return return_data
