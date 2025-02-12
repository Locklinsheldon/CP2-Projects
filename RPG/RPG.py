def upnlow():
    print("erm")
def numberz():
    print("erm")
def speshal():
    print("erm")
def main():
    print("Welcome to the Random Password Generator.")
    length = input("How long does your password need to be?: ")
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