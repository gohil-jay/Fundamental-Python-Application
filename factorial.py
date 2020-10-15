import dots_small

def factorial():
    
    def Factorial(n):
        x = 1
        for i in range(n,1,-1):
            x *= i

        print(x)
        
    print("___________________________________")
    print()
    num = int(input("Enter the number for factorial to be calculated --->"))
    print()
    print("The factorial of ",num,"is ........")
    print(".")
    print(".")
    print(".")
    print(".")
    Factorial(num)

    print()
    input("Press enter to continue :")
    dots_small.dots()
