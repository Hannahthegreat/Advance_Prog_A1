
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import math

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self, sides):
        self.sides = sides

class Circle(Shape):
    def area(self):
        return math.pi * self.sides[0] ** 2

class Rectangle(Shape):
    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def area(self):
        a, b, c = self.sides
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

def calculate_area():
    shape_type = shape_var.get()
    try:
        if shape_type == "Circle":
            radius = float(simpledialog.askstring("Input", "Enter radius:"))
            shape = Circle()
            shape.inputSides([radius])

        elif shape_type == "Rectangle":
            width = float(simpledialog.askstring("Input", "Enter width:"))
            height = float(simpledialog.askstring("Input", "Enter height:"))
            shape = Rectangle()
            shape.inputSides([width, height])

        elif shape_type == "Triangle":
            side1 = float(simpledialog.askstring("Input", "Enter side 1:"))
            side2 = float(simpledialog.askstring("Input", "Enter side 2:"))
            side3 = float(simpledialog.askstring("Input", "Enter side 3:"))
            shape = Triangle()
            shape.inputSides([side1, side2, side3])

        area = shape.area()
        messagebox.showinfo("Area", f"The area of the {shape_type} is: {area:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("300x200")

# Dropdown for shape selection
shape_label = tk.Label(root, text="Select a shape:")
shape_label.pack(pady=5)

shapes = ["Circle", "Rectangle", "Triangle"]
shape_var = tk.StringVar(value=shapes[0])
shape_dropdown = ttk.Combobox(root, values=shapes, textvariable=shape_var, state="readonly")
shape_dropdown.pack(pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack(pady=10)

# Run the application
root.mainloop()
