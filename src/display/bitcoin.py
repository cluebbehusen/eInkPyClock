from PIL import Image
from src.util.fonts import ds64, find_string_width

bitcoin_icon = Image.open('icons/Bitcoin.png')
eink_width = 400


def add_bitcoin_graphics(image, draw, xoffset, yoffset, bitcoin_price):
    one = '1'
    draw.text((xoffset, yoffset / 2), one, font=ds64)
    add_bitcoin_icon(image, xoffset * 2 + find_string_width(one, 2), yoffset)
    bitcoin_string = '=   $' + '{0:,.2f}'.format(bitcoin_price)
    price_xoffset = (eink_width - find_string_width(bitcoin_string, 2) -
                     xoffset)
    draw.text((price_xoffset, yoffset / 2), bitcoin_string, font=ds64)


def add_bitcoin_icon(image, xoffset, yoffset):
    image.paste(bitcoin_icon, (xoffset, yoffset))
