# 2. Write a program to check if given number is Armstrong or not using recursive
# function.
def is_armstrong(n):
    if n == 0:
        return 0
    digit = n % 10
    return digit**3 + is_armstrong(n // 10)

num = 153
if is_armstrong(num) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
