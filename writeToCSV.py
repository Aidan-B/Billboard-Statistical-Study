import csv
import spotify_api as s

def writeTop100SongsDurations(songTitles):

    # open the file in the write mode
    with open('top100SongsDurations.txt', 'w', encoding="utf-8") as file:
                
        output = []
        artists = []
        for song in songTitles:
            # call to Spotify API to get track response using songTitle
            song = s.get_track(song)['tracks']['items'][0]
            artists += [ { "name": artist['name'], "id": artist['id'] } for artist in song['artists'] ]
            output.append("\"{}\"\t\"{}\"\t{}\n".format(song['id'], song['name'], song['duration_ms']))
        
        file.writelines(
            ["{}\n".format(len(songTitles))] + output
        )
    
    artists = [dict(t) for t in {tuple(d.items()) for d in artists}]
    with open('top100Artists.txt', 'w', encoding="utf-8") as file:
         file.writelines(["\"{}\"\t\"{}\"\n".format(artist['id'], artist['name']) for artist in artists])


    return artists


def writeTopArtistDurations(songs, artistName):

    # open the file in the write mode
    with open('./artists/{}'.format(artistName), 'w') as file:
        # create the csv writer
        output = ["{}\n".format(len(songs))] + [ '\"{}\"\t\"{}\"\t{}\n'.format(song['id'], song['name'].replace('"', ''), song['duration_ms']) for song in songs ]
        file.writelines(output)

        # for song in songs:
        #     # write the songDuration as a row to the csv file
        #     writer.writerow(['\"{}\"\t{}'.format(song['name'].replace('"', ''), song['duration_ms'])])

def writeTop100SongsSample(sample):

    # open the file in the write mode
    with open('top100SongsSample.txt', 'w', encoding="utf-8") as file:
        # write every sample in the sample as a line to the file      
        output = ["{}\n".format(song) for song in sample]  
        file.writelines(output)

def writeArtistsSongsSample(sample):

    # open the file in the write mode
    with open('artistsSongsSample.txt', 'w', encoding="utf-8") as file:
        # write every sample in the sample as a line to the file      
        output = ["{}\n".format(song) for song in sample]  
        file.writelines(output)