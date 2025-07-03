
import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.config(bg="white")

# Entry widget for display
entry = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button frame
btn_frame = tk.Frame(window)
btn_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(
            row_frame,
            text=btn_text,
            font=("Arial", 18),
            relief="ridge",
            border=1,
            width=5,
            height=2
        )
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

window.mainloop()
