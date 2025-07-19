# 3. Python Program to Sort the List According to the Second Element in Sublist
# Sample list of sublists
my_list = [[1, 5], [3, 2], [4, 8], [2, 4]]

# Define a function to return the second element
def get_second_element(sublist):
    return sublist[1]

# Use the function as the key for sorting
sorted_list = sorted(my_list, key=get_second_element)

# Display result
print("Original List:", my_list)
print("Sorted List (by second element):", sorted_list)
