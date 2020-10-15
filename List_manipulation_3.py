import dots_small

def List_manipulation():
    a = []
    print("__________________________________")
    print()
    print("Let's check how many times your entered number appaears in the list.")
    print()
    print("Here's the list -->",a)
    print()
    print("----------")
    n=int(input("Enter how many times you wanna add the number :"))
    print("----------")
    for i in range(1,n+1):
        print()
        b = int(input("Enter the number you want to add in the list :"))
        a.append(b)
    k = 0
    print()
    num = int(input("Enter the number to be counted --->"))

    for j in a:
        if (j == num):
            k += 1
    print()
    print("The number of times",num,"appears in the list is ===>",k)

    print()
    input("Press enter to continue :")
    dots_small.dots()
