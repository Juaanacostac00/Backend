import json
import cliClassesFunctions as cli

taskId = 0

#   Menu if the user want to add, modify or delete a task
def showTasksMenu():
    while True:
        print("---------------  TASK MENU  ---------------\n")
        print("1. Add.")
        print("2. Modify.")
        print("3. Delete.")
        print("4. Go back to main menu.\n")

        try:
            option = int(input("Choose an option: "))
            print()
            match option:
                case 1:
                    global taskId
                    cli.generateTask(taskId)
                    taskId += 1
                case 2:
                    cli.modifyMenu()
                case 3:
                    cli.deleteTask()
                case 4:
                    return
                case _:
                    print("Invalid option. Please choose a number between 1 and 4.")
            return
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def showFilterMenu():
    while True:
        print("---------------  SHOW BY  ---------------\n")
        print("1. All tasks.")
        print("2. To do tasks.")
        print("3. In progress tasks.")
        print("4. Completed tasks.")
        print("5. Abandoned tasks.")
        print("6. Go back to main menu.\n")

        try:
            showBy = int(input("Choose an option: "))
            print()
            if not cli.taskList:
                print("Task list is empty\n")
                return
            elif 1 <= showBy <= 5:
                cli.showFilter(showBy)
            elif showBy == 6:
                return
            else:
                print("Invalid option. Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#   Main menu
def main():
    while True:
        print("---------------  MENU  ---------------\n")
        print("1. Add, modify or delete a task.")
        print("2. Show the list of tasks by...")
        print("3. Export tasks to JSON.")
        print("4. Import tasks from JSON.")
        print("5. Exit.\n")

        try:
            option = int(input("Choose an option: "))
            print()
            match option:
                case 1:
                    showTasksMenu()
                case 2:
                    showFilterMenu()
                case 3:
                    cli.exportTo("tasks.json")
                case 4:
                    cli.importTo("tasks.json")
                case 5:
                    break
                case _:
                    print("Invalid option. Please choose a number between 1 and 3.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    main()