# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.
def count(num):
    numcopy = num 
    counter = 0
    while num > 0:
        num = num // 10
        counter += 1
    num = numcopy
    sum = 0
    while numcopy > 0:
        fact = 1
        rem = numcopy %10
        numcopy = numcopy // 10
        fact = rem ** counter
        sum = sum + fact
    res = checkArmtrong(num,sum)
    return sum
def checkArmtrong(num,sum):
    if num == sum:
        print(num,"No is ArmStrong No")
    else:
        print(num,"No is not ArmStrong No")
num = int(input("enter no check no is armstrong or not:"))
ans =count(num)