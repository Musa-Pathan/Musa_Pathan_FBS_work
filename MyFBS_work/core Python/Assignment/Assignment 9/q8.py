# 8. Write a program to check whether a number is prime or not using recursion
def prime(n, i=2):
    if n <= 1:
        return f"{n} is not prime"
    if i * i > n:  
        return f"{n} is prime"
    if n % i == 0:
        return f"{n} is not prime"
    return prime(n, i + 1)

n = int(input("Enter number to check if prime: "))
print(prime(n))
