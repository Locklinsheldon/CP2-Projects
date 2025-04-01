libr = []

t = True

def addItem():
    name = input("What is the name of your item?: ")

    auth = input("Who is the author of this item?: ")

    rDate = input("When was this item first released?: ")

    genre = input("What is this item's genre?: ")

    info = {'Name': name, 'Author': auth, 'Release Date': rDate, 'Genre': genre}

    libr.append(info)

    print(libr)

def change():#Make change
    

def menu():
    print("1. Add a new item to your library")
    print("2. Change the details of an item in your library")
    print("3. Remove an item from you library")
    print("4. View library")
    
    ask = input("What would you like to do?(1-4): ")
    if ask == "1":
        addItem()
    if ask == "2":
        change()

while t == True:
    menu()