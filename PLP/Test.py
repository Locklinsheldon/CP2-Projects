print("Welcome to The Grand Reopening of The Personal Library Program!\n(Now with the ability to update items!!!)")#Informs user of the program

libr = []#Library variable that stores the dictionaries
t = True#Makes it so the menu continues running

def addItem():#Function for adding items to the library
    name = input("\nWhat is the name of your item?: ")#Asks user for the name of the item
    auth = input("\nWho is the author of this item?: ")#Asks user for the author of the item
    rDate = input("\nWhen was this item first released?: ")#Asks user for the release date of the item
    genre = input("\nWhat is this item's genre?: ")#Asks user for the genre of the item
    print("")#This just makes it look pretty
    info = {'Item': len(libr), 'Name': name, 'Author': auth, 'Release Date': rDate, 'Genre': genre}#Organizes all of the details
    
    libr.append(info)#Attaches the organized details to the library
    print(libr)#Prints library

def remove():#Function for removing items from your library
    which = input("\nWhich item would you like to remove?(0-999): ")#Asks user what item they want removed
    
    if which.isdigit() and 0 <= int(which) < len(libr):#Requirements for deletion
        libr.pop(int(which))#Deletes the item
        print("")#Makes it look pretty
        print(libr)#Prints the library
    else:
        print("\nThat don't number")#Error for user

def change():#Function to change an items details
    askIt = input("\nWhich item are you looking for?(0-999): ")#Asks the user which item they are wanting to update
    
    if askIt.isdigit() and 0 <= int(askIt) < len(libr):#Requirements before updating
        item = libr[int(askIt)]#States that the item variable is equal to libr[(askIt)]
        print(item)#Prints the item
        print("1. Name\n2. Author\n3. Release Date\n4. Genre")#Users choices
        askDet = input("\nWhat detail do you want to change?(1-4): ")#Asks what detail they want changed
        askWhat = input("\nWhat would you like to change it to?: ")#Asks what they would like to change it to

        if askDet == "1":#Possible answers:
            item['Name'] = askWhat
        elif askDet == "2":
            item['Author'] = askWhat
        elif askDet == "3":
            item['Release Date'] = askWhat
        elif askDet == "4":
            item['Genre'] = askWhat
        else:
            print("Uhm... what?")#Error for user
    else:
        print("Couldn't find that :(")#Error for user

def menu():#Menu function for user to view options
    print("\n1. Add Item")#Possible options:
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Simple Library")
    print("5. View Detailed Library")
    print("6. Quit")
    
    ask = input("\nWhat would you like to do?: ")#Asks what the user what they want to do
    
    if ask == "1":#Possible answers:
        addItem()
    elif ask == "2":
        remove()
    elif ask == "3":
        change()
    elif ask == "4":
        print("")#This also just makes it look pretty
        print(libr)#Prints detailed library
    elif ask == "5":
        print("\nI'ma be so for real rn, I have no idea how to print a simple list, and it's already super late so like...")
    elif ask == "6":
        print("\n!WARNING! All items in your library will be lost!")#Warning for user before they end the program
        con = input("\nQuit?(y/n): ")#Asks user yes or no
        if con == "y":
            print("\nG'bye :(")#Says goodbye :(
            quit()#Ends the program
        if con == "n":
            print("\nGood choice...")
    else:
        print("I dunno what that means...")#Error for user

while t:#Makes the menu always run after a function finishes
    menu()#Calls the menu
