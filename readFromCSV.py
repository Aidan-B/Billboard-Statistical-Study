import csv

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

    print(f'Started processing rows.')

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
    
    #print("Printing songs list:")
    #print(*top100SongsList, sep = "| ")
    #print("Printing artists list:")
    #print(*top100SongsList, sep = "| ")

    print(f'Processed {len(top100SongsList)} songs and {len(top100ArtistsList)} artists.')