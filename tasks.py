import storage

def add_task(task):
    tasks = storage.load_tasks()
    new_task = {"task": task, "done": False}  # Cria um dicionário para representar a tarefa
    tasks.append(new_task)
    storage.save_tasks(tasks)
    print("Task added successfully!")

def remove_task(task_name):
    tasks = storage.load_tasks()
    updated_tasks = [task for task in tasks if task["task"] != task_name]  # Filtra a lista, removendo a tarefa desejada
    
    if len(updated_tasks) < len(tasks):
        storage.save_tasks(updated_tasks)
        print(f"Task '{task_name}' removed successfully!")
    else:
        print("Task not found!")

def view_tasks():
    tasks = storage.load_tasks()
    if tasks:
        print("\n=== Tasks ===")
        for i, task in enumerate(tasks, 1):
            status = "[X]" if task["done"] else "[ ]"  # Indica se a tarefa está concluída
            print(f"{i}. {status} {task['task']}")
    else:    
        print("No tasks found!")
