#7. WAP to print all integers upto n that aren’t divisible by 2 and 3
num = int(input("enter number : "))
for i in range(1,num+1):
    if (i %2 ==0 and i % 3==0):
        pass
    else:
        print(i,end=" ")
print()

#if only 2 or 3 
for i in range(1,num+1):
    if (i %2 ==0 or i % 3==0):
        pass
    else:
        print(i,end=" ")
