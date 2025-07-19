# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists
l1 = [1, 2, 3, 4, 5, 6, 7, 8,9,11,12,13,14,15,16,17,18,19]
oddList = []
evenList = []
for i in l1:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
print(f'Even No List :{evenList}\nOdd No List :{oddList}')