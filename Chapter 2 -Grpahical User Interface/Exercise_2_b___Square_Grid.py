
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Frame Layout with Labels")

# Create left frame
leftF = tk.Frame(root, bd=5, relief="raised")
leftF.pack(side='left', expand=True, fill='both')

root.minsize(300, 200)

# Create right frame
rightF = tk.Frame(root, bd=5, relief="raised")
rightF.pack(side='left', expand=True, fill='both')

# Label A in the left frame, top
labelA = tk.Label(leftF, text="A", bg="#22263D", fg="white")
labelA.pack(side='top', expand=True, fill='both')

# Label B in the left frame, bottom
labelB = tk.Label(leftF, text="B")
labelB.pack(side='bottom', expand=True, fill='both')

# Label C in the right frame, top
labelC = tk.Label(rightF, text="C" )
labelC.pack(side='top', expand=True, fill='both')

# Label D in the right frame, bottom
labelD = tk.Label(rightF, text="D", bg="#22263D",fg="white")
labelD.pack(side='bottom', expand=True, fill='both')

# Run the application
root.mainloop()