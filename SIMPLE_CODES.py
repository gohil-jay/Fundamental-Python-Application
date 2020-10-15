
def simple_codes():
    import PALINDROME
    import add_digit
    import Armstrong
    import Odd_Even
    import prime
    import Table
    import sum_even
    import factor
    import factorial
    import reverse
    import prime_in_range
    import Pangram
    import sum_odd

    def menu():
        print("--------------------------------------------")
        print()
        print("Let's run some simple programes---->")
        print()
        print('1. Palindrome')
        print("2. Pangram")
        print('3. Add Digits of a number')
        print('4. Armstrong')
        print('5. Odd_Even')
        print('6. Prime')
        print('7. Number Table')
        print('8. Sum of even numbers until given Number')
        print("9. Sum of odd numbers until given Number")
        print("10. Factors of a given number")
        print('11. Factorial of a given number')
        print("12. Reverse of a given number")
        print("13. Prime numbers upto a given range")
        print("14. Exit this MENU")
        print("--------------------------------------------")

    while True:
        menu()
        print()
        ch=int(input('Enter your choice:'))
        if ch==1:
            print()
            PALINDROME.PALINDROME()
        elif ch == 2:
            print()
            Pangram.Pangram()
        elif ch==3:
            print()
            add_digit.add_digit()
        elif ch==4:
            print()
            Armstrong.Armstrong()
        elif ch==5:
            print()
            Odd_Even.Odd_Even()
        elif ch==6:
            print()
            prime.prime()
        elif ch == 7:
            print()
            Table.Table()
        elif ch == 8:
            print()
            sum_even.sum_even()
        elif ch == 9:
            print()
            sum_odd.sum_odd()
        elif ch == 10:
            print()
            factor.factor()
        elif ch == 11:
            print()
            factorial.factorial()
        elif ch == 12:
            print()
            reverse.reverse()
        elif ch == 13:
            print()
            prime_in_range.prime_in_range()
        elif ch==14:
            print("Aborting..........")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            break
        else:
            print("Enter a valid number....")
