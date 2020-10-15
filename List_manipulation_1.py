import dots_small

def List_manipulation():
    lst=[]

    print("_______________________________________")
    print()
    print("----- LINEAR SEARCH -----")
    print()
    print("This is an empty list ----->",lst)
    print()
    x = int(input("Enter the number of times you want to add things in the list --->"))
    while x > 0:
        print()
        a = input("Enter what you want to add ---->")
        lst.append(a)
        x -= 1
    print("---------------------------------------")
    print()
    print("The new list ---->",lst)
    print()
    print()
    n=input("Enter something to search in this list:")
    i=1
    if n in lst:
        for m in lst:
            if n==m:
                print()
                print("The character is found at",i,"position.")
            i+=1
    else:
        print()
        print("Number not found in list !")

    print()
    input("Press enter to continue :")
    dots_small.dots()
    
