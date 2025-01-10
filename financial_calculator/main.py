# Locklin Sheldon, Financial Calculator

#this is the financial calculator program



def main():
    
    goal = input("What is you goal to save for by the end of the year?: ")
    Rizz()

def Rizz():
    mond = input("How much do you earn monthly?: ")
    aloeneeds = mond*5/10
    aloewants = mond*3/10
    aloesave = mond*2/10
    print("You should spend", aloeneeds, "on needs,", aloewants, "on wants, and you should deposit", aloesave, "into your savings account.")

main()