from PIL import Image
from waveshare_epd import epd4in2


album_icon = Image.open('icons/Album.png')
artist_icon = Image.open('icons/Artist.png')
playlist_icon = Image.open('icons/Playlist.png')
cloudy_icon = Image.open('icons/Cloudy.png')
mist_icon = Image.open('icons/Mist.png')
partly_cloudy_icon = Image.open('icons/Partly_Cloudy.png')
rain_icon = Image.open('icons/Rain.png')
snow_icon = Image.open('icons/Snow.png')
sun_icon = Image.open('icons/Sun.png')
thunderstorm_icon = Image.open('icons/Thunderstorm.png')
music_icon = Image.open('icons/Music.png')


def draw_weather_icon():
    epd = epd4in2.EPD()
    epd.init()
    epd.Clear()
    image = Image.new('1', (epd.width, epd.height), 128)
    image.paste(album_icon, (25, 75))
    image.paste(artist_icon, (25, 125))
    image.paste(playlist_icon, (25, 175))
    image.paste(cloudy_icon, (25, 225))
    image.paste(mist_icon, (75, 25))
    image.paste(partly_cloudy_icon, (75, 75))
    image.paste(rain_icon, (75, 125))
    image.paste(snow_icon, (75, 175))
    image.paste(sun_icon, (75, 225))
    image.paste(thunderstorm_icon, (125, 25))
    image.paste(music_icon, (125, 75))
    image_buffer = epd.getbuffer(image)
    epd.display(image_buffer)
