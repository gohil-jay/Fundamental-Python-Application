def Number_Conversion():

    import dots_small
    import math

    def menu():

        print()
        print("---- Number System Conversion ----")
        print()
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Octal to Decimal")
        print("4. Decimal to octal")
        print("5. Hexadecimal to Decimal")
        print("6. Decimal to Hexadecimal")
        print("7. exit")

    while True:

        print()
        menu()
        print()
        ch = int(input("Enter your choice :"))
        print()

        if ch == 1:
            print()
            b = int(input("Enter a binary number :"))
            print()
            t = b
            m = 1
            dec = 0
            while (t > 0):
                d = t%10
                dec += m*d
                m *= 2
                t //= 10

            print("The conversion of",b,"is",dec)
            print()
            input("Press Enter to continue :")

        elif ch == 2:

            print()
            dec = int(input("Enter a decimal number :"))
            print()
            t = dec
            b = ""
            while (t > 0):
                r = (t%2)
                b = str(r) + b
                t //= 2

            print("The conversion of",dec,"is",b)
            print()
            input("Press Enter to continue :")

        elif ch == 3:

            print()
            octal = int(input("Enter an octal number :"))
            print()
            t = octal
            i = 1
            dec = 0
            while ((octal!) > 0):
                r = octal%10
                octal /= 10
                dec += r*i
                i *= 8

            print("The conversion of",t,"is",dec)
            print()
            input("Press Enter to continue :")

        elif ch == 4:

            print()
            dec = int(input("Enter a deciaml number :"))
            print()
            t = dec
            i = 1
            octal = 0
            while ((math.factorial(dec)) > 0):

                r = dec%8
                dec /= 8
                octal += r*i
                i *= 10

            print("The conversion of",t,"is",octal)
            print()
            input("Press Enter to continue :")

        elif ch == 5:

            a = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
            print()
            h = input("Enter a hexadecimal number :")
            print()
            dec = 0
            k = 0
            for i in range(-1,-len(h)-1,-1):
                l = h[i]
                if l in a:
                    dec += a[l]
                else:
                    dec += (int(l)*(16**k))
                k += 1

            print("The conversion of",h,"is",dec)
            print()
            input("Press Enter to continue :")

        elif ch == 6:

            d = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
            print()
            dec = int(input("Enter a hexadecimal number :"))
            print()
            hx = ""
            t = dec
            while (t>0):
                a = (t%16)
                if (a<10):
                    hx = str(a) + hx
                else:
                    hx = d[a] + hx
                    t //= 16

            print("The conversion of",dec,"is",hx)
            print()
            input("Press Enter to continue :")

        elif ch == 7:
            print()
            print("Aborting ....")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            break

    dots_small.dots()

Number_Conversion()
    
        

            
            
        
