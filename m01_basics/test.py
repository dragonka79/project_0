
# Non list comprehension way

list1 = list()

for i in range(1,5):
    list1.append(i)
print("list1:",list1)

# List comprehension way

list2 = [i for i in range(1,5)]
print("list2:", list2)

# List comprehension way with conditional
# Listing the even numbers between [2,10]

list_even = [i for i in range(1,11) if i%2 ==0]
print("list_even:", list_even)

# List comprehension way with conditional
# Listing the odd numbers between [1,9]

list_odd = [i for i in range(1,11) if i%2 !=0]
print("list_odd:", list_odd)