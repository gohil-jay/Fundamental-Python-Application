import dots_small

def reverse():
    def Reverse(n):
        r = 0
        while n>0:
            d = n%10
            r = r*10+d
            n //= 10

        print(r)
    print("_____________________________")
    print()
    num = int(input("Enter the number to be reversed --->"))
    print()
    print("Reverse of ",num,"is .....")
    print(".")
    print(".")
    print(".")
    print(".")
    Reverse(num)
    print()
    print("_____________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
