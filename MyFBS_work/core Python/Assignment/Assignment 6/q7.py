for i in range(1,6):
    
    print(" " * (5 -i),end=" ")
    for j in range(1,2*i):  #--->it give 2 * i -1
        print(chr(64+j),end=" ")
    print()

#      A 
#     A B C 
#    A B C D E
#   A B C D E F G        
#  A B C D E F G H I     