# Sample dictionary
my_dict = {'b': 20, 'a': 10, 'c': 30, 'd': 40}

# Sort the dictionary by keys and create a new sorted dictionary
sorted_dict = dict(sorted(my_dict.items()))

# Print the sorted dictionary
print("Sorted Dictionary by Key:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")
