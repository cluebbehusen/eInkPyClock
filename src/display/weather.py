from PIL import Image
from waveshare_epd import epd4in2


weather_icon = Image.open('icons/Bitcoin.png')


def draw_weather_icon():
    epd = epd4in2.EPD()
    image = Image.new('1', (epd.width, epd.height), 128)
    image.paste(weather_icon, (100, 100))
    image_buffer = epd.getbuffer(image)
    epd.display(image_buffer)
