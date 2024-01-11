
import tkinter as tk
from tkinter import messagebox

def on_login():
    # You can add the logic to verify login credentials here
    messagebox.showinfo("Login", "Logged in, welcome!")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Set the geometry (width x height)
root.geometry("300x150")

# Username Label
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)

# Username Entry
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

# Password Entry
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = tk.Button(root, text="Login", command=on_login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()