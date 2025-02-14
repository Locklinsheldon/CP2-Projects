
libr = []


def addnew():
    print()
def search():
    item = input("What is the EXACT name of the item you're looking for?: ")
    if item in libr:
        searem = input("This item is in your list. Would you like to remove this item?(y/n)")
        if searem == "y":
            libr - item
        if searem == "n":
            print("This item will stay in your list.")
def remove():
    rem = input("What item would you like to be removed?(type it's EXACT name): ")
    libr - rem
def ex():
    while True:
        print("GOODBYE")
def main():
    while True:
        print("Personal Library Program")
        print("1. Add a new item to your personal library")
        print("2. Search for a specific item in your library")
        print("3. Remove an item from your personal library")
        print("4. Exit the program")
       
        action = input("What would you like to do?: ")


        if action == "2":
            search()


        if action == "3":
            remove()


        if action == "4":
            ex()
main()

