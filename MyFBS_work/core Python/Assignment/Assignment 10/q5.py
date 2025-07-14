# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.
def noCount(num):
    li = [10,10,20,30,40,50,60,70,80,90,10]
    count = 0
    for i in range(len(li)):
        if num == li[i]:
            count += 1
    if count <= 0:
        print("Num is not in list")
        
    if count > 0:
        print(f"num is found and {count} no of time present in list")
        

num = int(input("enter no  : "))
res = noCount(num)   
