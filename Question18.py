# Sample list of dictionaries
list_of_dicts1 = [{}, {}, {}]
list_of_dicts2 = [{1, 2}, {}, {}]

# Function to check if all dictionaries in a list are empty
def all_dicts_empty(lst):
    return all(not d for d in lst)

# Check if all dictionaries in the first list are empty
result1 = all_dicts_empty(list_of_dicts1)

# Check if all dictionaries in the second list are empty
result2 = all_dicts_empty(list_of_dicts2)

# Print the results
print("Result for list_of_dicts1:", result1)
print("Result for list_of_dicts2:", result2)
