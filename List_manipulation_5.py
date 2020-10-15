import dots_small

def List_manipulation():

    print()
    print("_____________________________________")
    print()
    print("---- Computation of substring in the given string ----")
    print()
    print()
    string = input("Enter the string --->")
    print()
    word = input("Enter the substring -->")
    print()
    a = []
    count = 0
    a = string.split()
    for i in range(0,len(a)):
        if (word == a[i]):
            count += 1

    print("The number of times the entered string appears is ===>",count)
    print()
    print("______________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()


    
