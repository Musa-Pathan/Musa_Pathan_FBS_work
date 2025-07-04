#7. Find the sum of three-digit number.
num=int(input("enter the three digits number="))
print("sum of three digit number is:",int(num // 100) + int(num // 10 % 10) + int(num % 10))