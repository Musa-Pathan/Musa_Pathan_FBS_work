# 3. Write a program to reverse a given number using recursive function.
def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        rem = n % 10
        rev = rev * 10 + rem
        return reverse(n // 10, rev)
n = int(input("enter no:"))
print(reverse(n))
