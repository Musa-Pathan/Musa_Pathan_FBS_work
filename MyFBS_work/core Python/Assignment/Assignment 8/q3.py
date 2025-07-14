# 3. Write a program to find sum of following series using functions :
# # a. 1+ 2 + 3 + 4+..... + n
# # b. 1!+ 2! + 3! + 4!+..... + n!
# # c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumOfSeries():
    num = int(input("enter no of terms you want to sum : "))
    sum = 0
    for i in range(1,num +1):
        
        sum +=i
    return sum
sum = sumOfSeries()
print("sum of series is = ",sum)

# #####################################################

def fact():
    n = int(input("enter how many no of terms factorial sum you want = "))
    sumOfFact = 1
    for i in range(1,n+1):
        sumOfFact = sumOfFact * i
    return sumOfFact
print("factorial series of sum = ",fact())


#####################################################
# c. 1^1 + 2^2 + 3^3+ ...... n^n
#####################################################
def sumOfNumberSeriesPower():
    n = int(input("enter last term for power = "))
    sumOfPower = 0
    for i in range(1,n+1):
        sumOfPower += i ** i
    return sumOfPower
res = sumOfNumberSeriesPower()
print("sum of power series : ",res)
