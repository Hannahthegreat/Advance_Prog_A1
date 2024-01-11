
import tkinter as tk
from tkinter import messagebox

class Animal:
    def __init__(self, type, name, colour, age, weight, noise):
        self.type = type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        return f"Hello, my name is {self.name}!"

    def makeNoise(self):
        return f"{self.name} says {self.noise}!"

    def animalDetails(self):
        return f"Type: {self.type}\nName: {self.name}\nColour: {self.colour}\nAge: {self.age}\nWeight: {self.weight}"

# Instantiate animal objects
dog = Animal("Dog", "Gojo", "Brown", 5, "30kg", "Woof")
cow = Animal("Cow", "Itadori", "Black and White", 3, "150kg", "Moo")

# GUI Functions
def dog_hello():
    messagebox.showinfo("Animal Greeting", dog.sayHello())

def dog_noise():
    messagebox.showinfo("Animal Noise", dog.makeNoise())

def dog_details():
    messagebox.showinfo("Animal Details", dog.animalDetails())

def cow_hello():
    messagebox.showinfo("Animal Greeting", cow.sayHello())

def cow_noise():
    messagebox.showinfo("Animal Noise", cow.makeNoise())

def cow_details():
    messagebox.showinfo("Animal Details", cow.animalDetails())

# Create the main window
root = tk.Tk()
root.title("Animal Class Demo")
root.geometry("300x200")

# Dog Buttons
dog_hello_button = tk.Button(root, text="Dog says Hello", command=dog_hello)
dog_hello_button.pack(pady=5)
dog_noise_button = tk.Button(root, text="Dog makes Noise", command=dog_noise)
dog_noise_button.pack(pady=5)
dog_details_button = tk.Button(root, text="Dog Details", command=dog_details)
dog_details_button.pack(pady=5)

# Cow Buttons
cow_hello_button = tk.Button(root, text="Cow says Hello", command=cow_hello)
cow_hello_button.pack(pady=5)
cow_noise_button = tk.Button(root, text="Cow makes Noise", command=cow_noise)
cow_noise_button.pack(pady=5)
cow_details_button = tk.Button(root, text="Cow Details", command=cow_details)
cow_details_button.pack(pady=5)

# Run the application
root.mainloop()
