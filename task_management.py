import dots_small

def task_management():
    tasks = ["Add_Some_python_programs","Have_a_healthy_sleep","Go_for_a_walk"]

    def menu():
        print()
        print("███████████████████████████████████████████████████████")
        print()
        print("====> TASK MANAGEMENT <====")
        print()
        print("1. Show tasks")
        print("2. Add new task")
        print("3. Complete the first task")
        print("4. Cancel a particular task")
        print("5. Change the priority of a task")
        print("6. Exit this MENU")

    def show():
        print("------------------------------")
        print()
        print("The tasks are :")
        for t in tasks:
            print()
            print("--->",t)

        print()
        print("------------------------------")
        print()
        input("Press enter to continue :")
        

    def add():
        print()
        x = input("Enter the new task -->")
        tasks.append(x)
        print()
        input("Press enter to continue :")

    def cancel():
        print()
        y = input("Enter the task to be cancelled --->")
        tasks.remove(y)
        print()
        print("Task successfully removed.")
        print()
        input("Press enter to continue :")

    def complete():
        print()
        print("Task cmplteted")
        tasks.pop(0)
        print()
        input("Press enter to continue :")

    def priority():
        print()
        z = input("Enter the task whose priority is to be changed --->")
        if z in tasks:
            tasks.remove(z)
            tasks.insert(0,z)
        print()
        input("Press enter to continue :")

    ch = 1
    while (ch>0) and (ch<6):
        menu()
        print()
        ch = int(input("Enter your choice -->"))
        print()
        if ch ==1:
            show()

        elif ch ==2:
            add()

        elif ch ==3:
            complete()

        elif ch ==4:
            cancel()

        elif ch ==5:
            priority()

        else:
            print()
            print("Aborting !!!!!")
            print(".")
            print(".")
            print(".")
            print(".")
            break
        print()
        print("Program OVER.")
        print()
        print("_____________________________________")

    print()
    input("Press enter to continue :")
    dots_small.dots()

