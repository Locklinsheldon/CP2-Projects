import csv

def thing():
    with open('MR/movies.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)

def genre():

def direct():

def length():

def actors():

def find():
    print("\n1. Genre\n2. Directors\n3. Length\n4. Actors")
    
    askWhatnum1 = input("\nWhat is the first thing you would like to search by?(1-4): ")
    if askWhatnum1 == "1":
        askWhat1 = genre()
    elif askWhatnum1 == "2":
        askWhat1 = direct()
    elif askWhatnum1 == "3":
        askWhat1 = length()
    elif askWhatnum1 == "4":
        askWhat1 = actors()
    else:
        print("\nSry, that's not an option :(")
   
    askWhatnum2 = input("\nWhat is the second thing you would like to search by?(1-4)")
    if askWhatnum2 == askWhatnum1:
        print("\nYou can't choose the same thing to search by.")
    elif askWhatnum2 == "1":
        askWhat2 = genre()
    elif askWhatnum2 == "2":
        askWhat2 = direct()
    elif askWhatnum2 == "3":
        askWhat2 = length()
    elif askWhatnum2 == "4":
        askWhat2 = actors()
    else:
        print("\nSry, that's not an option :(")
    
    