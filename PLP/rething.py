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
    del info
    print(libr)

def menu():
    ask = input("Wyt nummer?: ")
    if ask == "1":
        addItem()
    if ask == "2":
        change()

while t == True:
    menu()

#Is working :)