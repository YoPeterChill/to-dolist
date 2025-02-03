import json

ARQUIVO = "tasks.json"

def load_tasks():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            tasks = json.load(f)  # Carrega as tarefas do JSON
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []  # Se o arquivo não existir ou estiver vazio, retorna lista vazia
        
    return tasks

def save_tasks(tasks):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)  # Salva o JSON formatado
