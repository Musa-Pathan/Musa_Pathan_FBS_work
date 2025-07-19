# 9. Write a program to create three lists of numbers, their squares and cubes
def number(num_list):
    print("Number list :",num_list)
def squre(num_list):
    squre_list = []
    for i in num_list:
        squre_list.append(i**2)
    print("Squre list :",squre_list)
def cube(num_list):
    cube_list = []
    for i in num_list:
        cube_list.append(i**3)
    print("Squre list :",cube_list)
num_list = [1,2,3,4,5]
number(num_list)
squre(num_list)
cube(num_list)