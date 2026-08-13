tasks = []


def add_task():
    task = input("Task likho: ")
    tasks.append(task)
    print("Task add ho gaya!")


def list_tasks():
    print("\n===== MY TASKS =====")

    if len(tasks) == 0:
        print("Abhi koi task nahi hai.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def mark_complete():
    print("Mark Complete abhi banana hai")


def delete_task():
    print("Delete Task abhi banana hai")


while True:

    print("\n===== TODO APP =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Apni choice likho: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Program band ho raha hai")
        break

    else:
        print("Invalid choice")