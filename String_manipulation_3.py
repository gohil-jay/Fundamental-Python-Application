import dots_small

def String_manipulation():
    def menu():
        print()
        print("______________________________")
        print()
        print("---- String Manipulation ----")
        print()
        print("1. Capital conversion")
        print("2. Small coversion")
        print("3. Title conversion [Capitalise the first word]")
        print("4. Exit")
        print()
        print("______________________________")
        print()

    while True:
        menu()
        ch = int(input("Enter your choice -->"))
        if ch == 1:
            print()
            s = input("Enter the string to be manipulated --->")
            print()
            print("Upper conversion is ===>",s.upper())
        elif ch == 2:
            print()
            s = input("Enter the string to be manipulated --->")
            print()
            print("Small conversion is ===>",s.lower())
        elif ch ==3:
            print()
            s = input("Enter the string to be manipulated --->")
            print()
            print("Title conversion is ===>",s.title())
        elif ch == 4:
            print()
            print("Aborting ......")
            print(".")
            print(".")
            print(".")
            print(".")
            break
        else:
            print()
            print("Invalid key.")
            print()

    print()
    input("Press enter to continue :")
    dots_small.dots()
                
