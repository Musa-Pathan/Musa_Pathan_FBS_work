for i in range(1,6):
    
    print(" " * (5 -i),end=" ")
    for j in range(1,2*i):  #--->it give 2 * i -1
        print('*',end=" ")
    print()


#      * 
#     * * * 
#    * * * * *
#   * * * * * * *        
#  * * * * * * * * *