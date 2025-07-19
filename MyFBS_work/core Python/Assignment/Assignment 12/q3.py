# 3. Python Program to Detect if Two Strings are Anagrams
# s1 = 'silent'
# s2 = 'listen'
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not anagrams")


if len(s1) != len(s2):
    print("Not Anagram")
else:
    for i in s1:
        if i not in s1:
            print("not Anagram")
    else:
        print("Anagram")