import spotify_api as s
import json
import readFromCSV
import writeToCSV

top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

top100SongsList = top100SongsAndArtists[0]
top100ArtistsList = top100SongsAndArtists[1]

top100ArtistsList = ["pitbull"]
for artist in top100ArtistsList:

    albums = s.get_albums(
        s.get_artist_albums(
            s.get_artist_id(artist)
        )
    )

    tracks = []
    for album in albums:
        for track in album['tracks']['items']:
            tracks.append(track)
            
    tracks = s.remove_duplicates(tracks)

    writeToCSV.writeTopArtistDurations(tracks, artist)

print("Finished!")

# top100SongsDurations = getTop100SongsDurations(top100SongsList)
# print(*top100SongsDurations, sep=",")

# runawayBaby = s.get_track("Runaway Baby")
# trackId = runawayBaby['tracks']['items'][0]['id']
# trackDuration = runawayBaby['tracks']['items'][0]['duration_ms']

# print("Hi Matthew, track id is: " + trackId)
# print("Hi Matthew, track duration is: {}".format(trackDuration))

# for album in albums:
# #     print album
# for name in [ album['name'] for album in albums ]:    
#     print(name)

# for album in albums:
#     print()
#     print()
#     print(album['name'])
#     print("------")
#     for track in album['tracks']['items']:
#         print( '{} - {}ms'.format(track['name'], track['duration_ms']) )

# # for name in [ album['name'] for album in albums ]:    
# #     print(name)
