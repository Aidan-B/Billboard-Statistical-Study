import os
import random
import math


def samples_from_artists(samples):
    output = []
    lines = []
    files = os.listdir("./artists")
    for file in files:
        with open("./artists/{}".format(file)) as f:
            lines.append(int(f.readline().strip()))


    totalPopulation = sum(lines)


    for i in range(0, samples):
        line = ''
        sampleIndex = random.randint(1,totalPopulation)
        fileIndex = 0
        for count in lines:
            if sampleIndex - count > 0:
                sampleIndex -= count
                fileIndex += 1
            else:
                with open("./artists/{}".format(files[fileIndex])) as f:
                    f.readline().strip()
                    for index in range(0, sampleIndex):
                        line = f.readline().strip()
        
        output.append("{}, {}".format(files[fileIndex], line))
    return output
