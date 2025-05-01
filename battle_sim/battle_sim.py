import pandas as pd
print("Welcome to the Ultimate Battle Simulator")

def tutorial():
    print("\nTo start, the first thing you will need to do is create your character.")
    print("\nWhat would you like this character's name to be?")
    tutor_name = input("\nName: ")
    if tutor_name == "":
        tutor_name = "[No name]"
    print("Now that you have given your character a name, you must give it it's health, strength, defense, and speed atributes.")

def show_char():
    df = pd.read_csv('battle_sim/char.csv')
    print(df.to_string())

tutorial()