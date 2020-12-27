def BIG():
    
    import areas
    import STRING_MANIPULATION
    import sps_game
    import task_management
    import SIMPLE_CODES
    import Encrypt_Decrypt
    import LIST_MANIPULATION
    import SPECIAL_SERIES
    import Student_Records
    import BYE
    import dots_verysmall
    import calc

    def menu():
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("HI THERE,")
        print("Let's run some programes---->")
        print()
        print("1. Basic Programes")
        print('2. Stone-Paper-Scissor Game')
        print("3. Task Management")
        print("4. Student Details [Storage and Manipulation]")
        print("5. String Manipulation (s)")
        print("6. Special Series")
        print("7. Encryption and Decryption")
        print("8. List Manipulation")
        print("9. Areas of different shapes")
        print("10. Maths Calulator")
        print("11. Exit")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        menu()
        print()
        ch=int(input('Enter your choice:'))
        print()
        dots_verysmall.dots()
        if ch==1:
            print()
            SIMPLE_CODES.simple_codes()
        elif ch==2:
            print()
            sps_game.Stone_Paper_Scissor_Game()
        elif ch==3:
            print()
            task_management.task_management()
        elif ch == 4:
            print()
            Student_Records.Student_Records()
        elif ch==5:
            print()
            STRING_MANIPULATION.STRING_MANIPULATION()
        elif ch==6:
            print()
            SPECIAL_SERIES.SPECIAL_SERIES()
        elif ch == 7:
            Encrypt_Decrypt.Encrypt_Decrypt()
        elif ch == 8:
            LIST_MANIPULATION.LIST_MANIPULATION()
        elif ch == 9:
            print()
            areas.areas()
        elif ch == 10:
            calc.stcalc()
        elif ch == 11:
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print("  OKAY THEN , ....")

            BYE.BYE()
            
            break
        
        else:
            print()
            print("Enter a valid number....")
            print()
            print()
