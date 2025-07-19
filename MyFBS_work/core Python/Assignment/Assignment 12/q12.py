# 13. Python Program to count number of digits and letters in a string
s = input('enter string with digit :')
count = 0
for ch in s:
    if ch.isdigit():
        count += 1
print("Number of Digit in given String is :",count)