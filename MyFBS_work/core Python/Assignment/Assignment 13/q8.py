# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary
# sample string
text = "the quick brown fox jumps over the lazy dog the fox was quick"

# split into words
words = text.split()

# create an empty dictionary
freq = {}

# count each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# print the frequency dictionary
print("Word frequencies:")
for word, count in freq.items():
    print(word, ":", count)
