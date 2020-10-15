def Stone_Paper_Scissor_Game():

    import random
    import dots_small
    
    print("███████████████████████████████████████████████████████████████████████████████████████")
    print()
    print("===> THE CLASSIC - STONE PAPER SCISSOR GAME <===")
    print()
    print("Let's start...")
    print()
    input("Press Enter to continue :")

    def num2name(n):
        if n == 1:
            return 'stone'
        elif n == 2:
            return 'paper'
        elif n == 3:
            return 'scissor'
        return nm

    def name2num(nm):
        if nm.lower() == 'stone':
            n = 1
        elif nm.lower() == 'paper':
            n = 2
        elif nm.lower() == 'scissor':
            n = 3
        return n

    score = 0
    Score = 0
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    w = int(input("Enter how many times you want to play the game --->"))
    print()
    print('----------------')
    for i in range(w):
        c = random.randint(1,3)
        print()
        u = input("Enter your choice [ stone , paper , scissor ] ---->")

        unum = name2num(u)
        if (unum==1 and c==2) or (unum==2 and c==3) or (unum==3 and c==1):
            print()
            print("====> █ You Lost !! Better luck next time ! █")
            print()
            Score += 1
        elif (unum == c):
            print()
            print("====> █ It's a tie █")
            print()
        elif (unum==2 and c==1) or (unum==3 and c==2) or (unum==1 and c==3):
            print()
            print("====> █ You won !! Keep it up ! █")
            print()
            score += 1

        print("You choice was ",u)
        print("AI chose ",num2name(c))
        print()
        print("The score is ....")
        print()
        print("You ==>",score)
        print("AI  ==>",Score)

    def whowon():
        if (Score > score):
            print("██ The AI won !!!!!!!!!   ██")
            print("██ Better Luck next time! ██")
            print()
        elif (Score == score):
            print("██ It's a TIE !!!!!!!! ██")
            print("██ Come again !!       ██")
            print()
        elif (Score < score):
            print("██ You WON !!!!!!!!!!! ██")
            print("██ Have a nice day !!! ██")
            print()
    print("_________________________________________")
    print()
    input("Press enter to continue :")
            
    print(".")
    print(".")
    print(".")
    print(".")
    print("FINAL SCORES--->")
    print()
    print("======================> YOU:",score)
    print("======================>  AI",Score)
    print()
    print("SO,")
    print()
    whowon()
    print()
    print("The Game is Over.")
    print(".")
    print(".")
    print(".")
    print(".")
    print("Goodbye !!!!!")

    print()
    input("Press enter to continue :")
    dots_small.dots()
