# TO DO LIST

# task = []

# def show_menu():
#     print("/n === TO DO LIST ===")
#     print("1.ADD TASK ")
#     print("2.DISPLAY TASK ")
#     print("3.DELETE TASK ")
#     print("4.EXIT ")
#     print("/n === TO DO LIST ===")
    
tasks = []  # List to store tasks

def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Done")
    print("4. Show Tasks")
    print("5. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def delete_task():
    show_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted!")
    else:
        print("Invalid task number!")

def mark_done():
    show_tasks()
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number!")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n=== Your Tasks ===")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} [{status}]")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
