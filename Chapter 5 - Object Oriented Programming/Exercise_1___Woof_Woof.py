import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def woof(self):
        return f"{self.name} says: Woof!"

def display_dog_data():
    data = f"Dog 1: {dog1.name}, Age: {dog1.age}\n" \
           f"Dog 2: {dog2.name}, Age: {dog2.age}"
    data_label.config(text=data)

def oldest_dog_woof():
    if dog1.age > dog2.age:
        messagebox.showinfo("Oldest Dog", dog1.woof())
    elif dog2.age > dog1.age:
        messagebox.showinfo("Oldest Dog", dog2.woof())
    else:
        messagebox.showinfo("Oldest Dog", "Both dogs are of the same age.")

# Create dog objects
dog1 = Dog("Farris", 5)
dog2 = Dog("Rui", 7)

# Create the main window
root = tk.Tk()
root.title("Dog Data")
root.geometry("300x150")

# Styling
root.configure(bg='light gray')
style = {'font': ('Helvetica', 12), 'bg': 'light gray'}

# Display dog data
data_label = tk.Label(root, text="", **style)
data_label.pack(pady=10)

display_dog_data()

# Button to find out oldest dog
woof_button = tk.Button(root, text="The older doggo?", command=oldest_dog_woof)
woof_button.pack(pady=10)

# Run the application
root.mainloop()
