#6. Write a program to find print the following Fibonacci series using
# functions:
#  1 1 2 3 5 8 n terms
def febonaci(a,b,n):
    count =0
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term
        count += 1
n = int(input("enter nth term for fibonacci series :"))
a = 1
b = 1
res = febonaci(a,b,n)
