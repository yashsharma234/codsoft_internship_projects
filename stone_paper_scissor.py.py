import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {comp_choice}\n{result}")

# Main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x350")
window.config(bg="white")

# Title
tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Buttons
btn_frame = tk.Frame(window, bg="white")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Rock", width=12, height=2, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper", width=12, height=2, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissors", width=12, height=2, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Result Display
result_label = tk.Label(window, text="", font=("Arial", 12), bg="white", fg="blue")
result_label.pack(pady=20)

window.mainloop()

