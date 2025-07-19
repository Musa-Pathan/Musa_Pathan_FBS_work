# 15. Python Program to find larger string without using built-in functions.
s1 = input("enter First String :")
s2 = input("enter Second String :")
s3 = input("enter Third String :")
s1_length = 0
s2_length = 0
s3_length = 0
for ch in s1:
    s1_length += 1
for ch in s2:
    s2_length += 1
for ch in s3:
    s3_length += 1

if s1_length > s2_length and s1_length > s3_length :
    print("First String is largest")
elif s2_length > s3_length:
    print("Second String is largest")
else:
    print("Third String is largest")