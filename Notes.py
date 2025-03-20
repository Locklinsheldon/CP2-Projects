#1. What is a helper function?
    #A function written to be called in another function

def is_int(user_input):
    try:
        int(user_input)
    except:
        print("Please give me a number")
    else:
        return int(user_input)

def age():
    old = is_int(input("How old are you?\n"))

    print(f"Cool. You are {old}")

#2. What is the purpose of a helper function?
    #To be used in another function

#3. What is an inner function?
    #A function that exists inside of another function

def add(a):
    b = int(input("Give me a number: "))

    def additon():
        print(a+b)
    additon()

#add(3)

#4. What is the scope of a variable in a function WITH an inner function?
    #Variable in functionbecomes local to the inner function

#5. Why do we use inner functions?
    #For decomposition inside functions

#6. What is a closer function?
    #Closure functions allows a function to remember and access values from multiple calls

#7. Why do we write closure functions?
    #To remember values from multiple calls

#8. What is recursion?
    #When you call a function inside of itself