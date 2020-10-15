import dots_small

def SPECIAL_SERIES():
    
    import special_series_1
    import special_series_2
    import special_series_3
    import special_series_4

    def menu():
        print()
        print("______________________________________")
        print()
        print("--- SPECIAL SERIES ----")
        print()
        print("Lets run some freaky Special Series... :")
        print()
        print("1. Fibonacci Seiries [0,1,1,2,3,5,......]")
        print("2. Mersenne Series [of form (2**n - 1)]")
        print("3. Mersenne Prime Series")
        print("4. Series of the form [1 + x + (x**2) + ...]")
        print("5. Exit this MENU")
        print()
        print("_____________________________________")
        print()

    while True:
        menu()
        print()
        ch = int(input("Enter your choice --->"))
        if ch == 1:
            special_series_1.special_series()
        elif ch == 2:
            special_series_2.special_series()
        elif ch == 3:
            special_series_3.special_series()
        elif ch == 4:
            special_series_4.special_series()
        elif ch == 5:
            print()
            print("Aborting.....")
            print(".")
            print(".")
            print(".")
            print(".")
            break
        else:
            print("Invalid key.")
            print()
    print()
    print("-------------------------")
    print()
    print("Program over")

    print()
    input("Press enter to continue :")
    dots_small.dots()
