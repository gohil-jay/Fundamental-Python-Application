import dots_small

def String_manipulation():
    print()
    print("_____________________________________")
    print()
    print("---- Top Mosts Words Repeated In The String ----")
    print()
    print()

    str = input("Enter the string --->")
    if str != "":
        print()
        dep_word = input("Enter the words to be deprecated from search (seperate by comma) --->")
        dep_array = dep_word.split(",")

        print()
        number_word = input("Enter the First _________ words (num) --->")

        counts = dict()
        str = str.lower()
        words = str.split(" ")
        for word in words :
            if word not in dep_array:
                counts[word] = counts.get(word,0)+1

        def repeatedMost(num) :

            finalKey = None
            finalValue = None
            for key in counts :
                if finalValue is None or counts[key] > finalValue :
                    finalValue = counts[key]
                    finalKey = key
            counts[finalKey] = 0;
            print()
            print(num," Most Repeated Word is '"+finalKey+"' Repeated :",finalValue," times.")

        repeat = 0;
        tmp = str.split(" ")
        if len(tmp) < int(number_word):
            number_word = len(tmp)
        while repeat < int(number_word):
            repeatedMost((repeat+1))
            repeat = repeat+1


    print()
    print("_____________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()
