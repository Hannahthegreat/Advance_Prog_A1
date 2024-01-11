
import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage

def submit_order():
    coffee_choice = coffee_var.get()
    options = []
    if sugar_var.get():
        options.append("sugar")
    if milk_var.get():
        options.append("milk")
    messagebox.showinfo("Coffee Order", f"You ordered a {coffee_choice} with {' and '.join(options)}.")

# Create the main window
root = tk.Tk()
root.title("Coffee Vending Machine")

# Load images (replace 'image_path' with the actual file paths of your images)
#coffee_image = PhotoImage(file='cofffee.jpg')
# If using PIL for other formats:
from PIL import Image, ImageTk
coffee_image = Image.open('cofffee.jpg')
coffee_image = ImageTk.PhotoImage(coffee_image)

# Coffee Type Selection
coffee_label = tk.Label(root, text="Select your coffee:")
coffee_label.pack()
coffee_types = ["Espresso", "Latte", "Cappuccino", "Americano"]
coffee_var = tk.StringVar(value=coffee_types[0])
coffee_dropdown = ttk.Combobox(root, values=coffee_types, textvariable=coffee_var, state="readonly")
coffee_dropdown.pack()

# Options
options_label = tk.Label(root, text="Select additional options:")
options_label.pack()
sugar_var = tk.BooleanVar()
sugar_check = tk.Checkbutton(root, text="Sugar", variable=sugar_var)
sugar_check.pack()
milk_var = tk.BooleanVar()
milk_check = tk.Checkbutton(root, text="Milk", variable=milk_var)
milk_check.pack()

# Image Display
coffee_img_label = tk.Label(root, image=coffee_image)
coffee_img_label.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit Order", command=submit_order)
submit_button.pack()

# Run the application
root.mainloop()