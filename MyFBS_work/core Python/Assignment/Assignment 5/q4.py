# 4. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)
num = int(input("Enter number: "))
temp = num    # Save original number for final comparison
sum = 0
count = 0
n = num       # Make a copy of num to count digits

# First loop to count number of digits
while n > 0:
    n = n // 10
    count += 1

n = num       # Reset n for next calculation

# Second loop to calculate Armstrong sum
while n > 0:
    rem = n % 10
    sum = sum + rem ** count
    n = n // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
