# 9. Write a program to check if entered number is a palindrome or
# not.
def palindrome(num):
    numCopy = num
    revs = 0
    while num > 0 :
        rem = num % 10
        num = num // 10
        revs = revs * 10 + rem
    if numCopy == revs:
        print("No is palindrome")
    else:
        print("No is not palindrome")
num = int(input("enter no: "))
res = palindrome(num)
