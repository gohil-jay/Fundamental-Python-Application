import dots_small

def factor():
    def Factor(n):
        for i in range(1,n+1):
            if n%i == 0:
                print(" ~",i)
            
    print("_________________________________")
    print()
    num = int(input("Enter the number --->"))
    print()
    print("The Factors are as follows ......")
    print()
    Factor(num)

    print("_________________________________")

    print()
    print()
    input("Press enter to continue :")
    dots_small.dots()
