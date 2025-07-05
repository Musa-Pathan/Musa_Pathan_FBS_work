# 5. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)


amount = int(input("Enter the amount: "))

print("Minimum number of notes required:")

if amount >= 2000:
    count = amount // 2000
    amount = amount % 2000
    print("2000 :", count, "note(s)")

if amount >= 500:
    count = amount // 500
    amount = amount % 500
    print("500 :", count, "note(s)")

if amount >= 200:
    count = amount // 200
    amount = amount % 200
    print("200 :", count, "note(s)")

if amount >= 100:
    count = amount // 100
    amount = amount % 100
    print("100 :", count, "note(s)")

if amount >= 50:
    count = amount // 50
    amount = amount % 50
    print("50 :", count, "note(s)")

if amount >= 20:
    count = amount // 20
    amount = amount % 20
    print("20 :", count, "note(s)")

if amount >= 10:
    count = amount // 10
    amount = amount % 10
    print("10 :", count, "note(s)")

if amount >= 5:
    count = amount // 5
    amount = amount % 5
    print("5 :", count, "note(s)")

if amount >= 2:
    count = amount // 2
    amount = amount % 2
    print("2 :", count, "note(s)")

if amount >= 1:
    count = amount // 1
    amount = amount % 1
    print("1 :", count, "note(s)")
