for i in range (1,6):
    print(i,end=" ")
    for j in range(2,6-i):
        if(i==1 ):
            print(j,end=" ")
        
        else:
            print(" ",end=" ")
    if i < 5:        
        print("5")
    
# 1 2 3 4 5
# 2     5
# 3   5
# 4 5
# 5

