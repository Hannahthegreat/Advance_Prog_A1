#what is the largest number

print("who is the bigger number?")

while True:
    a = int(input("Give me a number: "))
    b = int(input("Second number please: "))
    c = int(input("One more time!: "))
    
    if a > b and a > c:
        print(a, "is the biggest number")
    elif b > a and b > c:
        print(b, "is the biggest number")
    elif c > a and c > b:
        print(c, "is the biggest number")
    else:
        print("invalid input")
    
    again = input("Do you want to go again? (yes/no): ")
    if again.lower() == "no":
        break
    
print("thank you loop ended")