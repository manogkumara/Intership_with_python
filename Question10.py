# Sample dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30}

# Key to remove
key_to_remove = 'b'

# Check if the key exists before removing it
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed from the dictionary.")
else:
    print(f"The key '{key_to_remove}' does not exist in the dictionary.")

# Print the updated dictionary
print("Updated Dictionary:", my_dict)
