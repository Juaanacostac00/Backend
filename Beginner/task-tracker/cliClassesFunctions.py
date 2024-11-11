import json
from datetime import datetime
from main import taskId


#   Lists | Variables
taskList = []


#   Definition of the task class
class Task:
    def __init__(self, taskId, description, status, createdAt, updatedAt):
        self.taskId = taskId
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __str__(self):
        return (f"ID: {self.taskId}\n"
                f"Description: {self.description}\n"
                f"Status: {self.status}\n"
                f"Created: {self.createdAt}\n"
                f"Last update: {self.updatedAt}\n")

#   Function to generate a new task
def generateTask(taskId):
    print("---------------  ADD TASK  ---------------\n")
    description = input("Put the description of your new task: ")
    print()
    status = "To do"
    timeStamp = datetime.now().isoformat().replace("T", " ")[:16]
    taskList.append(Task(taskId, description, status, timeStamp, timeStamp))

def modifyStatus(task):
    statusList = ["To do", "In progress", "Completed", "Abandoned"]
    statusTemporal = []
    print()
    while True:
        print("---------------  MODIFY STATUS  ---------------\n")
        print(f"Actual status of {task.description} is: {task.status}\n")
        for status in statusList:
            if status != task.status:
                statusTemporal.append(status)
                print(f"{len(statusTemporal)}. {status}")
        changeTo = int(input("\nChoose an option: ")) - 1
        try:
            if 0 <= changeTo < len(statusTemporal):
                taskList[task.taskId].status = statusTemporal[changeTo]
                taskList[task.taskId].updatedAt = datetime.now().isoformat().replace("T", " ")[:16]
                print(f"New status: {statusTemporal[changeTo]}\n")

                return
            else:
                print("Invalid option. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def modifyTask(task):
    while True:
        print("---------------  MODIFY TASK  ---------------\n")
        print("1. Description.")
        print("2. Status.")
        print("3. Go back to main menu.")

        try:
            option = int(input("\nChoose what you want to modify: "))
            match option:
                case 1:
                    print(f"\nOld description was: {task.description}")
                    taskList[task.taskId].description = input("New description: ")
                    taskList[task.taskId].updatedAt = datetime.now().isoformat().replace("T", " ")[:16]
                    return
                case 2:
                   modifyStatus(task)
                   return
                case 3:
                    return
                case _:
                    print("Invalid option. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#   Function to modify a task
def modifyMenu():
    while True:
        print("---------------  MODIFY  ---------------\n")
        print("\n".join(f"{task.taskId}. {task.description} - {task.status}" for task in taskList))

        try:
            searchFound = False
            search = int(input("\nWrite the ID of the task that you want to modify: "))
            print()
            for task in range(len(taskList)):
                if search == taskList[task].taskId:
                    search = taskList[task]
                    searchFound = True
                    break
            if not searchFound:
                print("Task ID was not found.")
            else:
                modifyTask(search)
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#   Function to delete a task
def deleteTask():
    while True:
        print("---------------  DELETE TASK  ---------------\n")
        print("\n".join(f"{task.taskId}. {task.description} - {task.status}" for task in taskList))
        try:
            search = int(input("Write the ID of the task that you want to delete: "))
            taskFound = False
            for task in range(len(taskList)):
                if not taskFound:
                    if search == taskList[task].taskId:
                        taskList.remove(taskList[task])
                        taskFound = True
                        print("Task was deleted successfully")
                else:
                    if search < taskList[task - 1].taskId:
                        taskList[task - 1].taskId = task - 1
            if not taskFound:
                print("Task not found.")
            return
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def notFound(taskFound):
    if not taskFound:
        print("Empty")

def showFilter(filter):
    while True:
        try:
            match filter:
                case 1:
                    for task in taskList:
                        print(task)
                    break
                case 2:
                    taskFound = False
                    for task in taskList:
                        if task.status == "To do":
                            print(task)
                            taskFound = True
                    notFound(taskFound)
                case 3:
                    taskFound = False
                    for task in taskList:
                        if task.status == "In progress":
                            print(task)
                            taskFound = True
                    notFound(taskFound)
                    break
                case 4:
                    taskFound = False
                    for task in taskList:
                        if task.status == "Completed":
                            print(task)
                            taskFound = True
                    notFound(taskFound)
                    break
                case 5:
                    taskFound = False
                    for task in taskList:
                        if task.status == "Abandoned":
                            print(task)
                            taskFound = True
                    notFound(taskFound)
                    break
                case 6:
                    print("Invalid option. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def exportTo(fileName):
    with open(fileName, 'w') as file:
        json.dump([task.__dict__ for task in taskList], file, indent=4)
    print(f"Tasks successfully exported to {fileName}.")

def importTo(fileName):
    global taskId

    try:
        with open(fileName, 'r') as file:
            tasks = json.load(file)
            for task_data in tasks:
                task = Task(**task_data)  # Desempaqueta el diccionario en los parámetros del constructor
                taskList.append(task)
                taskId = max(taskId, task.taskId + 1)  # Actualiza taskId si es necesario
        print(f"Tasks successfully imported from {fileName}.")
    except FileNotFoundError:
        print(f"The file {fileName} was not found.")
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")