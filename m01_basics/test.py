num_string = " one, two, three "

num_list = list()

for numbers in num_string.split(","):
    num_list.append(numbers.strip())

print(num_list)


# LIST COMPREHENSION

j = [str(i) for i in range(1,10)]
print(j)


# Printing odd numbers only in a range

l = [ p for p in range(1,15) if p%2 != 0 ]
print(l)