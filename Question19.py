# Sample list of lists
list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Create a temporary set to store unique elements
unique_set = set()

# Create a new list to store the unique lists
unique_list_of_lists = []

# Iterate through the original list of lists
for sublist in list_of_lists:
    sublist_tuple = tuple(sublist)
    if sublist_tuple not in unique_set:
        unique_set.add(sublist_tuple)
        unique_list_of_lists.append(list(sublist_tuple))

# Print the new list with duplicates removed
print("New List:", unique_list_of_lists)
