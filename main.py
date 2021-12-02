import spotify_api as s
import json
import readFromCSV
import writeToCSV
import sampleSelector
import duplicateHunter

def calculate_mean(samples, size):
    return (sum(samples) / size)

def get_sample_and_export_sample_for_top_100(sample_size):
    print("Reading and sampling top 100 songs durations list")
    sample = sampleSelector.samples_from_top_100(sample_size)
    songDurationsInSample = sample[0]
    songsInSample = sample[1]

    sampleMean = calculate_mean([ int(duration) for duration in songDurationsInSample], 300)
    print("The mean of the sample of top 100 songs is {} ms".format(sampleMean))

    print("Writing top 100 songs sample list")
    writeToCSV.writeTop100SongsSample(songsInSample)

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

def get_sample_and_export_sample_for_artists(sample_size):
    print("Reading and sampling top 100 songs durations list")
    sample = sampleSelector.samples_from_artists(sample_size)
    songDurationsInSample = sample[0]
    songsInSample = sample[1]

    sampleMean = calculate_mean([ int(duration) for duration in songDurationsInSample], 300)
    print("The mean of the sample of top 100 songs is {} ms".format(sampleMean))

    print("Writing artists songs sample list")
    writeToCSV.writeArtistsSongsSample(songsInSample)

print("Reading top 100 songs and artist list")
top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

# print("Writing top 100 songs with durations list")
# writeToCSV.writeTop100SongsDurations(top100SongsAndArtists[0])

get_sample_and_export_sample_for_top_100(300)

# print("Collecting all songs by artists")
# collect_all_songs_for_artists(top100SongsAndArtists[1], 0)
# collect_all_songs_for_artists(['n*e*r*d'], 0)

get_sample_and_export_sample_for_artists(300)

# print(duplicateHunter.hunt_duplicates())