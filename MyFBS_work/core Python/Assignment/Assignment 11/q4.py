# 4. Write a program to find the second largest element in the list.
def bubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    second_largest_no = li[-2]
    print("Second Largest No is :",second_largest_no)
    

li = [30,20,10,40,50]
print(bubbleSort(li))
