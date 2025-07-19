# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String
s = 'apple ball cat dog'
words = s.split() # split function by default use space and form a list
print("Number of words in stirng :",len(words))
ch = len(s)
print("Number of Characters in String :",ch)
