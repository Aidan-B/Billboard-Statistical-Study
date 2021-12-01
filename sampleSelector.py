import os
import random
import math
import re


def samples_from_artists(samples):
    output = []
    # list of songs already in sample to prevent songs being sampled twice (saved as full lines i.e. "[Song title] - [song duration]ms")
    songsInSample = []
    lines = []
    files = os.listdir("./artists")
    for file in files:
        with open("./artists/{}".format(file), encoding="mbcs") as f:
            lines.append(int(f.readline().strip()))


    totalPopulation = sum(lines)

    for i in range(0, samples):
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

                    regex = re.search('^(.*) - ([0-9]+)ms', line)
                    
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
                        # append to output an array containing [artist name, song name, duration in ms]
                        output.append([files[fileIndex], regex.group(1), regex.group(2)])
                        # append the song to the existing songsInSample
                        songsInSample.append(songToBeSampled)
                    break
        
    return output