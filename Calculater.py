import tkinter as tk
from tkinter import messagebox

# Functions for basic operations
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            return
        result = num1 / num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Main GUI window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operation buttons
tk.Button(root, text="Add", width=10, command=add).grid(row=2, column=0, pady=10)
tk.Button(root, text="Subtract", width=10, command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", width=10, command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", width=10, command=divide).grid(row=3, column=1)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
