#not clear
#     1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5
for i in range(1,6):
    print(" " *(6-i),end='')
    if i < 5:
        print(1,end="")
    for j in range(1,i+1):
        if i == 5:
            print(j,end="")
        else:
            print(" "*(i-1),end="")   
        print(i)
            
    # if i > 1: 
        
    print()