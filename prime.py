import dots_small

def prime():
   def Prime(n):
      if n>1:
         for i in range (2,n):
            if (n%i)==0:
               print()
               print("It's not a prime number.")
               break
         else:
            print()
            print("It's a prime number.")
            
   print("_____________________________________________")
   print()
   num=int(input("Enter the number you want check for prime ------>"))
   Prime(num)
   print()
   print("_____________________________________________")

   print()
   input("Press enter to continue :")
   dots_small.dots()
