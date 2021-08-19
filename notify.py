import sys

import requests
import json
import os
import time

TWITCH_NAME = ''
CHECK_TIME = 300

# get API authorization info
with open('data.json') as f:
    data = json.load(f)

response = requests.post('https://id.twitch.tv/oauth2/token', data = data)
r = response.json()
at = r['access_token']


def get_streamer_game():
    r = requests.get('https://api.twitch.tv/helix/streams',
                     headers = {'authorization': 'Bearer {}'.format(at),
                                'Client-ID': data['client_id']},
                     params = {'user_login': TWITCH_NAME}
                     )
    r = r.json()
    try:
        return r['data'][0]['game_name']
    except IndexError:
        os.system('notify-send "Notifica cambio gioco terminato" "{} non è online"'.format(TWITCH_NAME))
        sys.exit()


current_game = get_streamer_game()

os.system('notify-send "Notifica cambio gioco avviato" "{} sta giocando a {}\nwww.twitch.tv/{}"'.format(TWITCH_NAME,
                                                                                                        current_game,
                                                                                                        TWITCH_NAME))

while True:
    time.sleep(CHECK_TIME)
    game = get_streamer_game()
    if game != current_game:
        current_game = game
        os.system(
            'notify-send "Il gioco è cambiato alle `date "+%T"`" "{} sta ora giocando a {}\nwww.twitch.tv/{}"'.format(
                TWITCH_NAME, game, TWITCH_NAME))
