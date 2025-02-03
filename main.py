import tasks

def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.add_task(task)  # Corrigido para chamar a função correta
            
        elif choice == "2":
            task = input("Enter task: ")
            tasks.remove_task(task)  # Corrigido para chamar a função correta
        
        elif choice == "3":
            tasks.view_tasks()  # Removido argumento errado
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
