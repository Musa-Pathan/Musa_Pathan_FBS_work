# 5. Python Program to Count the Number of Vowels in a String
vowels = 'aeiouAEIOU'
s1 = 'apple banana cat'
count = 0
for i in s1:
    if i in vowels:
        count +=1
print(f'{count} no of vowel in list')