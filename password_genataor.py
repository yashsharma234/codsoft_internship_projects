import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        characters = ""
        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_special.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showwarning("Selection Error", "Please select at least one character set.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for length.")

# Main Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.config(bg="white")

# Heading
tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Length input
tk.Label(window, text="Password Length:", font=("Arial", 12), bg="white").pack()
length_entry = tk.Entry(window, font=("Arial", 12))
length_entry.pack(pady=5)

# Character options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(window, text="Include Uppercase (A-Z)", variable=var_upper, bg="white").pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Lowercase (a-z)", variable=var_lower, bg="white").pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Digits (0-9)", variable=var_digits, bg="white").pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Include Special (!@#)", variable=var_special, bg="white").pack(anchor="w", padx=20)

# Generate button
tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=15)

# Result
tk.Label(window, text="Generated Password:", font=("Arial", 12), bg="white").pack()
result_entry = tk.Entry(window, font=("Arial", 12), width=30)
result_entry.pack(pady=5)

window.mainloop()
