libr = set()
add = True
print("Add items to your library")



def getDictInput():
        my_dict = {}
        name = input("Enter name: ")
        author = input("Enter author: ")
        my_dict[name] = author
        user_dict = getDictInput()
        libr = libr.union(user_dict.items())
        print(libr)
        return my_dict

def search():#Function for checking if an item is in the library
    searItem = input("\nWhat is the EXACT name of the item you're looking for?: ")#Asks for the name of the item
    if searItem in libr:#Checks if the item is in the library
        seaRem = input("\nThis item is in your list. Would you like to remove this item?(y/n): ")#Asks if they would like the item to be removed
        if seaRem == "y":
            libr.remove(searItem)#Removes the item
            print("\nUpdated library:", libr)
        elif seaRem == "n":
            print("\nThis item will stay in your library.")
            print("\nLibrary:", libr)
        else:
            print("\nSorry, that isn't an option :(")#Error message

def remove():#Function for removing an item
    remItem = input("\nWhat item would you like to be removed?(type it's EXACT name): ")#Asks what item
    if remItem in libr:#Checks if the item is in the library
        libr.remove(remItem)
        print("\nUpdated library:", libr)
    else:
        print("\nThis item may not be in your library, or perhaps the name was not typed properly.")#Error message for user

def view():#Function for viewing the current library
    print("\nCurrent library:", libr)

def ex():#Function for ending the programm
    leave = input("\n!ALL ITEMS IN YOUR LIBRARY WILL BE LOST!. Are you sure you want to end the program?(y/n): ")#Warning message for user
    if leave == "y":
        while True:
            print("\nG O O D B Y E")#Prints goodbye indefinetley
    else:
        print("\nThe program will continue.")

def main():#Menu for the user to select what they would like to do
    print("\nPersonal Library Program")    
    while True:#Makes the menu recur
        print("\n1. Add a new item to your personal library")
        print("2. Search for a specific item in your library")
        print("3. Remove an item from your personal library")
        print("4. View current library")
        print("5. Exit the program")
        
        action = input("\nWhat would you like to do?: ")
        if action == "1":
            getDictInput()

        elif action == "2":
            search()

        elif action == "3":
            remove()

        elif action == "4":
            view()

        elif action == "5":
            ex()

        else:
            print("\nThat is not an available action.")#Error message
main()#Starts the program