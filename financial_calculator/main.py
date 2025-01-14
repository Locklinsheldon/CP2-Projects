# Locklin Sheldon, Financial Calculator

# This is the financial calculator program

def main():
    while True:
        print("\nFinancial Calculator:\n")
        print("1. Save for a Goal")
        print("2. Interest Calculator")
        print("3. Budget Allocator (Recommended to do first)")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        
        choice = input("\nPick (1-5): ")
        
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
            print("Invalid input. Try again.")

def SFG():
    goal = float(input("Your monthly savings goal: "))
    deposit = float(input("Amount you save each week: "))
    
    timeUntil = goal / deposit
    print("It'll take you", timeUntil, "weeks to save for your goal.")

def CIC():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Annual interest rate (in %): ")) / 100
    timesCompounded = int(input("Number of times te interest is compounded per year: "))
    years = int(input("Number of years: "))
    
    amount = principal * (1 + rate / timesCompounded) ** (timesCompounded * years)
    print("The amount after", years, "years will be: $", amount)

def BA():
    mond = float(input("How much do you earn weekly: "))
    aloeneeds = mond * 0.50
    aloewants = mond * 0.30
    aloesave = mond * 0.20
    print("You should spend $", aloeneeds, "on needs, $", aloewants, "on wants, and you should deposit $", aloesave, "into your savings account.")

def SPC():
    ogPrice = float(input("Enter the original price: $"))
    disPerc = float(input("Enter the discount percentage (without percent sign): ")) / 100
    salePrice = ogPrice * (1 - disPerc)
    print("The sale price is: $", salePrice)

def TC():
    billAm = float(input("Enter the bill amount: $"))
    tipPerc = float(input("Enter the tip percentage (without percent sign): ")) / 100
    tipAm = billAm * tipPerc
    totAm = billAm + tipAm
    print("The tip amount is: $", tipAm)
    print("The total amount to be paid is: $", totAm)

main()
