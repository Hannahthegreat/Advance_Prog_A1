import tkinter as tk
from tkinter import ttk, messagebox

def calculate_circle_area():
    try:
        radius = float(circle_radius_entry.get())
        area = 3.14159 * radius * radius
        messagebox.showinfo("Result", f"Area of the circle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_square_area():
    try:
        side = float(square_side_entry.get())
        area = side * side
        messagebox.showinfo("Result", f"Area of the square: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_rectangle_area():
    try:
        length = float(rectangle_length_entry.get())
        width = float(rectangle_width_entry.get())
        area = length * width
        messagebox.showinfo("Result", f"Area of the rectangle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("300x250")

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TEntry", font=("Helvetica", 10), padding=5)

# Create the tab control
tab_control = ttk.Notebook(root)

# Tab 1: Circle
tab_circle = ttk.Frame(tab_control)
tab_control.add(tab_circle, text='Circle')
circle_radius_label = ttk.Label(tab_circle, text="Radius:")
circle_radius_label.pack(pady=5)
circle_radius_entry = ttk.Entry(tab_circle)
circle_radius_entry.pack(pady=5)
circle_calculate_button = ttk.Button(tab_circle, text="Calculate Area", command=calculate_circle_area)
circle_calculate_button.pack(pady=5)

# Tab 2: Square
tab_square = ttk.Frame(tab_control)
tab_control.add(tab_square, text='Square')
square_side_label = ttk.Label(tab_square, text="Side Length:")
square_side_label.pack(pady=5)
square_side_entry = ttk.Entry(tab_square)
square_side_entry.pack(pady=5)
square_calculate_button = ttk.Button(tab_square, text="Calculate Area", command=calculate_square_area)
square_calculate_button.pack(pady=5)

# Tab 3: Rectangle
tab_rectangle = ttk.Frame(tab_control)
tab_control.add(tab_rectangle, text='Rectangle')
rectangle_length_label = ttk.Label(tab_rectangle, text="Length:")
rectangle_length_label.pack(pady=5)
rectangle_length_entry = ttk.Entry(tab_rectangle)
rectangle_length_entry.pack(pady=5)
rectangle_width_label = ttk.Label(tab_rectangle, text="Width:")
rectangle_width_label.pack(pady=5)
rectangle_width_entry = ttk.Entry(tab_rectangle)
rectangle_width_entry.pack(pady=5)
rectangle_calculate_button = ttk.Button(tab_rectangle, text="Calculate Area", command=calculate_rectangle_area)
rectangle_calculate_button.pack(pady=5)

# Add the tab control to the main window
tab_control.pack(expand=1, fill="both", padx=10, pady=10)

# Run the application
root.mainloop()
