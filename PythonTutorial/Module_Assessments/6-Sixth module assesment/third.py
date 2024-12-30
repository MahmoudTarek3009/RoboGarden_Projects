import os

# Function to add a task to the list
def add_task(task, task_list):
    task_list.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove a completed task
def remove_task(task, task_list):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' has been removed.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to view the current tasks
def view_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks available.")
    else:
        print("Current Task List:")
        for idx, task in enumerate(task_list, 1):
            print(f"{idx}. {task}")

# Function to save tasks to a file
def save_tasks(task_list, filename):
    try:
        with open(filename, 'w') as file:
            for task in task_list:
                file.write(task + '\n')
        print("Tasks have been saved to the file.")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                tasks = file.readlines()
            # Remove any extra whitespace (newlines)
            tasks = [task.strip() for task in tasks]
            print("Tasks have been loaded from the file.")
            return tasks
        except Exception as e:
            print(f"An error occurred while loading tasks: {e}")
            return []
    else:
        print(f"No file found named '{filename}'. Starting with an empty task list.")
        return []

# Function to handle file errors
def handle_file_error(func, *args):
    try:
        func(*args)
    except Exception as e:
        print(f"An error occurred: {e}")

# Main driver function to interact with the user
def main():
    task_list = load_tasks("tasks.txt")

    while True:
        print("\nTask List Manager:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Exit")
        
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task, task_list)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task, task_list)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            save_tasks(task_list, "tasks.txt")
        elif choice == '5':
            save_tasks(task_list, "tasks.txt")
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
