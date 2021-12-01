import os
import collections
import csv

def hunt_duplicates():
    
    files = os.listdir("./artists")
    lines = []
    allSongs = []

    for file in files:
        with open("./artists/{}".format(file), 'r') as f:
            
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
    with open('./AllArtists-NoDuplicates.txt', 'w') as csv_file:
        # create the csv writer
        writer = csv.writer(csv_file)
        
        writer.writerow([len(new_vals)])

        for song in new_vals:
            # write the songDuration as a row to the csv file
            writer.writerow([song])

    return len(new_vals) - len(allSongs)
