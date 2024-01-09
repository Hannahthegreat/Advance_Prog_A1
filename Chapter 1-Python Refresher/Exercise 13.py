def calc_prod(a_list):
    product = 1
    for num in a_list:
        product *= num
    return product

# Example list
a_list = [2, 3, 4, 5]

# Call the function and print the result
result = calc_prod(a_list)
print("The product of the list values is:", result)
