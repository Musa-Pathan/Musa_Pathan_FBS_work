# 8. Write a program find reverse of a number
def rev(num):
    revs = 0
    while num > 0 :
        rem = num % 10
        num = num // 10
        revs = revs * 10 + rem
    return revs
num = int(input("enter no: "))
res = rev(num)
print("Reverse No :",res)