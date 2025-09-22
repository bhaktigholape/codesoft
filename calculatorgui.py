import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Error", "Select an operation!")
            return

        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# GUI Setup
root = tk.Tk()
root.title("🧮 Simple Calculator")
root.geometry("350x300")

# Input fields
tk.Label(root, text="Enter First Number:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Operation selection
operation_var = tk.StringVar(value="Add")
tk.Label(root, text="Select Operation:").pack(pady=5)
tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide").pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display
tk.Label(root, text="Result:").pack(pady=5)
entry_result = tk.Entry(root)
entry_result.pack(pady=5)

root.mainloop()
