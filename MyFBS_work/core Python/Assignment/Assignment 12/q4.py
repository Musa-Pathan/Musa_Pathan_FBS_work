# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged
s = "python"
if len(s) >= 2:
    s = s[-1] + s[1:-1] + s[0] # it will modify s = n +ytho+ p 
print(s)
