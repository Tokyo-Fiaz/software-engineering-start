tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            if task["complete"] == True:
                status = "Complete"
            else:
                status = "Incomplete"

            print(index, "-", task["name"], "-", status)


while True:
    print("Student Life CLI Tracker")
    print("------------------------")
    print("Welcome! Choose an option from the menu below.")
    print()

    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task complete")
    print("4. Delete a task")
    print("5. Exit")
    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter a task: ")

        task = {
            "name": task_name,
            "complete": False
        }

        tasks.append(task)
        print("Task added:", task_name)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark complete.")
        else:
            show_tasks()

            task_number = input("Which task number do you want to mark complete? ")

            if task_number.isdigit():
                task_number = int(task_number)
                task_index = task_number - 1

                if task_index >= 0 and task_index < len(tasks):
                    tasks[task_index]["complete"] = True
                    print("Task marked complete:", tasks[task_index]["name"])
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            show_tasks()

            task_number = input("Which task number do you want to delete? ")

            if task_number.isdigit():
                task_number = int(task_number)
                task_index = task_number - 1

                if task_index >= 0 and task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print("Task deleted:", deleted_task["name"])
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")

    print()
