import csv

with open("maze.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        for col in row:
            print(col.replace('0;', '  '))