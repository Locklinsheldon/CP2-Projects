# Locklin Sheldon, Financial Calculator

# This is the financial calculator program

def main(): #Main menu for selecting options
    while True:
        print("\nFinancial Calculator:\n") #Title
        print("1. Save for a Goal")
        print("2. Interest Calculator")
        print("3. Budget Allocator (Recommended to do first)")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        
        choice = input("\nPick (1-5): ")#User choice
        
        if choice == '1':
            SFG()
        elif choice == '2':
            CIC()
        elif choice == '3':
            BA()
        elif choice == '4':
            SPC()
        elif choice == '5':
            TC()
        else:
            print("Bro duznt no how too tipe. Retri, sily guse.")#Tells the user if they mispelled or put in invalid characters

def SFG(): #Save for goal function
    goal = float(input("Your monthly savings goal: "))
    deposit = float(input("Amount you save each week: "))
    
    timeUntil = goal / deposit
    print("It'll take you", timeUntil, "weeks to save for your goal.")#Tells user when they will have reached their goal

def CIC(): #Compound interest calculator function
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Annual interest rate (in %): ")) / 100
    timesCompounded = int(input("Number of times te interest is compounded per year: "))
    years = int(input("Number of years: "))
    
    amount = principal * (1 + rate / timesCompounded) ** (timesCompounded * years)#Algorithm for finding compound interest
    print("The amount after", years, "years will be: $", amount) 

def BA(): #Budget allocator function
    mond = float(input("How much do you earn weekly: "))
    aloeneeds = mond * 0.50
    aloewants = mond * 0.30
    aloesave = mond * 0.20
    print("You should spend $", aloeneeds, "on needs, $", aloewants, "on wants, and you should deposit $", aloesave, "into your savings account.") #Tells the user what they should spend their money on

def SPC(): #Sale price calculator function
    ogPrice = float(input("Original price: $"))
    disPerc = float(input("Discount percentage (without percent sign): ")) / 100
    salePrice = ogPrice * (1 - disPerc)
    print("The sale price is: $", salePrice)#Tells the user the new sale price after discounts

def TC(): #Tip calculator function
    billAm = float(input("Enter the bill amount: $"))
    tipPerc = float(input("Enter the tip percentage (without percent sign): ")) / 100 #Finds tip percentage
    tipAm = billAm * tipPerc
    print("The tip amount is: $", tipAm)#Tells the user how much the tip is

main()
