# Original list of dictionaries
original_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28}
]

# Sort the list of dictionaries based on the 'age' key using a lambda function
sorted_list = sorted(original_list, key=lambda x: x['age'])

# Print the sorted list of dictionaries
for item in sorted_list:
    print(item)
