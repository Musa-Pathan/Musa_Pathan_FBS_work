#10. WAP to check if given number is Perfect Number. 

#A Perfect Number is a positive integer that is equal to 
# the sum of its proper positive divisors
#  (excluding the number itself).
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")