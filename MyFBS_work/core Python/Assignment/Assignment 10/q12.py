# 12. Write a program to create three lists of numbers, their squares
# and cubes
def square(l1):
    li2 = []
    for i in l1:
        li2.append(i**2)
    return li2
def cube(l1):
    li3 = []
    for i in l1:
        li3.append(i**3)
        
    return li3
l1 =[1,2,3,4,5]
res = square(l1)
print("Suare list :",res)
res2 = cube(l1)
print("Cube list :",res2)