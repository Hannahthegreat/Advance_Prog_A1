
import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = password_entry.get()
    attempt_count = 5 - attempts[0]

    # Password validation criteria
    if (len(password) < 6 or len(password) > 12 or
        not re.search("[a-z]", password) or
        not re.search("[0-9]", password) or
        not re.search("[A-Z]", password) or
        not re.search("[$#@]", password)):
        message = f"Invalid password. {attempt_count} attempts remaining."
        message_label.config(text=message)
        attempts[0] += 1
        if attempts[0] >= 5:
            messagebox.showwarning("Alert", "Authorities have been alerted!")
            root.destroy()  # Close the application
    else:
        messagebox.showinfo("Success", "Password is valid!")
        root.destroy()  # Close the application



root = tk.Tk()
root.title("Password Validator")
root.geometry("400x200")



# Password Entry
password_label = tk.Label(root, text="Enter your password:")
password_label.pack()
password_entry = tk.Entry(root)  # show="*" to mask the password
password_entry.pack()

# Check Button
check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()

# Message Label
message_label = tk.Label(root, text="")
message_label.pack()

criteria_label = tk.Label(root, text="Password must meet the following criteria:")
criteria_label.pack()

criteria = [
    "Contain at least 1 letter between a and z",
    "Contain at least 1 number between 0 and 9",
    "Contain at least 1 letter between A and Z",
    "Contain at least 1 character from $, #, @",
    "Minimum length of password: 6",
    "Maximum length of password: 12"
]

for criterion in criteria:
    lbl = tk.Label(root, text=f"• {criterion}")
    lbl.pack()

# Password attempt counter
attempts = [0]  # Using a list to allow modification within the function

# Run the application
root.mainloop()