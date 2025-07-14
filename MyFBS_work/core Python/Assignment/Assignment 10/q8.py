# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
l2 = []
for i in l1:
    l2.append(i)
print(l2)
# print(id(l1))
# print(id(l2))