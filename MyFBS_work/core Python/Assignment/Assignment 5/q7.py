# 7. Write a program to print first n prime numbers.
num = int(input("enter a number :"))
for num in range (1,num+1):
    count = 0
    for i in range (1,num+1):
        if num % i == 0 :
            count += 1
    if count == 2 :
        print(num,end="  ")