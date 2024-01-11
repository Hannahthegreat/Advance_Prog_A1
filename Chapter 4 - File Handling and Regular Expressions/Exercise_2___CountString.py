import tkinter as tk
from tkinter import messagebox

def count_strings():
    try:
        # Initialize counts to zero
        count_hello_peter = 0
        count_love_python = 0
        count_love = 0
        count_enemy = 0

        # Open the file and read line by line
        with open("sentences.txt", 'r') as file:
            for line in file:
                # Count occurrences of each string
                if "Hello my name is Peter Parker" in line:
                    count_hello_peter += 1
                if "I love Python Programming" in line:
                    count_love_python += 1
                if "love" in line:
                    count_love += 1
                if "enemy" in line:
                    count_enemy += 1

        # Prepare the result message
        result_message = ""
        result_message += "Hello my name is Peter Parker: " + str(count_hello_peter) + "\n"
        result_message += "I love Python Programming: " + str(count_love_python) + "\n"
        result_message += "Love: " + str(count_love) + "\n"
        result_message += "Enemy: " + str(count_enemy)

        # Show the result in a message box
        messagebox.showinfo("String Counts", result_message)

    except Exception as e:
        # Show an error message if something went wrong
        messagebox.showerror("Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("String Count in File")

# Create a button to start counting
count_button = tk.Button(root, text="Count Strings", command=count_strings)
count_button.pack(pady=20)

# Start the GUI application
root.mainloop()
    