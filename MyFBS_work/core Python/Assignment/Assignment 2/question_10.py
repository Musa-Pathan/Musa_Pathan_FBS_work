#10. Write a program to reverse three-digit number. 
num = 123

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

reverse = ones * 100 + tens * 10 + hundreds
print("Reversed number:", reverse)