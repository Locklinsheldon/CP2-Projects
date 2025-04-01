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
    "real"

def menu():
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