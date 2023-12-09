#author Michael Bersabe, CISC 179

import os

def menu():
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task(tasks, task):
    tasks.append(task) #Adds task to end of tasks list
    print("TASK ADDED")

def remove_task(tasks, task_num):
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1) #Removes task at the position specified
        print("TASK REMOVED")
    else:
        print("TASK NOT FOUND")

def view_tasks(tasks):
    if not tasks:
        print("NO TASKS")
    else:
        print("TASKS:")
        for index, task in enumerate(tasks, 1): #Numbers each task starting at 1
            print(f"{index}. {task}")

def save_tasks(tasks, filename="mytasks.txt"): #Saves tasks to a next file
    f = open(filename, "w")
    for task in tasks:
        f.write(task + "\n")
    f.close()

def load_tasks(filename="mytasks.txt"): #Loads tasks from a previous session
    tasks = []
    if os.path.exists(filename):
        f = open(filename, "r")
        for line in f:
            tasks.append(line.strip()) #Removes whitespace from each line and adds to tasks list
        f.close()
    return tasks

def main():
    tasks = load_tasks()

    while True:
        menu()
        option = input("SELECT AN OPTION (1-4): ")

        if option == "1":
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif option == "2":
            task_num = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_num)
        elif option == "3":
            view_tasks(tasks)
        elif option == "4":
            save_tasks(tasks)
            print("LIST SAVED. SEE YOU NEXT TIME!")
            break
        else:
            print("NOT AN OPTION. PLEASE SELECT AN OPTION BETWEEN 1 AND 4.")

if __name__ == "__main__":
    main()
