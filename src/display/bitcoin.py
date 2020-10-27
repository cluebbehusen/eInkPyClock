from PIL import Image
from src.util.fonts import fk64, find_string_width

bitcoin_icon = Image.open('icons/Bitcoin.png')
eink_width = 400


def add_bitcoin_graphics(image, draw, xoffset, yoffset, bitcoin_price):
    add_bitcoin_icon(image, xoffset, yoffset)
    btc = '$' + '{0:,.2f}'.format(bitcoin_price)
    btc_xoffset = find_string_width(btc, 2)
    draw.text((eink_width - btc_xoffset - xoffset, 0), btc, font=fk64)


def add_bitcoin_icon(image, xoffset, yoffset):
    image.paste(bitcoin_icon, (xoffset, yoffset))
