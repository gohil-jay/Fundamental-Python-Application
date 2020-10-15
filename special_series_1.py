import dots_small

def special_series():
    print()
    print("__________________________________________")
    print()
    print("---- FIBONACCI SERIES ----")
    print()
    x = int(input("Enter till where you want to print the Fibonacci series --->"))
    print()
    print("The series ===>")
    print()
    first = 0
    second = 1
    print(" ~",first)
    print(" ~",second)
    for a in range(1,x-1):
        third = first + second
        print(" ~",third)
        first,second = second,third

    print()
    print("Program Over !!!")
    print()
    print("________________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
