#7. Write a program to find sum of digits of a number.
def sumOfDigit(num):
    sum = 0
    while num > 0 :
        rem = num % 10
        num = num // 10
        sum = sum + rem
    return sum
num = int (input("enter no : "))
res = sumOfDigit(num)
print("Sum  of Digit of Given no is :",res)