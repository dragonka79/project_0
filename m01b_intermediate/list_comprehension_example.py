# Non list comprehension way

list1 = list()

for i in range(1,5):
    list1.append(i)
print("list1:",list1)

# List comprehension way

list2 = [i for i in range(1,5)]
print("list2:", list2)