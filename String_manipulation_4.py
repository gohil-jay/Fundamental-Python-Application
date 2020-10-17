import dots_small

def String_manipulation():
    print()
    print("_________________________________________________")
    print()
    print("Let's check how many times the substring occurs in the given string !... ")
    print()
    string = input("Enter the STRING --->")
    print()
    sub = input("Enter the substring ---->")
    print()
    string_size=len(string)
    substring_size=len(sub)
    count=0
    for i in range(0,string_size-substring_size+1):
        if string[i:i+substring_size] == sub:
            count += 1
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("The number of times the entered string appears is :",count)

    print()
    input("Press enter to continue :")
    dots_small.dots()
