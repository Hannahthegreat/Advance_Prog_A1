import tkinter as tk
from tkinter import ttk

def update_greeting():
    name = name_entry.get()
    color = color_combobox.get()
    greeting_label.config(text=f"Hello, {name}!", fg=color)

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("600x200")  # Set a fixed size for the window

# Styling
padding = {'padx': 5, 'pady': 5}
title_font = ("Helvetica", 12, "bold")
label_font = ("Helvetica", 10)

# Input Frame
input_frame = tk.Frame(root, bg="lightblue", bd=2, relief="groove")
input_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Title Label
title_label = tk.Label(input_frame, text="Enter your details:", fg="blue", bg="lightblue", font=title_font)
title_label.pack(**padding)

# Entry for Name
name_label = tk.Label(input_frame, text="Name:", bg="lightblue", font=label_font)
name_label.pack(side="left", **padding)
name_entry = tk.Entry(input_frame, width=20)
name_entry.pack(side="left", **padding)

# Dropdown for Color Selection
color_label = tk.Label(input_frame, text="Select a color:", bg="lightblue", font=label_font)
color_label.pack(side="left", **padding)
color_combobox = ttk.Combobox(input_frame, values=["Red", "Green", "Blue", "Black"], state="readonly", width=15)
color_combobox.pack(side="left", **padding)
color_combobox.set("Black")

# Update Button
update_button = tk.Button(input_frame, text="Update Greeting", command=update_greeting)
update_button.pack(side="left", **padding)

# Display Frame
display_frame = tk.Frame(root, bg="lightgrey", bd=2, relief="groove")
display_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

# Greeting Label
greeting_label = tk.Label(display_frame, bg="lightgrey", font=("Helvetica", 14))
greeting_label.pack(expand=True)

# Run the application
root.mainloop()
