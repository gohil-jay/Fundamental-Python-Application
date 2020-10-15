import dots_small

def List_manipulation():
    print()
    print("_________________________________")
    print()
    print("---- All possible combination of three entered numbers ----")
    print()
    print()
    a = int(input("Enter the first number --->"))
    print()
    b = int(input("Enter the second number --->"))
    print()
    c = int(input("Enter the third number --->"))
    print()
    e = int(input("Enter the fourth number ---->"))
    print()
    d = []
    d.append(a)
    d.append(b)
    d.append(c)
    d.append(e)
    print("All the possible combinations are ===>")
    print()
    for i in range(0,4):
        for j in range(0,4):
            for k in range(0,4):
                for m in range(0,4):
                    if (i!=j and j!=k and k!=i):
                        print(" ~",d[i],d[j],d[k],d[m])

    print()
    print("__________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
