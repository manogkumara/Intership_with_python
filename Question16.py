# Sample dictionary
my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

# Get the highest 3 values from the dictionary
highest_values = sorted(my_dict.values(), reverse=True)[:3]

# Find keys corresponding to the highest values
highest_keys = [key for key, value in my_dict.items() if value in highest_values]

# Create a dictionary with the highest 3 key-value pairs
highest_dict = {key: my_dict[key] for key in highest_keys}

# Print the highest 3 key-value pairs
print("Highest 3 Values in the Dictionary:")
for key, value in highest_dict.items():
    print(f"{key}: {value}")
