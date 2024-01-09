a_list = [1,2,3,4,5,6,7,8,9,10]

print("list: ")
for number in a_list:
    print(number, end=" ")

high_val = max(a_list)
low_val = min(a_list)
print("Highest value: ", high_val)
print("Lowest value: ", low_val)

a_list.sort()
print("Ascending order: ",a_list)

a_list.sort(reverse=True)
print("Descending order: ", a_list)

a_list.append(20)
a_list.append(15)

print("appended two new items", a_list)