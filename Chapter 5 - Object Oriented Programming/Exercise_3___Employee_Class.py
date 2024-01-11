
import tkinter as tk
from tkinter import messagebox, simpledialog

class Employee:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.id = 0
        self.salary = 0.0

    def setData(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def getData(self):
        return f"{self.name}\t{self.age}\t{self.id}\t{self.salary}"

# Function to add an employee
def add_employee():
    name = simpledialog.askstring("Input", "Enter Employee's Name:")
    age = simpledialog.askstring("Input", "Enter Employee's Age:")
    id = simpledialog.askstring("Input", "Enter Employee's ID:")
    salary = simpledialog.askstring("Input", "Enter Employee's Salary:")

    new_employee = Employee()
    new_employee.setData(name, age, id, salary)
    employees.append(new_employee)
    messagebox.showinfo("Success", "Employee added successfully!")

# Function to display all employees
def display_employee():
    display_text = "Name\tAge\tID\tSalary\n"
    for emp in employees:
        display_text += emp.getData() + "\n"
    messagebox.showinfo("All Employees", display_text)

# List to store employees
employees = []

# Create the main window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("300x200")

# Add Employee Button
add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.pack(pady=10)

# Display Employees Button
display_button = tk.Button(root, text="Display Employees", command=display_employee)
display_button.pack(pady=10)

# Run the application
root.mainloop()
