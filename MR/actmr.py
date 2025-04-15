#Imports csv
import csv

#Welcomes user
print("\nWelcome to the Movie Recommender")

#Function for showing the names of all of the movies
def show_movies(path='MR/movies.csv'):
    try:
        #Opens the csv file and prints it
        with open(path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                #Error for if the file can't be found
    except FileNotFoundError:
        print("<Couldn't find movie>")

#Function for the user to pick which genre
def genre():
    #List of all genres
    genre = ["Drama", "Comedy", "Sci-Fi", "Adventure", "Family", "Animation", "History", "Action", "Fantasy", "Biography", "Sport", "Musical", "Romance", "War", "Crime", "Mystery", "Thriller", "Music"]
    print("\nAvailable Genres:")
    #Makes the users answer work
    for index, x in enumerate(genre, start=1):
        print(f"{index}. {x}")
    
    #Makes happen while true
    while True:
        try:
            #User choice is taken
            choice = int(input("\nWhat genre?(1-18): "))
            if 1 <= choice <= 18:
                #Tells the user what genre they selected
                print(f"\nGenre selected: {genre[choice - 1]}")
                #Takes the user back to the menu
                break
            else:
                #Error message
                print("<Input needs to be a number(1-18)>")
        except ValueError:
            print("<Input needs to be a number(1-18)>")

#Function for user to select which director
def direct():
    #Users choice of director
    dire = input("\nEnter the director's name: ")
    print(f"\nSearching for movies directed by {dire}...")

def length():
    try:
        min_length = int(input("\nEnter minimum movie length in minutes: "))
        max_length = int(input("\nEnter maximum movie length in minutes: "))
        print(f"\nSearching for movies between {min_length}-{max_length} minutes...")
    except ValueError:
        print("<Input needs to be a number>")

def actors():
    act = input("\nEnter an actor's name: ")
    print(f"\nSearching for movies with {act}...")

def print_list():
    with open('MR/movies.csv', new_line='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

def find():
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

def menu():
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

while True:
    menu()
