# Original list of tuples
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sort the list of tuples based on the second element (scores) using a lambda function
sorted_list = sorted(original_list, key=lambda x: x[1])

# Print the sorted list
print("Original list of tuples:", original_list)
print("Sorting the List of Tuples:", sorted_list)
