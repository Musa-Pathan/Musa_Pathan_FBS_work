# 11. Write a program to print all numbers which are divisible by m and n in the
# list.
m = int(input("enter no to divide :"))
n = int(input("enter no to divide :"))
l1 = [10,20,30,40,44,50,60,70,80,90,12,15,55]
l2 = []  #---> this store all divisable no
for i in l1:
    if i % m == 0 and i % n == 0:
        l2.append(i)
print(l2)