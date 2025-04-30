import pandas as pd
print("Welcome to the Ultimate Battle Simulator")

def tutorial():
    print("\nTo start, the first thing you will need to do is create your character.")
    print("\nWhat would you like this character's name to be?")
    input("Name: ")

df = pd.read_csv('battle_sim/char.csv')
print(df.to_string())