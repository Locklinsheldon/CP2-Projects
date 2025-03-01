import random

def ranChar():
    print("\nWelcome to the Random Password Generator")
    
    length = int(input("\nHow long does your password need to be?: "))
    upper = str(input("Do you need upper case letters in your password?(y/n): ")) == "y"
    special = str(input("Do you need special characters in your password?(y/n): ")) == "y"
    nummerz = str(input("Do you need numbers in your password?(y/n): ")) == "y"
    
    if not (upper or special or nummerz): 
        return print("Thats not an option")
    
    print("Here are a few passwords you can use:")

    char = "abcdefghijklmnopqrstuvwxyz"
    if upper: char += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if special: char += "!@#$%&"
    if nummerz: char += "123456789"

    for _ in range(4):
        print("")
        password = "".join(random.choice(char) for _ in range(length))
        print(password)

ranChar()