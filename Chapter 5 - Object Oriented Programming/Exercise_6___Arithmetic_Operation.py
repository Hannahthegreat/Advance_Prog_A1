
import tkinter as tk
from tkinter import ttk, messagebox

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == 'Add':
                self.result = num1 + num2
            elif operation == 'Subtract':
                self.result = num1 - num2
            elif operation == 'Multiply':
                self.result = num1 * num2
            elif operation == 'Divide':
                self.result = num1 / num2
            else:
                self.result = 'Invalid operation'

            return self.result
        except ValueError:
            return "Invalid input"
        except ZeroDivisionError:
            return "Cannot divide by zero"

# Function to get inputs and perform calculation
def perform_calculation():
    operation = operation_var.get()
    num1 = num1_entry.get()
    num2 = num2_entry.get()

    result = calculator.calculate(operation, num1, num2)
    result_label.config(text=f"Result: {result}")

# Create instance of ArithmeticOperations
calculator = ArithmeticOperations()

# Create the main window
root = tk.Tk()
root.title("Arithmetic Operations")
root.geometry("300x200")

# Dropdown for operation selection
operation_var = tk.StringVar()
operation_label = tk.Label(root, text="Select Operation:")
operation_label.pack()
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_dropdown = ttk.Combobox(root, values=operations, textvariable=operation_var, state="readonly")
operation_dropdown.pack()
operation_dropdown.set("Add")

# Entry for first number
num1_label = tk.Label(root, text="Enter first number:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

# Entry for second number
num2_label = tk.Label(root, text="Enter second number:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

# Button to perform calculation
calc_button = tk.Button(root, text="Calculate", command=perform_calculation)
calc_button.pack()

# Label to display result
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Run the application
root.mainloop()
