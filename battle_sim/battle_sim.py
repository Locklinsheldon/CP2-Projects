import pandas as pd
import csv

print("Welcome to the Ultimate Battle Simulator")

def thing():
    who = input("Who would you like to add?: ")

    new = ", " + who

    with open('battle_sim/char.csv', newline='') as csvfile:
        charreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in charreader:
            print(new.join(row))

def tutorial():
    print("\nTo start, the first thing you will need to do is create a character.")
    print("\nWhat would you like this character's name to be?")
    tutor_name = input("\nName: ")
    if tutor_name == "":
        tutor_name = "[No name]"
    print("\nNow that you have given your character a name, you must give it it's health, strength, defense, and speed atributes.")
    print("\nYou have 20 total points available.")
    pts = 20
    prnt = str(pts)
    print("\nYou have",(prnt),"points left")
    health = input("\nHow many points would you like to give to health?: ")
    pts-=int(health)
    print("\nYou have",(prnt),"points left")
    strength = input("\nHow many points would you like to give to strength?: ")
    pts-=strength
    print("\nYou have",(prnt),"points left")
    defense = input("\nHow many points would you like to give to defense?: ")
    pts-=defense
    print("\nYou have",(prnt),"points left")
    speed = input("\nHow many points would you like to give to speed?: ")
    pts-=speed
    print("Health:", health, "Strength:", strength, "Defense:", defense, "Speed:", speed)
    hap = input("\nAre you happy with these stats? (y/n): ")
    if hap == "y":
        print("\nSaving character...\nChecking for duplicates...\nDeleting all .Sys files...")
        with open('battle_sim/char.csv', 'a', newline='') as csvfile:
            charwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            charwriter.writerow([tutor_name, health, strength, defense, speed])
        print("\nYour character has been added!")
        show_char()
    else:
        print("\nRestarting Tutorial...")
        thing()



def show_char():
    df = pd.read_csv('battle_sim/char.csv')
    print(df.to_string())

tutorial()