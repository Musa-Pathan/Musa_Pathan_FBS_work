# 2. Write a program to find maximum and minimum element in a list.
def bubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    max = li[-1]
    print("max element in list =",max)
    min = li[0]
    print("min element in list =",min)
    

li = [30,20,10,40,50]
print(bubbleSort(li))
