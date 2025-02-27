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
    
    print("Here are a few passwords you can use:")

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
        char1one = (random.choice(lowLet))
        if upperTrue == True:
            char2one = (random.choice(upLet))
        if specTrue == True:
            char3one = (random.choice(specLet))
        if numTrue == True:
            char4one = (random.choice(nummerz))
        
        if upperTrue == True and specTrue == True and numTrue == True:
            pickList4one = (char1one, char2one, char3one, char4one)
            ranPick4one = (random.choice(pickList4one))
            fourTrue = True

        elif upperTrue == True and specTrue == True and numTrue != True:
            pickList3one = (char1one, char2one, char3one)
            ranPick3one = (random.choice(pickList3one))
            threeTrue = True

        elif upperTrue == True and specTrue != True and numTrue != True:
            pickList2one = (char1one, char2one)
            ranPick2one = (random.choice(pickList2one))
            twoTrue = True

        elif upperTrue != True and specTrue != True and numTrue != True:
            pickList1one = (char1one)
            ranPick1one = (random.choice(pickList1one))
            oneTrue = True


        char1two = (random.choice(lowLet))
        if upperTrue == True:
            char2two = (random.choice(upLet))
        if specTrue == True:
            char3two = (random.choice(specLet))
        if numTrue == True:
            char4two = (random.choice(nummerz))
        
        if upperTrue == True and specTrue == True and numTrue == True:
            pickList4two = (char1two, char2two, char3two, char4two)
            ranPick4two = (random.choice(pickList4two))
            fourTrue = True

        elif upperTrue == True and specTrue == True and numTrue != True:
            pickList3two = (char1two, char2two, char3two)
            ranPick3two = (random.choice(pickList3two))
            threeTrue = True

        elif upperTrue == True and specTrue != True and numTrue != True:
            pickList2two = (char1two, char2two)
            ranPick2two = (random.choice(pickList2two))
            twoTrue = True

        elif upperTrue != True and specTrue != True and numTrue != True:
            pickList1two = (char1two)
            ranPick1two = (random.choice(pickList1two))
            oneTrue = True
        

        char1three = (random.choice(lowLet))
        if upperTrue == True:
            char2three = (random.choice(upLet))
        if specTrue == True:
            char3three = (random.choice(specLet))
        if numTrue == True:
            char4three = (random.choice(nummerz))
        
        if upperTrue == True and specTrue == True and numTrue == True:
            pickList4three = (char1three, char2three, char3three, char4three)
            ranPick4three = (random.choice(pickList4three))
            fourTrue = True

        elif upperTrue == True and specTrue == True and numTrue != True:
            pickList3three = (char1three, char2three, char3three)
            ranPick3three = (random.choice(pickList3three))
            threeTrue = True

        elif upperTrue == True and specTrue != True and numTrue != True:
            pickList2three = (char1three, char2three)
            ranPick2three = (random.choice(pickList2three))
            twoTrue = True

        elif upperTrue != True and specTrue != True and numTrue != True:
            pickList1three = (char1three)
            ranPick1three = (random.choice(pickList1three))
            oneTrue = True


        char1four = (random.choice(lowLet))
        if upperTrue == True:
            char2four = (random.choice(upLet))
        if specTrue == True:
            char3four = (random.choice(specLet))
        if numTrue == True:
            char4four = (random.choice(nummerz))
        
        if upperTrue == True and specTrue == True and numTrue == True:
            pickList4four = (char1four, char2four, char3four, char4four)
            ranPick4four = (random.choice(pickList4four))
            fourTrue = True

        elif upperTrue == True and specTrue == True and numTrue != True:
            pickList3four = (char1four, char2four, char3four)
            ranPick3four = (random.choice(pickList3four))
            threeTrue = True

        elif upperTrue == True and specTrue != True and numTrue != True:
            pickList2four = (char1four, char2four)
            ranPick2four = (random.choice(pickList2four))
            twoTrue = True

        elif upperTrue != True and specTrue != True and numTrue != True:
            pickList1four = (char1four)
            ranPick1four = (random.choice(pickList1four))
            oneTrue = True
        
        if fourTrue == True:
            if runCount < length:
                password1.append(ranPick4one)
                password2.append(ranPick4two)
                password3.append(ranPick4three)
                password4.append(ranPick4four)
                runCount+=1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

        elif threeTrue == True:
            if runCount < length:
                password1.append(ranPick3one)
                password2.append(ranPick3two)
                password3.append(ranPick3three)
                password4.append(ranPick3four)
                runCount+=1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

        elif twoTrue == True:
            if runCount < length:
                password1.append(ranPick2one)
                password2.append(ranPick2two)
                password3.append(ranPick2three)
                password4.append(ranPick2four)
                runCount+=1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

        elif oneTrue == True:
            if runCount < length:
                password1.append(ranPick1one)
                password2.append(ranPick1two)
                password3.append(ranPick1three)
                password4.append(ranPick1four)
                runCount+=1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

ranChar()