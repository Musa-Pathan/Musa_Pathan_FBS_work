# 6. Write a program to print prime numbers between 1 to 100.

for num in range (1,100+1):
    count = 0
    for i in range (1,num+1):
        if num % i == 0 :
            count += 1
    if count == 2 :
        print(num,end="  ")
