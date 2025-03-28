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

def remove():
    name = input("What is the name of your item")

def menu():
    ask = input("Wyt nummer?: ")
    if ask == "1":
        addItem()

while t == True:
    menu()