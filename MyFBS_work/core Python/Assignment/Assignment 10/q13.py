# 13 . Write a program to print list after removing even numbers.
l = [1, 2, 3, 4, 5, 6, 7, 8,9,11,12,13,14,15,16,17,18,19]
l1 =[]
for i in l:
    if i % 2 == 0:
        continue
    else:
        l1.append(i)
print(l1)

# we also use list comprihantion
l2 = [ x for x in (1, 2, 3, 4, 5, 6, 7, 8,9,11,12,13,14,15,16,17,18,19) if x%2 != 0]
print(l2)