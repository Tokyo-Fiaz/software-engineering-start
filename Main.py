tasks = []

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
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added:", task)

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for index, task in enumerate(tasks, start=1):
                print(index, task)

    elif choice == "3":
        print("You chose Mark task complete.")

    elif choice == "4":
        print("You chose Delete task.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")

    print()
