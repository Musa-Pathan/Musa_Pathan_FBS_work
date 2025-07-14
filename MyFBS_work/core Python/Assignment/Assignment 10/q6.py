# 6. Write a program to remove duplicates from the list.
l1 = [1,2,3,4,5,6,7,8,6,7,3,2,0]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)