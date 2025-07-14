#4. Sum of all odd numbers between 1 to n
def oddNum(n):
    add = 0
    for i in range(1,n+1,2):
        add += i
    return add
n = int(input("enter no : "))
print(f"addition of all odd numbers between 1 to {n} is  = ",oddNum(n))