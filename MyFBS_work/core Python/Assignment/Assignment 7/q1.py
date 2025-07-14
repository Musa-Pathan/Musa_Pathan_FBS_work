#      * 
#     *  * 
#    *    *
#   *      *
#  *        *
# *          *
# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *

for i in range(6):
    print(" " *(6-i-1),end="")
    print('* ',end="")
    if i > 0:
        print(" " * (2 * i -1),end="")
        print('* ')
    else:
        print()

#lower
for i in range(6-1,-1,-1):
    print(" "*(6-i-1),end="")
    print('*',end="")
    
    if i > 0 :
        print(" "*(2*i-1),end="")
        print("*")
    else:
        print()