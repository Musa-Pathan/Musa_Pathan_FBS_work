#5.Write a program to enter P, T, R and calculate Compound Interest.
P=int(input("enter the value of P="))
T=int(input("enter the value of T="))
R=int(input("enter the value of R="))

amount=P*(1 + R/100)**T
compound_interest=amount-P

print("compound interest is:",compound_interest)
print("total amount is:",amount)
