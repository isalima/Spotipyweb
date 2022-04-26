import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Musica import Musica


def get_dados(artist):

    client_credentials_manager = SpotifyClientCredentials(client_id='1e9ed5dc714d4ddb845be0be6921c767',
                                                          client_secret='429e7f402e654ec28e6a73500db8c47e')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    musics = []
    results = sp.search(q=artist, limit=10, type='track')

    for idx, track in enumerate(results['tracks']['items']):
        music = Musica(track['name'], track['album']['artists'][0]['name'], track['external_urls']['spotify'])
        musics.append(music)
        print(track['name'])

    return musics


