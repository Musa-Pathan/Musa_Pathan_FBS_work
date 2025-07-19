# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).
n = int(input("enter last number of key :"))
dict1 = {}
for i in range(1,n+1):
    dict1[i] = i * i
print(dict1) 


#o/p
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}