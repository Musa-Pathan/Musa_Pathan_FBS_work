# 4. Write a program to reverse the list.
def reverseList(li):
    li2 = []
    for i in range(len(li)-1,-1,-1):
        li2.append(li[i])
    return li2
li = [20,10,30,40,50]
res = reverseList(li)
print("Reverse List: ",res)