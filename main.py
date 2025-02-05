import tasks

def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Toggle Task Completion")
        print("5. Clear All Tasks")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.add_task(task)
            
        elif choice == "2":
            task = input("Enter task to remove: ")
            tasks.remove_task(task)
        
        elif choice == "3":
            tasks.view_tasks()
        
        elif choice == "4":
            tasks.view_tasks()  
            try:
                task_index = int(input("Enter task number to toggle completion: "))
                tasks.toggle_task_completion(task_index)
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == "5":
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
            if confirm.lower() == "yes":
                tasks.clear_all_tasks()
                print("All tasks have been cleared.")
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
