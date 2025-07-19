# 7. Python Program to Find the Intersection of Two Lists
l1 = [10,20,30,40,50]
l2 = [30,40,50,60,70,80,'abc']
intersection = []
if len(l1) > len(l2):
    for i in l2:
        if i in l1 :
            intersection.append(i)
else:
    for i in l1:
        if i in l2 :
            intersection.append(i)
print("intersection list :",intersection)