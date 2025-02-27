import random #imports random

print("\nWelcome to the Random Password Generator")

def ranChar(): #function for creating random characters
    length = int(input("\nHow long does your password need to be?: ")) #length variable
    
    upper = input("\nDo you need upper case letters in your password?(y/n): ") #variable determining whether or not they want upper case letters
    if upper == "y":
        upperTrue = True
    elif upper == "n":
        upperTrue = False
    else:
        print("That's not an option")
        return
    
    special = input("\nDo you need special characters in your password?(y/n): ") #variable determining whether or not they want special characters
    if special == "y":
        specTrue = True
    elif special == "n":
        specTrue = False
    else:
        print("That's not an option")
        return

    numbers = input("\nDo you need numbers in your password?(y/n): ") #variable determining whether or not they want numbers 
    if numbers == "y":
        numTrue = True
    elif numbers == "n":
        numTrue = False
    else:
        print("That's not an option")
        return
    
    print("Here are a few passwords you can use:")

    password1 = [] #variables for the 4 passwords
    password2 = []
    password3 = []
    password4 = []
    lowLet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #variables for all of the characters
    upLet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specLet = ["!", "@", "#", "$", "%", "&"]
    nummerz = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]    
    rc = 0 #sets the initial number of times run to 0
    runCount = rc
    fourTrue = threeTrue = twoTrue = oneTrue = False #sets the variables

    while runCount < length: #Reccurs while the run count is less than the chosen length
        char1one = random.choice(lowLet) #randomly selects characters
        if upperTrue:
            char2one = random.choice(upLet)
        if specTrue:
            char3one = random.choice(specLet)
        if numTrue:
            char4one = random.choice(nummerz)
        
        if upperTrue and specTrue and numTrue:
            pickList4one = (char1one, char2one, char3one, char4one)
            ranPick4one = random.choice(pickList4one)
            fourTrue = True

        elif upperTrue and specTrue and not numTrue:
            pickList3one = (char1one, char2one, char3one)
            ranPick3one = random.choice(pickList3one)
            threeTrue = True

        elif upperTrue and not specTrue and not numTrue:
            pickList2one = (char1one, char2one)
            ranPick2one = random.choice(pickList2one)
            twoTrue = True

        elif not upperTrue and not specTrue and not numTrue:
            pickList1one = (char1one)
            ranPick1one = random.choice(pickList1one)
            oneTrue = True

        char1two = random.choice(lowLet)
        if upperTrue:
            char2two = random.choice(upLet)
        if specTrue:
            char3two = random.choice(specLet)
        if numTrue:
            char4two = random.choice(nummerz)
        
        if upperTrue and specTrue and numTrue:
            pickList4two = (char1two, char2two, char3two, char4two)
            ranPick4two = random.choice(pickList4two)
            fourTrue = True

        elif upperTrue and specTrue and not numTrue:
            pickList3two = (char1two, char2two, char3two)
            ranPick3two = random.choice(pickList3two)
            threeTrue = True

        elif upperTrue and not specTrue and not numTrue:
            pickList2two = (char1two, char2two)
            ranPick2two = random.choice(pickList2two)
            twoTrue = True

        elif not upperTrue and not specTrue and not numTrue:
            pickList1two = (char1two)
            ranPick1two = random.choice(pickList1two)
            oneTrue = True

        char1three = random.choice(lowLet)
        if upperTrue:
            char2three = random.choice(upLet)
        if specTrue:
            char3three = random.choice(specLet)
        if numTrue:
            char4three = random.choice(nummerz)
        
        if upperTrue and specTrue and numTrue:
            pickList4three = (char1three, char2three, char3three, char4three)
            ranPick4three = random.choice(pickList4three)
            fourTrue = True

        elif upperTrue and specTrue and not numTrue:
            pickList3three = (char1three, char2three, char3three)
            ranPick3three = random.choice(pickList3three)
            threeTrue = True

        elif upperTrue and not specTrue and not numTrue:
            pickList2three = (char1three, char2three)
            ranPick2three = random.choice(pickList2three)
            twoTrue = True

        elif not upperTrue and not specTrue and not numTrue:
            pickList1three = (char1three)
            ranPick1three = random.choice(pickList1three)
            oneTrue = True

        char1four = random.choice(lowLet)
        if upperTrue:
            char2four = random.choice(upLet)
        if specTrue:
            char3four = random.choice(specLet)
        if numTrue:
            char4four = random.choice(nummerz)
        
        if upperTrue and specTrue and numTrue:
            pickList4four = (char1four, char2four, char3four, char4four)
            ranPick4four = random.choice(pickList4four)
            fourTrue = True

        elif upperTrue and specTrue and not numTrue:
            pickList3four = (char1four, char2four, char3four)
            ranPick3four = random.choice(pickList3four)
            threeTrue = True

        elif upperTrue and not specTrue and not numTrue:
            pickList2four = (char1four, char2four)
            ranPick2four = random.choice(pickList2four)
            twoTrue = True

        elif not upperTrue and not specTrue and not numTrue:
            pickList1four = (char1four)
            ranPick1four = random.choice(pickList1four)
            oneTrue = True

        if fourTrue:
            if runCount < length:
                password1.append(ranPick4one) #adds the characters to the passwords
                password2.append(ranPick4two)
                password3.append(ranPick4three)
                password4.append(ranPick4four)
                runCount += 1 #adds 1 to the run count
                if runCount == length:
                    print("") #puts space between the passwords
                    print("".join(password1)) #joins the password characters together to make them more appealing :(
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

        elif threeTrue:
            if runCount < length:
                password1.append(ranPick3one)
                password2.append(ranPick3two)
                password3.append(ranPick3three)
                password4.append(ranPick3four)
                runCount += 1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

        elif twoTrue:
            if runCount < length:
                password1.append(ranPick2one)
                password2.append(ranPick2two)
                password3.append(ranPick2three)
                password4.append(ranPick2four)
                runCount += 1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

        elif oneTrue:
            if runCount < length:
                password1.append(ranPick1one)
                password2.append(ranPick1two)
                password3.append(ranPick1three)
                password4.append(ranPick1four)
                runCount += 1
                if runCount == length:
                    print("")
                    print("".join(password1))
                    print("".join(password2))
                    print("".join(password3))
                    print("".join(password4))

ranChar() #runs the function
