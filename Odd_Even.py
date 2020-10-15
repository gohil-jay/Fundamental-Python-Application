import dots_small

def Odd_Even():
    def check(n):
        if n%2==0:
            return True
        else:
            return False
    print('_____________________________________________')
    print()
    print('Welcome Again!!!!!!!!!!')
    print()
    print('Enter the number you want to check whether is even or odd......')
    print()
    num=int(input('Enter the number ----> :'))
    if check(num):
        print()
        print(num,'is an even number.')
    else:
        print()
        print(num,'is an odd number.')
    print("_____________________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
