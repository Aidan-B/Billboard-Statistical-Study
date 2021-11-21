import requests
import json

token = "BQDD8mwKZu7ncJuwch4dfLr5bEIeAQ4cd_llr2zgYziL2XzeghzxmZmzPU-1WFI6Toti97wCUyNRZ0iQq4lbaHxQppIYlNvLl9QPqEEunrnHZ8DrhzC0FpMwLoSqAoiFjw02CjwYgFp4S_h425UgTPfW4eyoLLA"
headers = {
    'content-type': 'application/json',
    'Authorization': "Bearer {}".format(token)
}


spotify = "https://api.spotify.com/v1"

def get_artists(ids):
    url = spotify + "/artists"
    params = {'ids': ','.join(ids) }
    return requests.get(url, params=params, headers=headers).text

def get_tracks(ids):
    url = spotify + "/tracks"
    params = {'ids': ','.join(ids) }
    return requests.get(url, params=params, headers=headers).text

def get_albums(ids):
    url = spotify + "/albums"
    params = {'ids': ','.join(ids) }
    return requests.get(url, params=params, headers=headers).text

def get_artist_id(name):
    url = spotify + '/search'
    params = {
        'q': name,
        'type': 'artist',
    }
    response = json.loads(requests.get(url, params=params, headers=headers).text)
    return response['artists']['items'][0]['id']

def get_artist_albums(artistId):
    url = spotify + '/artists/{}/albums'.format(artistId)
    params = { 'limit': 50 }
    response = json.loads(requests.get(url, params=params, headers=headers).text)
    return [ sub['id'] for sub in response['items'] ]
