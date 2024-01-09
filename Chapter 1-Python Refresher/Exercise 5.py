#stya here a "while" lol

counter = 0

while True:
    again = input("Loop the while loop with y cuz y not: ")
    if again.lower() != "y":
        break
    
    counter += 1
    
print("thank you loop ended")
print("u pressed y and ran the loop about", counter, "times :O")