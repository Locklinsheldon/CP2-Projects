def EnToMo():
    translate = input("Type what you would like translated, then press enter: ")
    word = list(translate)
def MoToEn():
    translate = input("Type what you would like translated, then press enter: ")

def explode():
    while True:
        print("\nGOODBYE")

def main():
    while True:
        
        print("\nWelcome to the Morse Code Translator™")
        print("\n1. Translate English To Morse Code")
        print("2. Translate Morse Code To English")
        print("3. Quit Program")
        
        ask = input("\nWhat would you like to do?(1-3): ")
        
        if ask == "1":
            EnToMo()
        
        if ask == "2":
            MoToEn()
        
        if ask == "3":
            explode()

main()