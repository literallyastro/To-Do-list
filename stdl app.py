# Simple To-Do List Application

def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def to_do_list_app():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 4.")

to_do_list_app()
