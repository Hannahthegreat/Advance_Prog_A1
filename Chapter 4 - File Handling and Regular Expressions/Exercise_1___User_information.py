
import tkinter as tk
from tkinter import messagebox

def save_data():
    try:
        with open("bio.txt", "w") as file:
            file.write(f"Name: {name_entry.get()}\n")
            file.write(f"Age: {age_entry.get()}\n")
            file.write(f"Hometown: {hometown_entry.get()}\n")
        messagebox.showinfo("Success", "Data saved to bio.txt")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_data():
    try:
        with open("bio.txt", "r") as file:
            data = file.read()
            data_display.config(state=tk.NORMAL)
            data_display.delete(1.0, tk.END)
            data_display.insert(tk.END, data)
            data_display.config(state=tk.DISABLED)
    except FileNotFoundError:
        messagebox.showerror("Error", "bio.txt not found. Please save data first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Bio Data")

# Create and place widgets
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

hometown_label = tk.Label(root, text="Hometown:")
hometown_label.grid(row=2, column=0)
hometown_entry = tk.Entry(root)
hometown_entry.grid(row=2, column=1, padx=10, pady=5)

save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

display_button = tk.Button(root, text="Display Data", command=display_data)
display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

data_display = tk.Text(root, height=5, width=30 )
data_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
