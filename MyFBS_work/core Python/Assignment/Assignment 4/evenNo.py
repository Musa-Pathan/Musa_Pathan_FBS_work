#1. WAP to print all even numbers until n.
n = int (input("enter number : "))
for i in range(1,n+1):
    if(i%2==0):
        print(i,end=" ")