# maths
print("Hello, let's test Python math")

while True:
    op = input("Choose an operation: \n 1) Addition\n 2) Subtraction\n 3) Multiplication\n 4) Division\n 5) Remainder\n Choose: ")

    num_1 = int(input("Give me a number: "))
    num_2 = int(input("Second number please: "))
    
    if op.lower() == "addition":  # Corrected the method call to lower()
        print(num_1 + num_2)
    elif op.lower() == "subtraction":
        print(num_1 - num_2)
    elif op.lower() == "multiplication":
        print(num_1 * num_2)
    elif op.lower() == "division":
        print(num_1 / num_2)
    elif op.lower() == "remainder":
        print(num_1 % num_2)
    else:
        print("Invalid input")
    
    again = input("Do you want to go again? (yes/no): ")
    if again.lower() == "no":
        break
    
print("thank you loop ended")