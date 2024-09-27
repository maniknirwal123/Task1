import os

TODO_FILE = 'todo.txt'

# Function to read tasks from the file
def read_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        tasks = [line.strip().split(' | ') for line in file.readlines()]
    return tasks

# Function to write tasks to the file
def write_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(' | '.join(task) + '\n')

# Display all tasks
def display_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task[1] == "Done" else "✗"
            print(f"{i}. {task[0]} [{status}]")

# Add a new task
def add_task():
    task_name = input("Enter task: ")
    tasks = read_tasks()
    tasks.append([task_name, "Pending"])
    write_tasks(tasks)
    print("Task added successfully!")

# Update a task
def update_task():
    display_tasks()
    tasks = read_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 0 < task_num <= len(tasks):
            new_name = input("Enter new task name: ")
            tasks[task_num - 1][0] = new_name
            write_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    display_tasks()
    tasks = read_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            write_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as completed
def complete_task():
    display_tasks()
    tasks = read_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1][1] = "Done"
            write_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as completed")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
