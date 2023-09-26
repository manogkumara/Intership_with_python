# Sample dictionary
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}

# Find the maximum value and corresponding key
max_value = max(my_dict, key=lambda key: my_dict[key])

# Find the minimum value and corresponding key
min_value = min(my_dict, key=lambda key: my_dict[key])

# Print the maximum and minimum values and their keys
print("Maximum Value:", my_dict[max_value], "(Key:", max_value, ")")
print("Minimum Value:", my_dict[min_value], "(Key:", min_value, ")")
