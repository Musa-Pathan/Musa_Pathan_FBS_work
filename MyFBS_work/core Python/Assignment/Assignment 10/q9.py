# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
l1 = [1, 2, 3, 4, 5, 6, 7, 8,9,11,12,13,14,15,16,17,18,19]
oddList = []
evenList = []
for i in l1:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
print(f'Even No List :{evenList}\nOdd No List :{oddList}')