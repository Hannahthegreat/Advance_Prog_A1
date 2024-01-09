#triangle calculator

print("triangle inequality!! idk what that is")

while True:
    a = int(input("Give me a number: "))
    b = int(input("Second number please: "))
    c = int(input("One more time!: "))
    
    print("lets see if we have a triangle")
    if a + b >= c:
        print("IT is a triangle <:")
    else:
        print("its not a triangle :<")
    
    again = input("Do you want to go again? (yes/no): ")
    if again.lower() == "no":
        break
    
print("thank you loop ended")