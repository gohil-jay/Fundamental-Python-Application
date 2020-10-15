import dots_small

def special_series():

    def Mersenne(n):
        return ((2**n)-1)

    def primetest(n):
        if n>1:
         for i in range (2,n):
            if (n%i)==0:
               return False
         else:
            return True
            
    print()
    print("__________________________________")
    print()
    print("---- Mersenne Prime Series ----")
    print()
    print()
    x = int(input("Enter until which you want the series -->"))
    print()
    print("The Series ==>")
    print()
    for a in range(1,x+1):
        num = Mersenne(a)
        prime = primetest(num)
        if prime:
            print(num,"     [PRIME]")
        else:
            print(num)

    print()
    input("Press enter to continue :")
    dots_small.dots()
