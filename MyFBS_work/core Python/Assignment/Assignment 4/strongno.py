#11. WAP to check if given number Strong Number.

#A number is called a Strong Number if:
#Sum of factorial of each digit = the original number

num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    sum += fact
    temp //= 10
if sum == num:
    print("Strong number")
else:
    print("Not a strong number")
