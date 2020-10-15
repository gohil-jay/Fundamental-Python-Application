import __ME__
import welcome
import dots_small
import skull
import dots_large
import gap

sid = '#comp.python'
pw = '#ididit'
def login():
    print()
    gap.gap()
    print()
    print("Give your identity ======>")
    print()
    wid = input("Enter the USER ID --->")
    if sid == wid:
        print()
        password = input("Enter the password --->")
        if pw == password:
            print()
            print("Welcome !!!")
            print()
            print("You are successfully logged in !!!!")
            print()
            print("Let's Start .....")
            print()
            print()
            input("Press Enter to continue :")
            print()
            
            dots_small.dots()
            welcome.welcome()
            __ME__.BIG()
            
            print()
            print()
            
            gap.gap()
            
        else:
            dots_large.dots()
            skull.skull()

    else:
        print()
        password = input("Enter the password --->")
        print()
        dots_large.dots()
        skull.skull()

login()
            
