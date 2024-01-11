
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Resizable Labels")


frame = tk.Frame(root, bd=5, relief="ridge", bg="red")

label = tk.Label(frame, text="A", bg="red")

# Pack the label inside the frame, filling the entire frame
label.pack(expand=True, fill="both")

# Pack the frame, filling the width of the window
frame.pack(expand=True, fill="x" )

frame = tk.Frame(root)
frame.pack(fill='x')

# Label 2: In the same row as Label 3
label2 = tk.Label(frame, text="C", bd=5, bg="blue",width='10')
label2.pack(side='left', expand=1)

# Label 3: In the same row as Label 2
label3 = tk.Label(frame, text="D", bd=5, bg="white",width='10')
label3.pack(side='left', expand=0)

# Label 4: In the last row, does not expand
label4 = tk.Label(root, text="B", bd=5, relief="raised", bg="yellow",width='10')
label4.pack()

# Run the application
root.mainloop()

