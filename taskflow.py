# TaskFlow - Smart Task Management System

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['name']} | Priority: {task['priority']} | Status: {status}")

def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({"name": name, "priority": priority, "completed": False})
    print("Task added successfully!")

def complete_task():
    show_tasks()
    num = int(input("Enter task number to mark as completed: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

while True:
    print("\n--- TaskFlow Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting TaskFlow. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
