import storage

def add_task(task):
    tasks = storage.load_tasks()
    tasks.append(task)  # Corrigido: antes estava `tasks.append(tasks)`
    storage.save_tasks(tasks)
    print("Task added successfully!")
    
def remove_task(task):
    tasks = storage.load_tasks()
    if task in tasks:
        tasks.remove(task)
        storage.save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Task not found!")
    
def view_tasks():
    tasks = storage.load_tasks()
    if tasks:
        print("\n=== Tasks ===")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:    
        print("No tasks found!")
 