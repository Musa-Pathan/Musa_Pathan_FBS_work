#7.Program to Find the Roots of a Quadratic Equation
a=int(input('enter a '))
b=int(input('enter  b '))
c=int(input('enter  c '))
#qudtric equtation
import math
r1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
r2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
print('the roots are ',r1,r2)
