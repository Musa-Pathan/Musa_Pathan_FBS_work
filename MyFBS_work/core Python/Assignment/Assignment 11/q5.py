# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.
l1 = ['apple', 'banana', 'laturr', 'pune']
l2 = sorted(l1, key=len)
print(l2)


##########
# bubble sort based on string length
n = len(l1)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(l1[j]) > len(l1[j + 1]):
            # swap
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print(l1)