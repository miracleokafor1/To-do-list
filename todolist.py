tasks = []
loop = True

def Functionality ():
    #wrap it around a for loop or a while loop most likely while loop
    print("Functionality: Add Tasks (1), View Tasks (2), Delete Tasks (3), Exit (4)")
    
    while loop:   
        try:
            userInput_functionality = int(input(f"Please input a number between 1-4: "))
            if userInput_functionality > 4 or userInput_functionality < 1:
                 print(f"Please try again !")
                 continue
            else:
                break

        except ValueError:
            print("Please enter a valid number (1-4)!")
    return userInput_functionality

def addTasks(tasks):
    userInput = input("Add a new item: ")
    tasks.append(userInput)
    print(f"Added: {userInput}")
    return tasks


def viewTasks(tasks):
    if not tasks:
        print("There is nothing yet.")
    else:
        print("Tasks: ")
        for i, tasks in enumerate(tasks, start=1):
            list = print(f"{i}.{tasks}")
            list

def deleteTasks(tasks):
    viewTasks(tasks)
    while loop:
        if not tasks:
            break
        else:
            try:
                Input = int(input("Pick a number based on which item on the list you would like to delete? "))
                if Input < 1 or Input > len(tasks):
                    print(f"There are/is {len(tasks)} task(s) in the list. Please try again.")
                else:
                    tasks.pop(Input - 1)
                    break
            except ValueError:
                print("Try again!")
            
    return tasks

def Main(tasks):
    while loop:
        userInput_functionality = Functionality()
        try:
            if userInput_functionality == 1:
                addTasks(tasks)
            elif userInput_functionality == 2:
                viewTasks(tasks)
            elif userInput_functionality == 3:
                deleteTasks(tasks)
            elif userInput_functionality == 4:
                print("Exiting program.")
                break
        except Exception as e:
            print(f"Try again! this error occured {e}")
            
Main(tasks)