#8 . Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + …..n!
n = int(input("inter number : "))
fact = 1
sum = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        fact = fact * j
    # sum = sum + fact
    print(f"{fact} + ",end =" " )
    fact = 1