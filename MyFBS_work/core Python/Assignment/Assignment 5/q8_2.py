#b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)
n = int(input("enter no : "))
lastNo = int(input("enter last digit for exponent : "))

for i in range (1,lastNo +1):
    temp = n ** i
    print(temp," + ",end=" ")