# 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +….. + n! 
def factorial(num):
    
    if num == 0 or num == 1 :
        return 1
    return num * factorial(num -1)
def sumOfFact(num):
    if num == 0:
        return 0
    return factorial(num) + sumOfFact(num - 1)
    
    
num = int(input("enter num :"))
res = sumOfFact(num)
print("sum of factorial :",res)