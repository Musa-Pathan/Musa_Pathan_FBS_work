# 12. Python Program to count number of lowercase characters in a string.
s = 'Alpha Bet '
count = 0
for ch in s :
    if ch.islower():
        count += 1
    else :
        continue
print("lower case character in given string is :",count)