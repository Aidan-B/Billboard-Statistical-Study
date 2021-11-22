import csv
import linecache
import random
import collections

def readTop100SongsAndArtists():

    top100SongsList = []
    top100ArtistsList = []  

    with open('listOfTop100.txt') as csv_file:
        # remove any trailing characters at ends of lines
        lines = (line.rstrip() for line in csv_file)
        # remove any blank lines
        lines = (line for line in lines if line)
        # init a csv reader that divides lines using (\n) as delimiter
        csv_reader = csv.reader(lines, delimiter='\n')
        # track line count
        line_count = 0

        # iterate through all lines
        for line in csv_reader:
            if not line_count % 2:
                # odd lines are song titles, add them to the songs list
                top100SongsList.append(line[0])
            else:
                # even lines are artists, add them to the artists list
                top100ArtistsList.append(line[0])
            #increment line count    
            line_count += 1

        return [top100SongsList, top100ArtistsList]


def readAndSampleTop100SongsDurations():  

    with open('top100SongsDurations.txt') as csv_file:
        sampleOfTop100Songs = []

        # remove any trailing characters at ends of lines
        lines = (line.rstrip() for line in csv_file)
        # remove any blank lines
        lines = (line for line in lines if line)
        # init a csv reader that divides lines using (\n) as delimiter
        csv_reader = csv.reader(lines, delimiter='\n')
        # init a random number generator using the current time as the seed
        random.seed()
        # get number of songs in CSV file (first row in the file)
        numberOfSongs = lines[0]

        for _ in range (29):
            # generate a random number between 1 (do not include row 0 since that specifies number of songs in the CSV) and the
            randomNum = random.randint
            # select a song at a random line number
            sampledSong = lines[randomNum]
            # split the string after the \t character once, and select the second element
            sampledSongDuration = sampledSong.split("\t",1)[1] 
            # add the song duration to sample array
            sampleOfTop100Songs.append(sampledSongDuration)

        return sampleOfTop100Songs


def splitTop100Artists(top100Artists):
    # create new empty array to hold all split top 100 artists (in cases where multiple artists collaborated)
    splitTop100Artists = []
    # iterate through top100Artists
    for artist in top100Artists:
        if "," in artist:
            # if there is a comma, it is multiple artists, so split it around the commas into separate artists
            artists = artist.split(", ")
            # for each split artist, add them individually to splitTop100Artists
            for artist in artists:
                splitTop100Artists.append(artist)

    return splitTop100Artists

def removeDuplicatesFromTop100Artists(top100Artists):
    # create new empty array to hold filtered top 100 artists
    filteredTop100Artists = []
    # lowercase all artist names in the top100Artists array
    top100Artists = [artist.lower() for artist in top100Artists]
    # convert into a collections.Counter which has no duplicates, then add each element in the collections.Counter to the filtered array
    filteredTop100Artists = [i for i in collections.Counter(top100Artists)]

    return filteredTop100Artists
                

