import tkinter as tk
from tkinter import messagebox

def perform_operation(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        elif operation == 'modulo':
            result = num1 % num2

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero not allowed.")

# Create the main window
root = tk.Tk()
root.title("Arithmetic Operations")
root.geometry("300x200")

# Styling
button_style = {'padx': 10, 'pady': 5}
entry_style = {'padx': 5, 'pady': 5}

# Number 1
label_num1 = tk.Label(root, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack(**entry_style)

# Number 2
label_num2 = tk.Label(root, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack(**entry_style)

# Operation Buttons
label_operation = tk.Label(root, text="Select Operation:")
label_operation.pack()
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)
button_add = tk.Button(frame_buttons, text="Add", command=lambda: perform_operation('add'))
button_add.grid(row=0, column=0, **button_style)
button_subtract = tk.Button(frame_buttons, text="Subtract", command=lambda: perform_operation('subtract'))
button_subtract.grid(row=0, column=1, **button_style)
button_multiply = tk.Button(frame_buttons, text="Multiply", command=lambda: perform_operation('multiply'))
button_multiply.grid(row=0, column=2, **button_style)
button_divide = tk.Button(frame_buttons, text="Divide", command=lambda: perform_operation('divide'))
button_divide.grid(row=0, column=3, **button_style)
button_modulo = tk.Button(frame_buttons, text="Modulo", command=lambda: perform_operation('modulo'))
button_modulo.grid(row=0, column=4, **button_style)

# Result
label_result = tk.Label(root, text="Result:")
label_result.pack()

# Run the application
root.mainloop()