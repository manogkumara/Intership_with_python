input_string = input("Enter a string: ")
if len(input_string) < 3:
    result_string = input_string  # Leave it unchanged if length is less than 3
elif input_string.endswith('ing'):
    result_string = input_string + 'ly'  # If it ends with 'ing', add 'ly'
else:
    result_string = input_string + 'ing'  # Otherwise, add 'ing'
print("Result:", result_string)
