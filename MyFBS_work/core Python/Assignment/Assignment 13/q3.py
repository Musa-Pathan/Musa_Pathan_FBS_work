# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not
dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
key = int(input("enter key:"))
if key in dict1:
    print("Key Exist in dict")
else:
    print("Key Not exist in dict")