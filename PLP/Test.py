def get_dictionary_input():
    """Gets dictionary input from the user."""
    my_dict = {}
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value
    return my_dict

user_dict = get_dictionary_input()
print("The dictionary is:", user_dict)

#ADD A DICT