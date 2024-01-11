
import json

# Function to write student details to a JSON file
def write_student_details():
    # Ask user for student details
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    course = input("Enter student course: ")

    # Creating a dictionary for the student
    student_dict = {
        "Name": name,
        "ID": student_id,
        "course": course
    }

    # Writing to JSON file
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_dict, json_file, indent=4)

# Function to read and display student details from a JSON file
def read_student_details():
    # Reading from JSON file
    with open('StudentJson.json', 'r') as json_file:
        student_dict = json.load(json_file)

    # Displaying student details
    print("\nDetails of the Student are")
    for key, value in student_dict.items():
        print(f"\t{key}: {value}")

# Function to update student details in the JSON file
def update_student_details():
    # New details to append
    course_details = {
        "CourseDetails": {
            "Group": "A",
            "Year": 2
        }
    }

    # Reading the current data
    with open('StudentJson.json', 'r') as json_file:
        student_dict = json.load(json_file)

    # Updating the dictionary
    student_dict.update(course_details)

    # Writing the updated data back to JSON file
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_dict, json_file, indent=4)

# Main program
write_student_details()
read_student_details()
update_student_details()
read_student_details()
