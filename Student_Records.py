def Student_Records():

    s =[]

    def addstudent():
        i = []
        rn = input("Enter the roll no --->")
        name = input("Enter the student's name --->")
        std = input("Enter the standard --->")
        stream = input("Enter stream --->")
        grade = input("Enter the grade --->")
        i.append(rn)
        i.append(name)
        i.append(std)
        i.append(stream)
        i.append(grade)
        s.append(i)

    def showdata():
        for k in s:
            print("===>")
            print("----------------------------")
            print()
            print(" ~Roll no ===>",k[0])
            print(" ~Name ===>",k[1])
            print(" ~Standard ===>",k[2])
            print(" ~Stream ===>",k[3])
            print(" ~Grade ===>",k[4])
            print()
            print("----------------------------")
        return True

    def Query_1(std):
        for j in s:
            if std in j:
                print("===>")
                print("---------------------------------")
                print()
                print(" ~Roll no ===>",j[0])
                print(" ~Name ===>",j[1])
                print(" ~Standard ===>",j[2])
                print(" ~Stream ===>",j[3])
                print(" ~Grade ===>",j[4])
                print()
                print("---------------------------------")
    def Query_2(st):
        for k in s:
            if st in k:
                print("===>")
                print("---------------------------------")
                print(" ~Roll no ===>",k[0])
                print(" ~Name ===>",k[1])
                print(" ~Standard ===>",k[2])
                print(" ~Stream ===>",k[3])
                print(" ~Grade ===>",k[4])
                print("---------------------------------")
    def Query_3(gr):
        for y in s:
            if gr in y:
                print("===>")
                print("---------------------------------")
                print(" ~Roll no ===>",y[0])
                print(" ~Name ===>",y[1])
                print(" ~Standard ===>",y[2])
                print(" ~Stream ===>",y[3])
                print(" ~Grade ===>",y[4])
                print("---------------------------------")

    def menu():
        print()
        print("_____________________________________________________")
        print()
        print("---- STUDENT RECORDS ----")
        print()
        print("1. Add a student")
        print("2. Show all students")
        print("3. Query as per standard")
        print("4. Query as per stream")
        print("5. Query as per grade")
        print("6. Exit")
        print()
        print("_____________________________________________________")

    while True:
        menu()
        print()
        ch = int(input("Enter your choice --->"))
        print()
        print("-------------")
        print()

        if ch == 1:
            addstudent()

            print()
            input("Press Enter to continue :")
            print()

        elif ch == 2:
            
            if showdata():
                print()
            else:
                print()
                print("List Empty !")
                print()

            input("Press Enter to continue :")
            print()

        elif ch == 3:
            print()
            std = input("Enter the standard --->")
            print()

            if Query_1(std):
                print()
            else:
                print()
                print("No one is in",std,"standard.")
                print()

            input("Press Enter to continue :")
            print()

        elif ch == 4:
            print()
            st = input("Enter the stream --->")
            print()

            if Query_2(st):
                print()
            else:
                print()
                print("No one is in",st,"stream.")
                print()

            input("Press Enter to continue :")
            print()

        elif ch == 5:
            print()
            gr = input("Enter the grade --->")
            print()

            if Query_3(gr):
                print()
            else:
                print()
                print("No one has",gr,"grade.")
                print()

            input("Press Enter to continue :")
            print()

        elif ch == 6:
            
            print()
            print("Aborting .......")
            print(".")
            print(".")
            print(".")
            print(".")
            print(".")
            print("Goodbye !!")
            break


                
                
