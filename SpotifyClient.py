from secrets_spot import CLIENT_ID, CLIENT_SECRET

from random import randint
import requests
import base64

class SpotifyClient:
    """ Contains and controls Spotify elements """

    def __init__(self, name):
        self.name = name
        self.get_access_token()
        # self.get_all_genres()

    def get_access_token(self):
        """ Get authorization token from client credentials """

        url = 'https://accounts.spotify.com/api/token'

        # Encode to base 64
        # Refer to https://dev.to/mxdws/using-python-with-the-spotify-api-1d02
        message = f'{CLIENT_ID}:{CLIENT_SECRET}'
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)
        base64Message = base64Bytes.decode('ascii')

        r = requests.post(
            url,
            headers={'Authorization': f'Basic {base64Message}'},
            data={'grant_type': 'client_credentials'}
        )

        #self.access_token = r.json()['access_token']
        self.access_token='BQBvfWM7OgfXX3p1AVJPK3A4mjhpMsIUvzXxl3xEhJ1jQJe17v33Eqs6PH6pxX7r9XC-GhkZTZV9314a-qhVxZRFtUY-FshrDsoMshUNtA6rFNWNR4quR3gXEJEjiw7oDwwIhZZHJFVFxBuvCuCXz8eWpo-Em1GljTLmBaU2pTelCDARi32EvfWfM8w-A4LbI-UEceBrKdNqJGsyZ2MHJHNSlcpTfzKoAM4fHIChCkSGasUsRiSKyeMFm10eTA'

    def get_all_genres(self):
        """ Get list of available genres """

        url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            }
        )

        self.genres = r.json()['genres']


    def get_all_categories(self):
        """ Get list of available categories """

        url = 'https://api.spotify.com/v1/browse/categories'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'limit': 50,
            }
        )

        self.categories = r.json()
        return [category['id'] for category in self.categories['categories']['items']]
    
    def get_single_category(self, category_id):
        """ Get list of available categories """

        url = f'https://api.spotify.com/v1/browse/categories/{category_id}'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'country': 'US',
            }
        )

    def get_category_playlists(self, category_id):
        """ Get list of available categories """

        url = f'https://api.spotify.com/v1/browse/categories/{category_id}/playlists'
        

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'country': 'US',
                'limit': 50,
            }
        )

        return r.json()
    
    def get_playlist(self, playlist_id):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'country': 'US',
                'limit': 50,
            }
        )

        return r.json()


    def search_item(self, query, type):
        """ Search for item in Spotify
            Type must be:
            album, artist, playlist, track, show or episode.
        """

        url = 'https://api.spotify.com/v1/search'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'q': query,
                'type': type,
            }
        )

        try:
            return r.json()[f'{type}s']['items'][0]#['id']
        except:
            # raise SpotifyException("Bad Search Parameter")
            return None
        
    def get_artist(self, id):
        """ Gets an artist using their Spotify ID """

        url = f'https://api.spotify.com/v1/artists/{id}'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            }
        )

        return r.json()

    def get_multiple_artists(self, ids):
        """ Gets up to 50 artists using their Spotify IDs """

        url = f'https://api.spotify.com/v1/artists'

        formatted_ids = ','.join(ids)

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'ids': formatted_ids
            }
        )

        return r.json()

    def get_recommendations(
        self,
        num: int = 20,
        s_artist: str = None,
        s_track: str = None,
        popular: bool = True,
        random: bool = True,
        t_tempo: int = None,
        t_danceability: float = None,
        t_energy: float = None,
        t_instrumentalness: float = None,
        t_valence: float = None
        ):
        """ Get recommended songs from Spotify """

        self.get_all_genres()
        random_genres = ','.join([self.genres[randint(0,len(self.genres)-1)] for _ in range(2)])

        url = f'https://api.spotify.com/v1/recommendations'

        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            },
            params={
                'market': 'US',
                'seed_artists': self.search_item(s_artist, 'Artist'),
                'seed_genres': random_genres if random else 'pop',
                'seed_tracks': self.search_item(s_track, 'Track'),
                'limit': num,
                'min_popularity': 50 if popular else None,      # value 0 - 100
                'target_tempo': t_tempo,                        # no range given
                'target_danceability': t_danceability,          # value 0.0 - 1.0
                'target_energy': t_energy,                      # value 0.0 - 1.0
                'target_instrumentalness': t_instrumentalness,  # value 0.0 - 1.0
                'target_valence': t_valence                     # value 0.0 - 1.0
            }
        )

        # return [r.json()['tracks'][x]['uri'] for x in range(len(r.json()['tracks']))]
        #return [r.json()['tracks'][x]['preview_url'] for x in range(len(r.json()['tracks']))]
        return r.json()

    def get_current_user(self):
        url = f'https://api.spotify.com/v1/me/'
        
        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}',
            }
        )
        return r.json()['id']



class SpotifyException(Exception):
	pass

a = SpotifyClient("Mag")
#print(a.get_all_categories())
#print(a.get_all_genres())
#print(a.genres)
# r = a.get_category_playlists("mood")['playlists']['items']
#print(r)
# l = [(x['name'], x['id']) for x in r]
#print(l)

#print(a.get_playlist('37i9dQZF1DWYBO1MoTDhZI'))
#print(a.get_recommendations(s_track='6veNr8pvwqdErGuk5xp2Im', num=3))
# print(a.get_current_user())