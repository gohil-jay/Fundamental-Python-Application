import dots_small

def String_manipulation():
    uc = lc = v = c = o = 0
    print("_____________________________________")
    print()
    s = input("Enter the string to be manipulated ---->")
    print()
    l = len(s)
    for ch in s:
        if (ch.isupper()):
            uc += 1
            if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'U' or ch == 'O':
                v += 1
            else:
                c += 1
        elif (ch.islower()):
            lc += 1
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                v += 1
            else:
                c += 1
        else:
            o += 1
    print("_____________________________________")
    print()
    print("Total characters =",l)
    print()
    print("Total upper case =",uc)
    print()
    print("Total lower case =",lc)
    print()
    print("Total vowels =",v)
    print()
    print("Total others =",o)
    print()
    print("_____________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()



    
