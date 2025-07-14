# 2. Write a program to calculate area of circle
#pi*r**2
import math
def areaOfCircle():
    r = float(input("enter radius of circle : "))
    area = math.pi * r ** 2
    return area
res = areaOfCircle()
print("Area of circle is : ",res)