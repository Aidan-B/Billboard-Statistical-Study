import csv

top100SongsList = []
top100ArtistsList = []

with open('listOfTop100.txt') as csv_file:
    lines = (line.rstrip() for line in csv_file)
    lines = (line for line in lines if line)

    csv_reader = csv.reader(lines, delimiter='\n')
    line_count = 0
    for row in csv_reader:
        print(f'Started processing rows.')

        if (line_count % 2 == 0):
            #print(f'Song title: {row[0]}')
            top100SongsList.append(row[0])
        else:
            #print(f'Artist: {row[0]}')
            top100ArtistsList.append(row[0])
            
        line_count += 1

    print(f'Processed {line_count} lines.')

    print("Printing songs list")
    print(*top100SongsList, sep = ", ")

    print("Printing artists list")
    print(*top100ArtistsList, sep = ", ")