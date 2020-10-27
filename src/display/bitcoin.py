from PIL import Image
from src.util.fonts import fk64

bitcoin_icon = Image.open('icons/Bitcoin.png')
icon_width = 48
icon_height = 48


def add_bitcoin_graphics(image, draw, xoffset, yoffset, bitcoin_price):
    add_bitcoin_icon(image, xoffset, yoffset)
    btc = '$' + '{0:,.2f}'.format(bitcoin_price)
    draw.text((xoffset + icon_width + 140, 0), btc, font=fk64)


def add_bitcoin_icon(image, xoffset, yoffset):
    image.paste(bitcoin_icon, (xoffset, yoffset))
