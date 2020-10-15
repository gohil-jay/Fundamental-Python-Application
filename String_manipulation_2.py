import dots_small

def String_manipulation():
    F = {}
    print()
    print("_____________________________________")
    print()
    s = input("Enter the string --->")
    for c in s:
        if c in F:
            F[c] += 1
        else:
            F[c] = 1
    for k in F:
        print()
        print("~The character ",k,"appeared",F[k],"times.")
    print()
    print("_____________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
