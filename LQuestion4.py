# Function to check if a string starts with a given character using Lambda
starts_with_char = lambda string, char: string.startswith(char)

# Test cases
input_string = "Hello, world!"
start_char = "H"
result = starts_with_char(input_string, start_char)

# Print the result
if result:
    print(f"The string '{input_string}' starts with the character '{start_char}'.")
else:
    print(f"The string '{input_string}' does not start with the character '{start_char}'.")
