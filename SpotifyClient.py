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

        self.access_token = r.json()['access_token']
        # self.access_token='BQBvfWM7OgfXX3p1AVJPK3A4mjhpMsIUvzXxl3xEhJ1jQJe17v33Eqs6PH6pxX7r9XC-GhkZTZV9314a-qhVxZRFtUY-FshrDsoMshUNtA6rFNWNR4quR3gXEJEjiw7oDwwIhZZHJFVFxBuvCuCXz8eWpo-Em1GljTLmBaU2pTelCDARi32EvfWfM8w-A4LbI-UEceBrKdNqJGsyZ2MHJHNSlcpTfzKoAM4fHIChCkSGasUsRiSKyeMFm10eTA'

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

    def get_current_user(self, access_token=None):
        url = f'https://api.spotify.com/v1/me/'

        if access_token is None:
            access_token = self.access_token
        
        r = requests.get(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }
        )
        #print(r.json()['uri'])
        return r.json()['id']
    

    def new_playlist(
        self, 
        user_id, 
        name: str = "", 
        public: bool = False, 
        collab: bool = False, 
        descrip: str = ""):
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
        r = requests.post(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            },
            json={
                'name': name if name else 'New Playlist',
                'public': public,
                'collaborative': collab,
                'description': descrip,
                'Authorization': f'Bearer {self.access_token}',
            }
        )
        return r.json()


    def add_to_playlist(self, playlist_id, song_uris):
        '''song_uris = list of uris which are strings'''
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

        r = requests.post(
            url,
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            },
            json={
                'position': 0,
                'uris': song_uris
            }
        )
        return r.json()




class SpotifyException(Exception):
	pass

# a = SpotifyClient("Mag")
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
#s_id = a.get_current_user()
##print(s_id)
#p_id = a.new_playlist(s_id, name="New Playlist2")
#print(p_id)
##print(a.add_to_playlist(p_id, 'spotify:track:60iSKGrGazRzICtMjADNSM,spotify:track:5nzZGxQGfIc117nKyCQV8G,spotify:track:3Lp8Xd2K7TwlY32SPvXkvF,spotify:track:4Zy0XJh7mh562WmuiP0vw1,spotify:track:3AJwUDP919kvQ9QcozQPxg,spotify:track:4PnNzWe1LJoAMD5j5RHpI0,spotify:track:2ZltjIqztEpZtafc8w0I9t,spotify:track:5YUyW9opqNsMSEzzecZih1,spotify:track:3Vo4wInECJQuz9BIBMOu8i,spotify:track:4XNrMwGx1SqP01sqkGTDmo,spotify:track:1g1TeDflB6atAy7HKwrzXu,spotify:track:5DZwnLxHjWTZaz9jOpRhxb,spotify:track:1ULa3GfdMKs0MfRpm6xVlu,spotify:track:72jbDTw1piOOj770jWNeaG,spotify:track:1NDxZ7cFAo481dtYWdrUnR,spotify:track:2dLLR6qlu5UJ5gk0dKz0h3,spotify:track:60APt5N2NRaKWf5xzJdzyC,spotify:track:4Q4jmPHwu0wrJvqrld0FQ6,spotify:track:7Fa5UNizycSms5jP3SQD3F,spotify:track:1vVNlXi8gf8tZ7OhnEs4VE,spotify:track:7pNC5ZIKtwUK0ReSpM3P9f,spotify:track:37jTPJgwCCmIGMPB45jrPV,spotify:track:4tERsdVCLtLtrGdFBf9DGC,spotify:track:7s0lDK7y3XLmI7tcsRAbW0,spotify:track:2xbI8Vmyv3TkpTdywpPyNw'))
#print(a.add_to_playlist(p_id, ['spotify:track:0L3XCv9i9IHs8cJEVhsJ3J', 'spotify:track:0sBJA2OCEECMs0HsdIQhvR', 'spotify:track:5O7TgofxqSQh31TiRcKXzo', 'spotify:track:38XLUjlR84JEwK0SOvX77a', 'spotify:track:2cBvJkneFRqK62VDL3yr0c']))

