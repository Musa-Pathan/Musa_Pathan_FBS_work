# 5. Sum of all prime numbers between 1 to n
#prime no have only two factors 1 and no itself

def SumOfPrimeNo(num):
    add = 0
    for n in range(1, num + 1):
        factor = 0         # reset factor count for each n
        for i in range(1, n + 1):
            if n % i == 0:
                factor += 1
        if factor == 2:     # check after counting all factors
            add += n
    return add

num = int(input("Enter a number: "))
res = SumOfPrimeNo(num)
print("Sum of primes:", res)
