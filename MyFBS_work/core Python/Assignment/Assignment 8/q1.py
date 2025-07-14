# 1. Write a program to calculate area of rectangle
def area():
    l = float(input("enter length : "))
    b = float(input("enter breadth : "))
    areaOfRect = l * b
    return areaOfRect
res = area()
print("Area of Rectangle is  : ",res)
