# Original list of strings
original_list = ['red', 'black', 'white', 'green', 'orange']

# Function to filter elements containing a specific substring using lambda
filter_elements = lambda lst, substring: list(filter(lambda s: substring in s, lst))

# Input substring
substring1 = 'ack'
substring2 = 'abc'

# Find elements containing the first substring
result1 = filter_elements(original_list, substring1)

# Find elements containing the second substring
result2 = filter_elements(original_list, substring2)

# Print the results
print(f"Substring to search: {substring1}")
print(f"Elements of the said list that contain the specific substring: {result1}")

print(f"Substring to search: {substring2}")
print(f"Elements of the said list that contain the specific substring: {result2}")
