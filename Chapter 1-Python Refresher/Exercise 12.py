#area function
import math


def circle(r):
    area = math.pi*r**2
    print("Circle area is: ", area)
def square(s):
    area = s**2
    print("Square area is: ", area)
def triangle(b,h):
    area = (h*b)/2
    print(area)


while True:
    shape = input("pick a shape: \n 1) Circle\n 2)square\n 3)triangle\n")
    if shape.lower() == "circle":
        radius = int(input("Input cirlce radius: "))
        circle(radius)
    elif shape.lower() == "square":
        side = int(input("Input lenght of side: "))
        square(side)
    elif shape.lower() == "triangle":
        base = input("Triangle base: ")
        height = input("Triangle height: ")
        triangle(base,height)
    else:
        print("Invalid input")
        
    choice = input("Do you want to go again? (yes/no): ")
    if choice.lower() == "no":
        break