# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String
s1 = 'abcdefghijklmnopqrstuvwxyz'
n = int(input("enter index no to remove that character :"))
s = "python"
new_s = ""
for i in range(len(s1)):
    if i != n:
        new_s += s1[i]
print(new_s)  


      