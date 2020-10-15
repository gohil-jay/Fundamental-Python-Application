import dots_small

def prime_in_range():
    print()
    print("________________________________________________________")
    print()
    print("--- Prime numbers upto a given range ----")
    print()
    r = int(input("Enter the upper limit [starting from 1] --->"))
    print()
    print("The prime number unti",r,"are as follows :")
    for a in range(2,r+1):
        k = 0
        for i in range(2,a//2+1):
            if (a%i == 0):
                k = k+1
        if (k <= 0):
            print("===>",a)

    print()
    input("Press enter to continue :")
    dots_small.dots()
