import dots_small

def special_series():
    print()
    print("__________________________________________")
    print()
    print("---- BERSENNE SERIES ----")
    print()
    x = int(input("Enter till where you want to print the Bersenne series --->"))
    print()
    print("The series ===>")
    print()
    n = 1
    for a in range(0,x):
        print(" ~",((2**n)-1))
        n += 1

    print()
    print("Program Over !!!")
    print()
    print("________________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
