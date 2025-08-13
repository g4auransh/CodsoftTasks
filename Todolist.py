import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task['completed'] else "✖"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added.")
    else:
        print("Task title cannot be empty.")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
