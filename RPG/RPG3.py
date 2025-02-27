import random

print("\nWelcome to the Random Password Generator")

def ranChar(): 
    length = int(input("\nHow long does your password need to be?: "))
    
    upper = input("\nDo you need upper case letters in your password?(y/n): ")
    if upper == "y":
        upperTrue = True
    elif upper == "n":
        upperTrue = False
    else:
        print("That's not an option")
        pass
    
    special = input("\nDo you need special characters in your password?(y/n): ")
    if special == "y":
        specTrue = True
    elif special == "n":
        specTrue = False
    else:
        print("That's not an option")
        pass

    numbers = input("\nDo you need numbers in your password?(y/n): ")
    if numbers == "y":
        numTrue = True
    elif numbers == "n":
        numTrue = False
    else:
        print("That's not an option")
        pass

    password1 = []
    password2 = []
    password3 = []
    password4 = []
    lowLet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upLet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specLet = ["!", "@", "#", "$", "%", "&"]
    nummerz = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]    
    rc = (0)
    runCount = int(rc)
    
    while runCount < length:    
        char1 = (random.choice(lowLet))
        if upperTrue == True:
            char2 = (random.choice(upLet))
        if specTrue == True:
            char3 = (random.choice(specLet))
        if numTrue == True:
            char4 = (random.choice(nummerz))
        
        if upperTrue == True and specTrue == True and numTrue == True:
            pickList4 = (char1, char2, char3, char4)
            ranPick4 = (random.choice(pickList4))
            fourTrue = True

        elif upperTrue == True and specTrue == True and numTrue != True:
            pickList3 = (char1, char2, char3)
            ranPick3 = (random.choice(pickList3))
            threeTrue = True

        elif upperTrue == True and specTrue != True and numTrue != True:
            pickList2 = (char1, char2)
            ranPick2 = (random.choice(pickList2))
            twoTrue = True

        elif upperTrue != True and specTrue != True and numTrue != True:
            pickList1 = (char1)
            ranPick1 = (random.choice(pickList1))
            oneTrue = True

        if fourTrue == True:
            if runCount < length:
                password1.append(ranPick4)
                runCount+=1
                if runCount == length:
                    print("".join(password1))

        elif threeTrue == True:
            if runCount < length:
                password1.append(ranPick3)
                runCount+=1
                if runCount == length:
                    print(password1)

        elif twoTrue == True:
            if runCount < length:
                password1.append(ranPick2)
                runCount+=1
                if runCount == length:
                    print(password1)

        elif oneTrue == True:
            if runCount < length:
                password1.append(ranPick1)
                runCount+=1
                if runCount == length:
                    print(password1)

ranChar()