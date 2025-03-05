# Locklin Sheldon, Financial Calculator

#this is the financial calculator program

import random

def main():
    
    goal = input("What is you goal to save for by the end of the year?: ")
    Rizz()

def Rizz():
    mond = float(input("How much do you earn monthly?: "))
    rate = 1.03
    ratex = rate
    aloeneeds = mond*5/10
    aloewants = mond*3/10
    aloesave = mond*2/10
    print("You should spend", int(aloeneeds), "on needs,", int(aloewants), "on wants, and you should deposit", int(aloesave), "into your savings account. Your current interest rate is", rate, "" )

main()

def yearate():
    mo1 = aloesave