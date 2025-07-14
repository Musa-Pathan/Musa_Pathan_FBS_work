#6. Write a program to print Fibonacci series using recursion.
def fibo(a,b,n):
    if n == 0 :
        return 0
    else:
        c = a + b
        print(c)
        a = b
        b = c
        return fibo(a,b,n-1)
fibo(-1,1,6)