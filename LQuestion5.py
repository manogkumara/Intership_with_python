# Function to check if a string is a number using Lambda
is_number = lambda string: string.isdigit()

# Test cases
input_string1 = "12345"
input_string2 = "Hello, world!"

result1 = is_number(input_string1)
result2 = is_number(input_string2)

# Print the results
if result1:
    print(f"'{input_string1}' is a number.")
else:
    print(f"'{input_string1}' is not a number.")

if result2:
    print(f"'{input_string2}' is a number.")
else:
    print(f"'{input_string2}' is not a number.")
