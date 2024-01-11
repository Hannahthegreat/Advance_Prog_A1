import tkinter as tk
from tkinter import ttk, messagebox

def on_submit():
    # You can add the logic to handle form submission here
    messagebox.showinfo("Submission", "Form Submitted!")

# Create the main window
root = tk.Tk()
root.title("Student Management System")

# Title
title_label = tk.Label(root, text="Student Management System", font=("Helvetica", 16))
title_label.grid(row=0, columnspan=3, pady=(10, 0))

# Subheading
subheading_label = tk.Label(root, text="New Student Registration", font=("Helvetica", 12))
subheading_label.grid(row=1, columnspan=3, pady=(5, 10))

# Student Name
student_name_label = tk.Label(root, text="Student Name:")
student_name_label.grid(row=2, column=0, sticky=tk.W)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=2, column=1, sticky=tk.EW)

# Mobile Number
mobile_label = tk.Label(root, text="Mobile Number:")
mobile_label.grid(row=3, column=0, sticky=tk.W)
mobile_entry = tk.Entry(root)
mobile_entry.grid(row=3, column=1, sticky=tk.EW)

# Email ID
email_label = tk.Label(root, text="Email ID:")
email_label.grid(row=4, column=0, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, sticky=tk.EW)

# Home Address
address_label = tk.Label(root, text="Home Address:")
address_label.grid(row=5, column=0, sticky=tk.W)
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, sticky=tk.EW)

# Gender Dropdown
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=6, column=0, sticky=tk.W)
gender_combobox = ttk.Combobox(root, values=["Male", "Female", "Other"])
gender_combobox.grid(row=6, column=1, sticky=tk.EW)

# Course Enrolled (Checkboxes)
course_label = tk.Label(root, text="Course Enrolled:")
course_label.grid(row=7, column=0, sticky=tk.W)
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
course_vars = [tk.IntVar() for _ in courses]
for i, course in enumerate(courses):
    radio_button = tk.Radiobutton(root, text=course, variable=course_vars, value=course)
    radio_button.grid(row=7, column=i+1, sticky=tk.W)

# Languages Known (Checkboxes)
language_label = tk.Label(root, text="Languages Known:")
language_label.grid(row=8, column=0, sticky=tk.W)
languages = ["English", "Tagalog", "Hindi/Urdu"]
language_vars = [tk.IntVar() for _ in languages]
for i, lang in enumerate(languages):
    checkbox = tk.Checkbutton(root, text=lang, variable=language_vars[i])
    checkbox.grid(row=8, column=i+1, sticky=tk.W)

# English Communication Skills (Slider)
english_skills_label = tk.Label(root, text="Rate your English Communication Skills:")
english_skills_label.grid(row=9, column=0, sticky=tk.W)
english_skills_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
english_skills_scale.grid(row=9, column=1, sticky=tk.W)

# Submit and Clear Buttons
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=10, column=0, pady=(10, 10), sticky=tk.W)
clear_button = tk.Button(root, text="Clear" )
clear_button.grid(row=10, column=1, pady=(10, 10), sticky=tk.E)

# Run the application
root.mainloop()
