# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

uid = 'admin'
upass =1234

for i in range(1,4):
    uname = input("enter user name :")
    password = int(input("enter password : "))
    if uid == uname and upass == password :
        print("login sucessful !")
        break
    else:
        print("try again!")
else :
    print('wrong Username and password ')