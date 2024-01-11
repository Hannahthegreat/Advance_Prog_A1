
import tkinter as tk
from tkinter import ttk

def draw_shape(event=None):
    selected_shape = shape_var.get()
    canvas.delete("all")  # Clear the canvas before drawing a new shape

    if selected_shape == "Oval":
        canvas.create_oval(10, 10, 190, 100, fill="blue")
    elif selected_shape == "Rectangle":
        canvas.create_rectangle(10, 10, 190, 100, fill="green")
    elif selected_shape == "Square":
        canvas.create_rectangle(10, 10, 110, 110, fill="red")
    elif selected_shape == "Triangle":
        canvas.create_polygon(10, 100, 100, 10, 190, 100, fill="yellow")

# Create the main window
root = tk.Tk()
root.title("Shape Drawer")

# Dropdown for shape selection
shape_label = ttk.Label(root, text="Select a shape:")
shape_label.pack(pady=5)

shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_var = tk.StringVar()
shape_dropdown = ttk.Combobox(root, values=shapes, textvariable=shape_var, state="readonly")
shape_dropdown.pack(pady=5)
shape_dropdown.bind("<<ComboboxSelected>>", draw_shape)

# Canvas
canvas = tk.Canvas(root, width=200, height=120, bg="white")
canvas.pack(pady=20)

# Run the application
root.mainloop()