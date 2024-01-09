import tkinter as tk
from tkinter import font

root = tk.Tk()

root.title("Exercise 1")

label_font = font.Font(weight="bold")
label = tk.Label(root, text="Welcome Message", font=('Arial' ,18, 'bold'))
label.pack(padx=20, pady=20)

root.geometry("400x200")
root.configure(bg='blue')

root.resizable(False,False)
root.mainloop()