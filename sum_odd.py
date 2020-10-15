import dots_small

def sum_odd():

    print()
    print("__________________________________________________")
    print()
    print("---- Sum of odd numbers util a given RANGE ----")
    print()
    n = int(input("Enter the range --->"))
    print()

    sum = 0
    i = 1
    
    while i <= n:
        sum += i
        i += 2

    print("The sum is ====>",sum)

    print("__________________________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
