import dots_small

def List_manipulation():
    print()
    print("_______________________________________________________________________")
    print()
    n = int(input("Enter how many times you wanna add the numbers -->"))
    print()
    b = []
    for i in range(0,n):
        x = int(input("Enter the number --->"))
        b.append(x)
    c = []
    d = []
    for i in b:
        if (i%2 == 0):
            c.append(i)
        else:
            d.append(i)
    c.sort()
    d.sort()
    count1 = 0
    count2 = 0
    for k in c:
        count1 +=1
    for j in d:
        count2 += 1


    print()
    print("Largest even number in the list is :",c[count1-1])
    print()
    print("Largest odd number in the list is :",d[count2-1])

    print()
    input("Press enter to continue :")
    dots_small.dots()
    
    
              
            
