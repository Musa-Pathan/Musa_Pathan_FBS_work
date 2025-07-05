#5. WAP to print Fibonacci series upto n.
num = int (input("enter no of terms you want : "))
a = -1
b = 1
for i in range(1,num+1):
    c = a + b
    print(c)
    a = b
    b = c
