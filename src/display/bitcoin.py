from PIL import Image

bitcoin_icon = Image.open('icons/Bitcoin.png')
icon_width = 48
icon_height = 48


def add_bitcoin_graphics(image, xoffset, yoffset):
    add_bitcoin_icon(image, xoffset, yoffset)


def add_bitcoin_icon(image, xoffset, yoffset):
    image.paste(bitcoin_icon, (xoffset, yoffset))
