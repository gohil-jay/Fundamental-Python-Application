def Armstrong():

    import dots_small
    
    def armstrong():
        print("_____________________________________________")
        print()
        n = int(input("Enter the number to check if it's an Armstrong---->:"))
        temp = n
        s=0
        while n>0:
            d = n%10
            s += d**3
            n //= 10

        if  temp == s:
            print()
            print("Its an armstrong number !!!!!!!!")
            print()
        else:
            print()
            print("Its not an armstrong number !!")
            print()
        print("_____________________________________________")
        print()
        input("Press enter to continue :")
        dots_small.dots()

    armstrong()
