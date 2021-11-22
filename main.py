import spotify_api as s
import json
import readFromCSV
import writeToCSV

top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

top100SongsList = top100SongsAndArtists[0]
top100ArtistsList = top100SongsAndArtists[1]

writeToCSV.writeTop100SongsDurations(top100SongsList)

albums = s.get_albums(
    s.get_artist_albums(
        s.get_artist_id("pitbull")
    )
)

tracks = []
for album in albums:
    for track in album['tracks']['items']:
        tracks.append(track)
s.remove_duplicates(tracks)

for track in tracks:
    print( '{} - {}ms'.format(track['name'], track['duration_ms']) )