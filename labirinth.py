import csv


def walk():
    start = (1, 1)
    end = (len(matrix) - 2, len(matrix) - 2)
    matrix[start[0]][start[1]] = 'V'
    matrix[end[0]][end[1]] = 'X'

with open('maze.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    matrix = []
    for row in reader:
        matrix.append(row)

matrix = [[' ' if element == '0' else element for element in row] for row in matrix]

walk()
for row in matrix:
    print(' '.join(row))