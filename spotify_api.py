import requests
import json
import math

token = "BQCuQq3_0oJo591P2F8OqGzITfXfyGlmnZ4R15DPTBElmNQoD2zV0MNf9SrvFwqIXmNtHntyzzgEOITap9VRnlLfP20h6qvWjfxCJ1HEA36XIhtkXARjBaTnGPoCb-8E_ksFdhTOXQKnOaQbJ0pSg2_8czUlXNA"
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
    idList = []
    output = []
    for i in range(math.ceil(len(ids) / 20)):
        idList.append(ids[(i*20):(i*20)+20])
        
    for id in idList:
        params = {'ids': ','.join(id) }
        output += json.loads(requests.get(url, params=params, headers=headers).text)['albums']

    return output

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
