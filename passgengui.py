import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showwarning("Input Error", "Password length should be at least 4 characters.")
            return
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number!")
        return

    chars = ""
    if var_letters.get():
        chars += string.ascii_letters
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showwarning("Selection Error", "Select at least one character type!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Complexity Options
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Digits (0-9)", variable=var_digits).pack()
tk.Checkbutton(root, text="Include Symbols (!@#$...)", variable=var_symbols).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

root.mainloop()
