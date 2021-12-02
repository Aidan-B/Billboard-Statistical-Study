import os
import random
import math
import re

def samples_from_top_100(samples):
    with open('top100SongsDurations.txt', encoding="utf-8") as csv_file:
        songsInSample = []
        songDurationsInSample = []

        # init a random number generator using the current time as the seed
        random.seed()

        list = []

        # add each line in the csv file to a list
        for line in csv_file:
            # remove any whitespace in the line
            line = line.strip()
            # if the line is not blank, then append it to the list of lines
            if line:
                list.append(line)
                # print("Appended " + line)

        # get number of songs in CSV file (first row in the file)
        numberOfSongs = list[0]
        # print("Got number of songs: " + numberOfSongs)

        # loop until there are enough samples in the songDurationsInSample array
        while len(songDurationsInSample) < samples:
            # generate a random number between 1 (do not include row 0 since that specifies number of songs in the CSV) 
            # and the total number of songs
            randomNum = random.randint(1, int(numberOfSongs)-1)
            # print("Random number is: " + str(randomNum))

            # get number of songs in CSV file (first row in the file)
            songToBeSampled = list[randomNum]
            # print("Song to be sampled is: " + songToBeSampled)

            # split the string after the \t character twice, and select the third element (the duration in ms)
            sampledSongDuration = songToBeSampled.split("\t",2)[2]

            # check to see if a song has already been sampled
            hasAlreadyBeenSampled = False
            # loop through existing songsInSample
            for song in songsInSample:
                # compare the ids of the song to be sampled and the existing songs in the sample
                if songToBeSampled.split("\t",2)[0] == song.split("\t",2)[0]:
                    # if the songToBeSampled has already been sampled, set hasAlreadyBeenSampled
                    hasAlreadyBeenSampled = True
                    # print("Song has already been sampled")
                    break

            if hasAlreadyBeenSampled == False:
                # add the song duration to sample array
                songDurationsInSample.append(sampledSongDuration)
                songsInSample.append(songToBeSampled)

        return [songDurationsInSample, songsInSample]

def samples_from_artists(samples):
    songDurationsInSample = []
    # list of songs already in sample to prevent songs being sampled twice (saved as full lines i.e. "[Song title] - [song duration]ms")
    songsInSample = []
    lines = []
    files = os.listdir("./artists")
    for file in files:
        with open("./artists/{}".format(file), encoding="mbcs") as f:
            lines.append(int(f.readline().strip()))

    totalPopulation = sum(lines)

    # loop until there are enough samples in the songDurationsInSample array
    while len(songDurationsInSample) < samples:
        line = ''
        sampleIndex = random.randint(1,totalPopulation)
        fileIndex = 0
        for count in lines:
            if (sampleIndex - count > 0):
                sampleIndex -= count
                fileIndex += 1
            else:
                with open("./artists/{}".format(files[fileIndex]), encoding="mbcs") as f:
                    f.readline().strip()
                    for index in range(0, sampleIndex):
                        line = f.readline().strip()

                    # save the full line as the song to be sampled (full line i.e. "[Song title] - [song duration]ms"))
                    songToBeSampled = line
                    # print("Song to be sampled is: " + songToBeSampled)

                    # split the string after the \t character twice, and select the third element (the duration in ms)
                    sampledSongDuration = songToBeSampled.split("\t",2)[2]
                    
                    # check to see if a song has already been sampled
                    hasAlreadyBeenSampled = False
                    # loop through existing songsInSample
                    for song in songsInSample:
                        if songToBeSampled == song:
                            # if the songToBeSampled has already been sampled, set hasAlreadyBeenSampled
                            hasAlreadyBeenSampled = True
                            # print("Song has already been sampled")
                            break

                    if hasAlreadyBeenSampled == False:
                        # add song duration to songDurationsInSample
                        songDurationsInSample.append(sampledSongDuration)
                        # append the song to the existing songsInSample
                        songsInSample.append(songToBeSampled)
                    break
        
    return [songDurationsInSample, songsInSample]