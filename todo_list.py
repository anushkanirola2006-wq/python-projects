print("Welcome to Anushka's To-Do List! ❤️")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully! 🎉")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks added yet.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)

        if len(tasks) > 0:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted! 🗑️")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Thank you for using my To-Do List! ❤️")
        break

    else:
        print("Invalid choice! Try again.")