def LIST_MANIPULATION():

    import List_manipulation_1
    import List_manipulation_2
    import List_manipulation_3
    import List_manipulation_4
    import List_manipulation_5
    import List_manipulation_6
    import dots_small


    def menu():
        print()
        print("______________________________________")
        print()
        print("--- LIST MANIPULATION ----")
        print()
        print("Lets run some list manipulation programs :")
        print()
        print("1. Linear List search.")
        print("2. Print the largest odd and even number in entered list.")
        print("3. Print the number of times a particular number occurs in an entered list")
        print("4. To input two lists and then sort them [and print it]")
        print("5. To count the number of times the enterd sub-string appears in the entered string.")
        print("6. Print all the possible combination of four entered numbers.")
        print("7. Exit this MENU")
        print()
        print("_____________________________________")
        print()

    while True:
        menu()
        print()
        ch = int(input("Enter your choice --->"))
        if ch == 1:
            List_manipulation_1.List_manipulation()
        elif ch == 2:
            List_manipulation_2.List_manipulation()
        elif ch == 3:
            List_manipulation_3.List_manipulation()
        elif ch == 4:
            List_manipulation_4.List_manipulation()
        elif ch == 5:
            List_manipulation_5.List_manipulation()
        elif ch == 6:
            List_manipulation_6.List_manipulation()
        elif ch == 7:
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

    

    
