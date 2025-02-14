libr = set()

def addnew():
    new = input("What would you like to add to your personal library?: ")
    if new in libr:
        print("Sorry, this item is already in your library.")
    else:
        libr.add(new)
        print("Updated library:", libr)


def search():
    item = input("What is the EXACT name of the item you're looking for?: ")
    if item in libr:
        searem = input("This item is in your list. Would you like to remove this item?(y/n)")
        if searem == "y":
            libr.remove(item)
        elif searem == "n":
            print("This item will stay in your library.")
        else:
            print("Sorry, that isn't an option :(")

def remove():
    rem = input("What item would you like to be removed?(type it's EXACT name): ")
    if rem in libr:
        libr.remove(rem)
        print("Updated library:", libr)
    else:
        print("This item may not be in your library, or perhaps the name was not typed properly.")

def view():
    print("Current library:"libr)#Continue from here

def ex():
    proc = input("Are you sure you want to end the program? All items in your library will be lost(y/n): ")
    if proc == "y":
        while True:
            print("GOODBYE")
    else:
        print("The program will continue.")

def main():
    while True:
        print("Personal Library Program")
        print("1. Add a new item to your personal library")
        print("2. Search for a specific item in your library")
        print("3. Remove an item from your personal library")
        print("4. Exit the program")
        
        action = input("What would you like to do?: ")
        if action == "1":
            addnew()

        if action == "2":
            search()

        if action == "3":
            remove()

        if action == "4":
            ex()
main()
