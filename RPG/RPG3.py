import random #Gives python the ability to generate random values

print("\nWelcome to the Random Password Generator") #Notifies the user that they are in the Random Password Generator 
length = int(input("\nHow long does your password need to be?: ")) #Asks the user how long their password needs to be
upper = str(input("\nDo you need upper case letters in your password?(y/n): ")) == "y" #Asks the user if they need upper case letters in their password
special = str(input("\nDo you need special characters in your password?(y/n): ")) == "y" #Asks the user if they need special characters in their password
nummerz = str(input("\nDo you need numbers in your password?(y/n): ")) == "y" #Asks the user if they need lower case letters in their password

def excepts(): #Function to inform the user that they can
        if not (upper or special or nummerz): 
            return print("Thats not an option")        
excepts()

def main():
    char = "abcdefghijklmnopqrstuvwxyz"
    if upper: 
         char += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if special: 
         char += "!@#$%&"
    if nummerz: 
         char += "123456789"
    
    print("\nHere are a few passwords you can use:")
    
    for _ in range(4):
        print("")
        password = "".join(random.choice(char) for _ in range(length))
        
        print(password)
main()