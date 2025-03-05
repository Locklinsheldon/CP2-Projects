#Locklin Sheldon, writing to text notes
import csv
"""
r = to read the file w = write on the file (replaces the old file) w+ = read and write a = append (adds to the file, doesn't delte them) (create the file if it doesn't exist) a+ = append and read the file """

#with open("Notes_6th/test.txt") as file:
#    file.write("")

with open("Notes_6th/user_info.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f"user name: [{row[0]} color: {row[1]}")