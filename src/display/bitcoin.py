import locale
from PIL import Image
from src.util.fonts import fk64

bitcoin_icon = Image.open('icons/Bitcoin.png')
icon_width = 48
icon_height = 48


def add_bitcoin_graphics(image, draw, xoffset, yoffset, bitcoin_price):
    add_bitcoin_icon(image, xoffset, yoffset)
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    btc = '$' + locale.format('%.2f', bitcoin_price, grouping=True)
    draw.text((xoffset + icon_width + 20, 0), btc, font=fk64)


def add_bitcoin_icon(image, xoffset, yoffset):
    image.paste(bitcoin_icon, (xoffset, yoffset))
