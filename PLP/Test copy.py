libr = set()

print("Add items to your library")


def get_dictionary_input():
    my_dict = {}
    name = input("Enter name: ")
    author = input("Enter author: ")
    my_dict[name] = author
    return my_dict
    user_dict = get_dictionary_input()
    libr = libr.union(user_dict.items())

def thing():
    add = True
    while add == True:
        
        print(libr)
        isadd = input("Add another item?(y/n): ")
        if isadd == "n":
            add = False
        elif isadd == "y":
            print("Add an item")
        else:
            add = False
thing()

print(libr)