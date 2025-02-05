import tkinter as tk
from tkinter import messagebox, ttk  # Importamos ttk para a ComboBox
import tasks

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x550")

        # Entrada de texto para nova tarefa
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Dropdown para selecionar prioridade
        self.priority_label = tk.Label(root, text="Select Priority:")
        self.priority_label.pack()

        self.priority_options = ["High", "Medium", "Low"]
        self.priority_var = tk.StringVar(value="Low")  # Padrão: Low

        self.priority_dropdown = ttk.Combobox(root, textvariable=self.priority_var, values=self.priority_options)
        self.priority_dropdown.pack()

        # Botão para adicionar tarefas
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Lista de tarefas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Botões para interagir com as tarefas
        self.complete_button = tk.Button(root, text="Toggle Completion", command=self.toggle_task)
        self.complete_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        # Carregar tarefas ao iniciar o app
        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get()
        priority = self.priority_var.get()  # Obtém a prioridade selecionada

        if task_text:
            tasks.add_task(task_text, priority)  # Agora passamos a prioridade
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def toggle_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtém o índice selecionado
            tasks.toggle_task_completion(selected_index + 1)  # +1 porque a lista começa no índice 1
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtém o índice selecionado
            task_name = self.task_listbox.get(selected_index)  # Obtém o nome da tarefa
            task_name = task_name[4:].strip()  # Remove a numeração da lista
            tasks.remove_task(task_name)
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task first!")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        task_data = tasks.get_tasks()

        # Ordena as tarefas pela prioridade antes de exibir
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        task_data.sort(key=lambda x: priority_order[x["priority"]])

        for i, task in enumerate(task_data, 1):
            status = "[X]" if task["done"] else "[ ]"
            priority_emoji = {
                "High": "🚨",
                "Medium": "⚠️",
                "Low": "✅"
            }.get(task["priority"], "✅")

            self.task_listbox.insert(tk.END, f"{i}. {status} {priority_emoji} {task['task']} ({task['priority']})")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
