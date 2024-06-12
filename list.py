# Function to add a new task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    if task_index >= len(todo_list) or task_index < 0:
        print("Invalid task index!")
    else:
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")

# Function to display all tasks in the to-do list
def display_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks in the to-do list!")
    else:
        print("------------------------------------------------")
  
        print("Tasks in the to-do list:")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")
        print("------------------------------------------------")

# Main function to run the to-do list program
def main():
    todo_list = []

    while True:
        print("\nWelcome to the To-Do List Manager!")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "2":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(todo_list, task_index)
        elif choice == "3":
            display_tasks(todo_list)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the main function
main()
