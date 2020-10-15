import dots_small

def special_series():

    print()
    print("__________________________________")
    print()
    print("---- Special Series #4 ----")
    print()
    print()
    x = int(input("Enter the value of 'X' --->"))
    print()
    n = int(input("Enter until which you want the series -->"))
    print()
    s = 0
    for a in range(n):
        s += (x**a)

    print("The sum of the first",n,"terms is ===>",s)
    print()
    print("_________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
        
        
