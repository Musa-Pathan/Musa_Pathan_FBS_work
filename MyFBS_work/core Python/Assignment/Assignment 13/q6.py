# 6. Python Program to Multiply All the Items in a Dictionary
dict1 = {1: 10, 2: 20, 3: 30}
total = 1
for value in dict1.values():
    total *= value
print("Multiplication of all items in the dictionary:", total)
