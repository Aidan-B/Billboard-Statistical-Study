import csv
import spotify_api as s

def writeTop100SongsDurations(songTitles):

    # open the file in the write mode
    with open('top100SongsDurations', 'w') as csv_file:
        # create the csv writer
        writer = csv.writer(csv_file)

        for songTitle in songTitles:
            
            # call to Spotify API to get track response using songTitle
            song = s.get_track(songTitle)
            # get songDuration from the track response
            songDuration = song['tracks']['items'][0]['duration_ms']
            
            # print("Querying for: " + song)
            # print("Received response with duration {}".format(songDuration))

            # write the songDuration as a row to the csv file
            writer.writerow([songDuration])
