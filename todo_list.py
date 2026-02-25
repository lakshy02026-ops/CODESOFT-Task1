import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

class TodoApp:
    def __init__(self, root):
        self.todo = TodoList()
        self.root = root
        self.root.title("To-Do List")

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.update_button = tk.Button(root, text="Update Selected", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo.add_task(task)
            self.refresh_list()
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            new_task = self.task_entry.get()
            if new_task:
                self.todo.update_task(index, new_task)
                self.refresh_list()
                self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.todo.delete_task(index)
            self.refresh_list()

    def on_select(self, event):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, self.todo.tasks[index])

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo.tasks:
            self.task_listbox.insert(tk.END, task)

def update_file(file_path, new_data):
    try:
        with open(file_path, 'w') as file:  # Use 'w' to overwrite, not 'a' to append
            file.write(new_data)
        print("File updated successfully.")
    except Exception as e:
        print(f"Error updating file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()