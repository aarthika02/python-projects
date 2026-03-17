import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return[]

def save_tasks(tasks):
    with open(FILE,"w") as f:
        json.dump(tasks,f,indent=4)

def add_task(tasks):
    name = input("Task name : ")
    priority = input("Priority (Low/Medium/High) : ")
    deadline = input("Deadline (YYYY-MM-DD) :")

    task = {
        "name":name,
        "priority":priority,
        "deadline":deadline,
        "status":"Pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    for i,t in enumerate(tasks):
        print(f"{i+1}.{t['name']} | {t['priority']} | {t['deadline']} | {t['status']}")

def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("Task number to delete: "))
    tasks.pop(num-1)
    save_tasks(tasks)
    print("Task deleted...")

def main():
    tasks = load_tasks()

    while True:
        print("\n1.Add Task \n2.View Tasks \n3.Delete Task \n4.Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()