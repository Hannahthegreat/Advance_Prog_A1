#fizzbuzz??

for dfksf in range(1, 101):
    if dfksf % 3 == 0 and dfksf % 5 == 0:
        print("FizzBuzz")
    elif dfksf % 3 == 0:
        print("Fizz")
    elif dfksf % 5 == 0:
        print("Buzz")
    else:
        print(dfksf)
