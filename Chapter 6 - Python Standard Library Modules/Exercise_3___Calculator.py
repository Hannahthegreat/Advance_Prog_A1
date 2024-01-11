
import operator

# Displaying the calculator menu
print("Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Check greater number")

# Asking the user to choose an operation
choice = input("Choose an operation (1-6): ")

# Asking the user to input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing the chosen operation
if choice == '1':
    result = operator.add(num1, num2)
    print("Result of Addition:", result)

elif choice == '2':
    result = operator.sub(num1, num2)
    print("Result of Subtraction:", result)

elif choice == '3':
    result = operator.mul(num1, num2)
    print("Result of Multiplication:", result)

elif choice == '4':
    if num2 != 0:
        result = operator.truediv(num1, num2)
        print("Result of Division:", result)
    else:
        print("Error: Division by zero")

elif choice == '5':
    result = operator.mod(num1, num2)
    print("Result of Modulus:", result)

elif choice == '6':
    result = operator.gt(num1, num2)
    if result:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")

else:
    print("Invalid choice. Please choose a number between 1 and 6.")
