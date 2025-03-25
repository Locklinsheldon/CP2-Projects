libr = set()
add = True
print("Add items to your library")


def get_dictionary_input():
    my_dict = {}
    name = input("Enter name: ")
    author = input("Enter author: ")
    my_dict[name] = author
    return my_dict

def thing():
    while add == True:
        user_dict = get_dictionary_input()
        libr = libr.union(user_dict.items())
        print(libr)
        isadd = input("Add another item?(y/n): ")
        if isadd == "n":
            add = False
        elif isadd == "y":
            print("Add an item")
        else:
            add = False

print(libr)