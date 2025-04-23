import csv

print("\nWelcome to the Movie Recommender")

# Function to show all the movies
def show_movies(path='MR/movies.csv'):
    try:
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)  # Read as dictionary to get column names
            for row in reader:
                print(f"{row['Title']} - {row['Director']} - {row['Genre']} - {row['Length (min)']} min")
    except FileNotFoundError:
        print("<Couldn't find movie>")

# Function to let the user select a genre
def genre():
    genre_list = ["Drama", "Comedy", "Sci-Fi", "Adventure", "Family", "Animation", "History", "Action", 
                  "Fantasy", "Biography", "Sport", "Musical", "Romance", "War", "Crime", "Mystery", "Thriller", "Music"]
    print("\nAvailable Genres:")
    for index, x in enumerate(genre_list, start=1):
        print(f"{index}. {x}")
    
    while True:
        try:
            choice = int(input("\nWhat genre?(1-18): "))
            if 1 <= choice <= 18:
                print(f"\nGenre selected: {genre_list[choice - 1]}")
                break
            else:
                print("<Input needs to be a number(1-18)>")
        except ValueError:
            print("<Input needs to be a number(1-18)>")

# Function for selecting a director
def direct():
    dire = input("\nEnter the director's name: ")
    print(f"\nSearching for movies directed by {dire}...")

# Function to get movie length range
def length():
    try:
        min_length = int(input("\nEnter minimum movie length in minutes: "))
        max_length = int(input("\nEnter maximum movie length in minutes: "))
        print(f"\nSearching for movies between {min_length}-{max_length} minutes...")
    except ValueError:
        print("<Input needs to be a number>")

# Function to search by actor's name
def actors():
    act = input("\nEnter an actor's name: ")
    print(f"\nSearching for movies with {act}...")

# Function to print the movie list in a user-friendly format
def print_list():
    with open('MR/movies.csv', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(f"{row['Title']} - {row['Director']} - {row['Genre']} - {row['Length (min)']} min")

# Function to search for movies based on criteria
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
            print("<Input needs to be a number(1-4)>")

# Main menu function
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

# Main loop to run the program
while True:
    menu()
