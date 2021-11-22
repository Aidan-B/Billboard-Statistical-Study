import spotify_api as s
import json
import readFromCSV
import writeToCSV

import sampleSelector

# print("Reading top 100 songs and artist list")
# top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

# top100SongsList = top100SongsAndArtists[0]

# print("Writing top 100 songs durations")
# writeToCSV.writeTop100SongsDurations(top100SongsList)

print("Reading and sampling top 100 songs durations")
sampledSongs = readFromCSV.readAndSampleTop100SongsDurations()

sum = 0

for songDuration in sampledSongs:
    sum += int(songDuration)

mean = sum/len(sampledSongs)
print("The mean of the sample of top 100 songs is {} seconds".format(mean/1000))


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