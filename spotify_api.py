import requests
import json
import math
import collections

token = "BQAQ31MG0lZX0WmE5atOWyGKk1aGIYaJ4dUHB7qFHC7olI6E1p3HRv-OGXriDv4OgsdldHSOaZdMV6d4-DhtFoC3Gto7ed12Q_mBrAL_Ya24FLejYLEpAdgguwV7C1vLDI1U1Q3Cc6SAQrZ7SJ2oIGUuSoI_X2o"

headers = {
    'content-type': 'application/json',
    'Authorization': "Bearer {}".format(token)
}

spotify = "https://api.spotify.com/v1"

def get_artists(ids):
    url = spotify + "/artists"

    idList = []
    output = []
    for i in range(math.ceil(len(ids) / 20)):
        idList.append(ids[(i*20):(i*20)+20])
        
    for id in idList:
        params = {'ids': ','.join(id), 'market': 'US' }
        output += json.loads(requests.get(url, params=params, headers=headers).text)['artists']

    output = remove_duplicates(output)

    return output

def get_tracks(ids):
    url = spotify + "/tracks"

    idList = []
    output = []
    for i in range(math.ceil(len(ids) / 50)):
        idList.append(ids[(i*50):(i*50)+50])
        
    for id in idList:
        params = {'ids': ','.join(id), 'market': 'US' }
        output += json.loads(requests.get(url, params=params, headers=headers).text)['tracks']

    output = remove_duplicates(output)

    return output

def get_track(query):
    url = spotify + '/search'
    params = {
        'q': query,
        'market': 'US',
        'type': 'track',
    }
    return json.loads(requests.get(url, params=params, headers=headers).text)

def get_albums(ids):
    url = spotify + "/albums"
    idList = []
    output = []
    for i in range(math.ceil(len(ids) / 20)):
        idList.append(ids[(i*20):(i*20)+20])
        
    for id in idList:
        params = {'ids': ','.join(id), 'market': 'US' }
        query = requests.get(url, params=params, headers=headers)
        output += json.loads(query.text)['albums']

    output = remove_duplicates(output)

    return output


def get_track_id(songTitle):
    url = spotify + '/search'
    params = {
        'q': songTitle,
        'market': 'US',
        'type': 'track',
    }
    response = json.loads(requests.get(url, params=params, headers=headers).text)
    return response['tracks']['items'][0]['id']

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


def remove_duplicates(response):
    new_vals=[]
    k = [item['name'] for item in response]
    for i in collections.Counter(k):
        all = [x for x in response if x['name']==i]
        new_vals.append(all[0])
    return new_vals