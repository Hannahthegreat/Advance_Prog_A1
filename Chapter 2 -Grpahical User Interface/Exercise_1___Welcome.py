# First things first, importing in Tkinter because we're going to need it for the GUI.
import tkinter as tk
from tkinter import font

# Starting off by creating our main window. 
root = tk.Tk()
root.title("Welcome Program")

# I want our window to have a specific size, let's say 400x200 pixels. It's like picking the size of our canvas.
root.geometry("400x200")

# I don't want the window size to change. It's going to stay just the way we set it.
root.resizable(False, False)

# Let's add a bit of color to our window. I'm thinking a light blue background would look nice.
root.configure(background='lightblue')

# Fonts are important, they say a lot. So, let's make our message look good with a nice font.
custom_font = font.Font(family="Helvetica", size=14, weight="bold")

# Here's our welcome message. It's like our friendly greeting to anyone who opens our program.
welcome_label = tk.Label(root, text="Welcome to the Program!", font=custom_font, bg='lightblue')
welcome_label.pack(pady=50)

# All set! Let's run this and see how our little program looks.
root.mainloop()