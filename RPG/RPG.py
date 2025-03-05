import random #Gives python the ability to generate random values

print("\nWelcome to the Random Password Generator") #Notifies the user that they are in the Random Password Generator 
length = int(input("\nHow long does your password need to be?: ")) #Asks the user how long their password needs to be
upper = str(input("\nDo you need upper case letters in your password?(y/n): ")) == "y" #Asks the user if they need upper case letters in their password
special = str(input("\nDo you need special characters in your password?(y/n): ")) == "y" #Asks the user if they need special characters in their password
nummerz = str(input("\nDo you need numbers in your password?(y/n): ")) == "y" #Asks the user if they need lower case letters in their password

def excepts(): #Function to tell the user if their input is invalid
        if length != "y" or "n":
            return print("\nThats not an option") #Checks if input is valid
        if upper != "y" or "n":
            return print("\nThats not an option") #Checks if input is valid
        if special != "y" or "n":
            return print("\nThats not an option") #Checks if input is valid
        if nummerz != "y" or "n":
            return print("\nThats not an option") #Checks if input is valid        
excepts() #Calls the function

def main(): #Main function for the program
    char = "abcdefghijklmnopqrstuvwxyz" #Lower case letters to pick from
    if upper: #Checks if user selected upper case letters
         char += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Upper case letters to pick from
    if special: #Checks if user selected special characters
         char += "!@#$%&" #Special characters to pick from
    if nummerz: #Checks if user selected numbers
         char += "123456789" #Numbers to pick from
    
    print("\nHere are a few passwords you can use:") #Indicates where the passwords are
    
    for _ in range(4): #Continues adding characters until required character number is reached
        print("") #Prints a space between each password
        password = "".join(random.choice(char) for _ in range(length)) #Randomly selects characters from users requirments
        
        print(password) #Prints the passwords
main() #Calls the main function
