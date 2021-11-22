import spotify_api as s
import json
import readFromCSV
import writeToCSV

import sampleSelector

print("Reading artist list")
top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

print("Writing hot 100 song list")
top100SongsList = top100SongsAndArtists[0]
writeToCSV.writeTop100SongsDurations(top100SongsList)
sampledSongs = readFromCSV.readAndSampleTop100SongsDurations()
print(*sampledSongs, sep="|")

# print("Writing artist song lists")
# top100ArtistsList = top100SongsAndArtists[1]
# top100ArtistsList = ["pitbull", "blur"]
# for artist in top100ArtistsList:
#     print(artist)
#     albums = s.get_albums(
#         s.get_artist_albums(
#             s.get_artist_id(artist)
#         )
#     )

#     tracks = []
#     for album in albums:
#         for track in album['tracks']['items']:
#             tracks.append(track)
            
#     tracks = s.remove_duplicates(tracks)

#     writeToCSV.writeTopArtistDurations(tracks, artist)

# print("Finished writing files")

# print("Grabbing random sample from artist")
# samples = sampleSelector.samples_from_artists(10)
# print(samples)

# albums = s.get_albums(
#     s.get_artist_albums(
#         s.get_artist_id("pitbull")
#     )
# )