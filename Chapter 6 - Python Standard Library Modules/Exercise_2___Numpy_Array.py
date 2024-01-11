
# Define the array
a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find the indices of even numbers
indices_of_even = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        indices_of_even.append(i)
print("Indices of even numbers:", indices_of_even)

# Sort the array
sorted_a = sorted(a)
print("Sorted array:", sorted_a)

# Slice elements from index 3 to the end of the array
sliced_from_3 = a[3:]
print("Elements from index 3 to end:", sliced_from_3)

# Slice elements from index 0 to index 4
sliced_to_4 = a[:5]
print("Elements from index 0 to 4:", sliced_to_4)

# Print [32, 15, 67] using negative slicing
negative_sliced = a[-6:-3]
print("Elements [32, 15, 67] using negative slicing:", negative_sliced)
