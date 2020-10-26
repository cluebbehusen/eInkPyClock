from PIL import Image
from waveshare_epd import epd4in2


bitcoin_icon = Image.open('icons/Bitcoin.png')
album_icon = Image.open('icons/Album.png')
artist_icon = Image.open('icons/Artist.png')
playlist_icon = Image.open('icons/Playlist.png')
cloudy_icon = Image.open('icons/Cloudy.png')
mist_icon = Image.open('icons/Mist.png')
partly_cloudy_icon = Image.open('icons/Partly_Cloudy.png')
rain_icon = Image.open('icons/Rain.png')
snow_icon = Image.open('icons/Snow.png')
sun_icon = Image.open('icons/Sun.png')
thunderstorm_icon = Image('icons/Thunderstorm.png')


def draw_weather_icon():
    epd = epd4in2.EPD()
    bitcoin_image = Image.new('1', (epd.width, epd.height), 128)
    bitcoin_image.paste(bitcoin_icon, (25, 25))
    album_image = Image.new('1', (epd.width, epd.height), 128)
    album_image.paste(album_icon, (25, 75))
    artist_image = Image.new('1', (epd.width, epd.height), 128)
    artist_image.paste(artist_icon, (25, 125))
    playlist_image = Image.new('1', (epd.width, epd.height), 128)
    playlist_image.paste(playlist_icon, (25, 175))
    image_buffer = epd.getbuffer(album_image)
    epd.display(image_buffer)
    image_buffer = epd.getbuffer(artist_image)
    epd.display(image_buffer)
    image_buffer = epd.getbuffer(playlist_image)
    epd.display(image_buffer)
