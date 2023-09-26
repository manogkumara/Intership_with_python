from collections import Counter

# Sample dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Create Counter objects for both dictionaries
counter1 = Counter(d1)
counter2 = Counter(d2)

# Combine the counters by adding values for common keys
combined_counter = counter1 + counter2

# Convert the combined_counter to a regular dictionary if needed
combined_dict = dict(combined_counter)

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)
