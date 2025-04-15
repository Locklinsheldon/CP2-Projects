import csv

print("\nWelcome to the Movie Recommender")

def showMovies(path='MR/movies.csv'):
    try:
        with open(path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("<Couldn't find movie>")

def genre():
    genre = ["Drama", "Comedy", "Sci-Fi", "Adventure", "Family", "Animation", "History", "Action", "Fantasy", "Biography", "Sport", "Musical", "Romance", "War", "Crime", "Mystery", "Thriller", "Music"]
    print("\nAvailable Genres:")
    for index, x in enumerate(genre, start=1):
        print(f"{index}. {x}")
    
    while True:
        try:
            choice = int(input("\nWhat genre?(1-18): "))
            if 1 <= choice <= 18:
                print(f"\nGenre selected: {genre[choice - 1]}")
                break
            else:
                print("<Input needs to be a number(1-18)>")
        except ValueError:
            print("<Input needs to be a number(1-18)>")

def direct():
    dire = input("\nEnter the director's name: ")
    print(f"\nSearching for movies directed by {dire}...")

def length():
    try:
        minLength = int(input("\nEnter minimum movie length in minutes: "))
        maxLength = int(input("\nEnter maximum movie length in minutes: "))
        print(f"\nSearching for movies between {minLength}-{maxLength} minutes...")
    except ValueError:
        print("<Input needs to be a number>")

def actors():
    act = input("\nEnter an actor's name: ")
    print(f"\nSearching for movies with {act}...")

def printList():
    with open('MR/movies.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

def find():
    print("\nSearch Options:")
    print("1. Genre\n2. Directors\n3. Length\n4. Actors")
    
    availChoices = {"1": genre, "2": direct, "3": length, "4": actors}
    
    while True:
        askWhat1 = input("\nSelect the first search option(1-4): ")
        if askWhat1 in availChoices:
            availChoices[askWhat1]()
            break
        else:
            print("<Input needs to be a number(1-4)>")

    while True:
        print("\nSearch Options:")
        print("1. Genre\n2. Directors\n3. Length\n4. Actors")
        askWhat2 = input("\nSelect the second search option(1-4): ")
        if askWhat2 == askWhat1:
            print("\n<You can't choose the same option twice>.")
        elif askWhat2 in availChoices:
            availChoices[askWhat2]()
            break
        else:
            print("<Input needs to be a number(1-4)")

def menu():
    print("\n1. Print All Movies\n2. Find A Movie\n3. End Program")
    which = input("What would you like to do?(1-3): ")
    if which == "1":
        showMovies()
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
