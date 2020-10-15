def add_digit():

    import dots_small
    while True:
        print("________________________________________________")
        print()
        print("Welcome (Maybe again too)")
        print()
        print("[Enter 'x' for exit..]")
        print()
        num = input("Enter any number:")
        if num == 'x':

            print("________________________________________________")
            
            break
        try:
            number = int(num)
        except ValueError:
            print('Enter a number ..........')
        else:
            sum = 0
            temp = number
            while number > 0:
                rem = number % 10
                sum += rem
                number //= 10
            print()
            print("Sum of digits of",temp,"is",sum,"     <====")
            print()
            print("________________________________________________")
    print()
    input("Press enter to continue :")
    dots_small.dots()

