
import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        average = self.calcGrade()
        return f"Student Name: {self.name}, Average Grade: {average:.2f}"

# Function to get user input and display grade
def display_grade():
    try:
        name = name_entry.get()
        mark1 = int(mark1_entry.get())
        mark2 = int(mark2_entry.get())
        mark3 = int(mark3_entry.get())

        student = Student(name, mark1, mark2, mark3)
        result = student.display()
        messagebox.showinfo("Student Grade", result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid marks.")

# Create the main window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("300x200")

# Name Entry
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Mark1 Entry
mark1_label = tk.Label(root, text="Mark 1:")
mark1_label.pack()
mark1_entry = tk.Entry(root)
mark1_entry.pack()

# Mark2 Entry
mark2_label = tk.Label(root, text="Mark 2:")
mark2_label.pack()
mark2_entry = tk.Entry(root)
mark2_entry.pack()

# Mark3 Entry
mark3_label = tk.Label(root, text="Mark 3:")
mark3_label.pack()
mark3_entry = tk.Entry(root)
mark3_entry.pack()

# Display Button
display_button = tk.Button(root, text="Display Grade", command=display_grade)
display_button.pack()

# Run the application
root.mainloop()
