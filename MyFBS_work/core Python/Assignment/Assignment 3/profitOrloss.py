#Write a program to calculate profit or loss.
#profit = s p - p p
#loss = pp - sp
pp = int(input("enter purchase price :"))
sp = int(input("enter selling price :"))
if sp > pp:
    profit = sp - pp
    print(f'you have got {profit} rupees profit ')
else :
    loss = pp - sp
    print(f'you have got {loss} rupees loss ')