# Original list of mixed integers and strings
original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

# Separate the numbers and strings using lambda
sort_mixed_list = lambda lst: sorted([x for x in lst if isinstance(x, int)]) + sorted([x for x in lst if isinstance(x, str)])

# Sort the mixed list
sorted_mixed_list = sort_mixed_list(original_list)

# Print the sorted mixed list
print("Sort the said mixed list of integers and strings:", sorted_mixed_list)
