#6.Write a Program to input two angles from user and find third angle of the triangle.
first_angle=float(input("enter the value of first angle="))
second_angle=float(input("enter he value of second angle="))

third_angle=180-(first_angle+second_angle)

print("third angle of a triangle is:",third_angle)