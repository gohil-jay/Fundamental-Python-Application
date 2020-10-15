def STRING_MANIPULATION():

    import String_manipulation_1
    import String_manipulation_2
    import String_manipulation_3
    import String_manipulation_4
    import dots_small

    def menu():
        print()
        print("______________________________________")
        print()
        print("--- STRING MANIPULATION ----")
        print()
        print("Lets run some freaky types of str manipulation as follow :")
        print()
        print("1. To print [vowels],[uppercase letters],[lowercase letters],[other] in a given STRING.")
        print("2. To the number of times a word appears in a given STRING.")
        print("3. To manipulate the String and perform its Capital , Small and Title Conversion.")
        print("4. To find the number of times an entered substring appears in given string")
        print("5. Exit this MENU")
        print()
        print("_____________________________________")
        print()

    while True:
        menu()
        print()
        ch = int(input("Enter your choice --->"))
        if ch == 1:
            String_manipulation_1.String_manipulation()
        elif ch == 2:
            String_manipulation_2.String_manipulation()
        elif ch == 3:
            String_manipulation_3.String_manipulation()
        elif ch == 4:
            String_manipulation_4.String_manipulation()
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
                  
