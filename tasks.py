import storage

import storage

PRIORITY_LEVELS = {
    "High": "High",
    "Medium": "Medium",
    "Low": "Low"
}

def add_task(task, priority="Low"):  # Agora aceita prioridade
    tasks = storage.load_tasks()
    
    new_task = {
        "task": task,
        "done": False,
        "priority": priority
    }
    
    tasks.append(new_task)
    storage.save_tasks(tasks)
    print(f"Task added successfully! Priority: {priority}")

def get_tasks():
    return storage.load_tasks()


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
        tasks.sort(key=lambda x: ["High", "Medium", "Low"].index(x["priority"]))

        for i, task in enumerate(tasks, 1):
            status = "[X]" if task["done"] else "[ ]"
            priority_emoji = {
                "High": "🚨",
                "Medium": "⚠️",
                "Low": "✅"
            }.get(task["priority"], "✅")  # Usa ✅ como padrão

            print(f"{i}. {status} {priority_emoji} {task['task']} ({task['priority']})")
    else:    
        print("No tasks found!")
        
def toggle_task_completion(task_index):
    tasks = storage.load_tasks()
    
    if 1 <= task_index <= len(tasks):  # Garante que o índice está dentro do range da lista
        tasks[task_index - 1]["done"] = not tasks[task_index - 1]["done"]  # Alterna True/False
        storage.save_tasks(tasks)
        status = "completed" if tasks[task_index - 1]["done"] else "reopened"
        print(f"Task '{tasks[task_index - 1]['task']}' marked as {status}.")
    else:
        print("Invalid task number!")

def clear_all_tasks():
    storage.save_tasks([])
    print("All tasks have been cleared.")


