import dots_small

def sum_even():
  
  print()
  print("____________________________________________________________________")
  print()
  print("---- Sum of even numbers util a given RANGE ----")
  print()
  n = int(input("Enter the number --->"))
  if (n <= 0):
    print()
    print("Enter a valid number......")
    print()
  else:
    sum = 0
    x = 0
    while (n>0):
      for x in range(0,n+1):
        if (x%2 == 0):
          sum = sum + x
          n = n-2
    print()
    print("The sum of even number till given number is ===>",sum)

    print()
    input("Press enter to continue :")
    dots_small.dots()
    


