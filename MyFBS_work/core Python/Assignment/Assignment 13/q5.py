# 5. Python Program to Sum All the Items in a Dictionary
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
total = 0
for value in dict1.values():
    total += value
print("Sum of all items in the dictionary:", total)
