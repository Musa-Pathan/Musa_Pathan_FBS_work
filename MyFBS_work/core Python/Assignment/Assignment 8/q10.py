# 10. Write a program to check if entered year is a leap year or not.
def leapyear(year):
    if year % 4 == 0 :
        if (year % 100 != 0) or (year % 400 == 0):
            print("Leap year !")
        else:
            print("IS Not Leap Year !")
    else:
            print("IS Not Leap Year !")
year = int(input("enter year = "))
res = leapyear(year)