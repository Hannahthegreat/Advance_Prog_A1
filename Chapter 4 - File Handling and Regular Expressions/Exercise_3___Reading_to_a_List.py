
# Define a function to read numbers from a file and convert them into a list of integers
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

# Define a function to display the list of numbers
def display_numbers(numbers):
    for number in numbers:
        print(number)

# File path (you'll need to update this with the actual path of your file)
file_path = 'path_to_your_file/numbers.txt'

# Read numbers from the file
numbers_list = read_numbers_from_file("numbers.txt")

# Display the numbers
display_numbers(numbers_list)