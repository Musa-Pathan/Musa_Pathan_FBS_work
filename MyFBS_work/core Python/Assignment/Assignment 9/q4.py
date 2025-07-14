#4. Write a program to find sum of n numbers using recursion.
def sumOfNum(n):
    if n == 0:
        return 0
    else:
        return n + sumOfNum(n-1)
n = int(input("enter no :"))
print("sum of n numbers : ",sumOfNum(n)) 