import csv
import spotify_api as s

def writeTop100SongsDurations(songTitles):

    # open the file in the write mode
    with open('top100SongsDurations', 'w') as csv_file:
        # create the csv writer
        writer = csv.writer(csv_file)
        # get number of songs in songTitles
        numberOfSongs = len(songTitles)
        # write the number of songs to the top of the csv
        writer.writerow(numberOfSongs)

        for songTitle in songTitles:
            
            # call to Spotify API to get track response using songTitle
            song = s.get_track(songTitle)
            # get songDuration from the track response
            songDuration = song['tracks']['items'][0]['duration_ms']

            # write the songTitle and songDuration as a row to the csv file
            writer.writerow(songTitle + '\t' + [songDuration])
