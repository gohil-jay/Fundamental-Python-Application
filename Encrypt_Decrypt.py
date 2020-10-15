import dots_small

def Encrypt_Decrypt():
    v=['a','e','i','o','u']
    nums=['0','1','2','3','4','5','6','7','8','9']
    cons=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    def menu():
        print()
        print('_____________________________________')
        print()
        print("---- CRYPTOGRAPHY ----")
        print()
        print("1.Encrypt a given text")
        print("2.Decrypt a given text")
        print("3.Exit this MENU")
        print()
        print("_____________________________________")
        print()

    def enc(txt):
        ct=''
        for c in txt:
            if c not in ". ,'?":
                if c in v:
                    i=v.index(c)
                    i+=1
                    i%=len(v)
                    ct+=v[i]
                elif c in cons:
                    i=cons.index(c)
                    i+=3
                    i%=len(cons)
                    ct+=cons[i]
                elif c in nums:
                    i=nums.index(c)
                    i-=2
                    ct+=nums[i]
            else:
                ct+='-'
        return ct

    def dec(txt):
        pt=''
        for c in txt:
            if c=='-':
                pt+=' '
            elif c in v:
                i=v.index(c)
                i-=1
                pt+=v[i]
            elif c in cons:
                i=cons.index(c)
                i-=3
                pt+=cons[i]
            elif c in nums:
                i=nums.index(c)
                i+=2
                i%=len(nums)
                pt+=nums[i]

        return pt

    while True:
        menu()
        ch=int(input("Enter choice number:"))
        if ch==1:
            print()
            pt=input("Enter your message:")
            print()
            print ("Encrypted text is ----->",enc(pt))
        elif ch==2:
            print()
            ct=input("Enter the cipher text:")
            print()
            print ("Decrypted message is ---->",dec(ct))
        elif ch==3:
            print()
            print()
            print ("Good bye !")
            break

    print()
    input("Press Enter to continue :")
    dots_small.dots()
