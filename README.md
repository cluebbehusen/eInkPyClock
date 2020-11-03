# eInkPyClock
Python program for an E-Ink display to show the time and other information when connected to a Raspberry Pi.


This program is written for [Waveshare's 4.2 inch e-ink display](https://www.waveshare.com/product/4.2inch-e-paper-module.htm). The program was written for and tested on a Raspberry Pi Zero W. The program displays the current current price of Bitcoin in USD; the local time, date, and day of the week; the current or most recent song, artist, and context (playlist, artist, album) from Spotify; and the current weather information along with the forecast for the next two days.

## Running the Program

### Requirements

This program requires Python3. Requirements used directly by this program can be found in `requirements.txt`. They can be installed with pip or used in a virtual environment. Along with these requirements, all installation instructions found on [Waveshare's website](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module) must be followed before running, and the display must be properly wired to the Raspberry Pi's GPIO pins.

### API Configuration

In order to access the Spotify API, you must first access the Spotify Developer Porta, create an app, and add [http://www.google.com/](http://www.google.com/) as the Redirect URI for the app. For the OpenWeatherMap API, you must create a free account in order to generate an API key. Then a file named `config.json` with the following format must be added to the root directory of the project.

```json
{
  "spotify": {
    "client_id": "<INSERT CLIENT ID>",
    "client_secret": "<INSERT CLIENT SECRET>"
  },
  "weather": {
    "api_key": "<INSERT API KEY>",
    "latitude": "<INSERT LATITUDE>",
    "longitude": "<INSERT LONGITUDE>"
  }
}
```

The first time the program is run, it will ask you to paste a link into a web browser to link the Spotify account to the project. After pasting the link, copy the full Google redirect URL and paste it back into the terminal.

### Running

Run the program with
```bash
python3 eInkPyClock.py
```