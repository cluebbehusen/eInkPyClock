import requests as req

from src.util.util import request_log


def get_bitcoin_price():
    response = req.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if response.status_code > 400 and response.status_code < 499:
        request_log(' Bitcoin price get request failed with status code: ' +
                    str(response.status_code))
        return 0
    data = response.json()
    return float(data['bpi']['USD'].get('rate_float', 0))
