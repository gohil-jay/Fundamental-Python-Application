import dots_small

def Table():
    def table(n):
        i=0
        print()
        x = int(input("Enter the range till you want the NUMBER TABLE -->"))
        while i<=x:
            print(n,i,n*i)
            print("---------")
            i+=1
    print("_____________________________________________")
    print()
    num=int(input('Enter the number you want Table of ------>:'))
    table(num)
    print('_____________________________________________')

    print()
    input("Press enter to continue :")
    dots_small.dots()
