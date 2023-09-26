# Sample dictionaries
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

# Iterate through the keys in dict1 and check if they exist in dict2 with the same value
for key, value in dict1.items():
    if key in dict2 and dict2[key] == value:
        print(f"{key}: {value} is present in both dict1 and dict2")
