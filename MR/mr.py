import csv

print("\nWelcome to the Movie Recommender.")

def thing():
    with open('MR/movies.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def genre():
    print("\n1. Drama\n2. Comedy\n3. Sci-Fi\n4. Adventure\n5. Family\n6. Animation\n7. History\n8. Action\n9. Fantasy\n10. Biography\n11. Sport\n12. Musical\n13. Romance\n14. War\n15. Crime\n16. Mystery\n17. Thriller\n18. Music")

    whatGen = input("\nWhat genre of movie would you like to see?(1-18): ")
    
    with open('MR/movies.csv', 'r') as file:
        reader = csv.reader(file)
    for row in reader:
        print(f"Column 1: {row[0]}, Column 2: {row[1]}")

def direct():
    ()

def length():
    ()

def actors():
    ()

def find():
    print("\n1. Genre\n2. Directors\n3. Length\n4. Actors")
    
    askWhat1 = input("\nWhat is the FIRST thing you would like to search by?(1-4): ")
    if askWhat1 == "1":
        genre()
    elif askWhat1 == "2":
        direct()
    elif askWhat1 == "3":
        length()
    elif askWhat1 == "4":
        actors()
    else:
        print("\nSry, that's not an option :(")
   
    askWhat2 = input("\nWhat is the SECOND thing you would like to search by?(1-4)")
    if askWhat2 == askWhat1:
        print("\n<You can't choose the same thing to search by>")
    elif askWhat2 == "1":
        genre()
    elif askWhat2 == "2":
        direct()
    elif askWhat2 == "3":
        length()
    elif askWhat2 == "4":
        actors()
    else:
        print("\nSry, that's not an option :(")

while True:
    find()