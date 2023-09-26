# Sample dictionary with duplicates
my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

# Create an empty dictionary to store unique key-value pairs
unique_dict = {}

# Iterate through the original dictionary and add key-value pairs to the unique dictionary
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

# Print the dictionary with duplicates removed
print("Dictionary with Duplicates Removed:", unique_dict)
