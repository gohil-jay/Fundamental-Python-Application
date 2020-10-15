import mymodule
import dots_small

def areas():
    def menu():
        print()
        print("Welcome Again....")
        print("The choices provided are to calculate the area of the following shapes---->")
        print()
        print('1. Square.')
        print('2. Circle.')
        print('3. Rectangle.')
        print('4. Triangle.')
        print('5. Exit this MENU.')
        print()
        print()

    while True:
        menu()
        print("----------------------------------------------")
        print()
        ch=int(input('Enter your choice:'))
        if ch==1:
            print()
            s=int(input('Enter the measurment of side --->'))
            print()
            print('The area of square is ===>',mymodule.areaS(s))
        elif ch==2:
            print()
            r=int(input('Enter the measurement of radius --->'))
            print()
            print('The area of circle is ===>',mymodule.areaC(r))
        elif ch==3:
            print()
            l=int(input('Enter the measurement of length of the rectangle ---->'))
            print()
            b=int(input('Enter the measurement of breadth of the rectangle ---->'))
            print()
            print('The area of rectangle is ===>',mymodule.areaR(l,b))
        elif ch==4:
            print()
            x=int(input('Enter the measurement of SIDE 1 of the triangle --->'))
            print()
            y=int(input('Enter the measurement of SUDE 2 of the triangle --->'))
            print()
            z=int(input('Enter the measurement of SUDE 3 of the triangle --->'))
            print()
            print('The area of  triangle is ===>',mymodule.areaT(x,y,z))
        elif ch==5:
            print("Aborting..........")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            break
        
        print()
        print("----------------------------------------------")
        print()
        input("Press enter to continue :")
        dots_small.dots()
        
    
