import random

lowlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
(random.choice(lowlet))

uplet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def upnlow():
    lowlet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    (random.choice(lowlet))
def numberz():
    print("erm")
def speshal():
    print("erm")
def main():
    pass1 = []
    pass2 = []
    pass3 = []
    pass4 = []
    print("Welcome to the Random Password Generator.")
    length = input("How long do you want your password to be or how long does your password need to be?: ")
    uplow = input("Do you need upper and lowercase letters?(y/n): ")
    if uplow == "y":
        upnlow()
    elif uplow == "n":
        print("There will be no uppercase letters in your password.")
    nums = input("Does your password need numbers?(y/n): ")
    if nums == "y":
        numberz()
    elif nums == "n":
        print("There will be no numbers in your password.")
    spechar = input("Does your password need special characters?(y/n): ")
    if spechar == "y":
        speshal()
    elif spechar == "n":
        print("There will be no special characters in your password.")
main()