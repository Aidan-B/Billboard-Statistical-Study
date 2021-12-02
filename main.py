import spotify_api as s
import json
import readFromCSV
import writeToCSV
import sampleSelector
import duplicateHunter


def calculate_mean(samples, size):
    return (sum(samples) / size)

def collect_all_songs_for_artists(artistList, startIndex):
    print("Writing artist song lists")
    sampleIndex = 0
    for artist in artistList:
        if startIndex <= sampleIndex:
            print(artist)
            artistId = s.get_artist_id(artist)
            albums = s.get_albums(
                s.get_artist_albums(
                    artistId
                )
            )
            artist = artist.strip().lower().replace(".", '').replace("*", '')
            tracks = []
            for album in albums:
                for track in album['tracks']['items']:

                    for artists in track['artists']:
                        if artists['id'] == artistId:
                            tracks.append(track)
                    
            tracks = s.remove_duplicates(tracks)

            writeToCSV.writeTopArtistDurations(tracks, artist)
        sampleIndex += 1

    print("Finished writing files")

# print("Reading top 100 songs and artist list")
# top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

# print("Writing top 100 songs durations")
# writeToCSV.writeTop100SongsDurations(top100SongsAndArtists[0])

print("Reading and sampling top 100 songs durations")
print(
    "The mean of the sample of top 100 songs is {} ms".format(
        calculate_mean([ int(sample) for sample in sampleSelector.samples_from_top_100(300)], 300)
    )
)

# print("Collecting all songs by artists")
# collect_all_songs_for_artists(top100SongsAndArtists[1], 0)
# collect_all_songs_for_artists(['n*e*r*d'], 0)

# print("Grabbing random sample from artists")
# print(
#     "The mean of the sample of all artist songs is {} ms".format(
#         calculate_mean([ int(sample[2]) for sample in sampleSelector.samples_from_artists(300)], 300)
#     )
# )

# print(duplicateHunter.hunt_duplicates())