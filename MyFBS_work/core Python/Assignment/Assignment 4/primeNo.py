#6. WAP to check if a given number is prime number or not
num = int (input('enter number : '))
for i in range(2,(num //2)+1):
    if(num % i == 0):
        print(f'{num} is not a prime number.')
        break

else:
    print(f'{num} is prime number.')

#print prime no betn 1 to 100
r = int (input("enter range :"))
for num in range(2,r+1):
    for i in range(2,(num //2)+1):
        if(num % i == 0):
            break
        

    else:
        print(num)

    