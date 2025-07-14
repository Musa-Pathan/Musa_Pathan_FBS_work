# 10. Write a program to remove all occurrences of a given element in the list.
num = int(input("enter number to remove all occurrence in list :"))
l1 = [1, 2, 3,8,19,1, 2, 3, 4, 5, 6, 7, 8,9,1, 2, 3, 4, 5, 6, 7, 8,9,11,8,19]
for i in l1:
    if i == num:
        l1.remove(i)
print(l1)