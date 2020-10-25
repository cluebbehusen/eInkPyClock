from datetime import datetime
import spotipy
from src.util.util import request_log, general_log

SPOT_SCOPE = ('user-read-private, user-read-recently-played,' +
              ' user-read-playback-state, user-read-currently-playing')
REDIRECT_URI = 'http://www.google.com/'


def get_spotify():
    try:
        with open('spotify.txt', 'r') as weather_file:
            lines = weather_file.readlines()
            client_id = lines[0].strip()
            client_secret = lines[1].strip()
    except FileNotFoundError:
        general_log(str(datetime.now()) +
                    ' Failed to open spotify metadata file')
        return None
    oauth = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, REDIRECT_URI,
                                        scope=SPOT_SCOPE, requests_timeout=10,
                                        cache_path='.cache')
    token_info = oauth.get_cached_token()
    token = get_token(oauth, token_info)
    return get_info(token)


def get_token(oauth, token_info):
    token = None
    if not token_info:
        auth_url = oauth.get_authorize_url()
        print(auth_url)
        response = input('Paste the above link in a browser and' +
                         ' paste the redirect url here: ')
        code = oauth.parse_response_code(response)
        if code:
            token_info = oauth.get_access_token(code)
    if token_info:
        token = token_info['access_token']
    return token


def get_info(token):
    sp = spotipy.Spotify(auth=token)
    recent = sp.current_user_playing_track()
    track, artist, type, name, time_passed = None, None, None, None, None
    if recent and recent['item']:
        type, name = get_context_from_json(recent['context'], sp)
        track = recent['item'].get('name', None)
        artist = get_artists(recent['item'].get('artists', []))
        time_passed = ' is listening to'
    else:
        recent = sp.current_user_recently_played(1)
        item = recent['items'][0]
        type, name = get_context_from_json(item['context'], sp)
        track = item['track'].get('name', None)
        artist = get_artists(item['track']['artists'])
        time = datetime.strptime(item['played_at'].replace('T', ' ')[:19],
                                 '%Y-%m-%d %H:%M:%S')
        time_delta = datetime.utcnow() - time
        hours_passed, minutes_passed = get_time_values(time_delta.seconds)
        time_passed = get_time_passed(hours_passed, minutes_passed)
    return_dict = {
        'track': track,
        'artist': artist,
        'time_passed': time_passed,
        'type': type,
        'name': name
    }
    for key in return_dict:
        if not return_dict[key]:
            request_log(str(datetime.now()) +
                        'Failed to get ' + key + ' from spotipy')
    return return_dict


def get_context_from_json(context_json, spotipy_obj):
    type, name = None, None
    if context_json:
        type = context_json.get('type', None)
        uri = context_json['uri']
        if type == 'playlist':
            type_json = spotipy_obj.playlist(uri)
        elif type == 'album':
            type_json = spotipy_obj.album(uri)
        elif type == 'artist':
            type_json = spotipy_obj.artist(uri)
        if type_json:
            name = type_json['name']
    return type, name


def get_artists(artist_array):
    artist_name = ''
    for i in range(len(artist_array)):
        artist_name += artist_array[i]['name'] + ', '
    if artist_array:
        artist_name = artist_name[:-2]
    return artist_name


def get_time_values(seconds_passed):
    hours = seconds_passed // 3600
    seconds_passed = seconds_passed % 3600
    minutes = seconds_passed // 60
    return hours, minutes


def get_time_passed(hours, minutes):
    if hours == 0 and minutes <= 4:
        return ' is listening to'
    elif hours == 0:
        return str(minutes - (minutes % 5)) + ' minutes ago'
    elif hours == 1:
        return ' 1 hour ago'
    elif hours < 24:
        return str(hours) + ' hours ago'
    elif hours < 48:
        return ' one day ago'
    else:
        return str(hours // 24) + ' days ago'
