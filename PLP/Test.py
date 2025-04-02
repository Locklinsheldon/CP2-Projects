print("Welcome to The Grand Reopening of The Personal Library Program!\n(Now with the ability to update items!!!)")#Informs user of the program

libr = []#Library variable that stores the dictionaries
t = True#Makes it so the menu continues running

def addItem():
    name = input("\nWhat is the name of your item?: ")
    auth = input("\nWho is the author of this item?: ")
    rDate = input("\nWhen was this item first released?: ")
    genre = input("\nWhat is this item's genre?: ")
    print("")#This just makes it look pretty
    info = {'Item': len(libr), 'Name': name, 'Author': auth, 'Release Date': rDate, 'Genre': genre}
    
    libr.append(info)
    print(libr)

def remove():
    which = input("\nWhich item would you like to remove?(0-999): ")
    if which.isdigit() and 0 <= int(which) < len(libr):
        libr.pop(int(which))
    else:
        print("\nThat don't number")

def change():
    askIt = input("\nWhich item are you looking for?(0-999): ")
    if askIt.isdigit() and 0 <= int(askIt) < len(libr):
        item = libr[int(askIt)]
        print(item)
        print("1. Name\n2. Author\n3. Release Date\n4. Genre")
        askDet = input("\nWhat detail do you want to change?(1-4): ")
        askWhat = input("\nWhat would you like to change it to?: ")

        if askDet == "1":
            item['Name'] = askWhat
        elif askDet == "2":
            item['Author'] = askWhat
        elif askDet == "3":
            item['Release Date'] = askWhat
        elif askDet == "4":
            item['Genre'] = askWhat
        else:
            print("Uhm... what?")
    else:
        print("Couldn't find that :(")

def menu():
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Library")
    print("5. Quit")
    ask = input("\nWhat would you like to do?: ")
    if ask == "1":
        addItem()
    elif ask == "2":
        remove()
    elif ask == "3":
        change()
    elif ask == "4":
        print("")#This also just makes it look pretty
        print(libr)
    elif ask == "5":
        print("\n!WARNING! All items in your library will be lost!")
        con = input("\nQuit?(y/n): ")
        if con == "y":
            print("\nG'bye :(")
            quit()
        if con == "n":
            print("\nGood choice...")
    else:
        print("I dunno what that means...")
while t:
    menu()
