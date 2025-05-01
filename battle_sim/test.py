import csv
who = input("Who would you like to add?: ")

new = ", " + who

with open('battle_sim/char.csv', newline='') as csvfile:
    charreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in charreader:
        print(new.join(row))