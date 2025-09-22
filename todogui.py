import tkinter as tk
from tkinter import messagebox
import json, os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append({"title": task, "done": False})
        save_tasks()
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        listbox.insert(tk.END, f"{i}. {task['title']} {status}")

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Load existing tasks
tasks = load_tasks()

# GUI setup
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

update_listbox()

root.mainloop()

