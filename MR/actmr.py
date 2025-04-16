
import csv#Imports csv

print("\nWelcome to the Movie Recommender")#Welcomes user

def show_movies(path='MR/movies.csv'):#Function for showing the names of all of the movies
    try:
        with open(path, mode='r') as file:#Opens the csv file and prints it
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:#Error for if the file can't be found
        print("<Couldn't find movie>")

def genre():#Function for the user to pick which genre
    genre = ["Drama", "Comedy", "Sci-Fi", "Adventure", "Family", "Animation", "History", "Action", "Fantasy", "Biography", "Sport", "Musical", "Romance", "War", "Crime", "Mystery", "Thriller", "Music"]#List of all genres
    print("\nAvailable Genres:")
    for index, x in enumerate(genre, start=1):#Makes the users answer work
        print(f"{index}. {x}")
    
    while True:#Makes happen while true
        try:
            choice = int(input("\nWhat genre?(1-18): "))#User choice is taken
            if 1 <= choice <= 18:
                print(f"\nGenre selected: {genre[choice - 1]}")#Tells the user what genre they selected
                break#Takes the user back to the menu
            else:
                print("<Input needs to be a number(1-18)>")#Error message
        except ValueError:
            print("<Input needs to be a number(1-18)>")

def direct():#Function for user to select which director
    dire = input("\nEnter the director's name: ")#Users choice of director
    print(f"\nSearching for movies directed by {dire}...")

def length():#Function for getting how long the user wants the movie to be
    try:
        min_length = int(input("\nEnter minimum movie length in minutes: "))#Variable for the minimum length
        max_length = int(input("\nEnter maximum movie length in minutes: "))#Variable for the maximum length
        print(f"\nSearching for movies between {min_length}-{max_length} minutes...")
    except ValueError:#Error for if its not a number
        print("<Input needs to be a number>")

def actors():#Function for finding which actors the use wants
    act = input("\nEnter an actor's name: ")#Variable for which actor
    print(f"\nSearching for movies with {act}...")

def print_list():#Function for printing all of the movies
    with open('MR/movies.csv', new_line='') as csv_file:#Opens, then closes the movies csv
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

def find():#Function for finding which movie
    print("\nSearch Options:")
    print("1. Genre\n2. Directors\n3. Length\n4. Actors")
    
    avail_choices = {"1": genre, "2": direct, "3": length, "4": actors}
    
    while True:
        ask_what1 = input("\nSelect the first search option(1-4): ")
        if ask_what1 in avail_choices:
            avail_choices[ask_what1]()
            break
        else:
            print("<Input needs to be a number(1-4)>")

    while True:
        print("\nSearch Options:")
        print("1. Genre\n2. Directors\n3. Length\n4. Actors")
        ask_what2 = input("\nSelect the second search option(1-4): ")
        if ask_what2 == ask_what1:
            print("\n<You can't choose the same option twice>.")
        elif ask_what2 in avail_choices:
            avail_choices[ask_what2]()
            break
        else:
            print("<Input needs to be a number(1-4)")

def menu():#Menu for selecting what you want to do
    print("\n1. Print All Movies\n2. Find A Movie\n3. End Program")
    which = input("What would you like to do?(1-3): ")
    if which == "1":
        show_movies()
    elif which == "2":
        while True:
            find()
    elif which == "3":
            print("G O O D B Y E")
            exit()
    else:
        print("<Input needs to be a number(1-3)>")

while True:#Runs the program while true
    menu()
