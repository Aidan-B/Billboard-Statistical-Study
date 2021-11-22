import requests
import json
import math

<<<<<<< HEAD
token = "BQAnlc9vmd1otsd948AT68CNHVBnnr5o_eYrjSP3AUYklJsHh2iIty0Be6FTKQiPFpehHQ-PrTYEJesfqPiRaPG7BwQTX1opoM7rGoPyapMAtM71OaK1zssqZgN8Z_o7jmu32ihfiHLZmUFtjdM"
=======
token = "BQCuQq3_0oJo591P2F8OqGzITfXfyGlmnZ4R15DPTBElmNQoD2zV0MNf9SrvFwqIXmNtHntyzzgEOITap9VRnlLfP20h6qvWjfxCJ1HEA36XIhtkXARjBaTnGPoCb-8E_ksFdhTOXQKnOaQbJ0pSg2_8czUlXNA"
>>>>>>> 9458f078f358ad8baf5ac5961b9aece8688e059d
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

def get_track_id(songTitle):
    url = spotify + '/search'
    params = {
        'q': songTitle,
        'type': 'track',
    }
    response = json.loads(requests.get(url, params=params, headers=headers).text)
    return response['tracks']['items'][0]['id']

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
