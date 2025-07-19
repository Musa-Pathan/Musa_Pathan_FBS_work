# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions
s1 = input("enter string 1 :")
s2 = input("enter string 2 :")
s1_count = 0
for i in s1 :
    s1_count += 1

s2_count = 0
for i in s2 :
    s2_count += 1
if s1_count == s2_count:
    print("Both String are equal in length")
elif s1_count > s2_count:
    print("First String is largest")
else:
    print("Second String is largest")