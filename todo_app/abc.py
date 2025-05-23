def task():
    tasks = [] 
    print("Welcome to the TODO list app!")
    
    total_task = int(input("Enter how many tasks you want: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
        
    print(f"Today’s tasks are:\n{tasks}")
    
    while True:
        print("\nChoose an operation:")
        print("1 - Add task")
        print("2 - Update task")
        print("3 - Delete task")
        print("4 - Show all tasks")
        print("5 - Exit")
        
        try:
            operation = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
            
        elif operation == 2:
            updated_val = input("Enter the task to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task to '{up}'.")
            else:
                print("Task not found.")
        
        elif operation == 3:
            del_val = input("Which task do you want to delete? ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' deleted.")
            else:
                print("Task not found.")
        
        elif operation == 4:
            print(f"Total tasks: {tasks}")
            
        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# CALL THE FUNCTION HERE
task()
