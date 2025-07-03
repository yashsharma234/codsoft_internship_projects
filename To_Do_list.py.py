import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("350x400")
window.config(bg="white")

# Title Label
title_label = tk.Label(window, text="To-Do List", font=("Arial", 16, "bold"), bg="white")
title_label.pack(pady=10)

# Entry field
task_entry = tk.Entry(window, font=("Arial", 12), width=25)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(window, text="Add Task", command=add_task, width=15)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Selected Task", command=delete_task, width=20)
delete_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear All Tasks", command=clear_tasks, width=15)
clear_button.pack(pady=5)

# Task listbox
tasks_listbox = tk.Listbox(window, font=("Arial", 12), width=30, height=10, selectbackground="lightblue")
tasks_listbox.pack(pady=10)

window.mainloop()
