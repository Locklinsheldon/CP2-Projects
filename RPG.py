import random

print("\nWelcome to the Random Password Generator")

length = input("\nHow long does your password need to be?(1-100): ")

askUp = input("\nDo you need uppercase letters in your password?(y/n): ")
if askUp == "y":
    upTrue = True
else:
    upTrue = False

askSpec = input("\nDo you need special characters in your password?(y/n): ")
if askSpec == "y":
    specTrue = True
else:
    specTrue = False

askNum = input("\nDo you need numbers in your password?(y/n): ")
if askNum == "y":
    numTrue = True
else:
    numTrue = False

if upTrue == True and specTrue == True and numTrue == True:
    allTrue = True
if upTrue == True and specTrue == True and numTrue != True:
        threeTrue = True
if upTrue == True and specTrue != True and numTrue != True:
    twoTrue = True
if upTrue != True and specTrue != True and numTrue != True:
    oneTrue = True

runCount = (0)

def main():
    ranChar()   

   
password1 = []
password2 = []
password3 = []
password4 = []



def ranChar():
    lowLet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upLet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specLet = ["!", "@", "#", "$", "%", "&"]
    nummerz = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]    
    
    
    if allTrue == True:
        char4one = (random.choice(lowLet))
        char4two = (random.choice(upLet))
        char4three = (random.choice(specLet))
        char4four = (random.choice(nummerz))
        pickList4 = (char4one, char4two, char4three, char4four)
        ranPick4 = (random.choice(pickList4))
    
    elif threeTrue == True:
        char3one = (random.choice(lowLet))
        char3two = (random.choice(upLet))
        char3three = (random.choice(specLet))
        pickList3 = (char3one, char3two, char3three)
        ranPick3 = (random.choice(pickList3))
    
    elif twoTrue == True:
        char2one = (random.choice(lowLet))
        char2two = (random.choice(upLet))
        pickList2 = (char2one, char2two)
        ranPick2 = (random.choice(pickList2))
    
    elif oneTrue == True:
        char1one = (random.choice(lowLet))
        pickList1 = (char1one)
        ranPick1 = (random.choice(pickList1))

    if allTrue == True:
        if runCount < length:
            password1.append(ranPick4)
            runCount + 1
        else:
            pass

    if threeTrue == True:
        if runCount < length:
            password1.append(ranPick3)
            runCount + 1
        else:
            pass

    if twoTrue == True:
        if runCount < length:
            password1.append(ranPick2)
            runCount + 1
        else:
            pass
    
    if oneTrue == True:
        if runCount < length:
            password1.append(ranPick1)
            runCount + 1
        else:
            pass

ranChar()
