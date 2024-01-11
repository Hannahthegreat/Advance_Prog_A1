
import tkinter as tk
from tkinter import messagebox

def count_occurrences():
    char_to_count = char_entry.get()
    if len(char_to_count) != 1:
        messagebox.showerror("Error", "Please enter a single character.")
        return

    try:
        with open('sentences.txt', 'r') as file:
            contents = file.read()
            count = contents.count(char_to_count)
            result_label.config(text=f"Occurrences of '{char_to_count}': {count}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Character Count in File")

# Character Entry
char_label = tk.Label(root, text="Enter a character:")
char_label.pack()
char_entry = tk.Entry(root)
char_entry.pack()

# Count Button
count_button = tk.Button(root, text="Count Occurrences", command=count_occurrences)
count_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
