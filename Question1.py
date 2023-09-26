# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5}

# Sort the dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort the dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionaries
print("Ascending Order:")
for key, value in sorted_dict_asc.items():
    print(f"{key}: {value}")

print("\nDescending Order:")
for key, value in sorted_dict_desc.items():
    print(f"{key}: {value}")
