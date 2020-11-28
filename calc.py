# Jay Calculator
def stcalc():
    print("________________________________________________")
    print()
    print()
    stop = 0

    def inputTake(x):
        tmp = 0
        AllNumbers = list()
        while tmp < x:
            Numbers = input("Enter The Number - ")
            AllNumbers.append(int(Numbers))
            tmp = tmp+1
        return AllNumbers

    def adder(num):
        sum = 0
        for digit in num:
            sum += digit
        return sum

    def subtractor(num):
        sub = num[0]
        num.pop(0)
        for digit in num:
            sub -= digit
        return sub

    def multiplier(num):
        mul = num[0]
        num.pop(0)
        for digit in num:
            mul *= digit
        return mul

    def divisor(num):
        div = num[0]
        num.pop(0)
        for digit in num:
            div /= digit
        return div

    def power(num):
        pow = num[0]
        print("First ",pow)
        num.pop(0)
        for digit in num:
            pow **= digit
        return pow


    def operation(x,y):
        Numbers = inputTake(y)
        if x == 1:
            ans = adder(Numbers)
        elif x == 2:
            ans = subtractor(Numbers)
        elif x == 3:
            ans = multiplier(Numbers)
        elif x == 4:
            ans = divisor(Numbers)
        else:
            ans = power(Numbers)
        return ans

    while stop == 0:
        print()
        print()
        print("1) Addition Of Number")
        print("2) Subtraction Of Number")
        print("3) Muliplication Of Number")
        print("4) Division Of Number")
        print("5) Power Of Number")
        print("6) Exit Calculator")
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        op = input("Choose the Operation - ")
        op = int(op)


        if op == 6:
            print()
            print("Thank You For Visit !!!")
            stop = 1
        else:
            totalNumber = input("Total Numbers - ")
            totalNumber = int(totalNumber)
            final = operation(op,totalNumber)
            print()
            print()
            print("Final Ans - ", final)
