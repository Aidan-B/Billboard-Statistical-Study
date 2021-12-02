import readFromCSV
import writeToCSV
import sampleSelector
import duplicateHunter
import spotify_api as s

import csv
import json

# The mean of the sample of top 100 songs is 223274.53666666665 ms

# The mean of the sample of top 100 songs is 218892.91 ms

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

def collect_all_songs_for_artists(artistIdList, startIndex):
    print("Writing artist song lists")
    sampleIndex = 0
    for artist in artistIdList:
        if startIndex <= sampleIndex:
            print(artist)
            try:
                albums = s.get_albums(
                    s.get_artist_albums(
                        artist['id']
                    )
                )
            except:
                print("Error at " + str(sampleIndex))
                exit(1)

            artist['name'] = artist['name'].strip().lower().replace(".", '').replace("*", '')
            tracks = []
            for album in albums:
                for track in album['tracks']['items']:

                    for artists in track['artists']:
                        if artists['id'] == artist['id']:
                            tracks.append(track)
                    
            tracks = s.remove_duplicates(tracks)

            writeToCSV.writeTopArtistDurations(tracks, artist['name'])
        sampleIndex += 1

    print("Finished writing files")

def get_sample_and_export_sample_for_artists(sample_size):
    print("Reading and sampling artists songs durations list")
    sample = sampleSelector.samples_from_artists(sample_size)
    songDurationsInSample = sample[0]
    songsInSample = sample[1]

    sampleMean = calculate_mean([ int(duration) for duration in songDurationsInSample], 300)
    print("The mean of the sample of artists songs is {} ms".format(sampleMean))

    print("Writing artists songs sample list")
    writeToCSV.writeArtistsSongsSample(songsInSample)


# print("Reading top 100 songs and artist list")
# top100SongsAndArtists = readFromCSV.readTop100SongsAndArtists()

# print("Writing top 100 songs durations")
# # top100Artists = writeToCSV.writeTop100SongsDurations(top100SongsAndArtists[0])

# top100Artists = []
# with open('top100Artists.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         top100Artists.append({ "name": line[1], "id": line[0] })


# print("Collecting all songs by artists")
# collect_all_songs_for_artists(top100Artists, 0)
# duplicateHunter.hunt_duplicates()

print("Removing duplicates between top 100 songs and artist list")
readFromCSV.removeTop100SongsfromTop100Artists()

print("Done!")

# get_sample_and_export_sample_for_top_100(300)


# get_sample_and_export_sample_for_artists(300)

# print(duplicateHunter.hunt_duplicates())