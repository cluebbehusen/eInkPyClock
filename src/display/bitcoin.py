from PIL import Image
from src.util.fonts import fk64

bitcoin_icon = Image.open('icons/Bitcoin.png')
icon_width = 48
icon_height = 48


def add_bitcoin_graphics(image, draw, xoffset, yoffset, bitcoin_price):
    add_bitcoin_icon(image, xoffset, yoffset)
    draw.text((xoffset + icon_width + 10, yoffset), str(bitcoin_price), font=fk64)


def add_bitcoin_icon(image, xoffset, yoffset):
    image.paste(bitcoin_icon, (xoffset, yoffset))
