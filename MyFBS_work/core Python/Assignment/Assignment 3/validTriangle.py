#3. Write a program to input angles of a triangle and check whether triangle is valid or not.
# a1+ a2 +a3 = 180 then triangle
a1 = int(input("enter angle 1 = "))
a2 = int(input("enter angle 2 = "))
a3 = int(input("enter angle 3 = "))
if a1 + a2 + a3 == 180 :
    print("Valid triangle")
else:
    print("InValid triangle")