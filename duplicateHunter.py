import os
import collections
import csv

def hunt_duplicates():
    
    files = os.listdir("./artists")
    lines = []
    allSongs = []

    for file in files:
        with open("./artists/{}".format(file), 'r', encoding="utf-8") as f:
            
            lines = f.readlines()
            lines.pop(0)
            for line in lines:
                allSongs.append(line.strip())
    
    print("{} songs to be searched".format(len(allSongs)))

    new_vals=[]
    col = collections.Counter(allSongs)
    for i in col:
        all = [x for x in allSongs if x==i]
        new_vals.append(all[0])
        if (len(new_vals) % 4096 == 0):
            print("{}%".format(round(len(new_vals)/len(allSongs)*100)))
    print("100%")

    # open the file in the write mode
    with open('./AllArtists-NoDuplicates.txt', 'w') as file:
        
        file.writelines(["{}\n".format(len(new_vals))] + ["{}\n".format(line) for line in new_vals])
        
    return len(new_vals) - len(allSongs)
