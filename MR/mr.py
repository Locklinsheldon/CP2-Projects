import csv

with open('MR/movies.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)