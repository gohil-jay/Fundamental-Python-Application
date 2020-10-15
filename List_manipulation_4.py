import dots_small

def List_manipulation():
    a=[]
    c=[]
    print()
    print("___________________________")
    print()
    n1 = int(input("Enter the number of elements to be put in list 1 --->"))
    for i in range(1,n1+1):
        print()
        b = input("Enter the element --->")
        a.append(b)

    print() 
    n2 = int(input("Enter the number of elements to be put in list 2 --->"))
    for i in range(1,n2+1):
        print()
        d = input("Enter the element --->")
        c.append(d)

    new = a + c
    new.sort()
    print()
    print("The sorted list is ===>",new)

    print()
    input("Press enter to continue :")
    dots_small.dots()
