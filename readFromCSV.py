import os
import spotify_api as s
import csv
import random
import collections
import readFromCSV
import writeToCSV
import re


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
                # even lines are artists, append the artist name to the associated song in the songs list, 
                # then add them to the artists list
                indexOfLastSong = len(top100SongsList)-1
                top100SongsList[indexOfLastSong] = top100SongsList[indexOfLastSong] + " " + line[0]
                top100ArtistsList.append(line[0])
            #increment line count    
            line_count += 1

        splitArtists = splitTop100Artists(top100ArtistsList)
        filteredTop100Artists = removeDuplicatesFromTop100Artists(splitArtists)

        filteredTop100Songs = removeDuplicatesFromTop100Songs(top100SongsList)

        return [filteredTop100Songs, filteredTop100Artists]

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
        else: 
            splitTop100Artists.append(artist)

    return splitTop100Artists

def removeDuplicatesFromTop100Artists(top100Artists):
    # create new empty array to hold filtered top 100 artists
    filteredTop100Artists = []
    # lowercase all artist names in the top100Artists array
    top100Artists = [artist.lower() for artist in top100Artists]
    # convert into a collections.Counter which has no duplicates, then add each element in the 
    # collections.Counter to the filtered array
    filteredTop100Artists = [i for i in collections.Counter(top100Artists)]

    return filteredTop100Artists
                
def removeDuplicatesFromTop100Songs(top100Songs):
    filteredTop100Songs=[]
    
    # Turns each element to lowercase
    lowercaseTop100Songs = [x.lower() for x in top100Songs]
    
    filteredTop100Songs = [i for i in collections.Counter(lowercaseTop100Songs)]

    return filteredTop100Songs

def removeTop100SongsfromTop100Artists():

    # step 1: grab top 100 songs
    # step 2: loop through all artist files
    # step 2.1: compare all top 100 songs to things in artist file

    top100SongsList = []

    with open('top100SongsDurations.txt', encoding="utf-8") as csv_file:
        

        # add each line in the csv file to a list
        for line in csv_file:
            # remove any whitespace in the line
            line = line.strip()
            # if the line is not blank, then append it to the list of lines
            if line:
                top100SongsList.append(line)
                # print("Appended " + line)

        # get number of songs in CSV file (first row in the file)
        numberOfSongs = top100SongsList.pop(0)
        print("Got number of top 100 songs: " + numberOfSongs)

    #list to contain the artist's songs excluding those on the Top 100
    filteredTop100FromArtistSongs = []
    #open AllArtists-NoDuplicates file as f
    with open("AllArtists-NoDuplicates.txt", encoding='utf-8') as f:
        #read each line/song of the artist, save the full version and just the song title
        duplicatedSongs = []
        foundDuplicates = 0
        f.readline()
        for line in f:
            artistSong = line.strip()
            artistSongIdentifier = re.split("\t", artistSong)

            # loop through each song in the top100List, comparing to the current artist song
            # duplicate set to true if the artist song matches the current top 100 
            for top100song in top100SongsList:
                duplicate = False

                # breakpoint for twenty one pilots ride: top100SongIdentifier == "\"2Z8WuEywRWYTKe1NybPQEW\""
                top100SongIdentifier = re.split("\t", top100song)
                if artistSongIdentifier[0] == top100SongIdentifier[0] or (artistSongIdentifier[1] == top100SongIdentifier[1] and artistSongIdentifier[2] == top100SongIdentifier[2]):
                    duplicate = True
                    duplicatedSongs.append(top100song)
                    foundDuplicates += 1
                    print(artistSong + " is a duplicate")
                    
                    # BREAK HERE?

            #if the current artist song does not appear on the top 100 list, append the full line to the array
            if duplicate == False:
                filteredTop100FromArtistSongs.append(artistSong)
                # print(fullLine + " is NOT a duplicate")
        
        collection = collections.Counter( top100SongsList + duplicatedSongs )

        
        songsNotFound = 0

        for i in collection:
            if collection[i] == 1:
                print("{} was not found".format(i))
                songsNotFound += 1
                

        print("Duplicates found: " + str(foundDuplicates) + ", songs not found: " + str(songsNotFound))

    f.close()

    #write each full song line to the artist file
    with open("AllArtists-NoDuplicates.txt", "w", encoding='utf-8') as f:
        for song in filteredTop100FromArtistSongs:
            f.write(song + "\n")
    f.close()

    # files = os.listdir("./artists")
    # #loop through artist files
    # for file in files:
    #     #list to contain the artist's songs excluding those on the Top 100
    #     filteredTop100FromArtistSongs = []
    #     #open artist file as f
    #     with open("./artists/{}".format(file), encoding='utf-8') as f:
    #         #read each line/song of the artist, save the full version and just the song title
    #         for line in f:
    #             fullLine = f.readline().strip()
    #             artistSong = re.split("\s+\(feat\.|\s+\-\s+", fullLine)[0]

    #             # loop through each song in the top100List, comparing to the current artist song
    #             # duplicate set to true if the artist song matches the current top 100 
    #             for top100song in top100SongsList:
    #                 duplicate = 0
    #                 if artistSong.lower() == top100song.lower():
    #                     duplicate = 1
    #                     break

    #             #if the current artist song does not appear on the top 100 list, append the full line to the array
    #             if duplicate == 0:
    #                 filteredTop100FromArtistSongs.append(fullLine)
    #     f.close()

    #     #write each full song line to the artist file
    #     with open("./artists/{}".format(file), "w", encoding='utf-8') as f:
    #         for song in filteredTop100FromArtistSongs:
    #             f.write(song + "\n")
    #     f.close()

    # loop through every artist file
        # loop through every song in the artist file
            # loop through every song in top 100 array
                # declare variable fullLine
                # each song in top100SongsList is JUST a song title "Baby"
                # each song in artist file is NOT it's WEIRD -> split around " - "  and save as justSongTitle 
                # compare song in top 100 to current song in artist file
                # comparison is literally if top100SongName.lowercased() == justSongTitle.lowercased()
                # if they are duplicates, either:
                # A) erase it from the artist file (Google if we can write/edit individual files while reading)
                # B) if we can't do that, save fullLine to array if NOT duplicate, or do NOT save to array if IS duplicate
                
        # if we did option B), artist file loop ends and we now have an array of fullLines for this artist
        # open up EXISTING artist file to WRITE this time, loop through array and write each fullLine to file (GOOGLE if we will have extra stuff at bottom)
        # done!   
    
    # with open('top100SongsDurations.txt') as csv_file:
    #     for line in csv_file: # good
    #         line = line.split("\t",1)[0] # good
    #         if line: 
    #             justTop100Songs.append(line)

    # files = os.listdir("./artists")
    # fileIndex = 0
    # for file in files:
    #     with open("./artists/{}".format(file)) as f:
    #         lines.append(f.readline().strip())

    # for songTitle in justTop100Songs:
    #     if songTitle in filteredTop100FromArtistSongs:
    #         filteredTop100FromArtistSongs.filter(songTitle)
    #         print(songTitle)

    # return filteredTop100FromArtistSongs
    return
