import csv
import spotify_api as s

def writeTop100SongsDurations(songTitles):

    # open the file in the write mode
    with open('top100SongsDurations.txt', 'w', encoding="utf-8") as file:
                
        output = []
        for song in songTitles:
            # call to Spotify API to get track response using songTitle
            song = s.get_track(song)['tracks']['items'][0]
            output.append("\"{}\"\t\"{}\"\t{}\n".format(song['id'], song['name'], song['duration_ms']))
        
        file.writelines(
            ["{}\n".format(len(songTitles))] + output
        )


def writeTopArtistDurations(songs, artistName):

    # open the file in the write mode
    with open('./artists/{}'.format(artistName), 'w') as file:
        # create the csv writer
        output = ["{}\n".format(len(songs))] + [ '\"{}\"\t\"{}\"\t{}\n'.format(song['id'], song['name'].replace('"', ''), song['duration_ms']) for song in songs ]
        file.writelines(output)

        # for song in songs:
        #     # write the songDuration as a row to the csv file
        #     writer.writerow(['\"{}\"\t{}'.format(song['name'].replace('"', ''), song['duration_ms'])])
