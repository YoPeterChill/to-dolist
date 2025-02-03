ARQUIVO = "tasks.txt"

def load_tasks():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            tasks = [task.strip() for task in f.readlines()]
    except FileNotFoundError:
        tasks = []
        
    return tasks

def save_tasks(tasks):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task}\n")
