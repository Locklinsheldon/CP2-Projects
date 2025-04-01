libr = []

t = True

def addItem():
    name = input("What is the name of your item?: ")
    auth = input("Who is the author of this item?: ")
    rDate = input("When was this item first released?: ")
    genre = input("What is this item's genre?: ")
    info = {'Item': len(libr), 'Name': name, 'Author': auth, 'Release Date': rDate, 'Genre': genre}
    
    libr.append(info)
    print(libr)

def remove():
    which = input("Which item would you like to remove?(0-999): ")
    libr.pop(which)

def change():
    askIt = input("Which item are you looking for?(0-999): ")
    if askIt in libr:
        print(libr(askIt))
        print("1. Name\n 2. Author\n 3. Release Date\n 4. Genre")
        askDet = input("What detail do you want to change?(1-4): ")
        askWhat = input("What would you like to change it to?: ")
        if askDet == "1":
            libr.update({name: askWhat})
        if askDet == "2":
            libr.update({auth})

def menu():
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Library")
    ask = input("What would you like to do?: ")
    if ask == "1":
        addItem()
    elif ask == "2":
        remove()
    elif ask == "3":
        change()
    elif ask == "4":
        print(libr)

while t == True:
    menu()